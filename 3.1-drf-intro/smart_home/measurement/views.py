# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response
# from rest_framework.generics import
from rest_framework.decorators import api_view
from .models import Sensor
from .serializers import SensorSerializer


@api_view(['GET', 'POST'])
def demo(request):
    if request.method == 'GET':
        sensors = Sensor.objects.all()
        ser = SensorSerializer(sensors, many=True)
        return Response(ser.data)
    if request.method == 'POST':
        return Response({'status': 'OK'})
