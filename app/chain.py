import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0,
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name="llama-3.1-8b-instant"
        )

    def extract_jobs(self, text):
        prompt = PromptTemplate.from_template("""
        ### PAGE TEXT:
        {page_data}
        ### TASK:
        Extract job postings with the following keys in JSON format: role, experience, skills, description.
        Return only JSON.
        """)
        chain = prompt | self.llm

        try:
            res = chain.invoke({"page_data": text})
            return JsonOutputParser().parse(res.content)
        except OutputParserException:
            return []

    def write_mail(self, job, links):
        prompt = PromptTemplate.from_template("""
        ### JOB INFO:
        {job_description}

        ### TASK:
        You are Bhuvan from AtliQ (an AI & software consulting firm). Write a cold email addressing the job and how AtliQ can help.
        Include the relevant portfolio links: {link_list}

        ### EMAIL (no preamble):
        """)
        chain = prompt | self.llm
        res = chain.invoke({
            "job_description": str(job),
            "link_list": ", ".join(links)
        })
        return res.content
