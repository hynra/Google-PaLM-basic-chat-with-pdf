import os

import streamlit
import joblib
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
import google.generativeai as palm
from langchain.embeddings import GooglePalmEmbeddings
from langchain.llms import GooglePalm

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
palm.configure(api_key=api_key)


def main():
    streamlit.header("Basic Chat With PDF")

    pdf = streamlit.file_uploader("Upload a PDF File", type='pdf')
    if pdf is not None:
        pdf_reader = PdfReader(pdf)

        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        # streamlit.write(text)
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )

        chunks = text_splitter.split_text(text=text)
        # streamlit.write(chunks)

        store_name = pdf.name[:-4]
        streamlit.write(store_name)

        embeddings = GooglePalmEmbeddings(model_name="models/embedding-gecko-001")
        vector_store = FAISS.from_texts(chunks, embedding=embeddings)
        # with open(f"{store_name}.json", "w") as f:
        #  joblib.dump(vector_store, f)
        # joblib.dump(vector_store, f"{store_name}.joblib")

        query = streamlit.text_input("Ask questions about your PDF file:")
        # streamlit.write(query)

        if query:
            docs = vector_store.similarity_search(query=query, k=3)
            # streamlit.write(docs)

            llm = GooglePalm(model_name="models/text-bison-001")
            chain = load_qa_chain(llm=llm, chain_type="stuff")

            response = chain.run(input_documents=docs, question=query)
            streamlit.write(response)


if __name__ == '__main__':
    main()
