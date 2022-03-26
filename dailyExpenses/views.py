from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from dailyExpenses.license import IsOwnerProfileOrReadOnly
from dailyExpenses.models import Parent, Child, Category, Plan, Invitation
from dailyExpenses.serializers import ParentCreateSerializer, ParentListSerializer, ChildCreateSerializer, \
    ChildListSerializer, ChildrenDetailSerializer, PlanCreateSerializer, CategoryCreateSerializer, \
    CategoryListSerializer, PlanChildrenDetailSerializer, PlanConfirmUpdateSerializer, ChildCheckDetailSerializer, \
    ChildAuthSerializer, CheckChildSerializer, SaveChildEncodedSerializer, SaveParentEncodedSerializer, \
    CheckParentSerializer, SendInvitationSerializer, ChildrenByParentIdSerializer


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


class SaveParentEncodedView(generics.CreateAPIView):
    serializer_class = SaveParentEncodedSerializer


class SaveChildEncodedView(generics.CreateAPIView):
    serializer_class = SaveChildEncodedSerializer


class CheckParentView(generics.ListAPIView):
    serializer_class = CheckParentSerializer
    queryset = Parent.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            login = request.query_params["login"]
            password = request.query_params["password"]
            if login is not None and password is not None:
                parent = Parent.objects.get(login=login, password=password)
                if parent is not None:
                    serializer = CheckParentSerializer(parent)
                    return Response(serializer.data)
        except Exception:
            return Response({'id': 0, 'login': "", 'password': "", 'parent': None}, status=status.HTTP_404_NOT_FOUND)


class CheckChildView(generics.ListAPIView):
    serializer_class = CheckChildSerializer
    queryset = Child.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            login = request.query_params["login"]
            password = request.query_params["password"]
            if login is not None and password is not None:
                child = Child.objects.get(login=login, password=password)
                if child is not None:
                    serializer = CheckChildSerializer(child)
                    return Response(serializer.data)
        except Exception as ex:
            return Response({'id': 0, 'login': "", 'password': "", 'parent': None}, status=status.HTTP_404_NOT_FOUND)
            # return Response(Child.objects.none())


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


class SendInvitationCreateView(generics.CreateAPIView):
    serializer_class = SendInvitationSerializer


class ChildrenByParentId(generics.ListAPIView):
    serializer_class = ChildrenByParentIdSerializer
    queryset = Child.objects.all()

    def get(self, request, *args, **kwargs):
        parentId = request.query_params["parentId"]
        if parentId is not None:
            children_invitations = Invitation.objects.filter(parent=parentId)
            serializer = ChildrenByParentIdSerializer(children_invitations, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'userId not found'})
