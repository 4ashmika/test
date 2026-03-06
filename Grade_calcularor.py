def main():
    while True:
        name = input("Enter student name (or type 'exit' to quit): ")
        if name.lower() == 'exit':
            break
            
        # Collect 3 marks and handle invalid input
        marks = []
        for i in range(1, 4):
            while True:
                try:
                    m = float(input(f"Mark for Subject {i}: "))
                    if 0 <= m <= 100:
                        marks.append(m)
                        break
                    else:
                        print("Error: Marks should be between 0 and 100.")
                except ValueError:
                    print("Error: Please enter a valid number.")

        average = sum(marks) / 3
        
        # Grading logic
        if average >= 75:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 40:
            grade = "C"
        else:
            grade = "Fail"

        # Formatted output
        print("-" * 30)
        print(f"Name   : {name}")
        print(f"Average: {average:.1f}")
        print(f"Grade  : {grade}")
        print("-" * 30)
        print() # Add a blank line for readability between entries

if __name__ == "__main__":
    main()
