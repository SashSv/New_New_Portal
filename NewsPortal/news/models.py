from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('Author', null=True, on_delete=models.PROTECT)
    category = models.ForeignKey('Category', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title.title()} : {self.description[:200]}'

    def get_absolute_url(self):
        return f'/news/{self.id}'


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.category}'