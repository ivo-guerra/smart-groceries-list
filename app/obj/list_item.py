from mongoengine import *


class ListItem(EmbeddedDocument):
    item_id = StringField()
    item_name = StringField()
    bar_code = StringField()
    complete = BooleanField()
