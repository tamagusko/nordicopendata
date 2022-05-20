Results:

Train loss: 0.2786875069141388
Train accuracy: 0.8939393758773804
Val loss: 0.4845251441001892
Val accuracy: 0.78125
Test loss: 0.49772122502326965
Test accuracy: 0.8333333134651184
MCC: 0.7071067811865475
================================================================================
Confusion Matrix - TEST (TN, FP, FN, TP)
[[20 10]
 [ 0 30]]
================================================================================
Classification Report
              precision    recall  f1-score   support

       alarm       1.00      0.67      0.80        30
      normal       0.75      1.00      0.86        30

    accuracy                           0.83        60
   macro avg       0.88      0.83      0.83        60
weighted avg       0.88      0.83      0.83        60

================================================================================
Metadata
Best Epoch: 17
Base model: MobileNetV2
Camera: FI_C0166000
Image size: 160x160
Batch: 32
python train.py --basemodel MobileNetV2 --datapath  --cam FI_C0166000 --img    47,32s user 1,56s system 114% cpu 42,640 total
