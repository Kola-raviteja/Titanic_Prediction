# Titanic Survival Prediction 

## Project Overview
The Titanic Survival Prediction project is a Machine Learning classification problem where the objective is to predict whether a passenger survived the Titanic disaster based on their personal and travel-related details.

This project demonstrates a complete **end-to-end data science workflow**, including data exploration, preprocessing, feature engineering, model building, and evaluation. It is designed as a beginner-to-intermediate level project suitable for learning and portfolio presentation.

---

## Dataset Description
The dataset used in this project is the **Titanic dataset**, originally provided by Kaggle.

- **Source**: Kaggle Titanic Dataset  
- **Type**: Structured tabular data  
- **Rows**: Passenger records  
- **Columns**: Demographic and travel information  

### Target Variable
- `Survived`
  - `0` → Passenger did not survive
  - `1` → Passenger survived

This makes the problem a **binary classification task**.

---

## Feature Explanation
The dataset contains the following important features:

- `Pclass` – Passenger class (1st, 2nd, 3rd)
- `Sex` – Gender of the passenger
- `Age` – Age of the passenger
- `SibSp` – Number of siblings or spouses aboard
- `Parch` – Number of parents or children aboard
- `Fare` – Ticket fare paid
- `Embarked` – Port of embarkation (C, Q, S)

These features are used as input variables to predict survival.

---

## Tools & Libraries Used
The project is implemented using Python and popular data science libraries:

- **Python** – Core programming language
- **Pandas** – Data manipulation and analysis
- **NumPy** – Numerical computations
- **Matplotlib & Seaborn** – Data visualization
- **Scikit-learn** – Machine learning models and preprocessing

---

## Project Workflow (Step-by-Step)

### Data Understanding & Exploration (EDA)
In this step:
- The dataset structure is analyzed
- Missing values are identified
- Statistical summaries are reviewed
- Visualizations are created to understand data distribution and relationships

This helps in identifying patterns such as:
- Survival rate by gender
- Survival rate by passenger class
- Effect of age and fare on survival

---

### Data Preprocessing
Before training the model, the data is cleaned and prepared:

- Missing values are handled using appropriate strategies
- Categorical variables like `Sex` and `Embarked` are encoded
- Numerical features are scaled where necessary
- Dataset is split into training and testing sets

This ensures the data is suitable for machine learning models.

---

### Feature Engineering
Feature engineering involves:
- Selecting relevant features
- Transforming categorical data into numerical format
- Removing unnecessary or redundant columns

This step improves model performance and interpretability.

---

### Model Building
Multiple machine learning models are trained to predict survival:

- **Logistic Regression**
  - Used as a baseline linear classification model
- **Random Forest Classifier**
  - A tree-based ensemble model that handles non-linearity and feature interactions effectively

Each model is trained using the same preprocessed dataset to allow fair comparison.

---

### Model Evaluation
The performance of each model is evaluated using:

- **Accuracy Score** – Overall correctness of predictions
- **Confusion Matrix** – Breakdown of true/false predictions
- **Classification Report** – Precision, recall, and F1-score

This helps in selecting the best-performing model.

---

## Results & Observations
- Tree-based models performed better than linear models
- Gender and passenger class were strong predictors of survival
- Random Forest handled non-linear relationships more effectively
- The final model achieved good generalization on unseen data

---

