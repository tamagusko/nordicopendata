# Nordic AI & Open Data Hackathon (18-19 of March 2022)

### Intelligent Real-time Accident Warning System (IRAWS)

The project uses transfer learning (base model: EfficientNetB1) with deep learning to train a model to detect unusual events (skids, vehicles off-street, and on the wrong lane). To this end, images from the cameras of the Nordic countries' highways provided in the dataset were used. The team generated fake images from these real ones to simulate the unusual events. The last layer of the base model (classes) was eliminated, and the model was retrained to identify roads with normal flow and unusual events.

## Team:

[Matheus Correia](https://github.com/matheusgomesms) (transportation specialist)  
[Minh Anh Huynh](https://github.com/MarcX23) (backend dev/speaker)  
[Tiago Tamagusko](https://github.com/tamagusko) (backend dev/transportation specialist)

## Concept ([Pitch](https://www.youtube.com/watch?v=thCYkNci55o))

![Concept](https://github.com/tamagusko/nordicopendata/raw/main/img/concept.png)

## Technical Detais
You can see more details about the models [here.](https://github.com/tamagusko/nordicopendata/tree/main/models)

## MVP
### Site: [image2alarm.herokuapp.com/](https://image2alarm.herokuapp.com/) (base model: MobileNetV2)

![MVP](https://github.com/tamagusko/nordicopendata/raw/main/img/preview.gif)

## How to use MVP

Just drag and drop images from trained cameras:

- [FI_C0151303](https://github.com/tamagusko/nordicopendata/tree/main/data/FI_C0151303)
- [FI_C0166000](https://github.com/tamagusko/nordicopendata/tree/main/data/FI_C0166000)

---

Codes and data are protected. Please see [LICENSE](LICENSE) for details.
