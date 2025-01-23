from django.urls import path
from .views import UploadDataView, TrainModelView, PredictView

urlpatterns = [
    path('upload/', UploadDataView.as_view(), name='upload_data'),
    path('train/', TrainModelView.as_view(), name='train_model'),
    path('predict/', PredictView.as_view(), name='predict'),
]
