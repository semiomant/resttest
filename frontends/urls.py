from django.urls import path
from frontends.views import jqfront, formfront, tokenfront

urlpatterns = [
    path('jq/', jqfront, name='jqfront'),
    path('form/', formfront, name='formfront'),
    path('token/', tokenfront, name='tokenfront'),
    # path('post/<int:blogpostid>/', blogpost, name='blogpost'),
]
