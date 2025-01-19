from rest_framework import serializers
from .models import Supplier, Product, StockMovement, SaleOrder
from bson import ObjectId


class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return ObjectId(data)


class SupplierSerializer(serializers.Serializer):
    id = ObjectIdField(read_only=True)
    name = serializers.CharField(required=True, max_length=255)
    email = serializers.EmailField(required=True)
    phone = serializers.CharField(required=True, max_length=10)
    address = serializers.CharField(required=True)

    def create(self, validated_data):
        return Supplier.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance


class ProductSerializer(serializers.Serializer):
    id = ObjectIdField(read_only=True)
    name = serializers.CharField(required=True, max_length=255)
    description = serializers.CharField(required=False)
    category = serializers.CharField(required=True, max_length=255)
    price = serializers.DecimalField(
        required=True, max_digits=10, decimal_places=2)
    stock_quantity = serializers.IntegerField(required=True)
    supplier = ObjectIdField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.category = validated_data.get('category', instance.category)
        instance.price = validated_data.get('price', instance.price)
        instance.stock_quantity = validated_data.get(
            'stock_quantity', instance.stock_quantity)
        instance.supplier = validated_data.get('supplier', instance.supplier)
        instance.save()
        return instance


class StockMovementSerializer(serializers.Serializer):
    id = ObjectIdField(read_only=True)
    product = ObjectIdField()
    quantity = serializers.IntegerField(required=True)
    movement_type = serializers.CharField(required=True)
    movement_date = serializers.DateTimeField(required=False)
    notes = serializers.CharField(required=False)

    def create(self, validated_data):
        product = Product.objects.get(id=validated_data['product'])
        if validated_data['movement_type'] == 'In':
            product.stock_quantity += validated_data['quantity']
        elif validated_data['movement_type'] == 'Out':
            if product.stock_quantity < validated_data['quantity']:
                raise serializers.ValidationError(
                    'Insufficient stock quantity.')
            product.stock_quantity -= validated_data['quantity']
        product.save()
        return StockMovement.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.product = validated_data.get('product', instance.product)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.movement_type = validated_data.get(
            'movement_type', instance.movement_type)
        instance.movement_date = validated_data.get(
            'movement_date', instance.movement_date)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.save()
        return instance


class SaleOrderSerializer(serializers.Serializer):
    id = ObjectIdField(read_only=True)
    product = ObjectIdField()
    quantity = serializers.IntegerField(required=True)
    total_price = serializers.DecimalField(
        read_only=True, max_digits=10, decimal_places=2)
    sale_date = serializers.DateTimeField(required=False)
    status = serializers.CharField(required=True)

    def create(self, validated_data):
        product = Product.objects.get(id=validated_data['product'])
        if product.stock_quantity < validated_data['quantity']:
            raise serializers.ValidationError('Insufficient stock quantity.')

        validated_data['total_price'] = validated_data['quantity'] * \
            product.price
        validated_data['status'] = 'Pending'
        sale_order = SaleOrder.objects.create(**validated_data)

        return sale_order

    def update(self, instance, validated_data):
        if 'status' in validated_data:
            if validated_data['status'] == 'Completed':
                if instance.product.stock_quantity < instance.quantity:
                    raise serializers.ValidationError(
                        'Insufficient stock quantity.')
                instance.product.stock_quantity -= instance.quantity
            instance.product.save()

        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance


class ProductStockSerializer(serializers.Serializer):
    id = ObjectIdField(read_only=True)
    name = serializers.CharField(read_only=True)
    stock_quantity = serializers.IntegerField(read_only=True)
