from django.urls import path
from user.views import UserSignUp, UserSignIn, UserSignOut, UserProfile, UserUpdate, UserDelete

urlpatterns = [
    path('signup/', UserSignUp.as_view(), name='user-signup'),
    path('signin/', UserSignIn.as_view(), name='user-signin'),
    path('signout/', UserSignOut.as_view(), name='user-signout'),
    path('profile/', UserProfile.as_view(), name='user-profile'),
    path('update/', UserUpdate.as_view(), name='user-update'),
    path('delete/', UserDelete.as_view(), name='user-delete'),
]