from django.contrib import admin

from secret.models import Secret


@admin.register(Secret)
class SecretAdmin(admin.ModelAdmin):
    list_display = ('id', 'key', 'secret_key', 'text', 'lifetime', 'created_at', 'is_open', )
