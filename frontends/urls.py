from django.urls import path
from frontends.views import jqfront, formfront

urlpatterns = [
    path('jq/', jqfront, name='jqfront'),
    path('form/', formfront, name='formfront'),
    # path('post/<int:blogpostid>/', blogpost, name='blogpost'),
]
