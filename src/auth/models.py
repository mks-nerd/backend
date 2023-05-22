import mongoengine  # type: ignore


class User(mongoengine.Document):
    first_name = mongoengine.StringField(required=True)
    last_name = mongoengine.StringField(required=True)
    age = mongoengine.IntField(required=True)
    likes = mongoengine.ListField(required=True)

    meta = {"db_alias": "backend_data"}
