def create_employee():
    name=input("Name:")
    salary=float(input("salary:"))
    emp={"name":name,"salary":salary} 
    return emp
emp_1=create_employee()
emp_1["name"]=""
print(emp_1)
# -----------Data Tyeps-------
# x=8.9
# y=x+20
# print(y)
name="user_name"
name.replace("_","*")
