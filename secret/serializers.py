from rest_framework import serializers

from secret.models import Secret
# from secret.validators import KeySymbolsValidator


class SecretSerializer(serializers.ModelSerializer):
    secret_key = serializers.CharField(read_only=True)

    class Meta:
        model = Secret
        fields = ['text', 'key', 'lifetime', 'secret_key', ]
