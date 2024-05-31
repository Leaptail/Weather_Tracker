import weatherfunc as wfc
import datetime as dt
import meteomatics.api as api
import pandas as pd
from datetime import datetime


username = 'student_soh_evans'
password = 'R5VrVo87aZ'


#Singapore Coordinates
coordinates = [(1.35,103.82)]

#2 meters above ground in Celsius, precipitation over the hour, 
parameters = ['t_2m:C', 'precip_1h:mm']


model = 'mix'

#starting time in utc.
startdate = dt.datetime.utcnow().replace(minute=0, second=0, microsecond=0)
enddate = startdate + dt.timedelta(days=1)
interval = dt.timedelta(hours=1)

df = api.query_time_series(coordinates, startdate, enddate, interval, parameters, username, password, model=model)

temperature_list = wfc.get_column(df, "t_2m:C")

#list of hours in negative numbers
hour_list = []
for i in range(25):
    tempnum = i - 25
    hour_list.append(tempnum)

# print(hour_list)
# print(temperature_list)

wfc.plot_graph(hour_list,temperature_list, 'Temperature trend in Singapore')