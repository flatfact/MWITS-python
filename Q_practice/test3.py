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
"""
MIT License
Copyright 2018
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""