#Input the relevant libraries
import streamlit as st
import altair as alt
from textblob import TextBlob


# Define the Streamlit app


def getSubjectivity(text):
    return TextBlob(text).sentiment.subjectivity
  
 #Create a function to get the polarity
def getPolarity(text):
    return TextBlob(text).sentiment.polarity

def getAnalysis(score):
    if score < 0:
        return ‘Negative’
elif score == 0:
    return ‘Neutral’
else:
    return ‘Positive’
    
def app():
    st.title('Simple TextBlob Sentiment Demo')
    st.subheader('by Louie F. Cervantes, M.Eng.')
    
    st.write('We use the textblob package to generate the \
        sentiment of a statement.')
    
    #Get the user input
    user_input = st.text_input("Input a sentence: ")
    
    # Add a button to update the data
    if st.button("Get sentiment"):
        polarity = getPolarity(user_input)
        st.write('Polarity: ' + str(polarity))
        st.write('Subjectivity: ' + getSubjectivity(user_input))
        st.write('Sentiment: ' + getAnalysis(polarity))
# run the app
if __name__ == "__main__":
    app()
