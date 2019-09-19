from django.urls import path
from frontends.views import jqfront

urlpatterns = [
    path('jq/', jqfront, name='jqfront'),
    # path('post/<int:blogpostid>/', blogpost, name='blogpost'),
]
