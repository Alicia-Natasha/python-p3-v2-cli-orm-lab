from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    departments = Department.all()
    for dept in departments:
        print(dept)

def __str__(self):
    return f"{self.name} ({self.location})"


def find_employee_by_name():
    name = input("Enter the employee's name: ")
    employee = Employee.find_by_name(name)
    if employee:
        print(employee)
    else:
        print(f"Employee {name} not found")


def find_employee_by_id():
    try:
        employee_id = int(input("Enter the employee's id: "))
        employee = Employee.find_by_id(employee_id)
        if employee:
            print(employee)
        else:
            print(f"Employee {employee_id} not found")
    except ValueError:
        print("Invalid input. Please enter a number.")


def create_employee():
    name = input("Enter the employee's name: ").strip()
    job_title = input("Enter the employee's job title: ").strip()
    try:
        department_id = int(input("Enter the employee's department id: "))
        try:
            employee = Employee.create(name, job_title, department_id)
            print(f"Success: {employee}")
        except Exception as e:
            print("Error creating employee: ", e)
    except ValueError:
        print("Invalid department id. Please enter a number.")


def update_employee():
    try:
        employee_id = int(input("Enter the employee's id: "))
        employee = Employee.find_by_id(employee_id)
        if not employee:
            print(f"Employee {employee_id} not found")
            return

        name = input("Enter the employees's new name: ").strip()
        job_title = input("Enter the employee's new job title: ").strip()
        department_id = int(input("Enter the employees's new department id: "))

        try:
            employee.name = name
            employee.job_title = job_title
            employee.department_id = department_id
            employee.update()
            print(f"Success: {employee}")
        except Exception as e:
            print("Error updating employee: ", e)
    except ValueError:
        print("Invalid input. Please enter numeric ID.")



def delete_employee():
    try:
        employee_id = int(input("Enter the employee's id: "))
        employee = Employee.find_by_id(employee_id)
        if employee:
            employee.delete()
            print(f"Employee {employee_id} deleted")
        else:
            print(f"Employee {employee_id} not found")
    except ValueError:
        print("Invalid input. Please enter a number.")



def list_department_employees():
    try:
        department_id = int(input("Enter the department's id: "))
        department = Department.find_by_id(department_id)
        if department:
            for emp in department.employees():
                print(emp)
        else:
            print(f"Department {department_id} not found")
    except ValueError:
        print("Invalid input. Please enter a number.")
