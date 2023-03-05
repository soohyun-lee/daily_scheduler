from datetime import datetime, date
from pytz import timezone

from tortoise.models import Model
from tortoise import fields


class BaseMixin:
    id = fields.BigIntField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    @property
    def created_at_kst(self):
        kst = timezone('Asia/Seoul')
        dt = datetime.strftime(self.created_at.astimezone(kst), '%Y-%m-%d %H:%M:%S')
        return dt

    @property
    def updated_at_kst(self):
        kst = timezone('Asia/Seoul')
        dt = datetime.strftime(self.updated_at.astimezone(kst), '%Y-%m-%d %H:%M:%S')
        return dt
