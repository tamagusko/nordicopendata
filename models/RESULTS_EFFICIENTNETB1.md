Using:

Python version: 3.8.13 (default, Apr 18 2022, 15:15:58)
[GCC 11.2.0]
TensorFlow version: 2.8.0
tf.keras version: 2.8.0
================================================================================
================================================================================
Results:

Train loss: 0.22786952555179596
Train accuracy: 0.8787878751754761
Val loss: 0.20868703722953796
Val accuracy: 0.9375
Test loss: 0.42413902282714844
Test accuracy: 0.8833333253860474
MCC: 0.7775419143502352
================================================================================
Confusion Matrix - TEST (TN, FP, FN, TP)
[[24  6]
 [ 1 29]]
================================================================================
Classification Report

              precision    recall  f1-score   support

       alarm       0.96      0.80      0.87        30
      normal       0.83      0.97      0.89        30

    accuracy                           0.88        60
   macro avg       0.89      0.88      0.88        60
weighted avg       0.89      0.88      0.88        60

================================================================================
Metadata:

Base model: EfficientNetB1
Camera: FI_C0166000
Image size: 240x240
Batch: 32
Best Epoch: 26
Time to train: 72s
