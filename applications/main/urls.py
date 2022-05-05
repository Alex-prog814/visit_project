from django.urls import path
from applications.main.views import TradePointView, VisitCreateView

urlpatterns = [
    path('points/', TradePointView.as_view()),
    path('visit/', VisitCreateView.as_view())
]
