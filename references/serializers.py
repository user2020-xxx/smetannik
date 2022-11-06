from rest_framework import serializers
from .models import GroupReferencesModel, ReferencesModel, File, TzModel, SPGZKPGZModel, EstimateModel


class GroupRefSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupReferencesModel
        fields = '__all__'


class RefSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferencesModel
        fields = '__all__'


class EstimateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstimateModel
        fields = '__all__'


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"


class TZSerializer(serializers.ModelSerializer):
    class Meta:
        model = TzModel
        fields = "__all__"


class SPGZSerializer(serializers.ModelSerializer):
    class Meta:
        model = SPGZKPGZModel
        fields = "__all__"
