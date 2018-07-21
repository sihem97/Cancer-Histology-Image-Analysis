# Predicting Invasive Ductal Carcinoma (IDC) through Breast Cancer Histology Images

### What is Invasive Ductal Carcinoma?
Breast cancer is the most common form of cancer in women. Invasive ductal carcinoma (IDC) is the most common form of breast cancer. Accurately identifying and categorizing breast cancer subtypes is an important clinical task, and automated methods can be used to save time and reduce error. The progression of in situ ductal carcinoma leads to IDC, which then progresses into metastatic disease.

### Our Data

The dataset consists of 277,524 50x50 pixel RGB digital image patches that were derived from 162 H&E-stained breast histopathology samples. These images are small patches that were extracted from digital images of breast tissue samples. The breast tissue contains many cells but only some of them are cancerous. Patches that are labeled "1" contain cells that are characteristic of invasive ductal carcinoma. 

### Our Models: How were the IDC Images Classified?
Test VS Train Selection

- Convolutional Neural Networks (CNN)
- k-Nearest Neighbors
- Support Vector Machines
- Random Forest, xgBoost

### Our Results (CNN)
##### Summary

|             Method           |acccuracy|sensitivity|
| ---------------------------- |---------|-----------|
|    Support Vector Machine    | 0.7638  |  0.7317   |
|      k-Nearest Neighbors     | 0.7403  |  0.7626   |
|     Random Forest, xgBoost   | 0.7899  |  0.7641   |
| Convolutional Neural Network | 0.8248  |    N/A    |

acc: train data's accuracy
val-acc: test data's accuracy.

A low Val-acc and high acc is indicative of overfitting. Our results show that Epoch 5 exhibits overfitting, where val-acc is 74.40% but acc is 98.09%. The model fits the train data with 98.09% accuracy but when applied to the test data, accuracy is 74.40%

|  Epoch #  |  acc   |  val_acc |
| --------- | ------ | -------- |
|     1     | 0.7024 |  0.8248  |
|     2     | 0.8516 |  0.7597  |
|     3     | 0.9410 |  0.7874  |
|     4     | 0.9685 |  0.7466  |
|     5     | 0.9809 |  0.7440  |
|     6     | 0.9847 |  0.7591  |
|     7     | 0.9880 |  0.7612  |
|     8     | 0.9901 |  0.7720  |
|     9     | 0.9902 |  0.7665  |
|     10    | 0.9927 |  0.7733  |



