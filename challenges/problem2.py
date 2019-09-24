employees = {
    'employee1': {
        "name": "Ron Swanson",
        "age": 55,
        "department": "Management",
        "phone": "555-1234",
        "salary": "$87,000"
    },
    'employee2': {
        "name": "Leslie Knope",
        "age": 55,
        "department": "Middle Management",
        "phone": "555-4321",
        "salary": "$87,0001"
    }
}

def funct(employees):
    for employee in employees:
        print(f'{employees[employee][0]} in {employees[employee][2]} can be reached at {employees[employee][3]}')
