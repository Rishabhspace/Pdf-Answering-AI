from flask import Flask, request, jsonify, render_template
from transformers import pipeline
import os
import fitz

app = Flask(__name__)
qa_pipeline = pipeline("question-answering")
UPLOAD_DIR = 'docs'
os.makedirs(UPLOAD_DIR, exist_ok=True)

extracted_pdf_text = ""

def read_pdf_text(file_path):
    document = fitz.open(file_path)
    text_content = ""
    for page_index in range(len(document)):
        page = document.load_page(page_index)
        text_content += page.get_text()
    return text_content

def get_answer(question, context):
    result = qa_pipeline(question=question, context=context)
    return result['answer']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/doc-upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file:
        saved_path = os.path.join(UPLOAD_DIR, uploaded_file.filename)
        uploaded_file.save(saved_path)
        global extracted_pdf_text
        extracted_pdf_text = read_pdf_text(saved_path)
        return jsonify({"message": "PDF uploaded and processed successfully"})
    return jsonify({"error": "File upload failed"}), 400

@app.route('/get-answer', methods=['POST'])
def ask():
    user_question = request.form['question']
    context_text = extracted_pdf_text
    if not user_question or not context_text:
        return jsonify({'error': 'Both question and context are required'}), 400
    answer = get_answer(user_question, context_text)
    return jsonify({'response': answer})

if __name__ == '__main__':
    app.run(debug=True)
