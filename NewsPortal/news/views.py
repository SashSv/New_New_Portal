from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator

from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
import datetime
from .models import Article, Author
from .filters import ArticleFilter
from .forms import ArticleForm


class ArticleList(ListView):
    model = Article
    template_name = 'articles.html'
    context_object_name = 'news'
    ordering = ['-datetime']
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.datetime.utcnow()  # добавим переменную текущей даты time_now
        context['filter'] = ArticleFilter (self.request.GET, queryset=self.get_queryset ())  # вписываем наш фильтр в контекст
        return context


class ArticleDetail(DetailView):
    template_name = 'article.html'
    queryset = Article.objects.all()


class ArticlePost(CreateView):
    permission_required = ('news.add_Article')
    template_name = 'add.html'
    form_class = ArticleForm


class ArticleUpdateView(UpdateView):
    permission_required = ('news.add_Article')
    template_name = 'add.html'
    form_class = ArticleForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Article.objects.get(pk=id)


class ArticleDeleteView(DeleteView):
    template_name = 'delete.html'
    queryset = Article.objects.all()
    success_url = '/news/'


class SearchArticleList(ListView):
    model = Article
    template_name = 'search.html'
    context_object_name = 'news'
    ordering = ['-datetime']
    paginate_by = 1

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = ArticleFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context

# class SearchArticleList(ListView):
#     model = Article
#     template_name = 'search.html'
#     context_object_name = 'news'
#     ordering = ['-datetime']
#     paginate_by = 10

    # def get_filter(self):
    #     return ArticleFilter(self.request.GET, queryset=super().get_queryset())
    #
    # def get_queryset(self):
    #     return self.get_filter().qs
    #
    # def get_context_data(self, *args, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
    #     return {
    #         **super().get_context_data(*args, **kwargs),
    #         "filter": self.get_filter(),
    #     }
