def convertDateFormat(date):
    day = date[:2]
    month = date[2:4]
    year = date[4:]
    return f"{month}/{day}/{year}"

