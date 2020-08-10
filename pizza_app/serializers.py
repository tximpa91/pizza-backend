from pizza_app.models import Pizza, Topping
from rest_framework import serializers

__all__ = ['ToppingSerializer', 'PizzaSerializer', 'Pizza']


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ('name',)


class PizzaSerializer(serializers.ModelSerializer):
    toppings = ToppingSerializer(many=True)

    def to_representation(self, instance):
        try:
            data = super().to_representation(instance)
            return {}
        except Exception as error:
            print(str(error))
    class Meta:
        model = Pizza
        fields = ('pizza_id', 'name', 'toppings', 'status')



