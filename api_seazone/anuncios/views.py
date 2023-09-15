from anuncios.models import Anuncio, AnuncioSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get(request, pk):
    try:
        anuncio = Anuncio.objects.get(pk=pk)
    except Anuncio.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = AnuncioSerializer(anuncio)
    return Response(serializer.data)  # 200 ok

@api_view(['GET'])
def get_list(request):
    anuncios = Anuncio.objects.all()
    serializer = AnuncioSerializer(anuncios, many=True)
    return Response(serializer.data)  # 200 ok

@api_view(['DELETE'])
def delete(request, pk):
    try:
        anuncio = Anuncio.objects.get(pk=pk)
    except Anuncio.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)  # 404 not found
    anuncio.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)  # 204 no content
