from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from .models import Department
from .serializers import DepartmentListSerializer


class DepartmentListView(ListAPIView):
    """
    API endpoint for display a list of departments with additional information about them (without pagination)
    """
    queryset = Department.objects.all().order_by('name')
    serializer_class = DepartmentListSerializer
    permission_classes = (AllowAny,)