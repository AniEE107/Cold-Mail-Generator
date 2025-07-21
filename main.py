import streamlit as st
from my_chains import Chain
import pyperclip
from PIL import Image
import os


# Developer section
def developer_info():
    st.sidebar.markdown("---")
    st.sidebar.header("Developer")

    # Load your photo (save it in app/assets/ folder)
    try:
        developer_img = Image.open("app/assets/manish.jpg")
        st.sidebar.image(developer_img, width=150)
    except:
        st.sidebar.warning("Developer photo not found")

    st.sidebar.markdown("""
    **Manish Kumar**  
    Python Developer  
    Garcia PLC  
    [LinkedIn Profile](www.linkedin.com/in/manish-kumar-8b323a258) 
    """)


@st.cache_resource
def get_chain():
    return Chain()


def main():
    st.title("📧 Cold Email Generator")
    developer_info()  # Add developer section

    # Rest of your existing code
    chain = get_chain()
    url_input = st.text_input("Enter Job URL:")

    if st.button("Generate Email"):
        with st.spinner("Generating..."):
            try:
                sample_job = {
                    "role": "Senior Python Developer",
                    "company": "TechCorp",
                    "description": "Looking for Python developers",
                    "skills": ["Python", "Django"]
                }
                portfolio_links = [
                    "https://stockanalysisbymanishkumar.streamlit.app/",
                    "https://myportfolio-react.web.app"
                ]

                email = chain.write_mail(sample_job, portfolio_links)
                st.success("Done!")
                st.text_area("Generated Email", email, height=300)

                if st.button("📋 Copy Email"):
                    pyperclip.copy(email)
                    st.toast("Copied to clipboard!")

            except Exception as e:
                st.error(f"Error: {str(e)}")


if __name__ == "__main__":
    main()