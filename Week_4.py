def histogram(l):
    counts = {}  

    for num in l:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    result = [(num, count) for num, count in counts.items()]
    
    # Sort the list first by repetitions (ascending) and then by number (ascending)
    result.sort(key=lambda x: (x[1], x[0]))
    
    return result

  
def transcript(coursedetails, studentdetails, grades):
    course_dict = dict(coursedetails)
    student_dict = dict(studentdetails)

    student_grades = {}
    for rollnumber, coursecode, grade in grades:
        if rollnumber not in student_grades:
            student_grades[rollnumber] = []
        student_grades[rollnumber].append((coursecode, course_dict[coursecode], grade))

    result = []
    for rollnumber, name in studentdetails:
        if rollnumber in student_grades:
            result.append((rollnumber, name, sorted(student_grades[rollnumber])))

    result.sort(key=lambda x: x[0])
    
    return result
# Hidden code below

import ast

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "histogram":
   arg = ast.literal_eval(farg)
   print(histogram(arg),end="\n")
elif fname == "transcript":
   arg = ast.literal_eval(farg)
   print(transcript(arg[0],arg[1],arg[2]),end="\n")
else:
   print("Function", fname, "unknown")
