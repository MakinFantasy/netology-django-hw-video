# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementSerializer


class SensorView(CreateAPIView, ListAPIView):                           # Вывод и создание сенсоров

    serializer_class = SensorDetailSerializer

    def get_queryset(self):
        queryset = Sensor.objects.all()
        return queryset

    def sensor_create(self, serializer):
        serializer.save()


class UpdateSensor(RetrieveAPIView):                                   # Изменение сенсора
    serializer_class = SensorDetailSerializer

    def get_queryset(self):
        queryset = Sensor.objects.all()
        return queryset

    def sensor_update(self, serializer):
        serializer.save()


class MeasurementView(CreateAPIView, ListAPIView):

    serializer_class = MeasurementSerializer

    def get_queryset(self):
        queryset = Measurement.objects.all()
        return queryset

    def measurement_create(self, serializer):
        serializer.save()


class UpdateMeasurement(RetrieveAPIView):
    serializer_class = MeasurementSerializer

    def get_queryset(self):
        queryset = Measurement.objects.all()
        return queryset

    def measurement_update(self, serializer):
        serializer.save()
