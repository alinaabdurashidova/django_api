from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Gadget
from .serializers import GadgetSerializer

@api_view(['GET'])
def get_gadgets(request):
    queryset = Gadget.objects.all()
    serializer = GadgetSerializer(queryset, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def create_gadget(request):
    serializer = GadgetSerializer(data = request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_one_gadget(request, pk):
    try:
        gadget = Gadget.objects.get(pk=pk)
    except Gadget.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serilizer = GadgetSerializer(gadget)
    return Response(serilizer.data)

@api_view(['PUT', 'PATCH'])
def update_gadget(request, pk):
    try:
        gadget = Gadget.objects.get(pk=pk)
    except Gadget.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = GadgetSerializer(gadget, data = request.data, partial=True)
    # gadget = gadget.objects.filter().update()
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)     

@api_view(['DELETE'])
def delete_gadget(request, pk):
    # request.method == 'DELETE':
    try:
        gadget = Gadget.objects.get(pk=pk)
    except Gadget.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = GadgetSerializer(gadget, data = request.data)
    gadget.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def detail(request, pk):
    try:
        gadget = Gadget.objects.get(pk=pk)
    except Gadget.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serilizer = GadgetSerializer(gadget)
        return Response(serilizer.data)
    
    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = GadgetSerializer(gadget, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        gadget.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)