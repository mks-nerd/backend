from datetime import date

from pydantic import BaseModel


class LeaveApplicationSchema(BaseModel):
    applicant_id: str
    start_date: date
    end_date: date
    reason: str

    class Config:
        orm_mode = True


class HolidaySchema(BaseModel):
    holiday_name: str
    holiday_date: date


class WeekendSchema(BaseModel):
    weekends: list[str]
