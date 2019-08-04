employees = []
running = True


class Employees:

    def __init__(self, alpha, bravo, charlie, retard):
        self.alpha = alpha
        self.bravo = bravo
        self.charlie = charlie
        self.retard = retard

    def compute(self, h):
        return h * self.retard


while running:
    print("Choose an option: ")
    print("[1] Add a new employee")
    print("[2] Enter the hourly of the employee")
    print("[3] Show the employee information")
    print("[4] Quit", "\n")

    print("Enter option: ", end="")
    ans = int(input())

    if ans == 1:
        print("Enter the employee name: ", end="")
        alpha = (input())

        print("Enter the department: ", end="")
        bravo = input()

        print("Enter the position: ", end="")
        charlie = input()

        print("Enter the rate: ", end="")
        retard = int(input())

        employees.append(Employees(alpha, bravo, charlie, retard))

        continue

    elif ans == 2:
        e1 = Employees(alpha, bravo, charlie, retard)
        print("Enter the index of the employee: ", end="")

        y = int(input())
        print(employees[y].alpha, " is selected")
        print("Enter the hourly of the employee: ", end="")
        z = int(input())
        print(employees[y].retard * z)
        continue

    elif ans == 3:

        for x in employees:
            print("\nName:", x.alpha, "\nDepartment:", x.bravo, "\nPosition:", x.charlie, "\nRate:", x.retard,"\n")

        continue

    elif ans == 4:
        running = False

    else:
        print("Invalid input, please try again: ")
        continue
    break
