from django.db import models


class Log(models.Model):
    ip_address = models.GenericIPAddressField()
    date_add = models.DateTimeField()
    remote_logname = models.CharField(max_length=128, default='-')
    remote_user = models.CharField(max_length=128, default='-')
    request_line = models.CharField(max_length=256, default='-')
    status = models.CharField(max_length=4, default='-')
    response_bytes = models.CharField(max_length=128, default='-')
    header_referer = models.CharField(max_length=256, default='-')
    header_user_agent = models.CharField(max_length=256, default='-')

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
