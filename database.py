import os
from datetime import datetime

from sqlalchemy import create_engine, text

db_connection_string = os.environ['CONNECTION_STRING']
engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})
with engine.connect() as conn:
  result = conn.execute(text("select * from contents"))
  #print(result.all())


def search(username):
  try:
    with engine.connect() as conn:
      query = text('SELECT * FROM login WHERE username = :user')
      result = conn.execute(query, {"user": username})
      user_data = result.fetchone()
      user_data1 = list(user_data)
      print(type(user_data))
      print(user_data)
    if user_data:
      return user_data1[1]  # Return user data as a dictionary
    else:
      return None  # User not found

  except Exception as e:
    # Handle any exceptions that may occur during the database query
    print(f"Error during database query: {str(e)}")
    return None


def insert(username, email, password):
  print("123")
  with engine.connect() as conn:
    query = text(
        'insert into login (username, email, pass)values(:username,:password,:email)'
    )
    conn.execute(
        query,
        {
            "username": username,
            "password": password,
            "email": email,
            #"confirm_password": confirm_password
        })
  return 'Data inserted'


def view():
  with engine.connect() as conn:
    query = text('select * from contents')
    result = conn.execute(query)
    column_names = result.keys()
    data = [list(row) for row in result]
    print(column_names)
    print(data)
    # Create a dictionary from column names and row values

    return data, column_names
def remove1(item):
  with engine.connect() as conn:
    query=text('delete from contents where item=:item')
    conn.execute(query,{"item":item})
    print('mani')
  return ""
#insert("Mani",'123@gmail.com','Mandy')
#print(search("Mani"))


def validate(username):
  try:
    with engine.connect() as conn:
      query = text('SELECT * FROM login WHERE username = :user')
      result = conn.execute(query, {"user": username})
      user_data = result.fetchone()
      user_data1 = list(user_data)
    if user_data:
      
      return user_data1[1],user_data1[2]  # Return user data as a dictionary
    else:
      return None  # User not found

  except Exception as e:
    # Handle any exceptions that may occur during the database query
    print(f"Error during database query: {str(e)}")
    return None
def add_db(items, quantity,doi,doe):
  print("123")
  with engine.connect() as conn:
    query = text(
        'insert into contents (item, quantity, doi, doe) values(:items,:quantity,:doi,:doe)'
    )
    conn.execute(
        query,
        {
            "items": items,
            "quantity": quantity,
            "doi": doi,
            "doe":doe,
            #"confirm_password": confirm_password
        })
  return 'Data inserted'












