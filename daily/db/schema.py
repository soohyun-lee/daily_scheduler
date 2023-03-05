from tortoise.models import Model
from tortoise import fields
from common.db.schema import BaseMixin


class Report(Model, BaseMixin):
    content = fields.CharField(max_length=255)

    class Meta:
        table = 'reports'