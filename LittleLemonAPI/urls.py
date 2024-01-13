from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('', views.home),
]

"""
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    
    #0112 required API routes for final project > use Djoser 
    #--------------------------------------------
    path('/api/users', )
    path('/api/users/users/me/', )
    path('/token/login/', )
    
    #0112 menu-item API endpoints
    #----------------------------
    # for customer and delivery crews
    
    path('/api/menu-items/', )              # for GET  > list all menu items, returns 200 -ok status code
    path('/api/menu-items/', )              # for POST,PUT,PATCH,DELETE > denies access, returns 403-unauthorized status code
    path('/api/menu-items/{menuItem}', )    # for GET > list single menu item
    path('/api/menu-items/{menuItem}', )    # for POST,PUT,PATCH,DELETE > returns 403-unauthorized
    
    # for manager login access
    #-------------------------
    path('/api/menu-items/', )              # GET > list all menu items
    path('/api/menu-items/', )              # POST > creates new menu item & returns 201-created 
    path('/api/menu-items/{menuItem}', )    # GET > list single menu item
    path('/api/menu-items/{menuItem}', )    # PUT, PATCH > updates single menu item
    path('/api/menu-items/{menuItem}', )    # DELETE > delete menu item
    
    # manager >  user group mgmt endpoints 
    #-------------------------
    path('api/groups/manager/users', )                  # GET > returns all managers
    path('api/groups/manager/users', )                  # POST > assigns the user in payload to manager group & returns 201-created
    path('api/groups/manager/users/{userId}', )         # DELETE > if ok then success output, not is 404- not found
    path('api/groups/delivery-crew/users', )            # GET > returns all delivery crew
    path('api/groups/delivery-crew/users', )            # POST > assigns the user in payload to delivery crew group & returns 201-Created 
    path('api/groups/delivery-crew/users/{userId}', )   # DELETE > removes user from manager group
    
    # customer > cart mgmt endpoints
    path('/api/cart/menu-items', )      # GET > return current items in cart for current user token 
    path('/api/cart/menu-items', )      # POST > adds menu item to cart, sets authenticated user as the user id for cart items
    path('/api/cart/menu-items', )      # DELETE > deletes all menu items created by current user token
    
    
    # customer > order mgmt endpoints
    path('/api/orders', )       # GET > returns all orders w/ order items created by user
    path('/api/orders', )       # POST > creates new order item for current user, 
    path('/api/orders/{orderId}', )         # GET > returns all items for this order id, if not correct order ID shows error status
    path('/api/orders/{orderId}', )         # PUT, PATCH > if delivery is assigned to order the status = 0, means out to deliver
     
    #manager 
    path('/api/orders', )                   # GET > returns all orders w/ order items by all users
    path('/api/orders/{orderId}', )        # DELETE > deletes order
    
    # delivery-crew
    path('/api/orders', )                  # GET > returns all orders w/ order items assigned to crew
    path('/api/orders/{orderId}', )        # PATCH > crew can use to update from order status from 0 to 1, 
"""