from setuptools import setup, find_packages

setup(
    name="hr_assistant",  # Name of your project
    version="0.1",        # Version number
    packages=find_packages(),  # Automatically finds all packages (folders with __init__.py)
    install_requires=[    # List of dependencies
        "langgraph==0.3.21",
        "langchain-google-genai==2.1.2",
        "langgraph-prebuilt==0.1.7",
        "google-generativeai",
        "PyPDF2",
        "pdfplumber",
        "openai",
        "pytest",          # For testing
    ],
)