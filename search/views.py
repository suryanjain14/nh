from django.views.generic import ListView
from projects.models import Project
# Create your views here.

class SearchProjectView(ListView):

    template_name = "search/view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProjectView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None )

        if query is not None:
            return Project.objects.filter(name__icontains=query)
        return Project.objects.featured()

