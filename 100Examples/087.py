class Student:
    a = 0
    c = 0
def fn(stu):
    stu.a = 20
    stu.c = 'x'

if __name__ == '__main__':
    student = Student()
    student.a = 10
    student.c = 'c'

    fn(student)

    print(student.a, student.c)