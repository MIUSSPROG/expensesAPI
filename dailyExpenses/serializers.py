import hashlib

from django.contrib.auth.hashers import make_password, PBKDF2PasswordHasher
from rest_framework import serializers

from dailyExpenses.models import Parent, Child, Plan, Category


# class RoleCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Role
#         fields = '__all__'


class ParentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'


class ParentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'


# class RoleListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Role
#         fields = "__all__"


class ChildCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = '__all__'


class ChildAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = '__all__'


class ChildListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = "__all__"


class ChildrenDetailSerializer(serializers.ModelSerializer):
    children = ChildListSerializer(many=True)

    class Meta:
        model = Parent
        fields = ('login', 'children')


# ('name', 'category_name', 'price', 'date', 'image', 'confirm')
class PlanCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"

    category_name = serializers.SerializerMethodField('get_category_name')

    def get_category_name(self, obj):
        return obj.category.name


class ChildCheckDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = "__all__"


class SaveParentEncodedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ('login', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        encoded_pass = hashlib.sha256(str(validated_data['password']).encode())
        pass_to_send = encoded_pass.hexdigest()
        parent = Parent(
            login=validated_data['login'],
            password=pass_to_send
        )
        parent.save()
        return parent


class SaveChildEncodedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = ('login', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # hasher = PBKDF2PasswordHasher()
        # password = make_password(validated_data['password'], hasher='pbkdf2_sha256', salt='4WSAQIdeZBGWWpovpH9uZ9')
        # password = hasher.encode(password=validated_data['password'], salt='4WSAQIdeZBGWWpovpH9uZ9', iterations=0)
        encoded_pass = hashlib.sha256(str(validated_data['password']).encode())
        pass_to_send = encoded_pass.hexdigest()
        child = Child(
            login=validated_data['login'],
            password=pass_to_send
        )
        child.save()
        return child


# class SendInvitationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Invitation
#         fields = "__all__"


class SendInvitation2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = "__all__"


class CheckParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = "__all__"


class CheckChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = "__all__"


class PlanChildrenDetailSerializer(serializers.ModelSerializer):
    plans = PlanCreateSerializer(many=True)

    class Meta:
        model = Child
        fields = ('login', 'plans')


class PlanConfirmUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"


class PlanListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


# class ChildrenByParentIdSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Invitation
#         fields = ('child_id', 'child_login', 'confirm')
#
#     child_login = serializers.SerializerMethodField('get_child_login')
#
#     def get_child_login(self, obj):
#         return obj.child.login


class ChildParentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = ('parent_id', 'parent_login', 'confirmed')

    parent_login = serializers.SerializerMethodField('get_parent_login')

    def get_parent_login(self, obj):
        return obj.parent.login


# class ConfirmInvitationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Invitation
#         fields = "__all__"


class ConfirmInvitation2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = "__all__"


# class GetInvitationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Invitation
#         fields = "__all__"


class CheckInvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = "__all__"
