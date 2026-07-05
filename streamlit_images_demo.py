from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
import base64
import os
import streamlit as st


def encode_image(uploaded_file):
    return base64.b64encode(uploaded_file.read()).decode()

llm = ChatOllama(model="llava", base_url="https://moonscape-consumer-tasting.ngrok-free.dev/")
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that can describe images."),
        (
            "human",
            [
                {"type": "text", "text": "{input}"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "data:image/jpeg;base64,""{image}",
                        "detail": "low",
                    },
                },
            ],
        ),
    ]
)
chain=prompt|llm
st.title("Image Analyser- Using ollama llava model connected to local server using ngrok")
st.text("Developed by: Arush A.H.")
uploaded_file=st.file_uploader("Upload your image",type=["jpg","png"])
question=st.text_input("Enter a question")
if question:
    image=encode_image(uploaded_file)
    response=chain.invoke({"input" : question,"image":image})
    st.write(response.content)
