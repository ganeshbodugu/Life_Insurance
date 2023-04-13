import mysql.connector as connector
import datetime as date
import logging

class User :

    dates1 = date.datetime.now()


    def __init__(self):

        self.con = connector.connect(host='localhost',
                                     user='root',
                                     password='Root@123',
                                     database='insurance')

    def create(self,uname,uaddress,phone,DOB,Insuancetype,insurance_amount ):
        query = "insert into user(uname,uaddress,phone,DOB,Insuancetype,insurance_amount)values('{}','{}',{},'{}','{}',{})".format(uname,uaddress,phone,DOB,Insuancetype,insurance_amount)
        curr = self.con.cursor()
        curr.execute(query)
        self.con.commit()
        print("Account created  successfully at  " , self.dates1)

    def find_user(self, uid):
        query = "select * from user where uid={}".format(uid)
        cur = self.con.cursor()
        cur.execute(query)
        res = cur.fetchall()
        if res:
            for row in res:
                print("UID  : ", row[0])
                print("name  : ", row[1])
                print("ADDRESS  : ", row[2])
                print("PHONE  : ", row[3])
                print("DOB : ", row[4])
                print(" INSURANCE TYPE   : ", row[5])
                print(" INSURANCE AMOUNT  : ", row[6])
                print()
                print()
        else:
            print("ACCOUNT DOESNT EXIST ! PLEASE TRY WITH VALID ACCOUNT ")

    def delete_user(self, uid):
        q = "select * from user where uid = {}".format(uid)
        curr = self.con.cursor()
        curr.execute(q)
        res = curr.fetchall()
        if res:
            query = "delete from user where uid = {}".format(uid)
            cur = self.con.cursor()
            cur.execute(query)
            res = cur.fetchone()
            self.con.commit()
            print("Your Account is deleted Successfully at  ", self.dates1)
            print()
        else:
            print("ACCOUNT DOESNT EXIST ! PLEASE TRY WITH VALID ACCOUNT")

    def update_user(self, uid):
        q = "select * from user where uid = {}".format(uid)
        curr = self.con.cursor()
        curr.execute(q)
        res = curr.fetchall()
        if res:
            newName = input("enter newname : ").capitalize()
            while True:
                newphone = int(input('enter your phone number : '))
                if len(str(newphone)) > 10 or len(str(newphone)) < 10:
                    print("Invalid phone number ! please enter 10 digit only ")
                else:
                    break
            newaddress = input("enter newaddress : ").capitalize()
            query = "update user set uname = '{}' , phone = {} , uaddress = '{}' where uid = {} ".format(
                newName, newphone, newaddress, uid)
            cur = self.con.cursor()
            cur.execute(query)
            self.con.commit()
            print("Account details updated successfully  at ", self.dates1)
        else:
            print("ACCOUNT DOESNT EXIST ! PLEASE TRY WITH VALID ACCOUNT")