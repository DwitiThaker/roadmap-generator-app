# 🧠 AI Resume-to-Roadmap Career Advisor

A Streamlit-based app that takes your **resume as input (PDF)** and gives back a **personalized career role recommendation** along with a **learning roadmap** based on your skills.

---

## 📌 Features

- 📄 Upload your resume in PDF format
- 🧠 Resume is processed using NLP and embedded via Hugging Face model
- 🔍 Role matching is done using FAISS vector similarity
- 🧭 Get a career role suggestion and a detailed learning roadmap (skills, tools, and path)

---

## 🛠️ Tech Stack

| Component          | Tech Used                         |
|--------------------|-----------------------------------|
| Language           | Python                            |
| Frontend           | Streamlit                         |
| Embedding Model    | Hugging Face (MiniLM)             |
| Vector Search      | FAISS                             |
| Resume Parsing     | PyMuPDF (`fitz`)                  |
| Role Dataset       | Custom JSON (`career_roadmaps_full.json`) |

---

## 🚀 How It Works

1. Upload your resume (PDF).
2. Extract text from resume → convert to vector (embedding).
3. Match it against role vectors in FAISS index.
4. Display the best-matched career role and its roadmap.

---

## 📂 Folder Structure

roadmap_app/
│
├── app.py # Main Streamlit app
├── embedder.py # Converts text to embeddings
├── extract_resume.py # Reads text from uploaded PDF
├── searcher.py # Searches most relevant role via FAISS
│
├── career_roadmaps_full.json # All role data (skills, tools, path)
├── roadmap_index_local.faiss # FAISS index for fast vector search
├── roles_metadata_hf.json # Role descriptions linked to index
│
└── requirements.txt # Python dependencies

---


## ▶️ How to Run

```bash
git clone https://github.com/yourusername/roadmap-app.git
cd roadmap-app

# Optional: Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```


## 📦 To-Do / Future Ideas

- 🤖 Add chatbot interaction for dynamic Q&A
- 🔮 Integrate OpenAI/Gemini for smarter roadmap generation (optional)
- 📌 Add support for multiple suggestions (e.g., top 3 best-matching roles)
- 📈 Add progress tracking on learning roadmap items
- 🧾 Allow input via form (skills/interests) as an alternative to resume upload
- 🌐 Deploy publicly using Streamlit Cloud or Hugging Face Spaces

---

## 🙋‍♀️ Author

Built by **Dwiti Thaker** – 7th-sem IT Engineering Student | AI/ML Enthusiast 👩‍💻  
📬 Contributions, issues, and stars are always welcome!

> ✨ Let's connect and learn together — building AI, one project at a time.
