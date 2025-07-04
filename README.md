
# 📧 Cold Email Generator using GenAI

An AI-powered web application that scrapes job descriptions from career pages and automatically generates cold outreach emails using Groq's LLaMA models.
This tool helps streamline the business development process by creating personalized emails based on job postings and a technical portfolio.

## 🚀 Features

- 🔍 Scrape job descriptions from any public job posting URL.
- 🤖 Extract job roles, skills, and descriptions using Groq LLaMA 3 models.
- 📂 Match job skills with a personal or company portfolio.
- ✉️ Generate professional cold emails for outreach.
- 🌐 Simple and interactive Streamlit web interface.

## 📁 Folder Structure

```
Cold email generator/
├── app/
│   ├── main.py               # Streamlit app entry point
│   ├── chain.py              # Handles Groq model interactions
│   ├── portfolio.py          # Manages portfolio and skill matching
│   ├── utils.py              # Text cleaning utilities
│   ├── resource/
│   │   └── my_portfolio.csv  # Portfolio data (tech stacks & links)
├── .env                      # Environment variables (GROQ_API_KEY)
└── requirements.txt          # Required Python packages
```

## 🔑 Prerequisites

- Python 3.9 or higher recommended
- Groq API Key (Get it from [Groq Console](https://console.groq.com/))
- GitHub account (optional)

## 📦 Installation

1. **Clone the Repository:**

```bash
git clone https://github.com/your-username/Cold-email-generator.git
cd Cold-email-generator
```

2. **Create a Virtual Environment (Optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Required Libraries:**

```bash
pip install -r requirements.txt
```

4. **Set Up Environment Variables:**

Create a `.env` file in the `app/` folder:

```
GROQ_API_KEY=your_actual_groq_api_key
```

## ▶️ Running the App

```bash
cd app
streamlit run main.py
```

Then open the provided URL in your browser (usually http://localhost:8501).

## 🛠️ Technologies Used

- [Streamlit](https://streamlit.io/) — Web Framework
- [Groq API](https://console.groq.com/) — LLaMA-3 based Large Language Models
- [LangChain](https://www.langchain.com/) — Language Model Abstraction
- [Python](https://www.python.org/)

## 📂 Example Portfolio CSV Format

**`my_portfolio.csv`:**

```csv
Techstack,Links
Python,https://github.com/yourusername/python-project
Machine Learning,https://github.com/yourusername/ml-project
Data Analysis,https://github.com/yourusername/data-analysis-tool
```

## 🔮 Future Enhancements

- Deploy to cloud platforms like AWS or Heroku.
- Add Gmail authentication and auto-email sending.
- Replace CSV with a real database like MongoDB.
- Improve portfolio matching using vector search and embeddings.
- Track email analytics and click rates.
- Support multiple language models like GPT-4, Claude, etc.
- Build a Chrome Extension for direct scraping and emailing.
