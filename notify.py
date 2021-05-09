import datetime
import mysql.connector
import requests
# -*- coding: utf-8 -*-
from Tools.demo.beer import n

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database ="so_list"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM cus_name ")
myresult = mycursor.fetchall()

from datetime import date

date1 = date.today()
today1 = str(date1)
# print(today1)

from calendar import mdays
from datetime import datetime, timedelta

today = datetime.now()
next_month_of_today = today + timedelta(mdays[today.month])
next_month = next_month_of_today.strftime("%Y-%m-%d")
next_month_str = str(next_month)
print(next_month_str)


for x in myresult:
  text2 = x[2].strftime("%Y-%m-%d")
  print(text2)
  text3 = str(text2)
  a = text3.split()
  b = str(x[0])
  # print(type(b))

  if a[0] == today1:
    url = 'https://notify-api.line.me/api/notify'
    token = '6Nw9xHyLY81jCFJKsKIXcbgcRr9XDRZJFYRNeSU60ta'
    headers = {'content-type': 'application/x-www-form-urlencoded', 'Authorization': 'Bearer ' + token}

    msg = "\nSO หมายเลข :" + x[1] + "\nCustomer NO. : " + b + " \nชื่อลูกค้า :" + x[4] + "\nชื่อผู้ดูแลงาน :  " + x[3] + " \nExpire : " + a[0]
    r = requests.post(url, headers=headers, data={'message': msg})
    print(r.text)

  if a[0] == next_month_str:
    url = 'https://notify-api.line.me/api/notify'
    token = '6Nw9xHyLY81jCFJKsKIXcbgcRr9XDRZJFYRNeSU60ta'
    headers = {'content-type': 'application/x-www-form-urlencoded', 'Authorization': 'Bearer ' + token}

    msg = "\nSO หมายเลข :" + x[1] + "\nCustomer NO. : " + b + " \nชื่อลูกค้า :" + x[4] + "\nชื่อผู้ดูแลงาน :  " + x[3] + "\nจะหมดอายุในอีกหนึ่งเดือนข้างหน้า : " + a[0]
    r = requests.post(url, headers=headers, data={'message': msg})
    print(r.text)