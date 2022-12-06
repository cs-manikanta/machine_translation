import streamlit as st
import pandas as pd
from io import StringIO
import googletrans 
from googletrans import Translator
from PIL import Image

image = Image.open('cg_logo2.jpg')

st.image(image, width = 200)

# st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
st.title('Translator')

st.markdown('#### Translate from any language to any other language of your choice.')

trans = Translator()


tab1, tab2 = st.tabs(["Translate Text", "Translate File"])

with tab1:
    input_text = st.text_area('Enter your text', height = 100)

    target_language =st.selectbox('Select the target language' , ('English','Telugu','Hindi','Bengali','Gujarati',
    'Kannada','Malayalam','Marathi','Odia','Punjabi','Tamil','Urdu','Arabic','German'))
    st.write('You selected: ', target_language)

    if st.button('Translate'):
        result = trans.translate(input_text, src='auto',dest = target_language).text
        st.text_area(label = "Translated Text", value = result, height =100)
   

with tab2:
    uploaded_file = st.file_uploader("Upload your file here.", type = None)

    if uploaded_file is not None:
        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

         # To read file as string:
        string_data = stringio.read()
        st.write(string_data)

    target_language = st.selectbox('Select the target language' , ('English','Telugu','Hindi','Bengali',
    'Gujarati','Kannada','Malayalam','Marathi','Odia','Punjabi','Tamil','Urdu','Arabic','German'), key = 2)
    st.write('You selected: ', target_language)

    if st.button('Translate the file'):
     result2 = trans.translate(string_data, src = 'auto', dest = target_language).text
     # st.write(result)
     st.text_area(label = "Translated File", value = result2, height =100)

    
    
   

   

















