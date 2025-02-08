# Streamlit Project Template for Project IDX

This project serves as a template for developing Streamlit applications within Google's Project IDX environment. It provides a pre-configured setup to get you started quickly with Streamlit and leverages the power of Project IDX for a seamless development experience.

## Getting Started

1.  **Environment Customization:** Begin by tailoring your development environment using the `.idx/dev.nix` file. This file is crucial for defining the necessary tools, packages, and IDE extensions for your project.
    *   **Nix Package Management:** The `.idx/dev.nix` file uses Nix to specify the packages your project needs. This ensures consistency and reproducibility of your environment. For example, python3 and pip are already specified.
    *   **IDE Extensions:** You can specify VS Code extensions to enhance your development workflow directly in the `dev.nix` file. "ms-python.python" extension is already added.
    *   **Environment Variables:** Define environment variables specific to your project here. We have the `PORT` already set to "9080".
    * **Pre-configured Start Script**: The start.sh script is preconfigured to run your app with Streamlit.

    Learn more about customizing your IDX environment: [https://developers.google.com/idx/guides/customize-idx-env](https://developers.google.com/idx/guides/customize-idx-env)

2.  **Dependencies:** A `requirements.txt` file is available to manage your Python dependencies.
    * When the environment is created the project will run the `pip install -r requirements.txt` command.

3. **Preview:** The application preview is configured by default in your `.idx/dev.nix` to run using the `start.sh` script.
    * **Important:** The preview feature might not function correctly until the environment setup (defined in `dev.nix`) is fully completed. If the preview fails initially, wait for the environment setup to finish and then try again. A prompt will show up when the setup is completed.

4. **Main Script:** The `main.py` file is set up to be your main Streamlit application. Modify its contents according to your needs.

## How to Use as a Template

This project is designed to be a starting point for your Streamlit projects in Project IDX. To use it as a template:

1.  **Create a New IDX Workspace:** Create a new IDX workspace from this repository's URL. For example: `https://idx.google.com/new?template=https://github.com/my-org/my-repo` (Replace `https://github.com/my-org/my-repo` with the correct repository URL of the project after you cloned it).

2.  **Customize:** Modify the `.idx/dev.nix`, `requirements.txt`, and `main.py` files to suit your project's specific requirements.

3.  **Develop:** Write your Streamlit application logic in `main.py`.

4.  **Run:** Start your Streamlit app by clicking the preview button, and make sure the environment is correctly configured.

## Key Features

*   **Pre-configured IDX Environment:** The `.idx/dev.nix` file sets up a basic development environment, including Python and pip.
*   **Streamlit Ready:** `start.sh` script is ready to start the app.
*   **Dependency Management:** `requirements.txt` is available to manage your project dependencies.
*   **Preview Enabled:** You can preview your Streamlit app directly within IDX using the built-in preview feature.
*   **Open in IDX button ready**: Once you're ready to share this template, you can publish it in a github repository and share that link to be used as a IDX template. Also you can add an "Open in IDX" button to make it easy for other user to use it.

## Known Issues

*   **Preview Timing:** As mentioned above, the preview might fail to work immediately after creating the workspace. This is because the environment needs to be fully built before the preview can function. Wait for the setup process to complete and retry.

## Learn More

*   **Project IDX:** [https://developers.google.com/idx](https://developers.google.com/idx)
*   **Customizing IDX Environments:** [https://developers.google.com/idx/guides/customize-idx-env](https://developers.google.com/idx/guides/customize-idx-env)
*   **Creating a workspace from a template:** [https://developers.google.com/idx/guides/introduction](https://developers.google.com/idx/guides/introduction)
*   **Sharing your template:** [https://developers.google.com/idx/guides/customize-idx-env](https://developers.google.com/idx/guides/customize-idx-env)

---
