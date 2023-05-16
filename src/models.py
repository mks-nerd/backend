from mongoengine import Document, StringField, IntField, ListField  # type: ignore


class User(Document):
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    age = IntField(required=True)
    likes = ListField(required=True)
