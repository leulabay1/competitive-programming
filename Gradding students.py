def gradingStudents(grades):
    
    if len(grades)<= 60:
        a = []
        for i in grades:
            q = (int(i)//5 +1)*5
            p = q - int(i)
            if i < 38:
                a.append(i)
            elif p < 3:
                a.append(q)
            else:
                a.append(i)  
    return a   
