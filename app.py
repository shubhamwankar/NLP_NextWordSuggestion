import streamlit as st
from load_predict import predict
st.title('Next Word Prediction')
text_input = st.text_input('Enter the sentence to predict the next word', placeholder='I love [MASK]!')
if text_input != "":
    prediction = predict(text_input)
    st.dataframe(prediction, use_container_width=True)

