# Nordic AI & Open Data Hackathon (18-19 of March 2022)

### Intelligent Real-time Accident Warning System (IRAWS)

The project uses transfer learning (base model: EfficientNetB1) with deep learning to train a model to detect unusual events (skids, vehicles off-street, and on the wrong lane). To this end, images from the cameras of the Nordic countries' highways provided in the dataset were used. The team generated fake images from these real ones to simulate the unusual events. The last layer of the base model (classes) was eliminated, and the model was retrained to identify roads with normal flow and unusual events.

## Team:

[Matheus Correia](https://github.com/matheusgomesms) (transportation specialist)  
[Minh Anh Huynh](https://github.com/MarcX23) (backend dev/speaker)  
[Tiago Tamagusko](https://github.com/tamagusko) (backend dev/transportation specialist)  

## Problem

Identify vehicles that have slipped, veered off the road, or are on the wrong lane.

## Concept

![Concept](https://github.com/tamagusko/nordicaiopendataimages/raw/main/img/concept.png)

## MVP
[image2alarm.herokuapp.com/](https://image2alarm.herokuapp.com/) (base model: MobileNetV2)  
![MVP](https://github.com/tamagusko/nordicaiopendataimages/raw/main/img/mvp.gif)  
[Youtube](https://youtu.be/xKLlYaEs0Bc)

---

Codes and data are protected. Please see [LICENSE](LICENSE) for details.
