# Deep Learning applied to Road Accident Detection with Transfer Learning and Synthetic Images (conference paper)

<!-- Published paper: https://doi.org/DOI -->

The project uses transfer learning (base models: EfficientNetB1 or MobileNetB2) with deep learning to train a model to detect road accidents. Thus, images from a road surveillance camera installed on highway 102 (Near Helsinki) is used as a source. As there were no accidents to train the model, the team generated synthetic images of accidents. The last layer of the base model (classes) was eliminated, and the model was retrained to identify images classified as normal (no accident) and alarm (with accident).

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
