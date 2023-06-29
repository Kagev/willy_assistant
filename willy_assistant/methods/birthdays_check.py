
from project_willy.methods.imports import datetime, timedelta

CURRENT_DATE = datetime.now()


# ----------Birthdays checking----------
def main(days_from_user: int, record_birthday: datetime) -> None:
    if len(str(days_from_user)) > 3:
        raise ValueError
    if isinstance(record_birthday, datetime) and len(str(days_from_user)) <= 3:
        next_date = CURRENT_DATE + timedelta(days=days_from_user)
        try:
            record_birthday_date = datetime(year=datetime.now().year, month=record_birthday.month, day=record_birthday.day)
        except ValueError:
            record_birthday_date = datetime(year=datetime.now().year, month=3, day=1)
        if CURRENT_DATE <= record_birthday_date <= next_date:
            return True
