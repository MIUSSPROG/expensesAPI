from rest_framework import serializers

from dailyExpenses.models import Parent, Child, Plan, Category


class ParentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'


class ParentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'


class ChildCreateSerializer(serializers.ModelSerializer):
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
