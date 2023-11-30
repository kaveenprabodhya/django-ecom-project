from email.mime import base
from xml.etree.ElementInclude import include
from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_nested import routers
from pprint import pprint

router = routers.DefaultRouter()

router.register("products", views.ProductViewSet, basename="products")
router.register("collections", views.CollectionViewSet)
router.register("carts", views.CartViewSet)
router.register("customers", views.CustomerViewSet)
router.register("orders", views.OrdersViewSet, basename="orders")

products_router = routers.NestedDefaultRouter(router, "products", lookup="product")
products_router.register("reviews", views.ReviewViewSet, basename="product-reviews")
products_router.register("images", views.ProdcutImageViewSet, basename="product-images")

carts_router = routers.NestedDefaultRouter(router, "carts", lookup="cart")
carts_router.register("items", views.CartItemViewSet, basename="cart-items")


urlpatterns = router.urls + products_router.urls + carts_router.urls
# pprint(urlpatterns)
