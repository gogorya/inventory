from mongoengine import Document, StringField, EmailField, ValidationError,  DecimalField, IntField, ReferenceField, DENY, NULLIFY, DateTimeField
from datetime import datetime


class Supplier(Document):
    name = StringField(required=True, max_length=255)
    email = EmailField(required=True, unique=True)
    phone = StringField(required=True, max_length=10)
    address = StringField(required=True)

    def clean(self):
        if len(self.phone) != 10 or not self.phone.isdigit():
            raise ValidationError('Phone number must be exactly 10 digits.')

    def __str__(self):
        return f'Name: {self.name}, Email: {self.email}'


class Product(Document):
    name = StringField(required=True, max_length=255)
    description = StringField()
    category = StringField(required=True, max_length=255)
    price = DecimalField(required=True)
    stock_quantity = IntField(required=True)
    supplier = ReferenceField(Supplier, reverse_delete_rule=DENY)

    def clean(self):
        if self.stock_quantity < 0:
            raise ValidationError(
                'Stock quantity must be greater than or equal to 0.')
        if self.price < 0:
            raise ValidationError('Price must be greater than or equal to 0.')

    def __str__(self):
        return f'Name: {self.name}, Category: {self.category}'


class SaleOrder(Document):
    product = ReferenceField(Product, required=True,
                             reverse_delete_rule=NULLIFY)
    quantity = IntField(required=True)
    total_price = DecimalField(required=True)
    sale_date = DateTimeField(default=datetime.utcnow)
    status = StringField(required=True)

    def clean(self):
        valid_statuses = ['Pending', 'Completed', 'Cancelled']
        if self.status not in valid_statuses:
            raise ValidationError(f'Status must be one of {valid_statuses}.')

        if self.total_price != self.quantity * self.product.price:
            raise ValidationError(
                'Total price must be equal to quantity * product price.')

    def __str__(self):
        return f'Product: {self.product.name}, status: {self.status}'


class StockMovement(Document):
    product = ReferenceField(Product, required=True,
                             reverse_delete_rule=NULLIFY)
    quantity = IntField(required=True)
    movement_type = StringField(required=True)
    movement_date = DateTimeField(default=datetime.utcnow)
    notes = StringField()

    def clean(self):
        valid_statuses = ['In', 'Out']
        if self.movement_type not in valid_statuses:
            raise ValidationError(f'Status must be one of {valid_statuses}.')

    def __str__(self):
        return f'Product: {self.product.name}, Movement: {self.movement_type}'
