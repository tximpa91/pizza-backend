from pizza_app.models import Pizza, Topping
from rest_framework import serializers

__all__ = ['ToppingSerializer', 'PizzaSerializer', 'Pizza']


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ('name',)


class PizzaSerializer(serializers.ModelSerializer):
    toppings = ToppingSerializer(many=True)

    class Meta:
        model = Pizza
        fields = ('pizza_id', 'name', 'toppings', 'status')



