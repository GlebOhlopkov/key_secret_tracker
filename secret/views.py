import cryptocode
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics

from config.settings import CRYPTO_KEY_PASS
from secret.models import Secret
from secret.serializers import SecretSerializer
from secret.services import replace_symbols


class SecretCreateAPIView(generics.CreateAPIView):
    """
    CreateView for create a Secret.
    For simple using you must be sent only dictionary like: {"text": ... , "key": ...}.
    Return {secret_key} which use for open your Secret
    """
    serializer_class = SecretSerializer

    def create(self, request, *args, **kwargs):

        # Determining the encryption password
        crypto_password = CRYPTO_KEY_PASS
        # Encrypting text of Secret
        text = request.data['text']
        encrypt_text = cryptocode.encrypt(text, crypto_password)
        request.data['text'] = encrypt_text
        # Encrypting key of Secret
        key = request.data['key']
        encrypt_key = cryptocode.encrypt(key, crypto_password)
        request.data['key'] = encrypt_key
        # Create special {secret_key} for view/open the Secret
        secret_key = encrypt_key[0:25]
        secret_key = replace_symbols(secret_key)
        request.data['secret_key'] = secret_key

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data['secret_key'], status=status.HTTP_201_CREATED, headers=headers)


class SecretDetailAPIView(generics.RetrieveAPIView):
    """
    RetrieveView for open and view Secret.
    For open and view Secret send {secret_key} in URL: .../secrets/{secret_key}.
    Will return text of Secret.
    """
    serializer_class = SecretSerializer
    queryset = Secret.objects.all()
    lookup_field = 'secret_key'

    def retrieve(self, request, *args, **kwargs):

        secret = self.get_object()
        secret.is_open = True
        secret.save()

        # Determining the encryption password
        crypto_password = CRYPTO_KEY_PASS
        # Encrypted text of Secret
        encrypt_text = secret.text
        # Decrypting text of Secret
        decrypt_text = cryptocode.decrypt(encrypt_text, crypto_password)
        secret.text = decrypt_text

        serializer = self.get_serializer(secret)

        return Response(serializer.data['text'])
