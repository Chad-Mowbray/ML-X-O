from rest_framework import serializers
from .models import SampleData

class SampleDataSerializer(serializers.Serializer):
    data = serializers.ListField(child=serializers.ListField(child=serializers.IntegerField()))
    category = serializers.CharField(max_length=1)
    id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        print("in create, validated_data: ", validated_data)
        return SampleData.objects.create(**validated_data)
        # return SampleData.objects.create(data=validated_data["data"], category=validated_data["category"])
