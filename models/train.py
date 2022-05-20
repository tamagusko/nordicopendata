# IRAWS (c) Tiago Tamagusko 2022
"""
Transfer Learning a with Deep Learning to train a model to detect unusual events (skids, vehicles off-street, and on
the wrong lane) in highways.

Models: https://github.com/tamagusko/nordicopendata/tree/main/models
Data: https://github.com/tamagusko/nordicopendata/tree/main/data

Usage:
    $ python path/to/train.py --basemodel MODEL --datapath path/to/data/ --cam COUNTRY_CAMERA --img SIZE --batch NUMBER --epoch NUMBER --reports all/text/graph

Example:
    $ python train.py --basemodel MobileNetV2 --datapath path/to/data/ --cam FI_C0166000 --img 160 --batch 4 --epoch 100 --reports all
"""
from __future__ import annotations

import argparse
import json

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import matthews_corrcoef
from tensorflow import keras
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten
from tensorflow.keras.models import load_model
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Read defaults parameters
with open('defaults.json', 'r') as read_file:
    default = json.load(read_file)


def main():
    # Parser
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='Train a custom model to detect unusual road events',
    )
    parser.add_argument(
        '-m', '--basemodel',
        type=str,
        default=default['BASEMODEL'],
        help="Base model for transfer learning: ['MobileNetV2', 'EfficientNetB1', 'EfficientNetB7']",
    )
    parser.add_argument(
        '-d', '--datapath',
        type=str,
        required=True,
        help='File path of data',
    )
    parser.add_argument(
        '-c', '--cam',
        type=str,
        default=default['CAMERA'],
        help='Camera to train the model',
    )
    parser.add_argument(
        '-i', '--img',
        type=int,
        default=default['CAMERA_SIZE'],
        help="Size of images to train the model, recommendation: ['MobileNetV2': 160, 'EfficientNetB1': 240, 'EfficientNetB7': 600]",
    )
    parser.add_argument(
        '-b', '--batch',
        type=int,
        default=default['BATCH_SIZE'],
        help='Batch size used to train the model',
    )
    parser.add_argument(
        '-e', '--epoch',
        type=int,
        default=default['EPOCHS'],
        help='Epoch number used to train the model',
    )
    parser.add_argument(
        '-r', '--reports',
        type=str,
        default=default['REPORTS'],
        help="Model training reports: ['all', 'text', 'graph']",
    )
    args = parser.parse_args()

    # Import base model
    # More on https://www.tensorflow.org/api_docs/python/tf/keras/applications
    if args.basemodel == 'EfficientNetB1':
        from tensorflow.keras.applications.efficientnet import preprocess_input
        from tensorflow.keras.applications.efficientnet import EfficientNetB1 as BASEMODEL
    elif args.basemodel == 'EfficientNetB7':
        from tensorflow.keras.applications.efficientnet import preprocess_input
        from tensorflow.keras.applications.efficientnet import EfficientNetB7 as BASEMODEL
    elif args.basemodel == 'MobileNetV2':
        from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
        from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2 as BASEMODEL
    else:
        print('Model not defined. Choose from: EfficientNetB1, EfficientNetB7, and MobileNetV2.')

    # Read args
    DATAPATH = args.datapath
    CAMERA = args.cam
    IMAGESIZE = args.img
    BATCH_SIZE = args.batch  # 1: stochastic

    # Variables
    IMG_SHAPE = (IMAGESIZE, IMAGESIZE)
    TRAINING_DIR = DATAPATH + CAMERA + '/train'
    TEST_DIR = DATAPATH + CAMERA + '/test'
    SEED = 10

    # Create more images
    data_generator = ImageDataGenerator(
        validation_split=0.2,
        width_shift_range=0.2,
        height_shift_range=0.2,
        preprocessing_function=preprocess_input,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest',
    )

    val_data_generator = ImageDataGenerator(
        preprocessing_function=preprocess_input,
        validation_split=0.2,
    )

    train_generator = data_generator.flow_from_directory(
        TRAINING_DIR,
        target_size=IMG_SHAPE,
        shuffle=True,
        seed=SEED,
        class_mode='categorical',
        batch_size=BATCH_SIZE,
        subset='training',
    )

    validation_generator = val_data_generator.flow_from_directory(
        TRAINING_DIR,
        target_size=IMG_SHAPE,
        shuffle=False,
        seed=SEED,
        class_mode='categorical',
        batch_size=BATCH_SIZE,
        subset='validation',
    )

    test_generator = ImageDataGenerator(
        preprocessing_function=preprocess_input,
    )

    test_generator = test_generator.flow_from_directory(
        TEST_DIR,
        target_size=IMG_SHAPE,
        shuffle=False,
        seed=SEED,
        class_mode='categorical',
        batch_size=BATCH_SIZE,
    )

    nb_train_samples = train_generator.samples
    nb_validation_samples = validation_generator.samples
    # nb_test_samples = test_generator.samples
    classes = list(train_generator.class_indices.keys())
    print('Classes: ' + str(classes))
    num_classes = len(classes)

    # Transfer Learning
    base_model = BASEMODEL(
        weights='imagenet',
        include_top=False,
        input_shape=(IMG_SHAPE[0], IMG_SHAPE[1], 3),
    )

    x = base_model.output
    x = Flatten()(x)
    x = Dense(100, activation='relu')(x)

    predictions = Dense(
        num_classes,
        activation='softmax',
        kernel_initializer='random_uniform',
    )(x)

    model = Model(inputs=base_model.input, outputs=predictions)

    # Freezing pretrained layers
    for layer in base_model.layers:
        layer.trainable = False

    optimizer = Adam()
    model.compile(
        optimizer=optimizer,
        loss='categorical_crossentropy',
        metrics=['accuracy'],
    )

    # Saving the best model
    callbacks_list = [
        keras.callbacks.ModelCheckpoint(
            filepath=f'{CAMERA}_{args.basemodel}.h5',
            monitor='val_loss',
            save_best_only=True,
            verbose=1,
        ),
        keras.callbacks.EarlyStopping(
            monitor='val_loss',
            # model will stop training if she doesn't improve (10 attempts)
            patience=100,
            verbose=1,
        ),
    ]

    history = model.fit(
        train_generator,
        steps_per_epoch=nb_train_samples // BATCH_SIZE,
        epochs=args.epoch,
        callbacks=callbacks_list,
        validation_data=validation_generator,
        verbose=1,
        validation_steps=nb_validation_samples // BATCH_SIZE,
    )

    # Load best model
    model = load_model(f'{CAMERA}_{args.basemodel}.h5')

    # Reports
    train_score = model.evaluate(train_generator)
    val_score = model.evaluate(validation_generator)
    test_score = model.evaluate(test_generator)
    Y_pred = model.predict(test_generator)
    y_pred = np.argmax(Y_pred, axis=1)
    mcc = matthews_corrcoef(test_generator.classes, y_pred)
    target_names = classes
    if args.reports == 'text' or args.reports == 'all':
        print('====' * 20)
        print('Results:')
        print('Train loss:', train_score[0])
        print('Train accuracy:', train_score[1])
        print('Val loss:', val_score[0])
        print('Val accuracy:', val_score[1])
        print('Test loss:', test_score[0])
        print('Test accuracy:', test_score[1])
        print('MCC:', mcc)
        print('====' * 20)
        print('Confusion Matrix - TEST (TN, FP, FN, TP)')
        print(confusion_matrix(test_generator.classes, y_pred))
        print('====' * 20)
        print('Classification Report')
        print(
            classification_report(
                test_generator.classes,
                y_pred, target_names=target_names,
            ),
        )
        print('====' * 20)
        print('Metadata')
        print(
            f'Base model: {args.basemodel} \nCamera: {args.cam}\nImage size: {args.img}x{args.img}',
        )
    if args.reports == 'graph' or args.reports == 'all':
        def plot_hist(hist):
            fig, ax = plt.subplots(1, 2, figsize=(10, 5))
            ax[0].plot(hist.history['loss'], color='b', label='Training')
            ax[0].plot(
                hist.history['val_loss'], color='r',
                label='Validation', axes=ax[0],
            )
            ax[0].set_xlabel('Epoch')
            ax[0].set_ylabel('Loss')
            # legend = ax[0].legend(loc='best', shadow=True)
            ax[1].plot(hist.history['accuracy'], color='b', label='Training')
            ax[1].plot(
                hist.history['val_accuracy'],
                color='r', label='Validation',
            )
            ax[1].set_xlabel('Epoch')
            ax[1].set_ylabel('Accuracy')
            # legend = ax[1].legend(loc='best', shadow=True)
            fig.suptitle(f'Training report: {CAMERA}_{args.basemodel}')
            fig.savefig(f'report_{CAMERA}_{args.basemodel}.png')

        plot_hist(history)


if __name__ == '__main__':
    main()
