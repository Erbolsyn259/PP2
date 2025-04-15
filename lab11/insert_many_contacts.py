import json
from psycopg2 import DatabaseError
from update import insert, update, query
from config import load_config

def main():
    config = load_config()

    with open("contacts.json", "r") as data:
        contacts = json.load(data)
    for contact in contacts:
        try:
            if query(contact["name"], contact["second_name"], contact["last_name"], config) == None:
                print(f"Новые данные про {contact["name"]}")
                insert(contact["name"], contact["second_name"], contact["last_name"], contact["phone_number"], config)
            else:
                print(f"Человек с данными \n{contact} \n уже есть \n")
                update(contact["name"], contact["second_name"], contact["last_name"], contact["phone_number"], config)
        except (DatabaseError, Exception) as error:
            print(error)

if __name__ == "__main__":
    main()