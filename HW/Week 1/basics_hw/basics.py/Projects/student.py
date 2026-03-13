def get_valid_int(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print("Value must be positive")
                continue
            if max_val is not None and value > max_val:
                print("Please enter a lower value ")
                continue
            return value
        except ValueError:
            print("Invalid number")


def get_students_info():
    students = {}

    while True:
        name = input("Enter student name ")
        if name == "exit":
            break

        age = get_valid_int("Enter age: ", min_val=1)

        scores = []
        for i in range(1,4):
            score = get_valid_int("Enter score: ", min_val=0, max_val=100)
            scores.append(score)

        students[name] = (age, scores)

    return students


def calculate_averages(students):
    averages = {}
    for name, (age, scores) in students.items():
        averages[name] = sum(scores) / len(scores)
    return averages


def list_students_above(averages):
    limit = get_valid_int("Enter minimum average: ", min_val=0, max_val=100)
    print("Students above average")
    for name, avg in averages.items():
        if avg >= limit:
            print(name, avg)


def save_to_file(filename, students):
    try:
        with open(filename, "w") as file:
            for name, (age, scores) in students.items():
                file.write(f"{name},{age},{scores} \n")
        print("Saved successfully")
    except :
        print("Not save")


def read_from_file(filename="students.data"):
    students = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                name, age, scores = line.strip().split(",")
                students[name] = (int(age), (scores))
        print("Read successfully")
    except :
        print("Error")

    return students
# def main():
#     students=get_students_info()
#     averages=calculate_averages(students)
#     list_students_above(averages)
#     save_to_file("students.data", students)
# main()
def main():
    students = {}

    while True:
        print("\n1. Add students","2. Calculate averages","3. List students above average","4. Save to file","5. Read from file","6. Exit")
        choice = get_valid_int("Enter choice: ", 1, 6)
        if choice == 1:
            students = get_students_info()

        elif choice == 2:
            averages = calculate_averages(students)
            print("Averages")
            for name, avg in averages.items():
                print(name, avg)

        elif choice == 3:
            averages = calculate_averages(students)
            list_students_above(averages)

        elif choice == 4:
            save_to_file("students.data", students)

        elif choice == 5:
            students = read_from_file("students.data")

        elif choice == 6:
            print("Exit program")
            break
main()
