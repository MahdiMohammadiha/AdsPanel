from django.db import models
from django.core.exceptions import ValidationError
from os import path as osPath
from uuid import uuid4


def validate_image_extension(value):
    ext = osPath.splitext(value.name)[1].lower()
    valid_extensions = [".jpg", ".jpeg", ".png", ".gif"]
    if ext not in valid_extensions:
        raise ValidationError("فرمت تصویر باید jpg، jpeg، png یا gif باشد.")


def ad_upload_path(instance, filename):
    return f"ads/images/{instance.uuid}_{filename}"


class Service(models.Model):
    title = models.CharField(max_length=256, verbose_name="عنوان سرویس")

    def __str__(self):
        return self.title


class Ad(models.Model):
    uuid = models.CharField(
        max_length=8,
        default=uuid4().hex[:8],
        editable=False,
        unique=True,
    )
    image = models.ImageField(
        upload_to=ad_upload_path,
        validators=[validate_image_extension],
        verbose_name="تصویر تبلیغ",
    )
    title = models.CharField(max_length=256, verbose_name="عنوان تبلیغ")
    link = models.URLField(verbose_name="لینک تبلیغ")
    description = models.TextField(max_length=256, verbose_name="توضیحات تبلیغ")
    is_active = models.BooleanField(default=True, verbose_name="فعال")
    services = models.ManyToManyField(Service, verbose_name="سرویس‌ها", related_name="ads")

    def __str__(self):
        status = "فعال" if self.is_active else "غیرفعال"
        description_preview = self.description[:30] + "..." if len(self.description) > 30 else self.description
        return f"{self.title} ({status}) - {description_preview}"
