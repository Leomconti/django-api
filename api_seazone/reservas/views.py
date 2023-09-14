from reservas.models import Reserva, ReservaSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get(request, pk):
    try:
        reserva = Reserva.objects.get(pk=pk)
    except Reserva.DoesNotExist:
        return Response(status=404)
    serializer = ReservaSerializer(reserva)
    return Response(serializer.data)  # 200 ok

@api_view(['GET'])
def get_list(request):
    reservas = Reserva.objects.all()
    serializer = ReservaSerializer(reservas, many=True)
    return Response(serializer.data)  # 200 ok

@api_view(['GET','POST'])
def delete(request, pk):
    try:
        reserva = Reserva.objects.get(pk=pk)
    except Reserva.DoesNotExist:
        return Response(status=404)  # 404 not found
    reserva.delete()
    return Response(status=204)  # 204 no content