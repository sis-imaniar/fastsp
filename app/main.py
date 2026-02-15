from fastapi import FastAPI, HTTPException
from . import services
from .schemas import EmployeeResponse

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from FastAPI on Azure!"}

@app.get("/employees", response_model=list[EmployeeResponse])
def get_employees():
    return services.call_sp_get_employees()

@app.get("/employees/{employee_id}", response_model=EmployeeResponse)
def get_employee(employee_id: int):
    result = services.call_sp_get_employee_by_id(employee_id)

    if not result:
        raise HTTPException(status_code=404, detail="Employee not found")

    return result
