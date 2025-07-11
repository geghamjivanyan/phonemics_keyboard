"""
URL configuration for keyboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .api.rhythms import RhythmView
from .api.koran import KoranView
from .api.words import WordView
from .api.translit_koran import TranslitKoranView
from .api.translit_words import TranslitWordView
from .api.hamza_words import HamzaWordView
from .api.statistics import StatisticView

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/rhythms/', RhythmView.as_view()),
    path('api/koran/', KoranView.as_view()),
    path('api/words/translit/remove/', TranslitWordView.remove),
    path('api/words/', WordView.as_view()),
    path('api/search/', WordView.search),
    path('api/translit/', TranslitKoranView.as_view()),
    path('api/translit_words/', TranslitWordView.as_view()),
    path('api/easy_shrift', KoranView.easy_shrift),
    path('api/words/remove', WordView.remove),
    path('api/koran/remove', KoranView.remove),
    path('api/koran/translit/remove', TranslitKoranView.remove),
    path('api/hamza', HamzaWordView.as_view()),
    path('api/hamza/remove', HamzaWordView.remove),
    path('api/shadda', WordView.shadda),
    path('api/statistics', StatisticView.as_view()),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


