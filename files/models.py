from django.db import models

# Create your models here.

class File(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    file = models.FileField(upload_to='uploads/', blank=True)
    is_folder = models.BooleanField(default=False)
    size = models.IntegerField(blank=True, null=True)
    expires_date = models.DateTimeField(blank=True, null=True)
    owner = models.ForeignKey('auth.User', related_name='files', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.is_folder == False:
            self.size = self.file.size
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name