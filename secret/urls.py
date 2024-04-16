from django.urls import path

from secret.views import SecretCreateAPIView, SecretDetailAPIView

app_name = 'secret'

urlpatterns = [
    # url for create secret
    path('generate/', SecretCreateAPIView.as_view(), name='generate'),
    # url for view/open secret
    path('secrets/<str:secret_key>', SecretDetailAPIView.as_view(), name='open_secret'),
]
