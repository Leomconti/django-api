from imoveis.models import Imovel, ImovelSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get(request, pk):
    try:
        imovel = Imovel.objects.get(pk=pk)
    except Imovel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ImovelSerializer(imovel)
    return Response(serializer.data)  # 200 ok

@api_view(['GET'])
def get_list(request):
    imoveis = Imovel.objects.all()
    serializer = ImovelSerializer(imoveis, many=True)
    return Response(serializer.data)  # 200 ok

@api_view(['GET','POST'])
def delete(request, pk):
    try:
        imovel = Imovel.objects.get(pk=pk)
    except Imovel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)  # 404 not found
    imovel.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)  # 204 no content

@api_view(['GET','PATCH'])
def patch(request, pk):
    try:
        imovel = Imovel.objects.get(pk=pk)
    except Imovel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ImovelSerializer(imovel, data=request.data, partial=True)  # partial=True to allow updates other than all fields
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # 400 bad request
