#Input the relevant libraries
import streamlit as st
import altair as alt
from textblob import TextBlob


# Define the Streamlit app
def app():
    st.title('Simple TextBlob Sentiment Demo')
    st.subheader('by Louie F. Cervantes, M.Eng.')
    
    st.write('We use the textblob package to generate the \
        sentiment of a statement.')
    
    #Get the user input
    user_input = st.text_input("Input a sentence: ")
    
    # Add a button to update the data
    if st.button("Get sentiment"):
        st.write(TextBlob("He is very good boy").sentiment)
# run the app
if __name__ == "__main__":
    app()
