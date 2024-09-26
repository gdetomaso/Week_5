"""
A menu - you need to add the database and fill in the functions. 
"""
import peewee

# TODO create database table OR set up Peewee model to create table

db = peewee.SqliteDatabase('chainsawjuggling.db') #initilized database

# this class is where you define the database struture i think
class JugglingRecord(peewee.Model):
    name = peewee.CharField()
    counrty = peewee.CharField()
    catches = peewee.IntegerField()
    #not sure about what this is for
    class Meta:
        database = db

JugglingRecord.create_table() #creates the table

#delete all records
JugglingRecord.delete().execute()

#filling data into the database
person1 = JugglingRecord.create(name='Janne Mustonen', counrty='Finland', catches=98)
person1.save()
person2 = JugglingRecord.create(name='Ian Stewart', counrty='Canada', catches=94)
person2.save()
person3 = JugglingRecord.create(name='Aaron Gregg', counrty='Canada', catches=88)
person3.save()
person4 = JugglingRecord.create(name='Chad Taylor', counrty='USA', catches=78)
person4.save()

def main():
    menu_text = """
    1. Display all records
    2. Search by name
    3. Add new record
    4. Edit existing record
    5. Delete record 
    6. Quit
    """

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            search_by_name()
        elif choice == '3':
            add_new_record()
        elif choice == '4':
            edit_existing_record()
        elif choice == '5':
            delete_record()
        elif choice == '6':
            break
        else:
            print('Not a valid selection, please try again')


def display_all_records():
    print('todo display all records')
    juggleRecords = JugglingRecord.select()
    for record in juggleRecords:
        print(f'Name: {record.name}, Country: {record.counrty}, Catches: {record.catches}')


def search_by_name():
    print('todo ask user for a name, and print the matching record if found. What should the program do if the name is not found?')
    jugglerName = input('Enter name to search for: ')
    juggleRecords = JugglingRecord.select().where(JugglingRecord.name == jugglerName)
    for record in juggleRecords:
        print(f'Name: {record.name}, Country: {record.counrty}, Catches: {record.catches}')

def add_new_record():
    print('todo add new record. What if user wants to add a record that already exists?')
    newRecord = JugglingRecord.create(name=input('Enter name: '), counrty=input('Enter country: '), catches=int(input('Enter catches: ')))
    newRecord.save()


def edit_existing_record():
    print('todo edit existing record. What if user wants to edit record that does not exist?') 
    #get what record needs to be edited
    jugglerID = int(input('Enter ID of record to edit: '))
    #edit the record
    JugglingRecord.update(name=input('Enter new name: '), counrty=input('Enter new country: '), catches=int(input('Enter new catches: '))).where(JugglingRecord.id == jugglerID).execute()
    
    

def delete_record():
    print('todo delete existing record. What if user wants to delete record that does not exist?') 
    jugglerID = int(input('Enter ID of record to delete: '))
    JugglingRecord.delete().where(JugglingRecord.id== jugglerID).execute()


if __name__ == '__main__':
    main()