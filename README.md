## Overview

This project is a Streamlit web application for extracting text from documents uploaded as images. Users can upload images containing documents, and the application will extract and display the text found within those documents.

## Features

**Image Upload** : Users can upload images containing documents.
**Text Extraction** : Extract text from uploaded images using OCR (Optical Character Recognition).
**Text Display** : Display extracted text to users for review.
**Supported Formats** : Supports common image formats such as JPEG, PNG, etc.

# Dependencies

## Ensure you have the following dependencies installed:

Python (3.x recommended)
Streamlit
pytesseract
Other dependencies as listed in requirements.txt

## Install dependencies using:
```
bash
Copy code
pip install -r requirements.txt
Getting Started
```
## Clone the repository:
```
bash
Copy code
git clone https://github.com/yourusername/document-extraction.git
cd document-extraction
```

## Setup Virtual Environment (optional but recommended):
```
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

## Install Dependencies:
```
bash
Copy code
pip install -r requirements.txt
```

## Download Tesseract OCR:
```
Download and install Tesseract OCR from Tesseract GitHub releases.
Ensure Tesseract executable (tesseract.exe on Windows) is accessible via PATH or set pytesseract.pytesseract.tesseract_cmd in your script.
```

## Run the Application:
```
bash
Copy code
streamlit run app.py
```

## Open the Application:
Open a web browser and go to http://localhost:8501 (or the URL provided by Streamlit) to view and interact with the application.

## Usage

**Upload Image** : Select an image file containing a document and upload it.
**Text Extraction** : The application will use OCR to extract text from the uploaded image.
**View Text** : Display the extracted text from the document.





## Acknowledgements
Thanks to the Streamlit community for providing an excellent framework for building interactive web applications in Python.
OCR functionality powered by Tesseract OCR and pytesseract.

---


*Vehicle Insurance* by Sanika Erande