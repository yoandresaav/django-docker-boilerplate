from django.shortcuts import render
from django.views.generic import TemplateView
from .documents import PostDocument

class HomePage(TemplateView):
    template_name = 'index.html'

    def post(self, request, *args, **kwargs):
        ctx = self.get_context_data(**kwargs)
        
        search_text = request.POST.get('search') or ''
        
        search = PostDocument.search()
        if search_text:
            search = search.filter('match_phrase', title=search_text)
        
        ctx.update({ 'results':  search })
        return self.render_to_response(ctx)
