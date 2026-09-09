import mysql.connector
import datetime

class con_db:
    def get_connect(self):
        try:
            self.con=mysql.connector.connect(
                host="localhost",
                user="root",
                password="Priyan@07",
                database="company_db"
            )
            return self.con
        except Exception as e:
            return None


class EmployeeManager(con_db):
    def get(self):
        try:
            self.connect=super().get_connect()
            self.cursor=self.connect.cursor()
            query="select * from employee"
            self.cursor.execute(query)
            r=self.cursor.fetchall()
            print(r)
        except Exception as e:
            print(e)

    def post(self,**kwargs):
        try:
            self.connect=super().get_connect()
            self.cursor=self.connect.cursor()
            query="insert into employee(name,place,mobile,email,department,salary,joining_date) values(%s,%s,%s,%s,%s,%s,%s)"
            values=[v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connect.commit()
            print("added successfully")
        except Exception as e:
            print(e)
    def get_one(self,id=None):
        try:
            self.connect = super().get_connect()
            self.cursor = self.connect.cursor()
            query = "select * from employee where id=%s"
            values = (id,)
            self.cursor.execute(query, values)
            r = self.cursor.fetchone()
            return r
        except Exception as e:
            return  None
    def dele(self,id=None):
        try:
            r=self.get_one(id=id)
            if r != None:
                self.connect=super().get_connect()
                self.cursor=self.connect.cursor()
                query="delete from employee where id =%s"
                values=(id,)
                self.cursor.execute(query,values)
                self.connect.commit()
                print("deleted successfully")
            else:
                print("404")
        except Exception as e:
            print(e)

    def update(self,id=None,**kwargs):
        try:
            r=self.get_one(id=id)
            if r!=None:
                self.connect=super().get_connect()
                self.cursor=self.connect.cursor()
                placeholder=""
                for k in kwargs:
                    placeholder+= k+"=%s, "
                placeholder=placeholder.rstrip(", ")
                query=f"update employee set {placeholder} where id=%s"
                values=[v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query,values)
                self.connect.commit()
                print("updated successfully")
            else:
                print("404")
        except Exception as e:
            print(e)

con_instance=con_db()
print(con_instance.get_connect())

emp=EmployeeManager()
# emp.get()
# emp.post(name="deslin",place="tvm",mobile="964587210",email="deslin@gmail.com",department="hr",salary=60000,joining_date=datetime.datetime.today())
# emp.update(id=1,name="maanav",place="gujarat")
# emp.dele(id=3)