import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect
from db.seeds import *
from db.db_models import *

engine = create_engine('sqlite:///db/rpg_database.db', echo=True)
Session = sessionmaker(bind=engine)


def create_table(table_class=None, overwrite=False):
    if table_class:
        if not hasattr(table_class, '__tablename__'):
            raise ValueError('Invalid table class')
        table_name = table_class.__tablename__
        if overwrite:
            table_class.__table__.drop(engine)
        table_class.__table__.create(engine)
    else:
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)


def drop_table(table_class):
    if not hasattr(table_class, '__table__'):
        raise ValueError('Invalid table class')
    table_class.__table__.drop(engine, checkfirst=True)


def drop_entry(table_class, row_id):
    if not hasattr(table_class, '__table__'):
        raise ValueError('Invalid table class')

    session = Session()
    try:
        if row := session.query(table_class).get(row_id):
            session.delete(row)
            session.commit()
            print(
                f"Row with ID {row_id} has been deleted from the table {table_class.__tablename__}.")
        else:
            print(
                f"No row found with ID {row_id} in the table {table_class.__tablename__}.")
    except Exception as e:
        session.rollback()
        print(f"An error occurred while deleting the row: {str(e)}")
    finally:
        session.close()


def update_entry(table_class, row_id):
    if not hasattr(table_class, '__table__'):
        raise ValueError('Invalid table class')

    session = Session()
    try:
        if row := session.query(table_class).get(row_id):
            inspector = inspect(table_class)
            for column in inspector.columns:
                if isinstance(column.type, DateTime):
                    setattr(row, column.name, datetime.datetime.now())
                else:
                    value = input(f"Enter new {column.name} ({column.type}): ")
                    setattr(row, column.name,
                            int(value) if value.isdigit() else value)
            session.commit()
            print(
                f"Row with ID {row_id} has been updated in the table {table_class.__tablename__}.")
        else:
            print(
                f"No row found with ID {row_id} in the table {table_class.__tablename__}.")
    except Exception as e:
        session.rollback()
        print(f"An error occurred while updating the row: {str(e)}")
    finally:
        session.close()


def create_entry(table_class, values=None):
    if not hasattr(table_class, '__table__'):
        raise ValueError('Invalid table class')

    session = Session()
    try:
        inspector = inspect(table_class)
        kwargs = {}
        value_index = 0
        for column in inspector.columns:
            if column.primary_key:
                continue  # Skip primary key and datetime columns
            elif isinstance(column.type, DateTime):
                kwargs[column.name] = datetime.datetime.now()
            elif values and value_index < len(values):
                kwargs[column.name] = values[value_index]
                value_index += 1
            else:
                value = input(f"Enter {column.name} ({column.type}): ")
                kwargs[column.name] = int(value) if value.isdigit() else value

        new_entry = table_class(**kwargs)
        session.add(new_entry)
        session.commit()
        print(
            f"New entry has been added to the table {table_class.__tablename__}.")
    except Exception as e:
        session.rollback()
        print(f"An error occurred while adding the entry: {str(e)}")
    finally:
        session.close()


def table_menu(table_class):
    while True:
        print(f"Selected table: {table_class.__tablename__}")
        print("1. Add row")
        print("2. Delete row")
        print("3. Update row")
        print("4. Reset table")
        choice = input("Enter your choice: ")
        if not choice:
            break
        elif choice.startswith('1'):
            try:
                values = choice.split('[')[1][:-1].split(',')
                create_entry(table_class, values)
            except Exception:
                print("Invalid input format.")
                create_entry(table_class)
        elif choice == '2':
            row_id = input("Enter row ID to delete: ")
            drop_entry(table_class, row_id)
        elif choice == '3':
            row_id = input("Enter row ID to update: ")
            update_entry(table_class, row_id)
        elif choice == '4':
            create_table(table_class)
        else:
            print("Invalid choice. Please try again.")


def menu():

    table_classes = {
        '1': User,
        '2': Character,
        '3': Char_Class,
        '4': Armor,
        '5': Weapon,
        '6': CharacterEquipment,
        '7': Achievement,
        '8': UserAchievement
    }

    while True:
        print("1. Create User")
        print("2. Create Character")
        print("3. Create Class")
        print("4. Create Armor")
        print("5. Create Weapon")
        print("6. Create CharacterEquipment")
        print("7. Create Achievement")
        print("8. Create UserAchievement")
        choice = input("Enter your choice: ")
        if not choice:
            break
        elif choice in table_classes:
            table_menu(table_classes[choice])
        elif choice == "reseed":
            create_table()
            seed_weapons()
            seed_armors()
            seed_classes()
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    menu()
