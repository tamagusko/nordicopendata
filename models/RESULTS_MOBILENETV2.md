## Using:

Python version: 3.8.13 (default, Apr 18 2022, 15:15:58)
[GCC 11.2.0]  
TensorFlow version: 2.8.0  
tf.keras version: 2.8.0  

## Results:

Train loss: 0.32010889053344727  
Train accuracy: 0.8636363744735718  
Val loss: 0.5249947309494019  
Val accuracy: 0.71875  
Test loss: 0.4787507951259613  
Test accuracy: 0.8166666626930237  
MCC: 0.6807456457050177  

Confusion Matrix - TEST (TN, FP, FN, TP)  
[[19 11]  
 [ 0 30]]  

## Classification Report  

              precision    recall  f1-score   support

       alarm       1.00      0.63      0.78        30
      normal       0.73      1.00      0.85        30

    accuracy                           0.82        60
    macro avg      0.87      0.82      0.81        60
    weighted avg   0.87      0.82      0.81        60



## Metadata:

Base model: MobileNetV2  
Camera: FI_C0166000  
Image size: 160x160  
Batch: 32  
Best Epoch: 17  
Time to train: 38s  
