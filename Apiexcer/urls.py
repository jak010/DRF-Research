from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import MemberView

urlpatterns = [
    path(r'member', MemberView.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])