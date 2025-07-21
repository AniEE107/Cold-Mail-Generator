from typing import Dict, List
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()


class Chain:
    def __init__(self):
        """Initialize the LLM chain with error handling"""
        try:
            self.llm = ChatGroq(
                temperature=0.7,
                groq_api_key=os.getenv("GROQ_API_KEY"),
                model_name="llama3-70b-8192"
            )
        except Exception as e:
            raise RuntimeError(f"Failed to initialize LLM: {str(e)}")

    def write_mail(self, job: Dict, links: List[str]) -> str:
        """
        Generate a cold email for a specific job
        Args:
            job: Dictionary containing job details
            links: List of relevant portfolio links
        Returns:
            Generated email text
        """
        prompt = PromptTemplate.from_template(
            """Generate a professional cold email with these strict requirements:

            Job Role: {role}
            Company: {company}
            Requirements: {requirements}

            Portfolio Projects:
            1. {project1}
            2. {project2}

            Requirements:
            1. Start directly with: "Hi Hiring Manager,"
            2. First paragraph must mention:
               - Garcia PLC
               - The specific job role
            3. Second paragraph must highlight:
               - Both portfolio projects
               - Their relevance to the job
            4. Closing paragraph with call-to-action
            5. End exactly with:
               "Best regards,
               Manish Kumar"
            6. No preamble text
            7. 150-200 words
            8. Professional tone
            """
        )

        try:
            chain = prompt | self.llm
            response = chain.invoke({
                "role": job.get("role", ""),
                "company": job.get("company", ""),
                "requirements": job.get("description", ""),
                "project1": links[0] if len(links) > 0 else "No project link provided",
                "project2": links[1] if len(links) > 1 else "No project link provided"
            })

            # Enforce strict formatting
            email = response.content.strip()
            if not email.startswith("Hi Hiring Manager,"):
                email = "Hi Hiring Manager,\n\n" + email
            if not email.endswith("Best regards,\nManish Kumar"):
                email = email.rstrip() + "\n\nBest regards,\nManish Kumar"

            return email

        except Exception as e:
            print(f"Email generation failed: {str(e)}")
            return ""


# Test function
def test_email_generation():
    chain = Chain()
    sample_job = {
        "role": "Senior Python Developer",
        "company": "TechCorp",
        "description": "Looking for Python developers with Django/Flask experience"
    }
    portfolio_links = [
        "https://stockanalysisbymanishkumar.streamlit.app/",
        "https://myportfolio-react.web.app"
    ]

    email = chain.write_mail(sample_job, portfolio_links)
    print("Generated Email:")
    print(email)


if __name__ == "__main__":
    test_email_generation()