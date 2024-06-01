import weatherfunc as wfc
import datetime as dt
import meteomatics.api as api
from datetime import datetime
import time


#list of hours in negative numbers
hour_list = []
for i in range(25):
    tempnum = i - 25
    hour_list.append(tempnum)

#this is the main loop, that runs the code approximately every hour to give a live feed of the graph.
while True:
    #Login for meteomatics
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

    #extract list of temperatures
    temperature_list = wfc.get_column(df, "t_2m:C")

    wfc.plot_graph(hour_list,temperature_list, 'Temperature trend in Singapore')

    time.sleep(3600)

    wfc.clear_graphs()
    print("running")

#debugging code
# print(hour_list)
# print(temperature_list)
