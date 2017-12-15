class Parent(object):
    def override(self):
        print("PARENT override")


class Children(Parent):
    def override(self):
        print("CHILD before")
        super(Children, self).override()
        print("CHILD after")

dad = Parent()
son = Children()

dad.override()
son.override()
