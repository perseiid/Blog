from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='Логин', on_delete=models.CASCADE)
    avatar = models.ImageField('Аватар',default='avatar.jpg', upload_to='avatars/')

    def __str__(self):
        return f'{self.user.username}'

    def save(self):
        super().save()

        image = Image.open(self.avatar.path)
        
        if image.height > 150 or image.width > 150:
            resize = (150, 150)
            image.thumbnail(resize)
            image.save(self.avatar.path)    

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
