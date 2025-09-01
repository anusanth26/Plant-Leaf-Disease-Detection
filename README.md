**Plant Disease Classification Using Machine Learning**

**Project Overview**

This project focuses on image classification using different machine learning algorithms and a combination of color, texture, and shape features. The goal was to evaluate multiple models and identify the most effective approach for achieving high accuracy and robustness on unseen data.

We experimented with Support Vector Machine (SVM), K-Nearest Neighbors (KNN), Random Forest (RF), and XGBoost classifiers, each trained on progressively richer feature sets.

**To Download Dataset:**
  
  --> Link: https://www.kaggle.com/datasets/emmarex/plantdisease?select=PlantVillage
  
  --> Execute the **download_dataset.py** file from the repository

**Features Extracted**

Color Features:

  -->Mean Color

  -->Color Histogram (RGB/HSV)

  -->Color Moments (Statistical Moments)

Texture Features:

  -->Local Binary Pattern (LBP)

  -->Gray Level Co-occurrence Matrix (GLCM)

Shape Features:

  -->Contour Descriptors: Aspect Ratio, Extent, Solidity

##  Models & Results

| Model | Features Used | Accuracy |
|-------|---------------|----------|
| **SVM** | Mean Color, Color Histogram, Color Moments, HSV | 91.49% |
| **SVM (Extended)** | Above + LBP, GLCM | 93.12% |
| **KNN** | Color Moments, HSV Histogram, LBP, GLCM, Shape Features | 95.44% (Overfitting on unseen data) |
| **Random Forest** | Statistical Moments, 3D Color Histogram, LBP, GLCM, Shape Features | 97.14% |
| **XGBoost** | Statistical Moments, 3D Color Histogram, LBP, GLCM, Shape Features | 98.13% |

**Key Observations**

SVM showed strong baseline performance but improved further with texture features.

KNN achieved high accuracy but struggled with generalization, leading to overfitting.

Random Forest provided stable performance with richer features.

XGBoost achieved the highest accuracy (98%) due to its boosting mechanism and hyperparameter tuning, and generalized well on unseen data.

**Conclusion**

The project demonstrates that combining color, texture, and shape features significantly improves classification accuracy. Among all models, XGBoost proved to be the most effective, offering both high accuracy and robustness on unseen data. This highlights the importance of advanced ensemble methods and feature richness in image classification tasks.

**Future Works**

Extend feature extraction with deep learning–based embeddings (CNNs).

Explore transfer learning using pretrained networks (ResNet, VGG).

Deploy the best model as a web application for real-time image classification.
