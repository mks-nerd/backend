import mongoengine  # type: ignore
from bson import ObjectId


class LeaveApplication(mongoengine.Document):
    application_id = mongoengine.StringField(primary_key=True, default=str(ObjectId()))
    applicant_id = mongoengine.StringField(required=True)
    start_date = mongoengine.DateField(required=True)
    end_date = mongoengine.DateField(required=True)
    reason = mongoengine.StringField(required=True)
    status = mongoengine.StringField(
        choices=("pending", "approved", "rejected"), default="pending"
    )

    meta = {"db_alias": "backend_data", "collection": "leave_applications"}


class Holiday(mongoengine.Document):
    holiday_name = mongoengine.StringField(required=True, unique=True)
    holiday_date = mongoengine.DateField(required=True, unique=True)

    meta = {"db_alias": "backend_data"}


class Weekend(mongoengine.Document):
    weekends = mongoengine.ListField(mongoengine.StringField())

    meta = {"db_alias": "backend_data"}
