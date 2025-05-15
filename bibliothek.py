import sqlite3
conn = sqlite3.connect('bibliothek.db') 
cursor = conn.cursor()  
cursor.execute(""" 

    CREATE TABLE bibliothek ( 

        id INTEGER PRIMARY KEY AUTOINCREMENT, 

        titel TEXT NOT NULL, 

        anzahl TEXT NOT Null,

        status TEXT NOT Null,

        standort TEXT ,

    ) 

""") 
cursor.execute(f"INSERT INTO bibliothek (IDD, titel, author, status, standort) VALUES ('{100010}', '{die_Zahlen}', '{aktiv}', '{toppingprice}', '{typeprice}')") 

         

conn.commit()  

conn.close() 
@app.route('/bücher') 
def bücher():
        
        return render_template('bücher.html')

@app.route('/add_bücher')
def add_bücher():
        return render_template('add_bücher.html')
        



