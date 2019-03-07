from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import proj.views

urlpatterns = [
    path("", proj.views.index, name="index"),
    path("info/", proj.views.info, name="info"),
    path("sala/", proj.views.upd, name="sala"),
    path("cozinha/", proj.views.upd, name="cozinha"),
    path("quarto/", proj.views.upd, name="quarto"),
    path("wc/", proj.views.upd, name="wc"),
    path("admin/", admin.site.urls),
]
