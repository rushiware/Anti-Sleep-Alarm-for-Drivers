import serial
import time
import firebase_admin
from firebase_admin import credentials, db
import json

srl = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)
srl.reset_input_buffer()

cred = credentials.Certificate("quadrangle_auth.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://quadrangle-5e637-default-rtdb.firebaseio.com/'
    })
ref = db.reference("/")
print("Connected to Firebase successfully!!")

def main():
    line = srl.readline() 

    if line:
        received_data = line.decode()  
        data = received_data.split(",")
        sid = data[0].upper()
        cnt = data[1]

        ref.set({sid: {"count": cnt}})
        print(ref.get())

if __name__ == '__main__':
    while (True):
        main()
        time.sleep(1)