from db_config import connect

def create_account():
    name=input("enter ur name=")
    email=input("enter ur email=")
    balance=float(input("enter ur opening balance="))
    db=connect()
    cursor=db.cursor()
    sql="insert into accounts (name,email,balance) values (%s,%s,%s)"
    values=(name,email,balance)
    cursor.execute(sql,values)
    db.commit()
    print("account created successfully")
    db.close()

def view_accounts():
    db=connect()
    cursor=db.cursor()
    cursor.execute("select * from accounts")
    accounts=cursor.fetchall()
    print("all accounts")
    for acc in accounts:
        print(f"ID : {acc[0]}, Name: {acc[1]}, Email : {acc[2]} , Balance: {acc[3]}")
    db. close()

def deposit_money():
    acc_id=int(input("enter account id"))
    amount=float(input("enter deposit amount"))
    db=connect()
    cursor=db.cursor()
    cursor.execute("update accounts set balance=balance + %s where id=%s",(amount,acc_id))
    db.commit()
    print("money is deposited")
    db.close()

def withdraw_money():
    acc_id=int(input("enter account id"))
    amount=float(input("enter the withdraw amount"))
    db=connect()
    cursor=db.cursor()
    cursor.execute("select balance from accounts where id=%s",(acc_id,))
    result=cursor.fetchone()
    if result and result[0]>=amount:
          cursor.execute("update accounts set balance=balance - %s where id=%s",(amount,acc_id))
          db.commit()
          print("money is withdrawed")
    else:
        print("insufficient balance")

    db.close()

def check_balance():
        acc_id=int(input("enter account id"))
        db=connect()
        cursor=db.cursor()
        cursor.execute("select name,balance from accounts where id=%s",(acc_id,))
        result=cursor.fetchone()
        if result:
            print(f"Account holder : {result[0]}, Balance : {result[1]}")
        else:
            print("account not found")
        db.close()


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   
