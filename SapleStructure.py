import myLib

def addMarks(marks):
  name = input("Enter name: ").title()
  if name in marks:
    print("Student already exists!")
  else:
    courseworkMark = myLib.getFloatRange("Coursework: ",0,100)
    examMark = myLib.getFloatRange("Exam: ",0,100)
    marks[name] = [courseworkMark,examMark]

def updateMarks(marks):
  name = input("Enter name: ").title()
  if name in marks:
    print("Coursework / Exam : {:.1f} / {:.1f}".format(marks[name][0],marks[name][1]))
    update = myLib.getCharacter("Update C or E: ","CcEe")
    if update in "Cc":
      courseworkMark = myLib.getFloatRange("Coursework: ",0,100)
      marks[name][0] = courseworkMark
    else:
      examMark = myLib.getFloatRange("Exam: ",0,100)
      marks[name][1] = examMark
      print("Updated!")
  else:
    print("Student not found!")

def removeStudent(marks):
  name = input("Enter name: ").title()
  if name in marks:
    marks.pop(name)
    print("Student {} removed".format(name))
    ("Student already exists!")
  else:
    print("No such Student!!")

def displayMarks(marks):
  print("Name     Cw    Ex    Overall Grade")
  for s, m in marks.items():
    overall = (m[0]+m[1])/2
    if overall >=50:
      grade = "P"
    else:
      grade = "F"
    print("{:<8s} {:<5.1f} {:<5.1f} {:<7.1f} {}".format(s,m[0],m[1],overall,grade))

def menuOption():
  print("Menu")
  print("1. Add marks")
  print("2. Update marks")
  print("3. Remove student")
  print("4. Display marks")
  print("0. Quit")
  option = myLib.getIntegerRange("Enter choice: ",0,4)
  return option

def main():
  marks = { "John":[65,70], "Jane":[45,60], "Peter":[40,50], "Joe":[20,80] }
  
  while True:
    option = menuOption()
    if option == 0:
      break
    elif option == 1:
      addMarks(marks)
    elif option == 2:
      updateMarks(marks)
    elif option == 3:
      removeStudent(marks)
    else:
      displayMarks(marks) 

main()