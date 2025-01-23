import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .model_handler import ModelHandler

model_handler = ModelHandler()

class UploadDataView(APIView):
    def post(self, request):
        file = request.FILES.get('file')
        if not file or not file.name.endswith('.csv'):
            return Response({"error": "Please upload a valid CSV file."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            df = pd.read_csv(file)
            model_handler.set_data(df)
            return Response({"message": "Data uploaded successfully.", "columns": list(df.columns)})
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class TrainModelView(APIView):
    def post(self, request):
        if not model_handler.data_available():
            return Response({"error": "No data available to train."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            metrics = model_handler.train()
            return Response({"message": "Model trained successfully.", "metrics": metrics})
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class PredictView(APIView):
    def post(self, request):
        input_data = request.data
        try:
            result = model_handler.predict(input_data)
            return Response(result)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
