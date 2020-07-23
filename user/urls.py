from django.conf.urls import  url
from .import views
urlpatterns=[
    url(r'^reg$',views.reg_view),
    url(r'^get$',views.get_cook),
    url(r'^show$',views.show_),
    url(r'^login$',views.login_view),
    url(r'^out$',views.logout_view),
    url(r'^session$',views.get_session),
    url(r'^reg2$',views.reg2_view)
]