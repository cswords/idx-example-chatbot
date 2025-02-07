import streamlit as st
from langchain_community.utilities import SearchApiAPIWrapper
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
import os
import json

# --- Functions to Manage API Keys ---
def show_api_key_modal():
    """Displays a modal to collect API keys."""
    with st.form("api_keys_form"):
        search_api_key = st.text_input("Enter your Search API Key:", type="password")
        google_api_key = st.text_input("Enter your Google API Key:", type="password")
        submitted = st.form_submit_button("Submit Keys")
        if submitted:
            if search_api_key and google_api_key:
                st.session_state.search_api_key = search_api_key
                st.session_state.google_api_key = google_api_key
                st.session_state.api_keys_submitted = True
                st.rerun()
            else:
                st.error("Please enter both API keys.")

def is_api_keys_configured():
    """Checks if the API keys are configured."""
    return "api_keys_submitted" in st.session_state and st.session_state.api_keys_submitted

# --- Initialize Components (only if API keys are configured) ---
if is_api_keys_configured():
    os.environ["SEARCHAPI_API_KEY"] = st.session_state.search_api_key
    os.environ["GOOGLE_API_KEY"] = st.session_state.google_api_key
    search = SearchApiAPIWrapper(api_key=os.environ["SEARCHAPI_API_KEY"])
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0)

    # --- Prompt Templates ---
    initial_answer_prompt_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a helpful assistant that tries to answer the questions as best as you can.",
            ),
            ("user", "{input}"),
        ]
    )

    missing_info_prompt_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You are an assistant that identifies what it does not know or understand in a question.
                You have to come up with particular questions to ask for the parts you do not know.
                The format has to be a json with key "questions" and value of a list.
                """,
            ),
            ("user", "{input}"),
        ]
    )

    context_answer_prompt_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You are a helpful assistant. You are provided with the following context from a search engine.
                Use this context to answer the question as accurately as possible.
                If the question does not relate to the context, you answer without context.
                """,
            ),
            ("user", "{context}\n\nQuestion: {question}"),
        ]
    )

    # --- Chains (Runnable Sequences) ---
    initial_answer_chain = initial_answer_prompt_template | llm
    missing_info_chain = missing_info_prompt_template | llm
    context_answer_chain = (
        {"context": lambda x: x["context"], "question": lambda x: x["question"]}
        | context_answer_prompt_template
        | llm
    )

    # --- Functions ---
    def process_question(question):
        """Processes the question through different steps and returns the final answer."""

        with st.chat_message("assistant"):
            st.write("Identifying missing information...")
            # 1. Get Missing Information
            missing_info_result = missing_info_chain.invoke({"input": question})
            try:
                missing_info_json = json.loads(missing_info_result.content)
                questions_to_ask = missing_info_json.get("questions", [])
            except json.JSONDecodeError:
                questions_to_ask = []
                st.write("Could not process missing information. Skipping questions step")


        # 2. Add initial answer
        with st.chat_message("assistant"):
            st.write("Getting initial answer...")
            initial_answer = initial_answer_chain.invoke({"input": question}).content
            st.write(f"Initial answer: {initial_answer}")
            st.session_state.chat_history.append({"role": "assistant", "content": f"Initial answer: {initial_answer}"})
            
        # 3. Ask Clarifying Questions
        if questions_to_ask:
            with st.chat_message("assistant"):
              st.write("Asking clarifying questions...")
              for q in questions_to_ask:
                  st.session_state.chat_history.append(
                      {"role": "assistant", "content": q}
                  )
                  clarification_answer = st.chat_input(
                      f"Please answer this question from the chatbot: {q}"
                  )
                  if clarification_answer:
                      st.session_state.chat_history.append(
                          {"role": "user", "content": clarification_answer}
                      )

        # 4. Search with Search (if needed)
        with st.chat_message("assistant"):
            st.write("Searching...")
            search_results = search.run(query=question)
            st.write(f"Search results: {search_results}")
            st.session_state.chat_history.append({"role": "assistant", "content": f"Search results: {search_results}"})

        # 5. Answer with Context
        with st.chat_message("assistant"):
          st.write("Generating final answer...")
          final_answer = context_answer_chain.invoke(
              {"context": search_results, "question": question}
          ).content
          st.write(f"Final answer: {final_answer}")
          st.session_state.chat_history.append({"role": "assistant", "content": f"Final answer: {final_answer}"})

        return final_answer

    # --- Streamlit App ---
    st.title("Enhanced Chatbot with Clarification")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []


    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if question := st.chat_input("What's your question?"):
        st.session_state.chat_history.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.write(question)

        process_question(question)

else:
    # API Key Modal
    if "api_keys_submitted" not in st.session_state:
        st.session_state.api_keys_submitted = False
    show_api_key_modal()
