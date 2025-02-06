from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Define redirection rules based on user group
GROUP_REDIRECTS = {
    "tutors": "/tutors/dashboard/",
    "students": "/students/dashboard/",
    "admins": "/admin/",
}

# Dynamic redirect view
@login_required
def group_redirect_view(request):
    user_groups = list(request.user.groups.values_list("name", flat=True))
    print(user_groups)
    for group, redirect_url in GROUP_REDIRECTS.items():
        if group in user_groups:
            return redirect(redirect_url)

    return redirect("home")