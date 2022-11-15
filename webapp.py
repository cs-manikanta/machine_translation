import streamlit as st

import googletrans 
from googletrans import Translator

st.title('Made by Mani')

st.header('Translator App')


st.subheader('Our machine will translate from English to Hindi.')


trans = Translator()

input_text = st.text_area('Enter your text', height = 100)

Target_Language =st.selectbox('Select the target language' , ('Telugu','Hindi','Bengali','Gujarati','Kannada','Malayalam','Marathi','Odia','Punjabi','Tamil','Urdu'))
st.write('You selected: ', Target_Language)

if st.button('Translate'):
    result = trans.translate(input_text, src='en',dest = 'hi').text
    st.write(result)





