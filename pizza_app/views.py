# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.http.response import Http404
from pizza_app.serializers import PizzaSerializer, Pizza
from rest_framework import authentication, permissions
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class ListPizzas(ListAPIView):
    """
    View to list all Pizzas
    """
    authentication_classes = []
    permission_classes = [permissions.AllowAny]
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all().order_by('created')

    def list(self, request, *args, **kwargs):
        res = super(ListPizzas, self).list(request, *args, **kwargs)
        return Response({"status": 200, "total": len(res.data), "data": res.data})
