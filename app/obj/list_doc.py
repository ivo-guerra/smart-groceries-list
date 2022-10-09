from mongoengine import *

from obj.list_item import ListItem


class ListDoc(Document):
    user_id = IntField()
    list_id = IntField()
    item_list = EmbeddedDocumentListField(ListItem)
    meta = {'collection': 'lists'}
