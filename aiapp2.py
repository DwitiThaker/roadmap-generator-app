import streamlit as st
from extract_resume import extract_text_from_pdf
from embedder import get_resume_embedding
from searcher import search_career_match
import openai
import os

# 🔑 Set your OpenAI key here (or use dotenv later)
openai.api_key = "your-openai-api-key"  # replace with your real key

uploaded_file = st.file_uploader("Upload resume", type=["pdf"])

if uploaded_file is not None:
    text = extract_text_from_pdf(uploaded_file)
    embedding = get_resume_embedding(text)
    role_data = search_career_match(embedding)

    st.subheader("✅ Suggested Role:")
    st.write(f"**{role_data['role']}**")
    st.markdown(f"""
    **Skills**: {', '.join(role_data['skills'])}  
    **Tools**: {', '.join(role_data['tools'])}
    """)

    # ✅ Step 3: Build Prompt and Call GPT
    prompt = f"""Generate a personalized step-by-step learning roadmap to become a {role_data['role']}.
List essential skills, tools, and give a progressive path starting from beginner to advanced."""

    if st.button("📘 Generate Full Roadmap"):
        with st.spinner("Generating roadmap..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # or "gpt-4" if available
                messages=[{"role": "user", "content": prompt}]
            )
            roadmap_text = response.choices[0].message.content
            st.subheader("📍 Roadmap:")
            st.markdown(roadmap_text)
