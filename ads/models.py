from django.db import models
from django.core.exceptions import ValidationError
from os import path as osPath


def validate_image_extension(value):
    ext = osPath.splitext(value.name)[1].lower()
    valid_extensions = [".jpg", ".jpeg", ".png", ".gif"]
    if ext not in valid_extensions:
        raise ValidationError(
            f'فرمت "{ext}" پشتیبانی نمی‌شود. فقط jpg, jpeg, png و gif مجاز هستند.'
        )


class Ad(models.Model):
    image = models.ImageField(
        upload_to="ads/images/",
        validators=[validate_image_extension],
        verbose_name="تصویر تبلیغ",
    )
    title = models.TextField(max_length=256, verbose_name="عنوان تبلیغ")
    link = models.URLField(verbose_name="لینک تبلیغ")
    description = models.TextField(max_length=256, verbose_name="توضیحات تبلیغ")

    def __str__(self):
        return f"{self.title}"
