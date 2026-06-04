from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from dotenv import load_dotenv

from utils.pdf_processor import extract_text_from_pdfs
from utils.vector_store import create_vector_store
from utils.chatbot import get_answer

load_dotenv()

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return send_file("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    try:

        files = request.files.getlist("pdfs")

        if not files:
            return jsonify({
                "message": "No PDFs uploaded"
            }), 400

        text, total_pages = extract_text_from_pdfs(files)

        total_chunks = create_vector_store(text)

        return jsonify({
            "message": "PDFs processed successfully",
            "pages": total_pages,
            "chunks": total_chunks
        })

    except Exception as e:

        return jsonify({
            "message": str(e)
        }), 500


@app.route("/ask", methods=["POST"])
def ask():

    try:

        data = request.get_json()

        question = data.get("question")

        if not question:
            return jsonify({
                "answer": "Please enter a question."
            })

        answer = get_answer(question)

        return jsonify({
            "answer": answer
        })

    except Exception as e:

        return jsonify({
            "answer": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)