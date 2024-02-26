from rest_framework.generics import CreateAPIView

from .serializers import CustomerCreateSerializer


class CustomerCreateAPIView(CreateAPIView):
    serializer_class = CustomerCreateSerializer


