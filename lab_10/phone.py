import psycopg2
from suppliers.config2 import load_config
# -*- coding: utf-8 -*-


def collect_info():
    """ Extracts data from the suppliers table """
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT user_id, name, phone_number FROM phonebook ORDER BY user_id")
                rows = cur.fetchall()

                print("Number of records: ", cur.rowcount)
                for row in rows:
                    print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def update_info(user_id, name, phone_number):
    """ Update contact """
    update_row_count = 0
    sql = """UPDATE phonebook
             SET name = %s, phone_number = %s
             WHERE user_id = %s"""
    
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Execute the UPDATE SQL statement
                cur.execute(sql, (name, phone_number, user_id))
                update_row_count = cur.rowcount

            # Commit changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return update_row_count

def delete_info(user_id):
    """ Delete contact """
    rows_deleted = 0
    sql = 'DELETE FROM phonebook WHERE user_id = %s'
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Execute the DELETE SQL statement
                cur.execute(sql, (user_id,))
                rows_deleted = cur.rowcount

            # Commit changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return rows_deleted

def insert_contact(name, phone_number):
    """ Insert new contact into phonebook table """
    sql = """INSERT INTO phonebook(name, phone_number)
             VALUES(%s, %s) RETURNING user_id;"""
    
    user_id = None
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Execute the INSERT SQL statement
                cur.execute(sql, (name, phone_number))

                # Get the generated user_id
                row = cur.fetchone()
                if row:
                    user_id = row[0]

                # Commit changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return user_id

if __name__ == '__main__':
    operation = input("Choose\n1 - add contact\n2 - update contact\n3 - view all contacts\n4 - delete contact\n")
    if operation == "1":
        name = input("Enter the name of the new contact: ")
        phone_number = input("Enter the phone number: ")
        user_id = insert_contact(name, phone_number)  # Example function call
        if user_id is not None:
            print("Contact successfully added. ID:", user_id)
        else:
            print("Error adding contact.")
    elif operation == "2":
        try:
            user_id = int(input("Enter the ID of the contact you want to update: "))
        except ValueError:
            print("Error: invalid ID entered.")
            exit()
        name = input("Enter the new name for the contact: ")
        phone_number = input("Enter the new phone number: ")
        updt = update_info(user_id, name, phone_number)
        if updt > 0:
            print("Contact successfully updated")
        else:
            print("Error updating contact")
    elif operation == "3":
        collect_info()
    elif operation == "4":
        try:
            user_id = int(input("Enter the ID of the contact you want to delete: "))
        except ValueError:
            print("Error: invalid ID entered.")
            exit()
        dlt = delete_info(user_id)
        if dlt > 0:
            print("Contact successfully deleted")
        else:
            print("Error deleting contact")
