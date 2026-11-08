class analyze_marks:
    def name(self,name):
        self.name = name

    def marks(self, mark):
        self.marks = []
        mark = input().split()
        for i in mark:
            self.marks.append(i)

    def grade(self, num):
        if 0 <= num < 100: 
            if 90 <= num <= 100:
                return "A"
            elif 80 <= num <= 89:
                return "B"
            elif 70 <= num <= 79:
                return "c"
            elif 60 <= num <= 69:
                return "D"
            elif 50 <= num <= 59:
                return "E"
            else:
                return "F"
        else:
            raise ValueError("The marks must be between 0 to 100")
        
    def __init__(self):
        self.total = sum(self.marks)

        self.percentage = (self.total/500)*100

        self.grade = []
        for i in self.marks:
            self.grade.append(self.grade(i))

        

    def high_score_sub(self):
        self.high_score = max(self.marks)
        return self.marks.index(self.high_score)

    
    def display(self, pas):
        print("Name:- ", self.name)
        print("Marks:- ", self.marks)
        print("Grades:- ", self.grade)
        print("Percentage:-", self.percentage)

        pas = 1
        for i in self.mark: 
            if i < 50:
                pas = 0
        if pas == 1:
            print("Congrajulations You have Passed1")
        else:
            print("Sorry You have failed")

        print("The High Subject is:-", self.high_score_sub)


s1 = analyze_marks()

s1.name("Rohan Prakash Shirgaonkar")
s1.marks([ ])
