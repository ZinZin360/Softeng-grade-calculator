"""Simple command-line grade calculator."""


def calculate_average(grades):
    """Return the average of a list of grades."""
    return sum(grades) / len(grades)


def main():
    grades = []
    print("Grade Calculator (type 'done' when finished)")
    while True:
        entry = input("Enter a grade: ")
        if entry.strip().lower() == "done":
            break
        grades.append(float(entry))

    if not grades:
        print("No grades entered.")
        return

    print(f"Average: {calculate_average(grades):.2f}")


if __name__ == "__main__":
    main()
