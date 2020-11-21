
from datetime import datetime as dt
from django.db import migrations, models
import os
import csv
from pathlib import Path
from django.shortcuts import get_object_or_404


csv_trans=os.path.join('trans.csv')
data_trans = csv.reader(open(csv_trans, encoding='utf-8'), delimiter = ',')


summs = []
for row in data_trans:
    summs.append(row[4])

for item in summs:
    try:
        int(item)
    except:
        float(item)
        print(item)
        print(dir(item.index))