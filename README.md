# predictive_analysis
Predictive Analysis for Manufacturing Operations

## Manufacturing Downtime Prediction API

This is a RESTful API built with Django and Django REST Framework to predict machine downtime or production defects using a manufacturing dataset. The API supports endpoints for uploading data, training a machine learning model, and making predictions.

## Features

- **Upload Dataset**: Upload a CSV file containing manufacturing data.
- **Train Model**: Train a supervised machine learning model (e.g., Decision Tree) to predict downtime.
- **Make Predictions**: Provide input data (e.g., temperature, run time) to get predictions and confidence scores.

## Installation and Setup

### Prerequisites

- Python 3.8+
- pip

### Steps

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:
   ```bash
   python manage.py migrate
   ```

4. Run the development server:
   ```bash
   python manage.py runserver
   ```

5. The API will be available at `http://127.0.0.1:8000/`.

---

## Endpoints

### 1. **Upload Data**

**Endpoint**: `POST /upload/`

- **Description**: Upload a CSV file with columns such as `Machine_ID`, `Temperature`, `Run_Time`, and `Downtime_Flag`.
- **Request**: Multipart form-data with a file field named `file`.
- **Response**:
  ```json
  {
      "message": "Data uploaded successfully.",
      "columns": ["Machine_ID", "Temperature", "Run_Time", "Downtime_Flag"]
  }
  ```

### 2. **Train Model**

**Endpoint**: `POST /train/`

- **Description**: Train the model using the uploaded dataset.
- **Request**: No body required.
- **Response**:
  ```json
  {
      "message": "Model trained successfully.",
      "metrics": {"accuracy": 0.85, "f1_score": 0.80}
  }
  ```

### 3. **Make Predictions**

**Endpoint**: `POST /predict/`

- **Description**: Make a prediction using input features.
- **Request**:
  ```json
  {
      "Temperature": 80,
      "Run_Time": 120
  }
  ```
- **Response**:
  ```json
  {
      "Downtime": "Yes",
      "Confidence": 0.85
  }
  ```

---
