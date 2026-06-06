# Student Grade Calculator

def calculate_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def main():
    print("Student Grade Calculator")
    print("=" * 30)
    
    # Accept marks for 5 subjects
    subjects = []
    for i in range(5):
        while True:
            try:
                mark = float(input(f"Enter mark for subject {i + 1}: "))
                if 0 <= mark <= 100:
                    subjects.append(mark)
                    break
                else:
                    print("Please enter a mark between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    # Calculate total
    total = sum(subjects)
    
    # Calculate average
    average = total / 5
    
    # Calculate grade
    grade = calculate_grade(average)
    
    # Display results
    print("\n" + "=" * 30)
    print("Results")
    print("=" * 30)
    print(f"Subject 1: {subjects[0]}")
    print(f"Subject 2: {subjects[1]}")
    print(f"Subject 3: {subjects[2]}")
    print(f"Subject 4: {subjects[3]}")
    print(f"Subject 5: {subjects[4]}")
    print("-" * 30)
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")
    print("=" * 30)

if __name__ == "__main__":
    main()
