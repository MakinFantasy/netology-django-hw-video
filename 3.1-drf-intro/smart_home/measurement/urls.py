from django.urls import path

from .views import SensorView, UpdateSensor, UpdateMeasurement, MeasurementView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', UpdateSensor.as_view()),
    path('measurements/', MeasurementView.as_view()),
    path('measurements/<pk>/', UpdateMeasurement.as_view()),
]
