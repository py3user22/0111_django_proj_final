from django.shortcuts import render
from .models import MenuItem
from .serializers import MenuItemSerializer
#from django.response import Response
from rest_framework import generics


""" edit 0112 from 0109 demo about tokens
@api_view()
def single_item(request, id):
    item = get_object_or_404(MenuItem, pk=id)
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)

@api_view()
def secret(request):
    return Response({"message":"Some secrets for you"})
"""

def home(request):
    return render(request, '0111_final_proj_notes.html', {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
