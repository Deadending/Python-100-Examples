class Student:
    name = ''
    age = 0 
    score = [None] * 4

    def input_stu(self):
        self.name = input("Input name:")
        self.age = int(input("Input age:"))
        for i in range(len(self.score)):
            self.score[i] = int(input('Input %d score:' %(i + 1)))
        
    def output_stu(self):
        print("Name：%s" % self.name)
        print("Age: %d" % self.age)
        for i in range(len(self.score)):
            print("%d score：%d" %((i + 1), self.score[i]))

if __name__ == '__main__':
    N = 5
    studentArray = [Student()] * N
    for i in range(len(studentArray)):
        studentArray[i].input_stu()

    for i in range(len(studentArray)):
        studentArray[i].output_stu()