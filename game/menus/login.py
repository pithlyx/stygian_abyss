from sqlalchemy.orm import sessionmaker
from stygian_abyss.db.db_models import User, Character, Base, Char_Class, Armor, Weapon
from stygian_abyss.db.db_menu import create_table, create_entry, update_entry, drop_entry
from sqlalchemy import create_engine
import datetime
from classes import *

engine = create_engine('sqlite:///db/rpg_database.db', echo=True)
Session = sessionmaker(bind=engine)

def create_user(session, username):
    print(f'Creating user {username}...')
    password = input("Create a new password: ")
    if not password:
        return
    password_verify = input("Enter the password again to verify: ")
    if password != password_verify:
        raise ValueError("Passwords do not match.")
    new_user = User(name=username, password=password,
                    created_at=datetime.datetime.now())
    session.add(new_user)
    session.commit()
    print("New user created!")
    user_id = new_user.id  # Retrieve the ID from the newly created user
    session.close()
    return Player(username, user_id)  # Pass the ID to the Player object


def login():
    while True:
        username = input("Enter your username: ")

        # Check if the user exists in the database
        session = Session()
        if user := session.query(User).filter_by(name=username).first():
            tries = 0
            while True:
                # User exists, validate password
                password = input("Enter your password: ")
                if password == user.password:
                    print("Login successful!")
                    session.close()
                    return user
                else:
                    print("Invalid password.")
                    tries += 1
                    if tries == 3:
                        print("Too many tries. Exiting.")
                        session.close()
                        break
        else:
            print("User not found.")
            while True:
                try:
                    return create_user(session, username)
                except ValueError as e:
                    print(f"Error creating user: {str(e)}")
                except Exception as e:
                    print(f"Error: {str(e)}")


def character_select(user):
    session = Session()
    characters = session.query(Character).filter_by(user_id=user.id).all()
    session.close()

    if not characters:
        print("No characters found.")
        create_character(user)
    else:
        print("Select a character:")
        user.list_characters()
        while True:
            choice = input("Enter the number of the character: ")
            if choice.isdigit():
                index = int(choice)
                if 1 <= index <= len(characters):
                    selected_character = characters[index - 1]
                    print(f"Character selected: {selected_character.name}")
                    return selected_character
            print("Invalid choice. Please try again.")

def create_character(user):
    while True:
        session = Session()
        classes = session.query(Char_Class).all()
        session.close()

        print("Create a new character:")
        name = input("Enter a character name: ")
        if not name:
            break

        session = Session()
        if session.query(Character).filter_by(user_id=user.id, name=name).first():
            session.close()
            print("Character name already exists.")
            continue

        print("Available classes:")
        for index, char_class in enumerate(classes, start=1):
            print(f"{index}. {char_class.name}")
        
        while True:
            choice = input("Enter the number of the class: ")
            if choice.isdigit():
                index = int(choice)
                if 1 <= index <= len(classes):
                    selected_class = classes[index - 1]
                    new_character = Character(
                        name=name,
                        user_id=user.id,
                        class_id=selected_class.id,
                        level=1,
                        health=selected_class.health,
                        mana=selected_class.mana,
                        phys_dmg=selected_class.phys_dmg_mod,
                        magic_dmg=selected_class.magic_dmg_mod,
                        phys_def=selected_class.phys_def_mod,
                        magic_def=selected_class.magic_def_mod,
                    )
                    session.add(new_character)
                    session.commit()
                    session.close()
                    user.create_character(new_character.name, selected_class)  # Update the player stats
                    print("Character created successfully.")
                    return new_character
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    user = login()
    selected_character = character_select(user)
    if not selected_character:
        selected_character = create_character(user)
    # Use the selected_character object as needed
