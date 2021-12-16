from django_filters import FilterSet, DateRangeFilter
from .models import Article


# создаём фильтр
class ArticleFilter(FilterSet):
    datetime = DateRangeFilter
    class Meta:
        model = Article
        fields = ('title', 'description', 'category', 'author')
