from django.urls import path
from materio.views import Main
# from materio.methods.all_json_format import dokon_maxsulot

urlpatterns = [
    path('main/', Main.as_view()),
    # path('dokon_maxsulot/<int:pk>/', dokon_maxsulot),
]
