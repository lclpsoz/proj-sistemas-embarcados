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
    
    path("lamp-quarto/", proj.views.upd, name="lamp-quarto"),
    path("lamp-sala/", proj.views.upd, name="lamp-sala"),
    path("lamp-cozinha/", proj.views.upd, name="lamp-cozinha"),
    path("lamp-garagem/", proj.views.upd, name="lamp-garagem"),
    path("lamp-ext/", proj.views.upd, name="lamp-ext"),
    path("garagem/", proj.views.upd, name="garagem"),
    path("alarme/", proj.views.upd, name="alarme"),
    
    path("admin/", admin.site.urls)
]
