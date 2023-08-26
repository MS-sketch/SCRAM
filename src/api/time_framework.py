import datetime

def convertToSTD(seconds):
    years = seconds // (365 * 24 * 3600)
    seconds %= 365 * 24 * 3600
    days = seconds // (24 * 3600)
    seconds %= 24 * 3600
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    strYears = ""
    strDays = ""
    strHours = ""
    strMinutes = ""
    strSeconds = ""

    if years == 1 or years == 0:
        strYears = str(years) + " year"

    elif years > 1:
        strYears = str(years) + " years"

    if days == 1 or days == 0:
        strDays = str(days) + " day"

    elif days > 1:
        strDays = str(days) + " days"

    if hours == 1 or hours == 0:
        strHours = str(hours) + " hour"

    elif hours > 1:
        strHours = str(hours) + " hours"

    if minutes == 1 or minutes == 0:
        strMinutes = str(minutes) + " minute"

    elif minutes > 1:
        strMinutes = str(minutes) + " minutes"

    if seconds == 1 or seconds == 0:
        strSeconds = str(seconds) + " second"

    elif seconds > 1:
        strSeconds = str(seconds) + " seconds"

    return strYears, strDays, strHours, strMinutes, strSeconds
