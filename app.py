import streamlit as st
import re
import string
import numpy as np
from keras.models import load_model
import trafilatura
from xgboost import XGBClassifier

 
try:
    model = load_model('news_classifier_neural_network_model.keras')
    # model=XGBClassifier()
    # model.load_model('news_classifier_xgb.json')
except:
    st.warning("Error loading the classification model. Please check the model file or retry by reloading the page")


def wordopt(t):
     '''cleans the text by removing/substituting non word characters,HTML code,hyperlinks,extra blanck spaces etc.'''
     t = t.lower()
     t = re.sub('\[.*?\]', 'bracket', t)
     t = re.sub("\\W"," ",t)
     t = re.sub('https?://\S+|www\.\S+', 'hyperlink', t)
     t = re.sub('<.*?>+', 'HTML', t)
     t = re.sub('[%s]' % re.escape(string.punctuation), '', t)
     t = re.sub('\n', '', t)
     #t = re.sub('\w*\d\w*', '', t)
     return t.strip()

def classify(text):
    '''classifies the text using the neural network model'''
    # text=wordopt(text)   this part is now done outside the function to be used by check_length_satisfaction also
    embedded_text = np.array(embedding.embed_query(text)).reshape(1, -1)
    prediction = model.predict(embedded_text)
    return prediction[0][0]  # Return the prediction score (0 for reliable, 1 for unreliable)

def check_length_satisfaction(text, min_length=100):
    '''Check whether the length of a text (in words) is less than the specified number'''
    length = len(text.split())
    if length < min_length:
        st.warning('The prediction may not be accurate on short texts')

try:
    try:
        from langchain_huggingface import HuggingFaceEmbeddings

        embedding = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
    except exception as e:
        st.warning("Error in importing/loading the embeddings module : ",e)
   
  
    st.title("Unreliable News Detection with Confidence Score")
    st.sidebar.title('About')
    st.sidebar.write("This app classifies news as either reliable  or unreliable based solely on the text and shows the confidence score of prediction.")
    st.sidebar.write("\n\n\n\n\n\n\n**Using URL may give unexpected results at the moment because the process of extracting content from URL is currently under improvement**")

    input_option = st.radio("Select Input Type", ("URL", "Text"))
    if input_option=='Text':

        user_input = st.text_area("Enter news text to classify(only main content without title, subheadings etc.)", "",height=50)

    elif input_option=='URL':
        user_input=st.text_area("Enter URL of the news article",height=10)

    classify_button=st.button('classify')
    if classify_button:
       
        try:
            result=-1
            # Get the classification result
            if input_option=='Text':
                with st.spinner("Classifying"):
                    if user_input:
                        user_input=wordopt(user_input)
                        result = classify(user_input)
                     
                        check_length_satisfaction(user_input,100)
                    else:
                        st.warning("Please enter some text for classification.")
                    
            else:
                if not user_input:
                    st.warning("please enter a URL")
                 
                else:
                    with st.spinner("Extracting content"):
                        downloaded = trafilatura.fetch_url(user_input)#userinput used here for the web url
                        main_content = trafilatura.extract(downloaded) if downloaded else None 
                    if main_content:
                        with st.spinner("classifying"):
                            st.write(main_content)
                            main_content=wordopt(main_content)
                            result=classify(main_content)
                            check_length_satisfaction(main_content,100)
                    else:
                        st.warning("Could not find any article or relevant text")
                    
            if result>=0:
                confidence = result if result >= 0.5 else 1 - result
                
                if result < 0.5:
                    st.success(f"The news is classified as Reliable  with a confidence of {round(confidence*100)}%")
                else:
                    st.error(f"The news is classified as Unreliable  with a confidence of {round(confidence * 100)}%")
        except Exception as e:
            st.warning(f"An error occurred during classification: {str(e)}")
        

except Exception as e:
    st.warning(f"An unexpected error occurred: {str(e)}. Please reload the page.")
