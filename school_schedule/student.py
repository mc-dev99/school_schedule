class Student:
    
    def __init__(self, name, grade, classes):
        
        valid_grades = ["freshman", "sophomore", "junior", "senior"]
        if not grade in valid_grades:
            raise ValueError("invalid grade")
        
        self.name = name
        self.grade = grade
        self.classes = classes