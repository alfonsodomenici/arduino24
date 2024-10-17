from app import db
from datetime import datetime

def findAllArduino():
    cur = db.connection.cursor()
    cur.execute("SELECT nome FROM arduino")
    return  cur.fetchall()

def createArduino(nome,macaddress):
    q = f"""
        insert into arduino (nome,macaddress) 
        values ('{nome}','{macaddress}')
        """
    conn = db.connection
    cursor = conn.cursor()
    cursor.execute(q)
    conn.commit()
    lastid = cursor.lastrowid
    return findArduino(lastid)

def findArduino(id):
    cursor = db.connection.cursor()
    q = f"""select id,nome,macaddress 
        from arduino 
        where id={id}
        """
    cursor.execute(q)
    return cursor.fetchone()

def findArduinoByMacaddress(macaddress):
    print(macaddress)
    cursor = db.connection.cursor()
    q = f"""select * 
        from arduino 
        where macaddress='{macaddress}'
        """
    cursor.execute(q)
    return cursor.fetchone()    

def findArduinoDati(id):
    cursor = db.connection.cursor()
    q = f"""select * 
        from dati 
        where arduino_id={id}
        """
    cursor.execute(q)
    return  cursor.fetchall()

def createArduinoDati(arduino_id,tipo,valore):
    now = datetime.now().isoformat()
    q = f"""
        insert into dati (arduino_id,tipo,valore,data_ora) 
        values ({arduino_id},'{tipo}',{valore},'{now}')
        """
    conn = db.connection
    cursor = conn.cursor()
    cursor.execute(q)
    conn.commit()
    lastid = cursor.lastrowid
    return findDatiById(lastid)

def findDatiById(id):
    cursor = db.connection.cursor()
    q = f"""select * 
        from dati 
        where id={id}
        """
    cursor.execute(q)
    return cursor.fetchone()