from django.db import models


class News(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(
        null=True, blank=True,
        upload_to='newsImage/'
    )
    desc = models.TextField(null=True)

    def __str__(self):
        return self.title


    class Meta:
        ordering = ['-id']


class AboutUs(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'страница " о нас "'

class Reviews(models.Model):
    title = models.CharField(max_length=50,verbose_name='ФИО' )
    desc = models.TextField(verbose_name='отзыв от человека')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'отзывы'
