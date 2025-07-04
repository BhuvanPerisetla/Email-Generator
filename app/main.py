import streamlit as st
from chain import Chain
from portfolio import Portfolio
from utils import clean_text

def create_app():
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    st.title("📧 Cold Mail Generator")

    url_input = st.text_input("Enter a URL:", value="Enter the job posting link")
    submit = st.button("Generate Email")

    if submit:
        try:
            from langchain_community.document_loaders import WebBaseLoader
            loader = WebBaseLoader([url_input])
            text = loader.load()[0].page_content
            cleaned = clean_text(text)

            chain = Chain()
            portfolio = Portfolio()

            jobs = chain.extract_jobs(cleaned)
            portfolio_data = portfolio.get_all_links()

            for job in jobs:
                matched_links = portfolio.match_links(job.get("skills", []), portfolio_data)


                email = chain.write_mail(job, matched_links)
                st.markdown("### ✉️ Generated Email")
                st.code(email, language="markdown")

        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    create_app()
