# Diamond Price Prediction

## Project Description

The Diamond Price Prediction project is a Machine Learning application developed using Python, Streamlit, and Scikit-learn. The application predicts the price of a diamond based on its physical and quality characteristics.

A Linear Regression model is trained using the Diamond dataset. The trained model is saved using Joblib and used in the Streamlit web application to predict diamond prices based on user input.

---

## Objectives

- Predict diamond prices using Machine Learning.
- Build an interactive web application using Streamlit.
- Apply data preprocessing techniques such as One-Hot Encoding and Feature Scaling.
- Save and reuse the trained model for prediction.

---

## Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- Joblib

---

## Project Structure

```
Diamond Price Prediction/
│
├── app.py
├── train_model.py
├── diamond(3).csv
├── LR_model.pkl
├── scaler.pkl
├── columns.pkl
└── README.md
```

---

## Dataset Information

The dataset contains information about diamonds and their selling prices.

### Target Variable

- Price – Selling price of the diamond.

---

## Input Features

The application accepts the following input features:

| Feature | Description |
|---------|-------------|
| Carat | Weight of the diamond |
| Cut | Quality of the diamond cut |
| Color | Diamond color grade |
| Clarity | Diamond clarity grade |
| Depth | Total depth percentage |
| Table | Width of the top facet |
| X | Length of the diamond (mm) |
| Y | Width of the diamond (mm) |
| Z | Depth of the diamond (mm) |

---

## Machine Learning Algorithm

- Linear Regression

---

## Data Preprocessing

The following preprocessing steps are performed before training the model:

- Handling input features
- One-Hot Encoding for categorical variables
- Feature Scaling using StandardScaler
- Train-Test Split
- Model Training using Linear Regression

---

## Features

- Simple and user-friendly interface
- Numerical input fields
- Dropdown selection for categorical values
- Automatic data preprocessing
- Real-time diamond price prediction
- Uses a trained Linear Regression model
- Fast and accurate predictions

---

## Files Generated

The training process generates the following files:

- LR_model.pkl
- scaler.pkl
- columns.pkl

These files are loaded by the Streamlit application during prediction.

---

## How to Run the Project

### Step 1: Install Required Libraries

```bash
pip install streamlit pandas scikit-learn joblib
```

### Step 2: Train the Model

```bash
python train_model.py
```

This command creates:

- LR_model.pkl
- scaler.pkl
- columns.pkl

### Step 3: Run the Application

```bash
streamlit run app.py
```

---

## Application Workflow

1. Enter the diamond details.
2. Click the **Predict Price** button.
3. The application creates a DataFrame from the input.
4. One-Hot Encoding is applied.
5. Feature Scaling is performed.
6. The trained model predicts the diamond price.
7. The predicted price is displayed on the screen.

---

## Expected Output

The application displays the predicted diamond price based on the values entered by the user.

---

## Future Enhancements

- Improve prediction accuracy using advanced machine learning algorithms.
- Add data visualization and charts.
- Deploy the application on Streamlit Cloud.
- Support multiple machine learning models for comparison.

---

## Developed By

**Name:** Your Name

**Course:** Artificial Intelligence and Machine Learning (AIML)

**Project:** Diamond Price Prediction

---

## License

This project is developed for educational and academic purposes.