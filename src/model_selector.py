# Copyright (C) 2022 Tiago Tamagusko
from __future__ import annotations

import os


def models_available():
    return [file for file in os.listdir('models') if file.endswith('.h5')]


def country(image: str):
    return image[:2]


def camera(image: str):
    return image.split('_', 2)[-1].rsplit('.', 1)[0]


def availability(image: str):
    return country(image) + '_' + camera(image) in str(models_available())


def model_selector(image: str):
    models = models_available()
    return [model for model in models if model.startswith(country(image) + '_' + camera(image))]
