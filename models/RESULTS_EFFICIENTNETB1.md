# Results:

Train loss: 0.3028409481048584
Train accuracy: 0.9090909361839294
Val loss: 0.2622383236885071
Val accuracy: 0.90625
Test loss: 0.43326535820961
Test accuracy: 0.8833333253860474
MCC: 0.7705289916987292
================================================================================
Confusion Matrix - TEST (TN, FP, FN, TP)
[[25  5]
 [ 2 28]]
================================================================================
Classification Report
              precision    recall  f1-score   support

       alarm       0.93      0.83      0.88        30
      normal       0.85      0.93      0.89        30

    accuracy                           0.88        60
   macro avg       0.89      0.88      0.88        60
weighted avg       0.89      0.88      0.88        60

================================================================================
Metadata
BEST EPOCH: 12
Base model: EfficientNetB1
Camera: FI_C0166000
Image size: 240x240
Batch: 32
python train.py --basemodel EfficientNetB1 --datapath  --cam FI_C0166000 --im  58,14s user 1,85s system 108% cpu 55,220 total
