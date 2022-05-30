# Deep Learning applied to Road Accident Detection with Transfer Learning and Synthetic Images (conference paper)

<!-- Published paper: https://doi.org/DOI -->

## Abstract

Artificial Intelligence (AI) has driven solutions in diverse areas. In road safety, Computer Vision (CV) has presented solutions to detect road accidents. The focus is on Vision Zero, i.e., eliminate all traffic fatalities and severe injuries. However, when an accident occurs, response time is essential. Thinking about this problem of rapid accident detection, several countries have cameras monitoring the road network. However, the surveillance of these infrastructures requires a considerable number of people with training and attention. Our project automates this with AI, using deep learning to train a model to detect probable accidents. The CV method based on binary image classification was used, being images without accidents classified as normal and images with accidents as alarm. The biggest challenge in the development of this model was to obtain images of accidents in the images of the analyzed cameras. Hence, the solution adopted was to create synthetic images of these rare events. Several architectures of Convolutional Neural Networks (CNNs) were tested, and it was found that the best approach was to use transfer learning. As base models for transfer learning, the best results were EfficientNetB1 and MobileNetV2. The former for its quality in prediction and the latter for its size and execution speed. As a case study, open data images from Finnish road surveillance cameras were used, provided every ten minutes. It was found that the solution trained with EfficientNetB1 as the base model has a Mean Average Precision (mAP) of 0.89 and a Matthews Correlation Coefficient (MCC) of 0.77. The solution based on MobileNetV2 has an mAP of 0.88 and an MCC of 0.71. Finally, a proof-of-concept has been made available at [image2alarm.herokuapp.com](https://image2alarm.herokuapp.com/).

## Concept

![Concept](https://github.com/tamagusko/nordicopendata/raw/zirp/img/conceptPaper.png)

## Technical Details
You can see more details about the models [here.](https://github.com/tamagusko/nordicopendata/tree/zirp/models)

## MVP
### Site: [image2alarm.herokuapp.com/](https://image2alarm.herokuapp.com/) (base model: MobileNetV2)

![MVP](https://github.com/tamagusko/nordicopendata/raw/zirp/img/preview.gif)

## How to use MVP

Just drag and drop images from trained cameras:

- [FI_C0151303](https://github.com/tamagusko/nordicopendata/tree/main/data/FI_C0151303)
- [FI_C0166000](https://github.com/tamagusko/nordicopendata/tree/zirp/data/FI_C0166000)

<!--
## Citation

Tamagusko, Tiago; Correia, Matheus; Ferreira, Adelino (2022). Deep Learning applied to Road Accident Detection with Transfer Learning and Synthetic Images. JOURNAL. https://doi.org/DOI

```bibtex
@article{Tamagusko-etal2022,
  author = {Tiago Tamagusko and Matheus Correia and Adelino Ferreira},
  title = "{Data-Driven Approach to Understand the Mobility Patterns of the Portuguese Population during the COVID-19 PandemicDeep Learning applied to Road Accident Detection with Transfer Learning and Synthetic Images}",
  keywords = {Road Accidents - Computer Vision - Deep Learning - Image Classification - Transfer Learning - Synthetic Data},
  journal = {JOURNAL},
  doi = {DOI NUMBER},
  year = {2022}
}
```

-->
---

Codes are protected. Please see [LICENSE](LICENSE) for details.
