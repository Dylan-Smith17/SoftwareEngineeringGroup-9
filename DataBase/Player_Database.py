import json, re
import random
from dotenv import load_dotenv
load_dotenv()
import ast 
import os
from Player import Player
from supabase import create_client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

def addPlayer(playerName):
    # temp_index = str(supabase.table('player').select('id').execute())
    # temp_index = int(temp_index[len(str(temp_index))-14])
    supabase.table('player').insert({'id' : random_id(), 'codename' : playerName}).execute()
    print(playerName + ' added.')

def getPlayer(playerName):
    print(supabase.table('player').select('*').eq('codename',playerName).execute())

def getId(id):
    print(supabase.table('player').select('*').eq('id',id).execute())

def deletePlayer(playerName):
    print(supabase.table('player').delete().eq('codename',playerName).execute())

def deleteId(id):
    print(supabase.table('player').delete().eq('codename',id).execute())

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
        playerName = input("Enter the player name: ")
        addPlayer(playerName)
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

