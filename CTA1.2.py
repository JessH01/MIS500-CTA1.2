SALARY_RAISE_FACTOR = 0.05
STATE_CODE_MAP = {'WA': 'Washington', 'TX': 'Texas'}

# This is the definition of the class

class Salary:

	def update_employee_record(rec):
		old_sal = rec['salary']
		new_sal = old_sal * (1 +  SALARY_RAISE_FACTOR)
		rec['salary'] = new_sal
		state_code = rec['state_code']
		rec ['state_name'] = STATE_CODE_MAP[state_code]

# This is the Data

input_data = [
	{'employee_name': 'Susan', 'salary': 100000.0, 'state_code': 'WA'},
	{'employee_name': 'Ellen', 'salary': 75000.0, 'state_code': 'TX'},
	]

# This is the actual script

for rec in input_data:
	Salary.update_employee_record(rec)
	name = rec['employee_name']
	salary = rec['salary']
	state = rec['state_name']
	print(name + ' now lives in ' +  state)
	print( 'and makes $' +  str(salary))
