#  Credit Scoring Model

A machine learning project developed as part of my **CodeAlpha Machine Learning Internship**.

The objective of this project is to predict an applicant's **creditworthiness** using financial and credit-related information. Multiple classification algorithms were trained and evaluated, and the best-performing model was used to build an interactive **Streamlit web application**.

---

##  Project Overview

Credit scoring is used to estimate whether an applicant is likely to be creditworthy based on their financial profile and previous credit behaviour.

This project follows a complete machine learning workflow:

- Exploratory Data Analysis (EDA)
- Data preprocessing
- Model training
- Cross-validation
- Model comparison
- Final model evaluation
- Streamlit web application

The final application allows a user to enter applicant details and receive a prediction of whether the applicant is **Creditworthy** or **Not Creditworthy**.

---

##  Features Used

The model uses the following applicant information:

- Age
- Annual Income
- Employment Years
- Monthly Debt
- Debt-to-Income Ratio
- Credit Utilization
- Late Payments
- Credit History Years
- Number of Credit Accounts
- Loan Amount
- Previous Defaults
- Payment History Score
- Home Ownership
- Marital Status
- Education Level

The target variable is:

**Creditworthy**

---

##  Exploratory Data Analysis

Exploratory Data Analysis was performed before model training to understand the dataset and identify patterns in the features.

The EDA includes analysis of:

- Dataset structure
- Missing values
- Numerical features
- Categorical features
- Feature distributions
- Relationships between different financial attributes
- Target variable distribution
- Correlation between numerical variables

The EDA is available in:

`EDA.ipynb`

---

##  Data Preprocessing

The dataset contains both numerical and categorical features, so preprocessing is performed before training the models.

The preprocessing workflow includes:

- Handling missing values
- Encoding categorical variables
- Scaling numerical features where required
- Separating features and target variable
- Splitting the dataset into training and testing sets

A machine learning pipeline is used so that preprocessing and prediction can be performed consistently.

---

##  Models Used

Four classification algorithms were trained and compared:

1. Logistic Regression
2. Decision Tree Classifier
3. Random Forest Classifier
4. Gradient Boosting Classifier

Cross-validation was used to compare the models using **Accuracy, Precision, Recall, and F1 Score**.

### Cross-Validation Results

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---:|---:|---:|---:|
| Logistic Regression | 0.995506 | 0.997297 | 0.997260 | 0.997260 |
| Decision Tree | **0.997753** | **1.000000** | 0.997260 | **0.998621** |
| Random Forest | 0.995506 | 0.997297 | 0.997260 | 0.997260 |
| Gradient Boosting | 0.995506 | 0.997297 | 0.997260 | 0.997260 |

Based on the cross-validation results, the **Decision Tree Classifier** achieved the best overall performance and was selected as the final model.

---

##  Final Model Performance

The selected Decision Tree model was evaluated on the test dataset.

| Metric | Score |
|---|---:|
| Accuracy | **0.9948** |
| Precision | **0.9935** |
| Recall | **1.0000** |
| F1 Score | **0.9968** |
| ROC-AUC | **0.9865** |

The model achieved approximately **99.48% test accuracy** with a recall of **1.0**.

These results indicate strong performance on the dataset used for this project.

---

##  Streamlit Web Application

An interactive web application was created using **Streamlit**.

The application allows users to enter information such as:

- Income and debt
- Employment history
- Credit utilization
- Previous defaults
- Payment history
- Loan amount
- Personal information

The submitted information is converted into the required input format and passed to the trained machine learning pipeline.

The application then displays one of two predictions:

-  **Creditworthy**
-  **Not Creditworthy**

---

##  Project Structure

```text
CodeAlpha_CreditScoringModel/
│
├── Data/
│   └── credit_data.csv
│
├── Model/
│   └── Decision_tree_Pipeline.pkl
│
├── Notebook/
│   ├── EDA.ipynb
│   └── Training.ipynb
├── app.py
├── .gitignore
├── requirements.txt
└── README.md
```

### File Description

**`EDA.ipynb`**  
Contains exploratory data analysis and visualization of the dataset.

**`Training.ipynb`**  
Contains data preprocessing, model training, cross-validation, model comparison, and final model evaluation.

**`Decision_tree_Pipeline.pkl`**  
Saved machine learning pipeline containing the selected Decision Tree model and required preprocessing.

**`app.py`**  
Streamlit application used to interact with the trained model.

---

##  Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Streamlit
- Joblib
- Jupyter Notebook

---

##  Running the Project

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd CodeAlpha_CreditScoringModel
```

### 2. Install the required packages

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit application

```bash
streamlit run app.py
```

The application will then open in your browser.

---

##  Machine Learning Workflow

```text
Dataset
   ↓
Exploratory Data Analysis
   ↓
Data Preprocessing
   ↓
Train/Test Split
   ↓
Model Training
   ↓
Cross-Validation
   ↓
Model Comparison
   ↓
Decision Tree Selection
   ↓
Final Evaluation
   ↓
Save Pipeline
   ↓
Streamlit Application
```

---

##  Disclaimer

This project was developed for **educational and internship purposes**.

The predictions generated by the model should not be used to make real-world lending, credit approval, or financial decisions. Model performance represents results on the dataset used in this project and does not imply equivalent performance on real-world financial data.

---

## 👨 Author

**Saurodeep De**

Machine Learning Internship Project  
**CodeAlpha**

---

##  Internship Task

**Task 1: Credit Scoring Model**

Build a model to predict an individual's creditworthiness using financial data and appropriate classification algorithms, and evaluate the model using metrics such as Precision, Recall, F1 Score, and ROC-AUC.
