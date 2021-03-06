import sqlite3
import datetime


def deposit(piggy_id, amount, desc='deposit'):
    conn = sqlite3.connect('piggy_bank.db')
    c = conn.cursor()
    try:
        create_at = datetime.datetime.now().strftime("%Y%m%d%H%M")
        sql = "INSERT INTO transactions (piggy_bank_id, desc, tran_type, amount, created_at) VALUES ("+str(piggy_id)+",'"+desc+"','deposit',"+str(amount)+",'"+create_at+"')"
        print(sql)
        c.execute(sql)
        conn.commit()
    except Exception :
        c.close()
        pass 


def withdraw(piggy_id,desc='withdraw'):
    conn = sqlite3.connect('piggy_bank.db')
    c = conn.cursor()
    try:
        amount = balance(piggy_id)
        create_at = datetime.datetime.now().strftime("%Y%m%d%H%M")
        sql = "INSERT INTO transactions (piggy_bank_id, desc, tran_type, amount, created_at) VALUES ("+str(piggy_id)+",'"+desc+"','withdraw',-"+str(amount)+",'"+create_at+"')"
        print(sql)
        c.execute(sql)
        conn.commit()
        return amount
    except Exception :
        c.close()
        pass 
    

def balance(piggy_id):
    conn = sqlite3.connect('piggy_bank.db')
    c = conn.cursor()
    try:
        sql = "select sum(amount) from transactions where piggy_bank_id="+str(piggy_id)
        print(sql)
        c.execute(sql)
        return c.fetchone()[0] 
    except Exception :
        c.close()
        pass 
 

