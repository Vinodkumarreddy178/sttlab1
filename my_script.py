"""Simple student records management script."""


def add_student(records, name, age, grade):
    """Add a new student to the records."""
    records[name] = {"age": age, "grade": grade}


def update_grade(records, name, new_grade):
    """Update the grade of a student if they exist in the records."""
    if name in records:
        records[name]["grade"] = new_grade
    else:
        print(f"Student {name} not found.")


def display_students(records):
    """Display all students with their age and grade."""
    for student, info in records.items():
        print(f"Name: {student}, Age: {info['age']}, Grade: {info['grade']}")


def average_age(records):
    """Calculate and return the average age of students."""
    if not records:
        return 0
    total_age = sum(info["age"] for info in records.values())
    return total_age / len(records)


def main():
    """Main function to demonstrate student record management."""
    students = {}
    add_student(students, "Alice", 20, "A")
    add_student(students, "Bob", 21, "B")
    add_student(students, "Charlie", 22, "A")

    print("Initial student records:")
    display_students(students)

    print("\nUpdating Bob's grade...")
    update_grade(students, "Bob", "A")

    print("\nFinal student records:")
    display_students(students)

    print("\nAverage student age:", average_age(students))


if __name__ == "__main__":
    main()
