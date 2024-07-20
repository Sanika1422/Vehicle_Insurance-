#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
import pytesseract
from PIL import Image
import re
import os
from io import BytesIO
path = r"C:\Users\sanika\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = path 


# In[4]:


image = Image.open("Vehical_Insurance.jpg")
st.sidebar.image("Vehical_Insurance.jpg",use_column_width=True)


st.sidebar.subheader("Why Vehical Insurance")

st.sidebar.write("1  Pays for serious injuries")
st.sidebar.write("2  Safeguards your family after you pass away")
st.sidebar.write("3  Reduces liabilities")
st.sidebar.write("4  Provides coverage for damage and repair costs due to accidents, collisions, and calamities")
st.sidebar.write("5  Protects third parties")
st.sidebar.write("6  Covers physical injuries")
st.sidebar.write("7  Provides insurance money in case of the death of the driver")
st.sidebar.write("8  Provides financial security")
st.sidebar.write("9  Is mandatory as per the Motor Vehicles Act")


# In[7]:


def allowed_image(filename):
    ext = os.path.splitext(filename)[1].lower()
    return ext in ['.jpg', '.jpeg', '.png'] # Check if the filename has the right extension
 
def extract_image_text(image_bytes, pattern):
    image = Image.open(BytesIO(image_bytes)) # Convert the image bytes to a PIL Image
    text = pytesseract.image_to_string(image) # Perform OCR on the image
    matches = re.findall(pattern, text) # Extract the desired text using the pattern
    return matches # Return the extracted text
 
def main():
    st.title("Hello! Welcome to our Vehical Insurance Portal.")
    uploaded_image = st.file_uploader("Upload an Image", type=['jpg', 'jpeg', 'png'])
    if uploaded_image is not None:
        if not allowed_image(uploaded_image.name):
            st.error("Only JPG, JPEG, and PNG images are allowed")
            return
        
            
        elif "pancard" in uploaded_image.name:
            image = Image.open("pancard.jpeg")
            st.image("pancard.jpeg")
            
            pan_card_no = re.compile(r"\b[A-Z]{5}[0-9]{4}[A-Z]\b")
            pan_card_name = re.compile(r"[A-Z]{6}[ ][A-Z]{7}[ ][A-Z]{6}")
            pan_card_DOB = re.compile(r"\d{2}\/\d{2}\/\d{4}")

            extracted_text1 = extract_image_text(uploaded_image.getvalue(), pan_card_no)
            extracted_text2 = extract_image_text(uploaded_image.getvalue(), pan_card_name)
            extracted_text3 = extract_image_text(uploaded_image.getvalue(), pan_card_DOB)
            
            st.write("PAN Card Number:", extracted_text1[0])
            st.write("Name:", extracted_text2[0])
            st.write("DOB:", extracted_text3[0])
            
        elif "aadhar_card" in uploaded_image.name:
            image = Image.open("aadhar_card.jpeg")
            st.image("aadhar_card.jpeg")
            
            Aaadhar_card_no = re.compile(r"\b[0-9]{4}[ ][0-9]{4}[ ][0-9]{4}\b")
            Aaadhar_card_name = re.compile(r"\b[A-Za-z]{6}[ ][A-Za-z]{5}\b")
            
            extracted_text1 = extract_image_text(uploaded_image.getvalue(), Aaadhar_card_no)
            extracted_text2 = extract_image_text(uploaded_image.getvalue(), Aaadhar_card_name)
            
            st.write("Aadhar Card Number:", extracted_text1[0])
            st.write("Aadhar Card Name:", extracted_text2[0])
            
        elif "passbook" in uploaded_image.name:
            image = Image.open("passbook.jpg")
            st.image("passbook.jpg")
            
            acc_number=re.compile(r"\d{10}")
            Aadhar_No=re.compile(r"\d{4}[ ][0-9]{4}[ ][0-9]{4}")
            name = re.compile(r"\b[A-Z]{4}[ ][A-Z]{5}\b")
            
            extracted_text1 = extract_image_text(uploaded_image.getvalue(), acc_number)
            extracted_text2 = extract_image_text(uploaded_image.getvalue(), Aadhar_No)
            extracted_text3 = extract_image_text(uploaded_image.getvalue(), name)
            
            st.write("Passbook Acc_Number:",extracted_text1[0])
            st.write("Passbook Aadhar_No:",extracted_text2[0])
            st.write("Passbook Name:",extracted_text3[0])
        else:
            st.error("Unsupported image type. Please upload a PAN card, Aadhar card, or passbook image.")
if __name__ == '__main__':
    main()







