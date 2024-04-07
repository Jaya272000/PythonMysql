import mysql.connector
# con=mysql.connector.connect(host='localhost',
#                           user='root',
#                           password='jaya123!',
#                           database='pythontest') 
# print(con)

class DBHELPr:
  def __init__(self):
    self.con=mysql.connector.connect(host='localhost',
                                     user='root',
                                    password='jaya123!',
                                    database='pythontest')
# create table
    qury='create table if not exists user(userid int primary key,userName Varchar(200),phone varchar(12))'
    cur=self.con.cursor()
    cur.execute(qury)
    print('created')
  
  # insert value in table (method)
  def insertuser(self,userid,userName,phone):
    query = "insert into user (userid,username,phone) values({},'{}','{}')".format(userid, userName.replace("'", "''"), phone)
    print(query)
    cur=self.con.cursor()
    cur.execute(query) 
    self.con.commit()
    print('user save to db')
  
# Fetch All

  def fetch_all(self):
    query='select * from user'
    cur=self.con.cursor()
    cur.execute(query)
    for row in cur:
      print('userid:',row[0])
      print('username:',row[1])
      print('phone:',row[2])
      print()
# delete user
  def delete_user(self,userid):
    query="delete from user where userid={}".format(userid)
    print(query)
    c=self.con.cursor()
    c.execute(query)
    self.con.commit()
    print('deleted')
# update user
  def update_user(self,userid,username,phone):
    query="update user set username='{}',phone='{}' where userid={}".format(username,phone,userid)
    print(query)
    d=self.con.cursor()
    d.execute(query)
    self.con.commit()
    print('updated')





# main coding help of object

help=DBHELPr()
# help.delete_user(112)
help.update_user(122,'durgesh',9823523672)
# help.insertuser(12,'deepti','3323')
# help.insertuser(112,'jaya','3313')
# help.insertuser(132,'deep','3393')
# help.insertuser(192,'priya','3423')
# help.insertuser(121,'shalini','3123')

 
# Fetch All
help.fetch_all()




