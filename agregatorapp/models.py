from django.db import models


class Log(models.Model):
    ip_address = models.GenericIPAddressField(db_index=True)
    date_add = models.DateTimeField(db_index=True)
    remote_logname = models.CharField(max_length=128, default='-')
    remote_user = models.CharField(max_length=128, default='-')
    request_line = models.TextField(default='-')
    status = models.CharField(max_length=4, default='-')
    response_bytes = models.CharField(max_length=128, default='-')
    header_referer = models.CharField(max_length=256, default='-')
    header_user_agent = models.TextField(default='-')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
