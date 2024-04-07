from  databasehelper import DBHELPr
def main():
  db=DBHELPr()
  while True:
    print("*********Welcom******")
    print("press 1 to insert new user")
    print('press 2 to display all user')
    print("press 3 to delete user")
    print("press 4 to update user")
    print("press 5 to exit program")
    print()
    # try:
    choice=int(input())
    if choice==1:
        # insert user
        uid=int(input("enter user id:"))
        username=input("enter username:")
        userphone=input("enter user phone:")
        db.insertuser(uid,username,userphone)
    elif choice==2:
        db.fetch_all()
        # display all user
        pass
    elif choice==3:
        useriid=int(input("enter userid to which you want to delete"))
        db.delete_user(useriid)
        # delete user
        
    elif choice==4:
        # update user
        uid=int(input("enter user id you want to update:"))
        username=input("enter New username:")
        userphone=input("enter Newuser phone:")
        db.update_user(uid,username,userphone)
    else:
        # exit program
        print("invalid")   

if __name__== "__main__":
  main()
    
      
