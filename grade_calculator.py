"""Simple command-line grade calculator."""


def calculate_average(grades):
    """Return the average of a list of grades."""
    return sum(grades) / len(grades)


def read_grade(entry):
    """Convert text to a grade between 0 and 100, or return None if invalid."""
    try:
        grade = float(entry)
    except ValueError:
        return None
    return grade if 0 <= grade <= 100 else None


def main():
    grades = []
    print("Grade Calculator (type 'done' when finished)")
    while True:
        entry = input("Enter a grade: ")
        if entry.strip().lower() == "done":
            break
        grade = read_grade(entry)
        if grade is None:
            print("Invalid grade. Enter a number from 0 to 100.")
            continue
        grades.append(grade)

    if not grades:
        print("No grades entered.")
        return

    print(f"Average: {calculate_average(grades):.2f}")


if __name__ == "__main__":
    main()
