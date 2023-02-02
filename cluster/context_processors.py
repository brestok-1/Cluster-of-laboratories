from cluster.models import News


def news(request):
    return {'news_list': News.objects.all()[:5]}
