from django.urls import path
from users.views import SignUpView, SignInView

urlpatterns = [
    path('/sign-up',SignUpView.as_view()),
    path('/sign-in',SignInView.as_view()),
    # path('/posts/<int:post_num>',UserPostDetailView.as_view()),
]