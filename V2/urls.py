from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('get-price', GetPriceView, basename='GetPriceView')

urlpatterns = [
    path('', main),
    path('add-distance-base-price/', DistanceBasePriceView.as_view(), name='add-distance-base-price'),
    path('delete-distance-base-price', DistanceBasePriceView.as_view(), name='delete-distance-base-price'),
    path('edit-distance-base-price', UpdateDistanceBasePriceView.as_view(), name='edit-distance-base-price'),


    path('add-distance-additional-price/', DistanceAdditionalPriceView.as_view(), name='add-distance-additional-price'),
    path('delete-distance-additional-price', DistanceAdditionalPriceView.as_view(), name='delete-distance-additional-price'),
    path('edit-distance-additional-price', UpdateDistanceAdditionalPriceView.as_view(), name='edit-distance-additional-price'),

    path('add-tmf/', TMFView.as_view(), name='add-tmf'),
    path('delete-tmf', TMFView.as_view(), name='delete-tmf'),
    path('edit-tmf', UpdateTMFView.as_view(), name='edit-tmf'),

    path('add-waiting-charge/', waitingChargeView.as_view(), name='add-waiting-charge'),
    path('delete-waiting-charge', waitingChargeView.as_view(), name='delete-waiting-charge'),
    path('edit-waiting-charge', UpdatewaitingChargeView.as_view(), name='edit-waiting-charge'),

    path('export', Export.as_view(), name="export") ,  

    path('api/', include(router.urls))
]
