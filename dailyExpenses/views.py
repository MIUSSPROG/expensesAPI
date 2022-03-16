from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from dailyExpenses.license import IsOwnerProfileOrReadOnly
from dailyExpenses.models import Parent, Child, Category, Plan
from dailyExpenses.serializers import ParentCreateSerializer, ParentListSerializer, ChildCreateSerializer, \
    ChildListSerializer, ChildrenDetailSerializer, PlanCreateSerializer, CategoryCreateSerializer, \
    CategoryListSerializer, PlanChildrenDetailSerializer, PlanConfirmUpdateSerializer, ChildCheckDetailSerializer, \
    ChildAuthSerializer, CheckChildSerializer


# class RoleView(generics)


# class RoleListView(generics.ListAPIView):
#     serializer_class = RoleListSerializer
#     queryset = Role.objects.all()
#
#
# class RoleCreateView(generics.CreateAPIView):
#     serializer_class = RoleCreateSerializer


class ParentCreateView(generics.CreateAPIView):
    serializer_class = ParentCreateSerializer


class ParentListView(generics.ListAPIView):
    serializer_class = ParentListSerializer
    queryset = Parent.objects.all()


# class ChildListCreateView(ListCreateAPIView):
#     serializer_class = ChildAuthSerializer
#     queryset = Child.objects.all()
#     permission_classes = [IsAuthenticated]
#
#     def perform_create(self, serializer):
#         user = self.request.user
#         serializer.save(user=user)


class ChildDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildAuthSerializer


class ChildCreateView(generics.CreateAPIView):
    serializer_class = ChildCreateSerializer


class ChildListView(generics.ListAPIView):
    serializer_class = ChildListSerializer
    queryset = Child.objects.all()


class ChildrenDetailView(generics.RetrieveAPIView):
    serializer_class = ChildrenDetailSerializer
    queryset = Parent.objects.all()


class ChildCheckView(generics.RetrieveAPIView):
    serializer_class = ChildCheckDetailSerializer
    queryset = Child.objects.all()


class CheckChildView(generics.ListAPIView):
    serializer_class = CheckChildSerializer
    queryset = Child.objects.all()

    def get(self, request, *args, **kwargs):
        login = request.query_params["login"]
        password = request.query_params["password"]
        if login is not None and password is not None:
            child = Child.objects.get(login=login, password=password)
            if child is not None:
                serializer = CheckChildSerializer(child)
                return Response(serializer.data)
            else:
                return Response({"Error": "Child not found"})
        else:
            return Response({"Error": "credentials fail"})


class PlanChildrenDetailView(generics.RetrieveAPIView):
    serializer_class = PlanChildrenDetailSerializer
    queryset = Child.objects.all()


class PlanConfirmView(generics.UpdateAPIView):
    serializer_class = PlanConfirmUpdateSerializer
    queryset = Plan.objects.all()


class PlanCreateView(generics.CreateAPIView):
    serializer_class = PlanCreateSerializer


class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategoryCreateSerializer


class CategoryListView(generics.ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()
