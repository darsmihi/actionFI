from django.http import HttpResponseForbidden
from functools import wraps
from .models import Role,UserProfile

def role_required(allowed_roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                user_role = request.user.userprofile.role.name
                if user_role in allowed_roles:
                    return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("You do not have permission to access this page.")
        return _wrapped_view
    return decorator
