from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from home.views import homePage
from about.views import aboutPage
from team.views import listTeam
from contact.views import contactPage

urlpatterns = [
    path("", homePage, name="home"),
    path("about/", aboutPage, name="about"),
    path("stories/", include("stories.urls")),
    path("updates/", include("updates.urls")),
    path("team/", listTeam, name="team"),
    path("contact", contactPage, name="contact"),
    path(
        "join-ieee/",
        TemplateView.as_view(template_name="pages/join-ieee.html"),
        name="join-ieee",
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("ieeesbtkmce.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
    path("_nested_admin/", include("nested_admin.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns

admin.site.site_header = "IEEE SB TKMCE Admin"
admin.site.site_title = "IEEE SB TKMCE Admin Portal"
admin.site.index_title = "Welcome to IEEE SB TKMCE Admin Portal"
