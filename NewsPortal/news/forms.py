from django.forms import ModelForm
from .models import Article


# Создаём модельную форму
class ArticleForm(ModelForm):
    # в класс мета, как обычно, надо написать модель, по которой будет строится форма и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = Article
        fields = ['title', 'author', 'description', 'category']