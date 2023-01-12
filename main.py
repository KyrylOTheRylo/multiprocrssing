import time
import datetime as dt
import random
import pandas as pd
import numpy as np
import pymongo
import threading

C = 190.0808880329132
# data = [{"DATE": str((dt.datetime.now() + dt.timedelta(i)).date()), "VALUE": random.randint(0, 1912312312)}
#       for i in range(500000)]
# df =pd.DataFrame.from_dict(data)
# df.to_csv(r"gen.csv", index=False)

db = pymongo.MongoClient()
db1 = db.get_database("db1")
db1.get_collection("test1").drop()
col = db1.get_collection("test1")

df = pd.read_csv("gen.csv").set_axis(["Date", "Value"], axis=1)


# start = time.time()
# for x in df.iterrows():
#    col.insert_one({str(x[1]['Date']): x[1]['Value']})
# end = time.time()
# print(end-start)

def send_data(data, col1):
    start = time.time()
    for x in data.iterrows():
        col1.insert_one({str(x[1]['Date']): x[1]['Value']})
    end = time.time()
    print(end - start)


df2 = df[int(len(df) / 4):int(len(df) / 2):]
df1 = df[:int(len(df) / 4):]
df3 = df[int(len(df) / 2):3 * int(len(df) / 4):]
df4 = df[3 * int(len(df) / 4):4 * int(len(df) / 4):]

db2 = db.get_database("db1")
db2.get_collection("test2").drop()
col1 = db2.get_collection("test2")
thr1 = threading.Thread(target=send_data, args=(df1, col1))
thr2 = threading.Thread(target=send_data, args=(df2, col1))
thr3 = threading.Thread(target=send_data, args=(df3, col1))
thr4 = threading.Thread(target=send_data, args=(df4, col1))
thr5 = threading.Thread(target=send_data, args=(df, col))


thr1.start()
thr2.start()
thr3.start()
thr4.start()
thr5.start()

