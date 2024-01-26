import uuid
from django.db import models

class Addcard(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    input_box = models.CharField(max_length=100, verbose_name="Input Box", unique=True)
    text_area = models.TextField(verbose_name="Text Area", unique=True)

    def __str__(self):
        return f"{self.id} - {self.input_box}"
