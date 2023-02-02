from cluster.models import News


def news(request):
    return News.objects.all()[:5]
