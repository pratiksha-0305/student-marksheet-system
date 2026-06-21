class academic:
    def study(self):
        print("student studies subjects")
class sports:
    def play(self):
        print("student pays sportts")
class student(academic,sports):
    def display(self):
        print("this is student") 
s=student()
s.display()
s.play()
s.study()                     