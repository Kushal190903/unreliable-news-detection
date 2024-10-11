import streamlit as st
import re
import string
import numpy as np
from keras.models import load_model

try:
    from langchain_huggingface import HuggingFaceEmbeddings

    embedding = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
    
    
    try:
        model = load_model('unreliable+news+detection+model.keras')
    except:
        st.warning("Error loading the model. Please check the model file or retry by reloading the page")
    
    
    def wordopt(text):
        text = text.lower()
        text = re.sub('\[.*?\]', '', text)
        text = re.sub(r"\W", " ", text)
        text = re.sub(r'https?://\S+|www\.\S+', '', text)
        text = re.sub(r'<.*?>+', '', text)
        text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
        text = re.sub(r'\n', '', text)
        text = re.sub(r'\w*\d\w*', '', text)
        return text

    
    def classify(text):
        cleaned_text = wordopt(text)
        embedded_text = np.array(embedding.embed_query(cleaned_text)).reshape(1, -1)
        prediction = model.predict(embedded_text)
        return prediction[0][0]  

  
    st.title("Unreliable News Detection with Confidence Score")

    
    user_input = st.text_area("Enter news text to classify", "")

    if st.button("Classify"):
        if user_input:
            try:
              
                result = classify(user_input)
                confidence = result if result >= 0.5 else 1 - result

                
                if result < 0.5:
                    st.success(f"The news is classified as Reliable  with a confidence of {round((1 - result)*100, 1)}%")
                else:
                    st.error(f"The news is classified as Unreliable  with a confidence of {round(result * 100, 1)}%")
            except Exception as e:
                st.warning(f"An error occurred during classification: {str(e)}")
            if len(user_input.split(" "))<100:
                st.warning("The prediction may not be accurate on short texts")
        else:
            st.warning("Please enter some text for classification.")
            
    st.write("This app classifies news as either reliable (0) or unreliable (1) and shows the confidence score.")

except Exception as e:
    st.warning(f"An unexpected error occurred: {str(e)}. Please reload the page.")
