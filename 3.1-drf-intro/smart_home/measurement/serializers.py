from rest_framework import serializers

from .models import Sensor, Measurement
# TODO: опишите необходимые сериализаторы


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id', 'sensor_id', 'temperature', 'measurement_date']


class SensorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


# class SensorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Sensor
#         fields = ['id', 'name', 'description']
#
