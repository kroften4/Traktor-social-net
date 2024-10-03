from django.shortcuts import render
from django.views.generic import ListView
# from django.contrib.auth.models import User
from users.models import CustomUser


# Create your views here.

class SearchView(ListView):
    model = CustomUser
    template_name = 'search/search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        query = self.request.GET.get('search')
        result = None
        if query:
            # SQL INJECTION
            result = CustomUser.objects.raw(
                f"SELECT * "
                f"FROM users_customuser "
                f"WHERE username LIKE '%{query}' "
                f"OR username LIKE '{query}%'"
                f"OR username LIKE '%{query}%'"
            )
            result = filter(lambda x: not x.is_superuser, result)
        return result
