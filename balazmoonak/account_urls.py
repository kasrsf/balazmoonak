from django.conf.urls import url, include
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from allauth.account import views as auth_views
# from authentication import views as custom_views
urlpatterns = [
    url(
        regex=r'^login/$', 
        view=auth_views.login, 
        kwargs={'template_name': 'account/login.html'}, 
        name='login'
        ),
    url(
        regex=r'^logout/$', 
        view=auth_views.logout, 
        kwargs={'template_name': 'account/logout.html'}, 
        name='logout'
        ),
    # url(
    #     regex=r'^signup/$', 
    #     view = custom_views.SignupView, 
    #     kwargs={'template_name': 'account/signup.html'}, 
    #     name='account_signup'
    #     ),
    url(r'^', include('allauth.urls')),
    #url(r'^accounts/login/$', auth_views.login),
]
# # urlpatterns = [
# #     url(r"^signup/$", views.signup, name="account_signup"),
# #     url(r"^login/$", views.login, name="account_login"),
# #     url(r"^logout/$", views.logout, name="account_logout"),

# #     url(r"^password/change/$", views.password_change,
# #         name="account_change_password"),
# #     url(r"^password/set/$", views.password_set, name="account_set_password"),

# #     url(r"^inactive/$", views.account_inactive, name="account_inactive"),

# #     # E-mail
# #     url(r"^email/$", views.email, name="account_email"),
# #     url(r"^confirm-email/$", views.email_verification_sent,
# #         name="account_email_verification_sent"),
# #     url(r"^confirm-email/(?P<key>[-:\w]+)/$", views.confirm_email,
# #         name="account_confirm_email"),

# #     # password reset
# #     url(r"^password/reset/$", views.password_reset,
# #         name="account_reset_password"),
# #     url(r"^password/reset/done/$", views.password_reset_done,
# #         name="account_reset_password_done"),
# #     url(r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
# #         views.password_reset_from_key,
# #         name="account_reset_password_from_key"),
# #     url(r"^password/reset/key/done/$", views.password_reset_from_key_done,
# #         name="account_reset_password_from_key_done"),
# # ]
