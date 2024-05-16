from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

employees = {
	1: {
		'name': 'John',
		'age': 21,
		'role': 'developer'
	},
	2: {
		'name': 'Riya',
		'age': 27,
		'role': 'hr'
	}
	
}
class Employee(BaseModel):
	name: str
	age: int
	role: str

class UpdateEmployee(BaseModel):
	name: Optional[str] = None
	age: Optional[int] = None
	role: Optional[str] = None

@app.get('/')
def index():
  return {"message" : "hello world"}
  
@app.get('/get_employee/{employee_id}')
def get_employee(employee_id: int):
	if employee_id not in employees:
		return {'message':'employee does not exists'}
	return employees[employee_id]

@app.get('/get-all-employee')
def get_all_employee():
	return employees

@app.get('/get-employee-by-name')
def get_employee_by_name(name : str):
	for id in employees:
		if employees[id]['name'] == name:
			return employees[id]
	return {'message': 'employee not found'}

@app.post('/add-employee/{employee_id}')
def add_new_employee(employee_id: int, employee: Employee):
	if employee_id in employees:
		return {'error':'employee already exists'}
	employees[employee_id] = employee
	return employees[employee_id]

@app.put('/modify-employee/{employee_id}')
def modifiy_employee(employee_id: int, employee: UpdateEmployee):
	if employee_id not in employees:
		return {'message': 'employee not found'}
	if employee.name != None:
		employees[employee_id].name = employee.name
	if employee.age != None:
		employees[employee_id].age = employee.age
	if employee.role != None:
		employees[employee_id].role = employee.role
	return employees[employee_id]

@app.delete('/delete-employee/{employee_id}')
def delete_employee(employee_id: int):
	if employee_id not in employees:
		return {'message': 'employee not found'}
	del employees[employee_id]
	return {'message': 'successfully deleted the employee record'}
