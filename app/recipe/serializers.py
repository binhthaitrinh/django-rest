from rest_framework import serializers

from core.models import Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    """ Serializer for ingredient objects"""
    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_fields = ('id', )
