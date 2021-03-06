from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Ingredient

from recipe import serializers


class IngredientViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """ Manage ingredients in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer

    def get_queryset(self):
        """ return objects for current authenticated user """
        return self.queryset.filter(user=self.request.user).order_by('-name')
