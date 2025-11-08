def getAlarmTime(day, onVacation):
    if onVacation:
            if day == 0 or day == 6:
                return "10:00"
            else:
                return "7:00"
    
    if day == 0 or day == 6:
        return "off"
    else:
        return "10:00"
    