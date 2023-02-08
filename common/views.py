from cluster.models import News
from robotics.models import Technologies, Projects, Courses


class CommonMixin:
    title = None

    def get_context_data(self, **kwargs):
        context = super(CommonMixin, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context


class ClusterMixin:
    def get_context_data(self, **kwargs):
        context = super(ClusterMixin, self).get_context_data(**kwargs)
        context['news_list'] = News.objects.all()[:5]
        context['projects'] = Projects.objects.all()[:5]
        return context


class LaboratoryMixin:
    title = None

    def get_context_data(self, **kwargs):
        context = super(LaboratoryMixin, self).get_context_data(**kwargs)
        context['title'] = self.title
        context['technologies'] = Technologies.objects.filter(owner__name=self.title)
        context['projects'] = Projects.objects.filter(owner__name=self.title)
        context['courses'] = Courses.objects.filter(owner__name=self.title)
        return context


class DetailMixin:
    def get_context_data(self, **kwargs):
        context = super(DetailMixin, self).get_context_data(**kwargs)
        context['technologies'] = Technologies.objects.filter(owner__name=self.object.owner.name)
        context['projects'] = Projects.objects.filter(owner__name=self.object.owner.name)
        context['courses'] = Courses.objects.filter(owner__name=self.object.owner.name)
        return context
