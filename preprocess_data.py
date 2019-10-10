import pandas as pd
import numpy as np
import os

m_time      = '   missn,_time '
t_time      = '   _totl,_time '
yaw_v       = '   ____Q,rad/s '
heading_mag = '   hding,__mag '
yaw_deg     = '   _beta,__deg '
roll_deg    = '   _roll,__deg '
roll_v      = '   ____R,rad/s '
pitch_deg   = '   pitch,__deg '
pitch_v     = '   ____P,rad/s '
alt         = '   __alt,ftmsl '
vv          = '   __VVI,__fpm '
v           = '   Vtrue,_ktas '
rpm_prop    = '   rpm_1,_prop '
throttle     = '   thro1,_part '

state = [ m_time,
    t_time,
    yaw_v,
    yaw_deg,
    roll_deg,
    roll_v,
    pitch_deg,
    pitch_v,
    vv,
    alt,
    v,
    rpm_prop,
    throttle,
]

elev_servo                  = '   _elev,servo '
ailrn_servo                  = '   ailrn,servo '
ruddr_servo                  = '   ruddr,servo '

action = [
    elev_servo,
    ailrn_servo,
    ruddr_servo
]


columns = []
columns.extend(state)
columns.extend(action)

data0 = 'dataset_00.csv'
data1 = 'dataset_01.csv'
data2 = 'dataset_02.csv'
data3 = 'dataset_03.csv'
data4 = 'dataset_04.csv'
files = [data0, data1, data2, data3, data4]
os.chdir('./data')

def count_lines(*files):
    num_lines = 0
    for file in files:
        num_lines += sum(1 for line in open(file))
    return num_lines

#print(count_lines(*files))
# >> 380.543

#doc https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html

df = pd.read_csv(data1, sep='|', usecols=columns, float_precision='high')

maneuver_index = 'maneuver_index'
maneuver_name = 'maneuver_name'
maneuver_datapoint_index = 'maneuver_datapoint_index'
maneuver_type = 'maneuver_type'

# add maneuver_index column
# add maneuver_name column
# add maneuver_datapoint_index column
# add maneuver_type column


# merke dir index an reset points.
#  predecessor > 1 AND current = 0
def get_maneuver_startindex(df: pd.DataFrame):
    row_predecessor = {m_time : 0}
    indices = []
    for index, row in df.iterrows():    
        if int(row_predecessor[m_time]) >= 1 and int(row[m_time]) == 0:
            indices.append(index)
        row_predecessor = row
    return indices

print(get_maneuver_startindex(df))
# füge index column hinzu 
# index_col namen vergeben und hochzaehlen
