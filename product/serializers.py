
from .models import Product
from rest_framework import serializers
from redsky.views import get_product_name


class ProductSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ["id", "price", "currency_code", "product_name"]

    def get_product_name(self, instance):
        return get_product_name(instance.id).get("name", "")

    def to_representation(self, instance):
        serialized_data = super(ProductSerializer, self).to_representation(instance)

        serialized_data["current_price"] = {"value": serialized_data.pop("price"),
                                            "currency_code": serialized_data.pop("currency_code")}
        return serialized_data

    def to_internal_value(self, data):
        data["price"] = data["current_price"].pop("value")
        data["currency_code"] = data["current_price"].pop("currency_code")
        data.pop("current_price")
        return data
