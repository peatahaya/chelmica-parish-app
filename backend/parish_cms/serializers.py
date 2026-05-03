from rest_framework import serializers
from .models import ParishProfile

class ParishProfileSerializer(serializers.ModelSerializer):
    """
    Serializator dla modelu ParishProfile.
    Wystawia wszystkie pola modelu, w tym konfigurację kolorów dla frontendu.
    """
    class Meta:
        model = ParishProfile
        fields = '__all__'