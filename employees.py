from fastapi import FastAPI,Body,HTTPException

from helper import load_data,save_data

app=FastAPI()

@app.get("/display/")
def display_all_employees():
    return load_data()



@app.delete("/delete/{dynamic_name}")
def delete_employee(eid: int):
    """
    This Python function deletes an employee from a dataset based on their employee ID.
    
    :param eid: The `eid` parameter in the `delete_employee` function is an integer representing the
    employee ID of the employee that needs to be deleted from the data
    :type eid: int
    :return: The function `delete_employee` is returning a dictionary with a message indicating that the
    employee with the specified ID has been deleted. The message includes the ID of the deleted
    employee.
    """
    data = load_data()
    filtered_data = [emp for emp in data if emp["eid"] != eid]

    if len(filtered_data) == len(data):
        raise HTTPException(status_code=404, detail="Employee not found")

    save_data(filtered_data)
    return {"message": f"Employee with ID {eid} deleted."}    




@app.put("/employees/{eid}")
# This `update_employee` function in your FastAPI application is responsible for updating an
# employee's information based on the provided `eid` (employee ID) and the updated employee data in
# the request body.
def update_employee(eid: int, updated_emp: EmployeeUpdate):
    if eid != updated_emp.eid:
        raise HTTPException(status_code=400, detail="Employee ID mismatch between path and request body.")

    data = load_data()
    for i, emp in enumerate(data):
        if emp["eid"] == eid:
            data[i].update(updated_emp.model_dump())
            save_data(data)
            return {"message": f"Employee with ID {eid} updated successfully."}

    raise HTTPException(status_code=404, detail="Employee not found")












