from influxdb import InfluxDBClient
import pandas as pd
import numpy as np
import time

def main():
    df = pd.DataFrame(data=np.random.randint(low=0, high=10, size=(5, 5)),
                      columns=['app_name', 'type', 'variable', 'd', 'e'],
                      index=pd.date_range('1/1/2018', periods=5))
    print(df)

    client = InfluxDBClient('host', 'port', 'user', 'passwd', 'dbname')
    lines=[]
    for index, row in df.iterrows():
        line_str = '{0},application={1},type={2} variable={3} {4}'.format(
                'measure', row['app_name'], row['type'], row['variable'], int(time.mktime(index.to_datetime().timetuple())*1e3))
        lines.append(line_str)

    client.write_points(lines, time_percision='ms', database='metrics_db', protocol='line')


if __name__ == '__main__':
    main()
