from fastapi import APIRouter

from .models import LeaveApplication, Holiday, Weekend
from .schema import LeaveApplicationSchema, HolidaySchema, WeekendSchema

router = APIRouter(prefix="/lms")


@router.post("/apply")
def apply(leave_application: LeaveApplicationSchema):
    LeaveApplication(**leave_application.dict()).save()
    return leave_application


@router.post("/add_holiday")
def add_holiday(holiday: HolidaySchema):
    Holiday(**holiday.dict()).save()
    return holiday


@router.get("/get_holidays")
def get_holidays():
    holidays = [
        HolidaySchema(**holiday.to_mongo()) for holiday in Holiday.objects.all()
    ]
    return holidays


@router.post("/add_weekend")
def add_weekend(weekend: WeekendSchema):
    Weekend(**weekend.dict()).save()
    return weekend


@router.get("/get_weekends")
def get_weekends():
    weekends = [
        WeekendSchema(**weekend.to_mongo()) for weekend in Weekend.objects.all()
    ]
    return weekends
