import streamlit
from PyPDF2 import PdfReader


def main():
    streamlit.header("Basic Chat With PDF")

    pdf = streamlit.file_uploader("Upload a PDF File", type='pdf')
    if pdf is not None:
        pdf_reader = PdfReader(pdf)

        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        streamlit.write(text)


if __name__ == '__main__':
    main()
