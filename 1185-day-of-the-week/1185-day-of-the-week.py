import datetime
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        date_obj = datetime.datetime(year, month, day)
    
        # Get the weekday as an integer (Monday is 0 and Sunday is 6)
        weekday = date_obj.weekday()

        # Use the weekday integer to get the corresponding day of the week
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return days_of_week[weekday]