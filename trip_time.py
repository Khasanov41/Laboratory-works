"""
trip_time.py

Печатает время прибытия поезда на конечную станцию в виде «HH час : MM мин».
Определяет также количество полных суток в пути до конечной станции.

(c)Хасанов Ислам, КЭ-101
"""


def get_time(departure_hour, departure_minutes, hours, minutes):
    """
    Input:
        departure_hour – departure hours (int)
        departure_minute – departure minutes (int)
        hours - trip duration in hours (int)
        minutes – trip duration in minutes (int)
    Output:
        arrival_hour - arrival hours (int)
        arrival_minute - arrival minutes (int)
        days - number of days in the trip (int)
    """

    days = hours // 24
    arrival_minute = (departure_minutes + minutes) % 60
    arrival_hour = ((departure_hour + hours) % 24) + (departure_minutes + minutes) // 60

    return arrival_hour, arrival_minute, days


if __name__ == "__main__":

    dep_hours = int(input("Departure hours: "))
    dep_minutes = int(input("Departure minutes: "))
    trip_hours = int(input("Trip duration in hours: "))
    trip_minutes = int(input("Trip duration in minutes: "))

    time = get_time(dep_hours, dep_minutes, trip_hours, trip_minutes)

    print(f"\n{time[0]:02} hours : {time[1]:02} minutes\n{time[2]} days")
