def s_list(mode,students):
    if mode == 1:    
        stu_class = []
        for stu in students:
            Class = stu[-2:]
            if Class in stu_class:
                continue
            else:
                stu_class.append(Class)
        return len(stu_class)
    elif mode == 2:
        toreturn = []
        db ={}
        for stu in students:
            Class = stu[-2:]
            if Class in db:
                db[Class].append(stu)
            else:
                db[Class] = [stu]
        sor = sorted(db)
        for order in sor:
            for item in db[order]:
                toreturn.append(item)
        return toreturn
    elif mode == 3:
        students = sorted(students)
        return None
