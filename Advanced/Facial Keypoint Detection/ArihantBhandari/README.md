### **Goal**

The objective of this project is to predict 15 essential facial key-points like center of eyes, edge-points of eyebrows and so on by using images.

### **Methodology Followed**

To achieve our goals, the following steps were implemented:

- Images were loaded using keras.utils and normalized to the range 0 to 1.

- Labels were used to lock onto features for each image.

- Features have been normalized using a MinMaxScaler.

- Images were resized to a fixed size of 96X96 pixels.

- Custom and pre-trained models were used for this task.

### **Exploratory Data Analysis Results**

#### **EDA**

##### Images with Actual Keypoints

<p align="center">
  <img src="https://github.com/DSCVITBHOPAL/Summer-of-Open-Source-ML-Projects/blob/facial-keypoint/Advanced/Facial%20Keypoint%20Detection/ArihantBhandari/Images/EDA%201.png" height="400px" width="400px" />
  <img src="https://github.com/DSCVITBHOPAL/Summer-of-Open-Source-ML-Projects/blob/facial-keypoint/Advanced/Facial%20Keypoint%20Detection/ArihantBhandari/Images/EDA%202.png" height="400px" width="400px" />
</p>

### **Performance of the Models based on the Accuracy Scores**

#### Metrics: 

We used **Validation** and **Test** **Mean Squared Error (MSE)** and **Mean Absolute Error (MAE)** as metrics.

| Models | Validation MSE | Validation MAE | Test MSE | Test MAE |
|--------|---------------------|--------------------------|---------------------|--------------------------|
| ResNet-50 | 0.0022 | 0.0221 | 0.0020 | 0.0218 |
| InceptionV3 | 0.0023  | 0.0277 | 0.0021 | 0.0273 | 
| CNN | 0.0015 | 0.0213 | 0.0013 | 0.0214 |
| VGG16 | 0.0022 | 0.0262 | 0.0019 | 0.0253 |
| MobileNet | 0.0023 | 0.0278 | 0.0022 | 0.0280 |
| DenseNet-121 | 0.0019 | 0.0245 | 0.0017 | 0.0240 |
| Xception | 0.0019 | 0.0240 | 0.0018 | 0.0239 |

### **Conclusion**

We conclude the following:

All models work well on the task; **CNN**, **DenseNet-121**, **Xception**, **VGG-16** and **Resnet-50** are ideal for this.
