# Leukemia-detector

![Screenshot_22](https://user-images.githubusercontent.com/71597038/120902457-3c35c080-c649-11eb-985e-4d6b1b7d3cac.png)

File map:
0. working.json -- params for launch 
1. launcher -- running the distributor function
2. distributor -- main pipeline:
  2.a. DataBuilder
    2.a.0. take the input data and chunck into 16 pieses(normalizing 'll be added later)
    2.a.1. putting into PyTorchs dataloader
  2.b. Model
    2.b.0. defining the model and parameters to work with (U-Net architecture)
  2.c. Predictor (standart prediction step)
  2.e. Utility worker
    2.e.0. count the division between "bad/good" cells amout
    2.e.1. makes edge-map from predicted data (using canny edge filter)
    2.e.2. applies this map onto an input image
    2.e.3. visualisating processed data
