import psycopg2


def connect(dbname):
   #Establishing the connection
   conn = psycopg2.connect("dbname=stations user=postgres password=qwerty")
   #Creating a cursor object using the cursor() method
   cursor = conn.cursor()
   return conn,cursor

def create_table(dbname,sqlstatement):
   #Doping table if already exists.
   conn, cursor = connect(dbname)
  


   cursor.execute(sqlstatement)
   print("Table created successfully........")
   conn.commit()
   #Closing the connection
   conn.close()

if __name__ == "__main__":
   create_table('stations',sqlstatement='''CREATE TABLE FLOW (
       flowid  SERIAL  PRIMARY KEY,
       date TIMESTAMP NOT NULL,
       flow1 INT NOT NULL,
       flow2 INT NOT NULL,
       flow3 INT NOT NULL,
       flowtotal INT NOT NULL
       )  
   ''')
