from rest_framework.generics import ListAPIView

from agregatorapp.models import Log
from agregatorapp.serializer import LogListModelSerializer


class LogListAPIView(ListAPIView):
    serializer_class = LogListModelSerializer
    queryset = Log.objects.all()
