class User:
    fullname="Paul"
    role_id="Worker"
    staff_id=13213123
    is_verified=True

person1=User()
print(person1)
print(person1.fullname)
print(person1.role_id)
print(person1.is_verified)
print(person1.staff_id)

class Person:
    def __init__(self,fullname,role_id,staff_id,is_verified):
        self.is_verified = is_verified
        self.staff_id = staff_id
        self.role_id = role_id
        self.fullname = fullname
    def __str__(self):
        return f"{self.fullname},{self.role_id},{self.staff_id},{self.is_verified}"
#custom object method
    def transform_word(self,msg):
        newword=self.fullname.upper()
        roleup=self.role_id.upper()
        print(msg)
        result=f"{newword} , {roleup}"
        return result


p1=Person("Joseph","lecturer",214135325,True)
p2=Person("Alice","Student",45566,True)

print(p1.transform_word("Transform Success"))
print(p2.transform_word("Transform Success"))