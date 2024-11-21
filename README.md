# AI ChatBot for Code Tutor

Welcome to the **AI ChatBot for Code Tutor**! This project is a Flask-based web application that provides an interactive chatbot designed to assist users with programming-related queries. The chatbot uses OpenAI’s API to generate context-aware responses, making it a valuable tool for learning, debugging, and exploring coding concepts.

![Description](assets/Demo.png)

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Features
- **Context-aware Responses:** Maintains a conversation history to provide meaningful replies.
- **Customizable Contexts:** Supports multiple predefined contexts like `code_explanation`, `language_basics`, and `implementation_guide`.
- **Error Handling:** Logs and returns appropriate error messages for debugging.
- **Cross-Origin Resource Sharing (CORS):** Allows integration with other frontend frameworks.
- **User-Friendly Logs:** Displays user agent information for tracking requests.

---

## Technologies Used
- **Flask**: A lightweight web framework for Python.
- **Flask-CORS**: Enables cross-origin resource sharing.
- **OpenAI API**: Powers the chatbot’s natural language processing.
- **dotenv**: Manages environment variables securely.
- **Logging**: Tracks and logs errors and debug information.

---

## Installation

### Prerequisites
- Python 3.8 or higher
- Pip (Python package manager)

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/MinhTienTH/AI-ChatBot-for-Code-Tutor.git
    cd AI-ChatBot-for-Code-Tutor
    ```

2. Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    - Create a `.env` file in the project root and add the following:
      ```env
      OPENAI_API_KEY=your_openai_api_key
      ```

5. Run the Flask app:
    ```bash
    python app.py
    ```

6. Access the application in your browser at `http://localhost:5001`.

---

## Usage
- Use the web interface to interact with the chatbot.
- Send `POST` requests to the `/chat` endpoint with a JSON payload:
  ```json
  {
      "message": "Explain Python lists.",
      "context": "language_basics"
  }
  ```

---

## API Endpoints

### `/chat` (POST)
- **Description**: Generates a response from the chatbot based on the input message.
- **Request Body**:
  ```json
  {
      "message": "Your query here",
      "context": "optional context"
  }
  ```
- **Response**:
  ```json
  {
      "response": "Chatbot's response",
      "user_agent": "Requester’s user agent"
  }
  ```

---

## Configuration
- **Environment Variables**:
  - `OPENAI_API_KEY`: Your OpenAI API key.
  - Adjust the base URL and model in the `CodeAssistantModel` class if using a custom API setup.

---

## Project Structure
```
AI-ChatBot-for-Code-Tutor/
├── app.py                 # Main application file
├── templates/
│   └── index.html         # Web interface template
├── static/                # Static files (e.g., CSS, JS)
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (not included in repo)
└── README.md              # Project documentation
```

---

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for review.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.
