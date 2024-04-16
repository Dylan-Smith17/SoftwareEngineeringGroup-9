import json, re
import random
from dotenv import load_dotenv
load_dotenv()
import ast 
import os
from Player import Player
from supabase import create_client

load_dotenv()
cwd = os.getcwd()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

def addPlayer(playerName, playerID):
    playerName.replace("'","/'")
    supabase.table('player').insert({'id': playerID, 'codename': playerName}).execute()
    write_data_to_json(readAll(), 'data.json')

def getPlayer(playerName):
    print('hi')
    #print(supabase.table('player').select('*').eq('codename',playerName).execute())
    codename = supabase.table('player').select('*').eq('codename',playerName).execute()
    temp = str(codename)
    temp = temp.split("data=")[1]
    temp = temp[:2]
    return temp

def getId(id):
    print(supabase.table('player').select('*').eq('id',id).execute())

def get_by_id(id):
    codename = supabase.table('player').select('codename').eq('id',id).execute()
    temp = str(codename)
    temp = temp[20:]
    temp = temp[:-14]
    return temp
# def get_player_by_id(player_id):
#     # Query the database for the player with the given ID
#     result = supabase.table('player').select('codename').eq('id', player_id).execute()
#     # Check if the result contains any data
#     if result['count'] > 0:
#         # Extract the player's name from the result
#         player_name = result['data'][0]['codename']
#         return player_name
#     else:
#         # If no player with the given ID is found, return None
#         return 'None'

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



def write_data_to_json(string, filename):
    start_index = string.index("[")
    end_index = string.index("]", start_index) +1
    data_string = string[start_index:end_index]
    data_string = data_string.replace("'", '"')
    #data_string = re.sub(r"(?<!codename': )'", '"', data_string)
    print(data_string)
    data = json.loads(data_string)
    
    with open(filename, 'w') as file:
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


# def random_id():
#     p = "0123456789"
#     temp = ''.join(random.choice(p) for _ in range(6))
#     temp_id = int(temp)
#     data = read_json_file('data.json')
#     temp_id = 357735
#     for d in data:
#         if(int(d['id']) == temp_id):
#             while temp_id == int(d['id']):
#                 temp_id= ''.join(random.choice(p) for _ in range(6))
#     return temp_id

# while True:
#     menu()
#     choice = input("Enter your choice: ")
#     if choice == '1':
#         name = input('Enter name: ')
#         id = input('Enter id: ')
#         addPlayer(name, id) # Call addPlayer without any arguments
#     elif choice == '2':
#         playerName = input("Enter the player name: ")
#         getPlayer(playerName)
#     elif choice == '3':
#         id = input("Enter the player ID: ")
#         print("id: " + get_by_id(id))
#     elif choice == '4':
#         playerName = input("Enter the player name: ")
#         deletePlayer(playerName)
#     elif choice == '5':
#         id = input("Enter the player ID: ")
#         deleteId(id)
#     elif choice == '6':
#         readAll()
#     elif choice == '7':
#         break
#     else:
#         print("Invalid choice. Please enter a number between 1 and 7.")




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

#Read all players from database

# def readAll():
#     print('begin')
#     result = supabase.table('player').select('*').execute()
#     print(result)
#     print('end')







