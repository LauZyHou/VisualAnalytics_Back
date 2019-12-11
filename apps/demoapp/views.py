from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework import status


class DemoViewSet(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = set()

    def retrieve(self, request, *args, **kwargs):
        return Response({
            'name': 'LauZyHou',
            'age': 22
        }, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        return Response([{
            'name': 'LauZyHou',
            'age': 22
        }, {
            'name': 'flora',
            'age': 22
        }], status=status.HTTP_201_CREATED)
