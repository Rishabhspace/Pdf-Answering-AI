# PDF Answering AI

## Project Overview

PDF Answering AI is a Flask-based web application that allows users to upload a PDF file, extract its text, and ask questions related to the content of the PDF. The application utilizes natural language processing techniques via the Hugging Face Transformers library to provide accurate answers to user queries.

## Installation Instructions

To run this project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Rishabhspace/Pdf-Answering-AI.git
   cd pdf-answering-ai

   ```

2. **Setup virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt

   ```

4. **Run the Flask application:**

   ```bash
   python app.py

   ```

5. **Open your web browser and go to:**

   ```
   http://127.0.0.1:5000/

6. **Upload a PDF file and start asking questions!**

## Usage

- Once the application is running and you've uploaded a PDF file:

- Navigate to the home page at http://127.0.0.1:5000/.

- Upload a PDF file using the provided form.

- After uploading, enter a question related to the content of the uploaded PDF in the question form.

- Click "Ask" to receive an answer based on the PDF content.

## Dependencies

- Flask
- PyMuPDF
- transformers (Hugging Face)

## Screenshot

![Home-Page](https://raw.githubusercontent.com/Rishabhspace/Pdf-Answering-AI/main/static/homepage.png)
