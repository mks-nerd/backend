import mongoengine  # type: ignore


class Menu(mongoengine.EmbeddedDocument):
    name = mongoengine.StringField(required=True)
    endpoint = mongoengine.StringField(required=True)


class HomePage(mongoengine.Document):
    name = mongoengine.StringField(required=True)
    menu = mongoengine.ListField(mongoengine.EmbeddedDocumentField(Menu))
