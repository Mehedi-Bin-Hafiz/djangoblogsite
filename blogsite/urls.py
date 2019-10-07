
from django.contrib import admin
from django.urls import path,include
import login.views
import regforms.views
import quotes.views
import quotesform.views
import UserProfile.views
import about.views

from django.conf import settings
from django.conf.urls.static import static
from . import  settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("home.urls")),
    path('',include("UserProfile.urls")),
    # path('about/',include("about.urls")),
    path('login/',login.views.loginview),
    path('signup/',regforms.views.signup),
    path('quotes/',quotes.views.quotesview),
    path('quotesform/',quotesform.views.quotesformview),
    path('UserProfile/',UserProfile.views.userview.as_view()),
    path('about/', about.views.aboutview.as_view()),


]
if settings.DEBUG: # new
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
