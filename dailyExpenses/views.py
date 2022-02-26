from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from dailyExpenses.models import Parent, Child, Category, Plan
from dailyExpenses.serializers import ParentCreateSerializer, ParentListSerializer, ChildCreateSerializer, \
    ChildListSerializer, ChildrenDetailSerializer, PlanCreateSerializer, CategoryCreateSerializer, \
    CategoryListSerializer, PlanChildrenDetailSerializer, PlanConfirmUpdateSerializer


class ParentCreateView(generics.CreateAPIView):
    serializer_class = ParentCreateSerializer


class ParentListView(generics.ListAPIView):
    serializer_class = ParentListSerializer
    queryset = Parent.objects.all()


class ChildCreateView(generics.CreateAPIView):
    serializer_class = ChildCreateSerializer


class ChildListView(generics.ListAPIView):
    serializer_class = ChildListSerializer
    queryset = Child.objects.all()


class ChildrenDetailView(generics.RetrieveAPIView):
    serializer_class = ChildrenDetailSerializer
    queryset = Parent.objects.all()


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
