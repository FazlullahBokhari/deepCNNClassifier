import streamlit as st
from PIL import Image 
import tensorflow as tf 
import numpy as np 


'''
# deep Classifier project

'''
model = tf.keras.models.load_model("model.h5")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    image = Image.open(uploaded_file)
    img = image.resize((224,224))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    
    result = model.predict(img_array)
    argmax_index = np.argmax(result, axis=1) 
    if argmax_index[0] == 0:
        st.image(image, caption='Predicted: Cat')
    else:
        st.image(image, caption='Predicted: Dog')
    
    #st.image(image, caption='Sunrise by the mountains')
    
    #st.write(image)
    