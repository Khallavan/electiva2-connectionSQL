# Electiva1

import psycopg2
import credentials
import sys

def create_table(cursor):
  try:
    cursor.execute("CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);")
    print("Finished creating table")
  except:
    raise
   
def insert(cursor):
  try: 
    item = input("Nuevo item a insertar: ")
    quantity = int(input("Cantidad: "))
    cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("nucleo f7xxxx", 150))
    cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("Capacitores", 154))
    cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("manzana", 100))
    cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", (item, quantity))
  except:
    raise
  
def update(cursor):
  try:
    cursor.execute("UPDATE inventory SET quantity = %s WHERE name = %s;", (200, "banano"))
    print("Updated 1 row of data")
  except:
    raise

def delete(cursor):
  try:
    cursor.execute("DELETE FROM inventory WHERE name = %s;", ("naranja",))
    print("Deleted 1 row of data")
  except:
    raise
  
def read(cursor):
  try:
    # Fetch all rows from table
    cursor.execute("SELECT * FROM inventory;")
    rows = cursor.fetchall()

    # Print all rows
    for row in rows:
        print("Data row = (%s, %s, %s)" %(str(row[0]), str(row[1]), str(row[2])))
        
  except:
    raise

def main():
  
# Connection
  conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(credentials.host, credentials.user, credentials.dbname, credentials.password, credentials.sslmode)
  conn = psycopg2.connect(conn_string) 
  print("Connection established")
  cursor = conn.cursor()
  
  # create_table(cursor)
  
  while True:
    
    print(""" 
      1. Insertar Valores.\n
      2. Actualizar Valores.\n
      3. Borrar Valores. \n
      4. Leer base de datos.\n
      5. cerrar connecion.\n
      6. Salir.
      """
    )  
    option = int(input("Ingrese una opcion: "))
    match option:
      
      case 1:
        insert(cursor)
      
      case 2:
        update(cursor)
      
      case 3:
        delete(cursor)
        
      case 4:
        read(cursor)
        
      case 5:
        conn.commit()
        cursor.close()
        conn.close()
        
      case 6:
        sys.exit()
        
      case _:
        print('Opcion incorrecta')

if __name__ == '__main__':
  main()
  