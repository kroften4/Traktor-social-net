from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import User


# Create your views here.

class SearchView(ListView):
    model = User
    template_name = 'search/search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        query = self.request.GET.get('search')
        result = None
        if query:
            # SQL INJECTION
            result = User.objects.raw(
                f"SELECT * "
                f"FROM auth_user "
                f"WHERE username LIKE '%{query}' "
                f"OR username LIKE '{query}%'"
                f"OR username LIKE '%{query}%'"
            )
        return result
