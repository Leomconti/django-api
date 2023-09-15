from reservas.models import Reserva, ReservaSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get(request, pk):
    try:
        reserva = Reserva.objects.get(pk=pk)
    except Reserva.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ReservaSerializer(reserva)
    return Response(serializer.data)  # 200 ok

@api_view(['GET'])
def get_list(request):
    reservas = Reserva.objects.all()
    serializer = ReservaSerializer(reservas, many=True)
    return Response(serializer.data)  # 200 ok

@api_view(['DELETE'])
def delete(request, pk):
    try:
        reserva = Reserva.objects.get(pk=pk)
    except Reserva.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)  # 404 not found
    reserva.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)  # 204 no content
