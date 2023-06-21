from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_nested import routers
#from pprint import pprint

router = routers.DefaultRouter()
router.register('products',views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet)

products_router = routers.NestedDefaultRouter(router,'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')

#pprint(router.urls)
#urlpatterns = router.urls + products_router.urls
carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', views.CartItemViewSet, basename='cart-items')

# URLConf
urlpatterns = router.urls + products_router.urls + carts_router.urls

# urlpatterns = [
#     path('', include(router.urls)),
#     path('', include(products_router.urls))
#     # path('products/', views.ProductList.as_view()),
#     # path('products/<int:pk>/', views.ProductDetail.as_view()),
#     # path('collections/', views.CollectionList.as_view()),
#     # path('collections/<int:pk>/', views.CollectionDetail.as_view(), name='collection_detail')
#  ]
