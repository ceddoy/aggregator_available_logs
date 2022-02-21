from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from agregatorapp.filters import LogsFilter
from agregatorapp.models import Log
from agregatorapp.serializer import LogListModelSerializer


class LogListAPIView(ListAPIView):
    serializer_class = LogListModelSerializer
    queryset = Log.objects.all()
    filterset_class = LogsFilter
    permission_classes = [IsAuthenticated, ]
