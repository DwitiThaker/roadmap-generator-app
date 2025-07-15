import streamlit as st
from extract_resume import extract_text_from_pdf
from embedder import get_resume_embedding
from searcher import search_career_match

st.title("📄 Resume to Career Roadmap")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    text = extract_text_from_pdf(uploaded_file)
    embedding = get_resume_embedding(text)
    role_data = search_career_match(embedding)

    st.markdown("### ✅ Suggested Career Match")
    st.write(f"**{role_data['role']}**")
    st.markdown("### 📚 Skills Required")
    st.write(", ".join(role_data["skills"]))
    st.markdown("### 🛠 Tools You Should Learn")
    st.write(", ".join(role_data["tools"]))
