from django.conf import settings
from django.urls import include, path


from . import views

app_name = 'minerals'

urlpatterns = [
    path('', views.mineral_list, name='list'),
    path('<int:pk>/', views.mineral_detail, name='detail'),
    path('search/<str:letter>/', views.mineral_letter, name='letter'),
    path('search/', views.mineral_search, name='search')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls, namespace='djdt')),
    ]
