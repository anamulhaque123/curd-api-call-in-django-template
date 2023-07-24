from  django.urls import path, include
from .import views
from .views import LoginView,get_token,Update,view,delete


urlpatterns=[
    path('LoginView/', views.LoginView.as_view(), name='LoginView'),
    path('create/', views.create.as_view(), name="create"),
    path('view/<id>/', views.view, name="view"),
    path('update/<str:id>/', views.Update, name="update"),
    path('delete/<id>/', views.delete, name="delete"),
    # path('success/', views.SuccessView, name='success')
    # path('updatedetail/<id>/', views.updatedetail, name="updatedetail")
    # path('country/', views.index, name="index"),
    # # path('login/', views.login, name="login"),
    # path('', views.get_token, name="userlogin"),
    # path('api/token/',views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]