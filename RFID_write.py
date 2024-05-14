from mfrc522 import *
import RPi.GPIO as GPIO
import signal
import sys
from DBHandler import *
from RFID_read import get_reading

def end_read(signal, frame):
    global continue_reading
    print("/n CTRL-C captured, ending reading")
    continue_reading = False
    GPIO.cleanup()
    sys.exit()

signal.signal(signal.SIGINT, end_read)

def write_to_card(personne: str, typeTravail: TypeTravail):
    reader = SimpleMFRC522()
    connection = create_connection()
    all_employees = get_all_employees(connection)

    try:
        #inputText = input("Input Badge Name : ")
        print(f"Place the RFID tag to the reader")
        id, text = get_reading()
        for results in all_employees:
            if results[1] == id:
                print(f"RFID already used. In database: {results[2]}, on the card {text}")
                sys.exit()
        reader.write(personne)
        create_new_employee(connection, id, personne, typeTravail)
        print(f"{personne} was written to the RFID Card and Database")
    finally:
        GPIO.cleanup
        connection.close()

if __name__ == "__main__":
    write_to_card("Karim", TypeTravail.HORRAIRE.value)
