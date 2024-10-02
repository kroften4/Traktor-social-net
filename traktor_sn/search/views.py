from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import User

# Create your views here.

class SearchView(ListView):
    model = User
    template_name = 'search/search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
       result = super(SearchView, self).get_queryset()
       query = self.request.GET.get('search')
       if query:
           #SQL INJECTION
          postresult = User.objects.raw(f"SELECT * FROM auth_user WHERE username LIKE '%{query}%'")
          result = postresult
       else:
           result = None
       return result
