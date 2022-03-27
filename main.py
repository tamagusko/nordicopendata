from __future__ import annotations

import numpy as np
import streamlit as st
from PIL import Image

from src.classifier import classifier
from src.model_selector import availability
from src.model_selector import model_selector
from src.model_selector import models_available

st.write(
    """
         # Intelligent Real-time Accident Warning System (IRAWS)
         by [Tiago Tamagusko](https://www.linkedin.com/in/tamagusko/)

         ## MVP for Nordic AI & Open Data Hackathon

         """,
)

file = st.file_uploader('Please upload an image file', type=['jpg', 'png'])

if file is None:
    st.text("You haven't uploaded an image file")
else:
    image = Image.open(file)
    filename = image.filename

    if availability(file.name):  # check if there is a model for this camera
        model = 'models/' + str(model_selector(file.name)[0])
        st.image(image, use_column_width=True)
        prediction = classifier(image, model)

        if np.argmax(prediction) == 0:
            pred = (prediction[0][0] * 100).round(2)
            st.error('Alarm!')
            st.write(f'Confidence: {pred}%')
        else:
            pred = (prediction[0][1] * 100).round(2)
            st.success('Normal!')
            st.write(f'Confidence: {pred}%')
    else:
        st.warning('There is no trained model for this camera.')
        st.write(f'Available models: {models_available()}')
        st.write('Model name format: COUNTRY_CAMERA_BASEMODEL.h5')

st.markdown(
    """<a style='display: block; text-align: right;' href="https://github.com/tamagusko/nordicopendata/">Project repository</a>
    """,
    unsafe_allow_html=True,
)
