from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
# from langchain_community.llms import Ollama
from langchain_ollama.llms import OllamaLLM
import streamlit as st
import os

# Set environment variables
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "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"

# Streamlit app title
st.title('Langchain Demo With LLAMA3.1 API')

# Streamlit user input
input_text = st.text_input("Enter your query:")

# Define ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),
        ("user", "Question: {question}")
    ]
)

# Initialize the Ollama LLM (make sure you have the model downloaded and available)
llm = OllamaLLM(model="llama3.1")

# Define the output parser
output_parser = StrOutputParser()

# Define the chain (using LangChain's pipeline functionality)
chain = prompt | llm | output_parser

# When input text is provided, invoke the chain and display the output
if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)
