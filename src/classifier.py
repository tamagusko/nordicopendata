# Copyright (C) 2022 Tiago Tamagusko
from __future__ import annotations

import numpy as np
import streamlit as st
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.models import load_model


@st.cache(allow_output_mutation=True)
def classifier(image, trained_model):
    image_size = (160, 160)  # MobileNetV2 size
    img = image.resize((image_size[0], image_size[1]))
    img_array = np.asarray(img)
    img_reshape = img_array.reshape((1, image_size[0], image_size[1], 3))
    img_preprocessed = preprocess_input(img_reshape)

    model = load_model(trained_model, compile=False)
    return model.predict(img_preprocessed)
