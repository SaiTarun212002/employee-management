from pydantic import BaseModel
class EmployeeUpdate(BaseModel):
    eid:int
    ename: str
    email: str
    depart: str
    designation: str
    salary: int
    joining_date: str