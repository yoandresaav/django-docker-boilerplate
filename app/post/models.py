from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=5000)
    created_at = models.DateTimeField(default=timezone.now)
    likes = models.PositiveIntegerField(default=0)
    slug = models.SlugField(max_length=128, db_index=True, null=True)
    draft = models.BooleanField(default=True)

    user = models.ForeignKey(
        get_user_model(),
        related_name='posts',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'post'
