from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, StockViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet, basename='Stock')

urlpatterns = router.urls
