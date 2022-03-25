from django.urls import path
from . import views

urlpatterns = [
    # auth
    # path("child", views.ChildListCreateView.as_view()),
    path('child_encoded/<int:pk>', views.ChildDetailView.as_view()),
    path("parent", views.ParentCreateView.as_view()),
    path("save_parent_encoded/", views.SaveParentEncodedView.as_view()),
    path("check_parent/", views.CheckParentView.as_view()),
    path("parents", views.ParentListView.as_view()),
    path("child", views.ChildCreateView.as_view()),
    path("child/<int:pk>/check", views.ChildCheckView.as_view()),
    path("check_child/", views.CheckChildView.as_view()),
    path("save_child_encoded/", views.SaveChildEncodedView.as_view()),
    path("children", views.ChildListView.as_view()),
    path("parent/<int:pk>/children", views.ChildrenDetailView.as_view()),
    path('plan', views.PlanCreateView.as_view()),
    path('plan/children/<int:pk>', views.PlanChildrenDetailView.as_view()),
    path('plan/<int:pk>/confirm', views.PlanConfirmView.as_view()),
    path('category', views.CategoryCreateView.as_view()),
    path('categories', views.CategoryListView.as_view()),
    path('send_invitation', views.SendInvitationCreateView.as_view())
    # path('role', views.RoleCreateView.as_view()),
    # path('role/all', views.RoleListView.as_view()),
    # path('role/get', views.RoleView.as_view())
]