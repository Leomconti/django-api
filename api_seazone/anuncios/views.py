from anuncios.models import Anuncio, AnuncioSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get(request, pk):
    try:
        anuncio = Anuncio.objects.get(pk=pk)
    except Anuncio.DoesNotExist:
        return Response(status=404)
    serializer = AnuncioSerializer(anuncio)
    return Response(serializer.data)  # 200 ok

@api_view(['GET'])
def get_list(request):
    anuncios = Anuncio.objects.all()
    serializer = AnuncioSerializer(anuncios, many=True)
    return Response(serializer.data)  # 200 ok

@api_view(['POST'])
def delete(request, pk):
    try:
        anuncio = Anuncio.objects.get(pk=pk)
    except Anuncio.DoesNotExist:
        return Response(status=404)  # 404 not found
    anuncio.delete()
    return Response(status=204)  # 204 no content