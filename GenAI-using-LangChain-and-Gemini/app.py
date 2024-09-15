LANGCHAIN_API_KEY="lsv2_pt_19f39e03a40a44cf996e64e0e349fe0a_44661255"
GOOGLE_API_KEY="AIzaSyA1i0PoAjJ5txJaebB1MfeRgHw55SiCg"
LANGCHAIN_PROJECT="CHATBOT"

from langchain_google_genai import ChatGoogleGenerativeAI;
from langchain_core.prompts import ChatPromptTemplate;
from langchain_core.output_parsers import StrOutputParser

import streamlit as st;
import os;

os.environ["GOOGLE_API_KEY"]=GOOGLE_API_KEY
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=LANGCHAIN_API_KEY

##prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

##streamlit
st.title("Langchain Demo With GEMINI API")
input_text=st.text_input("Search the topic you want")

#$gemini llm
llm=ChatGoogleGenerativeAI(model="gemini-1.5-pro")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
