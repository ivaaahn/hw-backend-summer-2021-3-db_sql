# INFO
# Вывести топ 5 самых коротких по длительности перелетов
# В ответе должно быть 2 колонки [flight_no, duration]
TASK_1_QUERY = """
select flight_no, (scheduled_arrival - scheduled_departure) as duration 
from flights
order by duration
limit 5;
"""

#  flight_no | duration
# -----------+----------
#  PG0148    | 00:25:00
#  PG0039    | 00:25:00
#  PG0040    | 00:25:00
#  PG0014    | 00:25:00
#  PG0149    | 00:25:00


# INFO
# Вывести топ 3 рейса по числу упоминаний в таблице flights
# количество упоминаний которых меньше 50
# В ответе должно быть 2 колонки [flight_no, count]
TASK_2_QUERY = """
select flight_no, COUNT(flight_no) as number_of_mention
    from flights
group by flight_no
having COUNT(*) < 50
order by number_of_mention desc
limit 3;
"""

#  flight_no | count
# -----------+-------
#  PG0611    |   396
#  PG0201    |   396
#  PG0303    |   396


# INFO
# Вывести число перелетов внутри одной таймзоны
# Нузно вывести 1 значение в колонке count
TASK_3_QUERY = """
select count(*) from flights f
    join airports_data dep on f.departure_airport = dep.airport_code
    join airports_data arr on f.arrival_airport = arr.airport_code
    where dep.timezone = arr.timezone
"""
#  count
# --------
#  109185
