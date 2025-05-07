from datetime import datetime, timedelta
import calendar

# 1. Current Time: Use datetime.now() to get the current date and time.
def current_time():
    now = datetime.now()
    print(f"Current date and time: {now}")

# 2. Time Delta Arithmetic: Add 7 days to today using timedelta(days=7).
def time_delta_arithmetic():
    now = datetime.now()
    future_date = now + timedelta(days=7)
    print(f"7 days from today: {future_date}")

# 3. Format Dates: Format today's date as "YYYY-MM-DD" using strftime().
def format_dates():
    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d")
    print(f"Formatted date (YYYY-MM-DD): {formatted_date}")

# 4. Parse Date String: Parse "2024-01-01" into a datetime object using strptime().
def parse_date_string():
    date_str = "2024-01-01"
    parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
    print(f"Parsed date from string '{date_str}': {parsed_date}")

# 5. Get Weekday Name: Use calendar.day_name[date.weekday()] to get the name of the day.
def get_weekday_name():
    today = datetime.now()
    weekday_name = calendar.day_name[today.weekday()]
    print(f"Today is: {weekday_name}")

# 6. Date Comparison: Compare two dates and print which is earlier.
def date_comparison():
    date1 = datetime(2024, 5, 1)
    date2 = datetime(2025, 5, 1)
    
    if date1 < date2:
        print(f"{date1} is earlier than {date2}")
    elif date1 > date2:
        print(f"{date1} is later than {date2}")
    else:
        print(f"{date1} and {date2} are the same")

# 7. Generate Calendar Month: Use calendar.month(2025, 5) to print a monthly calendar.
def generate_calendar_month():
    print(f"\nCalendar for May 2025:")
    print(calendar.month(2025, 5))

# 8. Round Time to Nearest Hour: Given datetime.now(), round it to the top of the hour.
def round_time_to_nearest_hour():
    now = datetime.now()
    rounded_time = now.replace(minute=0, second=0, microsecond=0)
    if now.minute > 30:
        rounded_time += timedelta(hours=1)
    print(f"Rounded time to nearest hour: {rounded_time}")

# --- Example Usage ---
if __name__ == "__main__":
    current_time()
    time_delta_arithmetic()
    format_dates()
    parse_date_string()
    get_weekday_name()
    date_comparison()
    generate_calendar_month()
    round_time_to_nearest_hour()
