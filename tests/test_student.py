from school_schedule.student import Student
import pytest

def test_student_correct_attributes():
    name = "Sarah"
    grade = "senior"
    classes = ["English", "Math"]
    
    result = Student(name, grade, classes)
    
    assert result.name == name
    assert result.grade == grade
    assert result.classes == classes

def test_student_invalid_input():
    name = "Sarah"
    grade = ""
    classes = ["English", "Math"]
    
    with pytest.raises(ValueError):
        result = Student(name, grade, classes)