from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('NewPurchase.html',views.purchase, name='purchase'),
    path('<int:budget_id>/',views.detail, name='detail'),
    path('Setbudget.html', views.setbudget,name='setbudget'),
    path('WalletData.html', views.wallet, name='wallet'),
    path('index.html', views.index, name='index')
]
