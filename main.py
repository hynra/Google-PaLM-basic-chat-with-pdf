import streamlit
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter


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
        streamlit.write(chunks)


if __name__ == '__main__':
    main()
