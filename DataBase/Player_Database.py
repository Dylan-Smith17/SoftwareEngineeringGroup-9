import json, re
import random
from dotenv import load_dotenv
load_dotenv()
import ast 
import os
from Player import Player
from supabase import create_client

load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

def addPlayer():
    playerName = input("Enter the player name: ")
    playerID = input("Enter the player ID: ")
    supabase.table('player').insert({'id': playerID, 'codename': playerName}).execute()
    print(playerName + ' added.')
    write_data_to_json(readAll())

def getPlayer(playerName):
    print(supabase.table('player').select('*').eq('codename',playerName).execute())

def getId(id):
    print(supabase.table('player').select('*').eq('id',id).execute())

def deletePlayer(playerName):
    print(supabase.table('player').delete().eq('codename',playerName).execute())

def deleteId(id):
    print(supabase.table('player').delete().eq('id',id).execute())

def readAll():
    print('begin')
    print(supabase.table('player').select('*').execute())
    print('end')
    output = str(supabase.table('player').select('*').execute())
    return output



def write_data_to_json(string):
    start_index = string.index("[")
    end_index = string.index("]", start_index) +1
    data_string = string[start_index:end_index]
    
    data_string = data_string.replace("'", '"')
    data = json.loads(data_string)
    
    with open('data.json', 'w') as file:
        json.dump(data, file)

def read_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def menu():
    print("1. Add Player")
    print("2. Get Player by Name")
    print("3. Get Player by ID")
    print("4. Delete Player by Name")
    print("5. Delete Player by ID")
    print("6. Read all in database")
    print("7. Exit")

def random_id():
    p = "0123456789"
    temp = ''.join(random.choice(p) for _ in range(6))
    temp_id = int(temp)
    data = read_json_file('data.json')
    temp_id = 357735
    for d in data:
        if(int(d['id']) == temp_id):
            while temp_id == int(d['id']):
                temp_id= ''.join(random.choice(p) for _ in range(6))
    return temp_id

while True:
    menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        addPlayer() # Call addPlayer without any arguments
    elif choice == '2':
        playerName = input("Enter the player name: ")
        getPlayer(playerName)
    elif choice == '3':
        id = input("Enter the player ID: ")
        getId(id)
    elif choice == '4':
        playerName = input("Enter the player name: ")
        deletePlayer(playerName)
    elif choice == '5':
        id = input("Enter the player ID: ")
        deleteId(id)
    elif choice == '6':
        readAll()
    elif choice == '7':
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")


write_data_to_json(readAll())

import socket
import json


#Socket sending Json data
def send_data_over_udp(json_data, host='localhost', port=7500):
    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        # Convert JSON data to bytes
        json_bytes = json.dumps(json_data).encode('utf-8')
        # Send data
        sock.sendto(json_bytes, (host, port))


json_data = [
    {"id": 1, "codename": "Opus"},
    {"id": 357735, "codename": "Biggie Smalls"},
    {"id": 357735, "codename": "test 2"},
    {"id": 13556, "codename": "bobby"},
    {"id": 357735, "codename": "test3"},
    {"id": 638895, "codename": "test4"},
    {"id": 650463, "codename": "uark wifi"},
    {"id": 420667, "codename": "test4"}
]
# Send JSON data over UDP
send_data_over_udp(json_data)

#menu implementation
#add player 
def addPlayer(playerName):
    supabase.table('player').insert({'id': random_id(), 'codename': playerName}).execute()
    print(playerName + ' added.')

#get/print player

def getPlayer(playerName):
    result = supabase.table('player').select('*').eq('codename', '=', playerName).execute()
    print(result)



#get/print by player ID

def getId(playerId):
    result = supabase.table('player').select('*').eq('id', playerId).execute()
    print(result)

#delete player by NAME

def deletePlayer(playerName):
    result = supabase.table('player').delete().eq('codename', playerName).execute()
    print(f"Player {playerName} deleted.")

#Delete player by ID
    
def deleteId(playerId):
    result = supabase.table('player').delete().eq('id', playerId).execute()
    print(f"Player with ID {playerId} deleted.")

#Read all players from database

def readAll():
    print('begin')
    result = supabase.table('player').select('*').execute()
    print(result)
    print('end')







