from django.contrib.auth.hashers import make_password
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


class PlanCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"


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
        parent = Parent(
            login=validated_data['login'],
            password=make_password(validated_data['password'])
        )
        parent.save()
        return parent


class SaveChildEncodedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = ('login', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        child = Child(
            login=validated_data['login'],
            password=make_password(validated_data['password'])
        )
        child.save()
        return child


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


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
