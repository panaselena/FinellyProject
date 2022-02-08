import datetime
last_date=datetime.datetime.now().strftime('%Y-%M-%d%H:%m')
print(last_date,type(last_date), id(last_date))


list=['jjj','kkkk']
print(list,type(list))
list.insert(0,'8888')
print(list,type(list))
list=tuple(list)
print(list,(type(list)))
