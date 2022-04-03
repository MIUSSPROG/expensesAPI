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
    CheckParentSerializer, SendInvitationSerializer, ChildrenByParentIdSerializer, ConfirmInvitationSerializer, \
    GetInvitationSerializer, SendInvitation2Serializer, ConfirmInvitation2Serializer, CheckInvitationSerializer, \
    ChildParentListSerializer


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


class ParentDeleteView(generics.DestroyAPIView):
    serializer_class = ParentListSerializer
    queryset = Parent.objects.all()


class ParentListView(generics.ListAPIView):
    serializer_class = ParentListSerializer
    queryset = Parent.objects.all()


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


class SendInvitation2UpdateView(generics.UpdateAPIView):
    serializer_class = SendInvitation2Serializer
    queryset = Child.objects.all()


class ChildrenByParentId(generics.ListAPIView):
    serializer_class = ChildrenByParentIdSerializer
    queryset = Child.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            parentId = request.query_params["parentId"]
            if parentId is not None:
                children_invitations = Invitation.objects.filter(parent=parentId)
                serializer = ChildrenByParentIdSerializer(children_invitations, many=True)
                return Response(serializer.data)
        except Exception:
            return Response({'error': "incorrect params"}, status=status.HTTP_400_BAD_REQUEST)


class ConfirmInvitation(generics.UpdateAPIView):
    serializer_class = ConfirmInvitationSerializer
    queryset = Invitation.objects.all()


class ConfirmInvitation2(generics.UpdateAPIView):
    serializer_class = ConfirmInvitation2Serializer
    queryset = Child.objects.all()


class CheckInvitationView(generics.ListAPIView):
    serializer_class = CheckInvitationSerializer
    queryset = Child.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            parentId = request.query_params["parentId"]
            login = request.query_params["login"]
            if parentId is not None and login is not None:
                try:
                    child = Child.objects.get(login=login, parent=parentId)
                    serializer = CheckInvitationSerializer(child)
                    return Response(serializer.data)
                except Exception:
                    return Response({'error': "child doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({'error': 'not found'}, status=status.HTTP_404_NOT_FOUND)


class GetInviatationId(generics.ListAPIView):
    serializer_class = GetInvitationSerializer
    queryset = Invitation.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            childId = request.query_params["childId"]
            parentId = request.query_params["parentId"]
            if childId is not None and parentId is not None:
                invitation = Invitation.objects.get(parent=parentId, child=childId)
                serializer = GetInvitationSerializer(invitation)
                return Response(serializer.data)
        except Exception:
            return Response({'error': "incorrect params"}, status=status.HTTP_400_BAD_REQUEST)


class CheckParentView(generics.ListAPIView):
    serializer_class = ParentListSerializer
    queryset = Parent.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            login = request.query_params["login"]
            if login is not None:
                try:
                    parent = Parent.objects.get(login=login)
                    serializer = ParentListSerializer(parent)
                    return Response(serializer.data)
                except Exception:
                    return Response({}, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({'error': "incorrect params"}, status=status.HTTP_400_BAD_REQUEST)


class CheckChildParentView(generics.ListAPIView):
    serializer_class = ChildParentListSerializer
    queryset = Child.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            login = request.query_params["login"]
            if login is not None:
                try:
                    child = Child.objects.get(login=login)
                    serializer = ChildParentListSerializer(child)
                    return Response(serializer.data)
                except Exception:
                    return Response({}, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({'error': "incorrect params"}, status=status.HTTP_400_BAD_REQUEST)
