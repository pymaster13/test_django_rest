from rest_framework import serializers

from department.models import Department
from .models import Department


class DepartmentListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Department
        fields = ['name', 'director_name', 'count_persons', 'count_salary']