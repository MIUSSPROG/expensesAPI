from django.urls import path
from . import views

urlpatterns = [
    path("parent", views.ParentCreateView.as_view()),
    path("parents", views.ParentListView.as_view()),
    path("child", views.ChildCreateView.as_view()),
    path("children", views.ChildListView.as_view()),
    path("parent/<int:pk>/children", views.ChildrenDetailView.as_view()),
    path('plan', views.PlanCreateView.as_view()),
    path('plan/children/<int:pk>', views.PlanChildrenDetailView.as_view()),
    path('plan/<int:pk>/confirm', views.PlanConfirmView.as_view()),
    path('category', views.CategoryCreateView.as_view()),
    path('categories', views.CategoryListView.as_view()),
    path('role', views.RoleCreateView.as_view()),
    path('role/all', views.RoleListView.as_view())
]