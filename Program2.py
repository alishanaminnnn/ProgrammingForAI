has_discipline_issue =True
is_Sports_Student=True
Marks=20;
Attendance=85;

if has_discipline_issue==True: #If a student has a disciplinary issue (has_discipline_issue = True), print "Scholarship Denied due todisciplinary record."
    print ("Scholarship Denied due to disciplinary record.")
elif Marks>=90 and Attendance>=85: #Full Scholarship (100%): Marks >= 90 AND Attendance >= 85
    print("Full Scholarship (100%)")
elif (Marks >= 75 and Attendance >= 80) or (is_Sports_Student==True  and Attendance >= 75): #Half Scholarship (50%): (Marks >= 75 AND Attendance >= 80) OR (Is Sports Student = True AND Attendance >= 75)
    print("Half Scholarship (50%)")
else: #"No scholarship granted."
    Print ("No scholarship granted.")
    
