def main():
    students_and_grades = {
        "Ishan" : "A+",
        "Aden" : "B", 
        "Ryan" : "C-"
        }
    reponse = input("Type your name: ")
    result = students_and_grades.get(reponse, "Student Not Found")
    print(result)

main()



