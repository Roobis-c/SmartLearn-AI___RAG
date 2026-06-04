# 📚 SmartLearn RAG - Multi PDF Chatbot

SmartLearn RAG is an AI-powered document question-answering system that allows users to upload multiple PDF documents and interact with them using natural language. The application leverages Retrieval-Augmented Generation (RAG), FAISS Vector Search, Sentence Transformers, and Google's Gemini AI to provide accurate answers based on the uploaded documents.

---

## 🚀 Features

- Upload and process multiple PDF documents
- Extract text from PDFs automatically
- Intelligent text chunking with overlap
- Generate semantic embeddings using Sentence Transformers
- Store embeddings in a FAISS vector database
- Perform semantic similarity search
- Ask questions in natural language
- Gemini AI generates answers using retrieved document context
- Modern and responsive user interface
- Real-time document statistics (Pages, Chunks, Documents)

---

## 🏗️ Architecture

```text
User Uploads PDFs
        │
        ▼
PDF Text Extraction
        │
        ▼
Text Chunking
        │
        ▼
Embedding Generation
        │
        ▼
FAISS Vector Store
        │
        ▼
User Question
        │
        ▼
Question Embedding
        │
        ▼
Similarity Search
        │
        ▼
Relevant Chunks Retrieved
        │
        ▼
Gemini 2.5 Flash
        │
        ▼
Generated Answer
```

---

## 🧠 RAG Workflow

### 1. Document Processing

- Users upload one or more PDF files.
- Text is extracted from all pages.
- Extracted text is combined into a single corpus.

### 2. Chunking

The text is divided into smaller overlapping chunks using:

```python
chunk_size = 1000
chunk_overlap = 200
```

This ensures context is preserved between chunks.

### 3. Embedding Generation

Each chunk is converted into a dense vector representation using:

```python
sentence-transformers/all-MiniLM-L6-v2
```

### 4. Vector Storage

Generated embeddings are stored in a FAISS vector database for fast similarity search.

### 5. Retrieval

When a question is asked:

- The question is converted into an embedding.
- FAISS finds the most relevant chunks.
- Top matching chunks are retrieved.

### 6. Generation

Retrieved chunks are passed to Gemini AI as context.

Gemini generates an answer grounded in the uploaded documents.

---

## 📂 Project Structure

```text
SmartLearn-RAG/
│
├── app.py
│
├── utils/
│   ├── chatbot.py
│   ├── pdf_processor.py
│   └── vector_store.py
│
├── faiss_index/
│   ├── index.faiss
│   └── index.pkl
│
├── index.html
│
├── .env
│
├── requirements.txt
│
└── README.md
```

---

## ⚙️ Technologies Used

### Backend

- Flask
- Flask-CORS
- Python

### AI & RAG

- LangChain
- Google Gemini 2.5 Flash
- HuggingFace Sentence Transformers
- FAISS Vector Database

### PDF Processing

- PyPDF

### Frontend

- HTML5
- CSS3
- JavaScript

---

## 📦 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/smartlearn-rag.git

cd smartlearn-rag
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

## ▶️ Run Application

```bash
python app.py
```

Flask server starts on:

```text
http://127.0.0.1:5000
```

Open in browser:

```text
http://localhost:5000
```

---

## 🔍 API Endpoints

### Upload PDFs

```http
POST /upload
```

#### Request

```form-data
pdfs : file[]
```

#### Response

```json
{
  "message": "PDFs processed successfully",
  "pages": 45,
  "chunks": 120
}
```

### Ask Questions

```http
POST /ask
```

#### Request

```json
{
  "question": "What is machine learning?"
}
```

#### Response

```json
{
  "answer": "Machine learning is..."
}
```

---

## 🗄️ FAISS Storage

After processing documents:

```text
faiss_index/
│
├── index.faiss
└── index.pkl
```

### index.faiss

Stores:

- Embeddings
- Vector similarity index

### index.pkl

Stores:

- Original text chunks
- Metadata

---

## 📊 Example Workflow

### Upload Documents

```text
Operating Systems.pdf
Database Management.pdf
Machine Learning.pdf
```

### Ask Question

```text
What is normalization?
```

### Retrieval

```text
Chunk 12
Chunk 18
Chunk 24
Chunk 30
```

### Gemini Response

```text
Normalization is the process of organizing data
to reduce redundancy and improve integrity.
```

---

## 🔐 Current Limitations

- New uploads overwrite existing FAISS indexes.
- No document source citation.
- No conversation memory.
- Single-user local storage.
- No authentication system.

---

## 🚀 Future Enhancements

- Multi-user support
- Chat history
- Source citation display
- PDF preview
- Persistent vector database
- Hybrid Search (Keyword + Semantic)
- Document summarization
- Export chat conversations
- Docker deployment
- Cloud storage integration

---

## 📈 Learning Outcomes

This project demonstrates practical implementation of:

- Retrieval-Augmented Generation (RAG)
- Vector Databases
- Semantic Search
- Embedding Models
- Large Language Models (LLMs)
- Document Intelligence Systems
- Full Stack AI Application Development

---

## 👨‍💻 Author

**Roobis C**

AI & Full Stack Developer

### Tech Stack

- Python
- Flask
- LangChain
- Generative AI
- RAG Systems
- Vector Databases
- React / JavaScript

---


Feel free to use, modify, and distribute for educational and personal projects.
