from tools import separator, section

emp = {
    "employee_id": 1234,
    "first_name": "John",
    "last_name": "Doe",
    "age": 30,
    "department": "Engineering",
    "position": "Software Engineer",
    "salary": 75000,
    "email": "john.doe@example.com",
    "phone": "+1234567890",
    "address": {
        "street": "123 Main St",
        "city": "Metropolis",
        "state": "NY",
        "zip": "10001"
    },
    "skills": ["Python", "JavaScript", "C++", "SQL"],
    "hire_date": "2022-01-15",
	"departments": ['sales', 'marketing']
}

section('display information from dictionary')
print(f"{emp['first_name']} {emp['last_name']} lives in {emp['address']['city']}.")

section('how many first-level properties')
print(len(emp))

section('can have any type as property values')
print(f"{emp['first_name']} {emp['last_name']} works in {len(emp['departments'])} departments.")

