import sqlite3

#einmal ausführen

my_db = sqlite3.connect('users.db')
my_dbc = my_db.cursor()

my_dbc.execute("""DROP TABLE IF EXISTS roles""")
my_db.commit()

my_dbc.execute("""CREATE TABLE roles (roles TEXT, can_see BOOLEAN, can_book BOOLEAN, can_add_item BOOLEAN, can_eddit_item BOOLEAN, can_delete_item BOOLEAN, can_eddit_categories BOOLEAN, can_eddit_roles BOOLEAN, can_eddit_user BOOLEAN)""")
my_db.commit()

my_dbc.execute("""INSERT INTO roles 
               (roles, can_see, can_book, can_add_item, can_eddit_item, can_delete_item, can_eddit_categories, can_eddit_roles, can_eddit_user)
                VALUES 
               ('admin',1,1,1,1,1,1,1,1),
               ('user',1,1,0,0,0,0,0,0),
               ('guest',0,0,0,0,0,0,0,0)""")
my_db.commit()