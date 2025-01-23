
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score

class ModelHandler:
    def __init__(self):
        self.data = None
        self.model = None
        self.target_column = "Downtime_Flag"

    def set_data(self, df: pd.DataFrame):
        self.data = df

    def data_available(self):
        return self.data is not None

    def train(self):
        if self.data is None:
            raise ValueError("No data available to train.")

        X = self.data.drop(columns=["Machine_ID", self.target_column])
        y = self.data[self.target_column]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        self.model = LogisticRegression()
        self.model.fit(X_train, y_train)

        y_pred = self.model.predict(X_test)
        metrics = {
            "accuracy": accuracy_score(y_test, y_pred),
            "f1_score": f1_score(y_test, y_pred)
        }
        return metrics

    def predict(self, input_data: dict):
        if self.model is None:
            raise ValueError("Model has not been trained.")

        input_df = pd.DataFrame([input_data])
        input_df = input_df.drop(columns=["Machine_ID"], errors="ignore") 

        prediction = self.model.predict(input_df)[0]
        confidence = max(self.model.predict_proba(input_df)[0])
        return {"Downtime": "Yes" if prediction == 1 else "No", "Confidence": round(confidence, 2)}

