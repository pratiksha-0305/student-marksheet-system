class parent:
    def show_parent(self):
        print("This is a parent class")
class child(parent): # sub class of parent class
    def show_child(self):
        print("This is child class")
c=child()
c.show_parent()
c.show_child()                