""" In second year computer engineering class, group A student’s play cricket, group B
students play badminton and group C students play football.
Write a Python program using functions to compute following: -
a) List of students who play both cricket and badminton
b) List of students who play either cricket or badminton but not both
c) Number of students who play neither cricket nor badminton
d) Number of students who play cricket and football but not badminton.
(Note- While realizing the group, duplicate entries should be avoided, Do not use SET
built-in functions)"""

# Function to remove duplicates manually
def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result


# a) Students who play both cricket and badminton
def both_cricket_badminton(A, B):
    result = []
    for i in A:
        if i in B and i not in result:
            result.append(i)
    return result


# b) Students who play either cricket or badminton but not both
def either_not_both(A, B):
    result = []

    for i in A:
        if i not in B and i not in result:
            result.append(i)

    for i in B:
        if i not in A and i not in result:
            result.append(i)

    return result


# c) Number of students who play neither cricket nor badminton
def neither_cricket_badminton(A, B, all_students):
    count = 0
    for i in all_students:
        if i not in A and i not in B:
            count += 1
    return count


# d) Number of students who play cricket and football but not badminton
def cricket_football_not_badminton(A, B, C):
    count = 0
    for i in A:
        if i in C and i not in B:
            count += 1
    return count


# ---------------- MAIN FUNCTION ----------------
def main():
    # Input
    A = input("Enter students playing Cricket (space separated): ").split()
    B = input("Enter students playing Badminton (space separated): ").split()
    C = input("Enter students playing Football (space separated): ").split()

    # Remove duplicates
    A = remove_duplicates(A)
    B = remove_duplicates(B)
    C = remove_duplicates(C)

    # Create list of all students
    all_students = []
    for i in A + B + C:
        if i not in all_students:
            all_students.append(i)

    # Output
    print("\na) Students who play both Cricket and Badminton:")
    print(both_cricket_badminton(A, B))

    print("\nb) Students who play either Cricket or Badminton but not both:")
    print(either_not_both(A, B))

    print("\nc) Number of students who play neither Cricket nor Badminton:")
    print(neither_cricket_badminton(A, B, all_students))

    print("\nd) Number of students who play Cricket and Football but not Badminton:")
    print(cricket_football_not_badminton(A, B, C))


# Run main
if __name__ == "__main__":
    main()
