import socket
import sqlite3
import datetime

con = sqlite3.connect('C:\\Users\Lena\Desktop\shop.sqlite')


cursor = con.cursor()

cursor.execute( '''CREATE TABLE IF NOT EXISTS station_status
                (station_id,
                last_date,
                alarm1,
                alarm2,
                PRIMARY KEY(station_id))
                ''')

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1', 12345))
s.listen(5)

while True:
    last_date=datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    c, addr =s.accept()
    print('Got connection from {}'.format(addr))
    c.send("Thank you for connecting".encode())
    recive = c.recv(1024)
    ar=recive.decode()
    print(ar,'ar(type)')
    ar=ar.split()
    print(ar,type(ar),'after split')
    ar.insert(1,last_date)
    ar=tuple(ar)
    print(ar,type(ar))
    # cursor = con.cursor()

    cursor.execute("INSERT OR REPLACE INTO station_status VALUES (?,?,?,?)", (ar))

    con.commit()
    # cursor.execute("SELECT last_date FROM TabLena2 ")
    # records = cursor.fetchone()
    # print(records, 'records')
# con.close()



