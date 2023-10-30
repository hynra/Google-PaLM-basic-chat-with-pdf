import streamlit
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import pickle
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain

load_dotenv()


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

        embeddings = OpenAIEmbeddings()
        vector_store = FAISS.from_texts(chunks, embedding=embeddings)
        with open(f"{store_name}.pkl", "rb") as f:
            pickle.dump(vector_store, f)

        query = streamlit.text_input("Ask questions about your PDF file:")
        # streamlit.write(query)

        if query:
            docs = vector_store.similarity_search(query=query, k=3)
            streamlit.write(docs)

            llm = OpenAI(model_name="gpt-3.5-turbo")
            chain = load_qa_chain(llm=llm, chain_type="stuff")

            response = chain.run(input_documents=docs, question=query)
            streamlit.write(response)


if __name__ == '__main__':
    main()
