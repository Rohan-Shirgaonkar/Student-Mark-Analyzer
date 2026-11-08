class analyze_marks:
    def name(self,name):
        self.name = name

    def marks(self):
        self.marks = []
        mark = input("enter marks for S1, S2, S3, S4, S5:- ").split()
        if len(mark) != 5:
            raise ValueError("Enter exactly 5 marks")
        for i in mark:
            self.marks.append(int(i))

    def cal_total(self):
        self.total = sum(self.marks)

    def percent(self):
        self.percentage = (self.total/500)*100

    def rank(self, num):
        if 0 <= num <= 100: 
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
        
    def grade(self):
        self.grad = []
        for i in self.marks:
            self.grad.append(self.rank(i))
        

    def high_score_sub(self):
            self.high_score = max(self.marks)
            self.sub = self.marks.index(self.high_score)

    
    def display(self):
            print("Name:- ", self.name)
            print("Marks:- ", self.marks)
            print("Grades:- ", self.grad)
            print("Total:- ", self.total)
            print("Percentage:-", self.percentage)

            pas = 1
            for i in self.marks: 
                if i < 50:
                    pas = 0
            if pas == 1:
                print("Congrajulations You have Passed")
            else:
                print("Sorry You have failed")

            print(f"The High Subject is:- S{self.sub+1}")


a1 = analyze_marks()

a1.name("Rohan Prakash Shirgaonkar")
a1.marks()
a1.cal_total()
a1.percent()
a1.grade()
a1.high_score_sub()
a1.display()
