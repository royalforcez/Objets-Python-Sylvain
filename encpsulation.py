class Student :
    def __init__(self,name):
        self._name = name
        self._gpa = 2.0

    def __str__(self):
        return f"{self._name} ({self.gpa})"
    
    def progresser(self,progres):
        if self._gpa + progres > 4:
            self._gpa = 4
        self._gpa += progres



if __name__ == '__main__':
    paul = Student ("Paul Lee")
    paul.progresser(1)

    peter = Student("Peter Tan")

    