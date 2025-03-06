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

from .api.rhythms import RhythmView
from .api.koran import KoranView
from .api.words import WordView
from .api.translit_koran import TranslitKoranView
from .api.translit_words import TranslitWordView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rhythms/', RhythmView.as_view()),
    path('koran/', KoranView.as_view()),
    path('remove/', TranslitWordView.remove),
    path('words/', WordView.as_view()),
    path('search/', WordView.search),
    path('translit/', TranslitKoranView.as_view()),
    path('split/', TranslitKoranView.split),
    path('translit_words/', TranslitWordView.as_view()),
    path('manage/pattern', TranslitWordView.manage_pattern),
    path('easy_shrift', KoranView.easy_shrift),
    path('word/easy_shrift', WordView.easy_shrift),
    path('dots/', WordView.remove_dots),
]
