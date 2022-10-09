from mongoengine import *


class Product(DynamicDocument):
    product_name = StringField()
    meta = {'collection': 'products'}
