from django.shortcuts import redirect


def mod_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_mod:
            return view_func(request)
        else:
            return redirect('posts-home')

    return wrapper_func
