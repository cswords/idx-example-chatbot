# Streamlit Project Starter for Project IDX

This project serves as a starter kit for developing Streamlit applications within Google's Project IDX environment. It's designed to provide a foundational setup, enabling you to begin building Streamlit apps swiftly while leveraging the powerful features of Project IDX.

**Note:** While this project is a helpful starting point for Streamlit development in Project IDX, it is not a fully defined IDX template. It does not contain the `idx-template.json` and `idx-template.nix` files that are required to have an official IDX template. Therefore, you will not be able to create a new workspace by using `https://idx.google.com/new?template=`.

## Project Structure

This starter kit comes with a pre-configured environment and a basic `main.py` to get you up and running. It includes:

*   **`.idx/dev.nix`:** Defines the development environment for your Streamlit app, including dependencies and configurations.
*   **`requirements.txt`:** Specifies the Python packages needed for your project.
*   **`main.py`:** Contains the core Streamlit application logic.

## About `main.py`

The `main.py` file is the heart of your Streamlit application. It's where you'll write the Python code that defines:

*   **User Interface (UI):** How your Streamlit app looks and what interactive elements it contains.
*   **Data Handling:** How your app reads, processes, and displays data.
*   **Logic:** The core functionality and computations performed by your app.
*   **AI Chatbot**: The code defines the interaction with the AI chatbot. It defines the different steps needed to ask for missing information, ask clarifying questions and provide the final answer.

The current `main.py` file has all the functions required to interact with the chatbot.

## How to Use this Starter Kit

This project is designed to kickstart your Streamlit projects in Project IDX. To utilize it:

1.  **Fork the Repository:**
    *   Fork this repository to your own GitHub account. This will create a copy of the project in your account, allowing you to make your own changes.
2.  **Create a New IDX Workspace:**
    *   Import your forked repository into Project IDX.
    *   Use this link pattern: `https://idx.google.com/import?url=https://github.com/your-username/your-repo-name`
    *   Replace `https://github.com/your-username/your-repo-name` with the URL of *your forked* repository.
3.  **Customize:** Modify the `.idx/dev.nix`, `requirements.txt`, and `main.py` files to align with your project's unique requirements.
    *   **`.idx/dev.nix`**: Customize your environment. This is a Nix file. Add packages, environment variables, or code-oss extensions here. When the file is changed, you will need to click the "Rebuild Environment" button.
    *   **`requirements.txt`**: List all your python packages here.
    *   **`main.py`**: This is your Streamlit application.
4.  **Develop:** Write your Streamlit application logic in `main.py`.
5.  **Run:** Launch your Streamlit app by clicking the preview button, ensuring the environment is correctly configured.

## Key Features

*   **Streamlined Setup:** Minimizes the initial configuration for Streamlit development within IDX.
*   **Environment Control:** `dev.nix` allows for precise environment definition and customization.
*   **Dependency Management:** `requirements.txt` provides a clear way to manage project dependencies.
*   **Preview Ready:** Configured for easy previewing of your Streamlit app in the IDX environment.

## Function

This project provides a foundation for rapidly developing and previewing Streamlit applications within Project IDX. Its key functions include:

*   **Environment Configuration**: Defining the necessary environment through the `.idx/dev.nix` file, including Python version, system packages, environment variables, and extensions.
*   **Dependency Specification**: Listing all Python package dependencies in the `requirements.txt` file.
*   **Application Development**: Providing a starting point with a `main.py` file where the Streamlit application logic is implemented.
*   **Previewing**: Supporting the quick previewing of the Streamlit app through the preview button in the Project IDX environment.
*   **Customization**: Allowing a user to customize the environment configuration, packages, and the main application.

## Learn More

*   **Project IDX:** [https://developers.google.com/idx](https://developers.google.com/idx)
*   **Customizing IDX Environments:** [https://developers.google.com/idx/guides/customize-idx-env](https://developers.google.com/idx/guides/customize-idx-env)
*   **Creating a workspace:** [https://developers.google.com/idx/guides/introduction](https://developers.google.com/idx/guides/introduction)
*   **Sharing your workspace:** [https://developers.google.com/idx/guides/share-your-workspace](https://developers.google.com/idx/guides/share-your-workspace)

---
