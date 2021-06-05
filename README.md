# Leukemia-detector

![Screenshot_22](https://user-images.githubusercontent.com/71597038/120902457-3c35c080-c649-11eb-985e-4d6b1b7d3cac.png)

File map:

0. working.json -- params for launch 
1. launcher -- running the distributor function
2. distributor -- main pipeline

DataBuilder:
1. Take the input data and chunk it into 16 pieces(normalizing will be added later),
2. Putting into PyTorchs data loader;

Model:
1. defining the model and parameters to work with (U-Net architecture);

Predictor:
1. Standart prediction step,
2. Putting together previously chunked data;

Utility worker:
1. Count the division between "bad/good" cells,
2. Makes edge-map from predicted data (using canny edge filter),
3. Applies this map onto an input image,
4. Visualisation processed data.
