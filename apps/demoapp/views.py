from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework import status

from demoapp.models import Demo
from demoapp.serializers import DemoSerializer


class DemoViewSet(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = Demo.objects.all()
    serializer_class = DemoSerializer

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, args, kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, args, kwargs)
