class Student:
    """Represents one student in a course."""

    def __init__(self, student_id: str, name: str, major: str) -> None:
        """Initialize a Student with an ID, name, and major."""
        self.__student_id = student_id
        self.__name = name
        self.__major = major

    @property
    def ID(self) -> str:
        return self.__student_id

    def get_student_id(self) -> str:
        """Return the student's ID."""
        return self.__student_id
      
    def get_name(self) -> str:
        """Return the student's name."""
        return self.__name
      
    def set_name(self, name: str) -> None:
        """Set student name to given value."""
        self.__name = name 

    def get_major(self) -> str:
        """Return the student's major."""
        return self.__major
      
    def set_major(self, major: str) -> None:
        """Set student's major to given value."""
        self.__major = major   

    def __str__(self) -> str:
        """Return a user-friendly string representation."""
        return f"Student named {self.__name}, and ID {self.__student_id}."

    def __repr__(self) -> str:
        """Return a debugging string representation."""
        return f"Student({self.__student_id}, {self.__name}, {self.__major})"

    def __eq__(self, other) -> bool:
        return (isinstance(other, Student) and self.__student_id == other.__student_id)

class Roster:
    """Manages a list of students in a course."""

    def __init__(self, course_code: str):
        """Initialize a roster with an course code and an empty list of students."""
        self.__course_code = course_code
        self.__students = []
      
    def add_student(self, student_id: str, name: str, major: str) -> None:
        """Create a student defined by their ID, nane and major,
        Add student to the course """
        new_student = Student(student_id, name, major)
        self.__students.append(new_student)

    def __len__(self) -> int:
        """Return the number of students in the roster."""
        return len(self.__students)

    def __bool__(self) -> bool:
        """Return True if the roster is not empty."""
        return len(self.__students) > 0

    def __lt__(self, other) -> bool:
        return (isinstance(other, Student) and len(self.__students) < len(other))   

    # Private helper 
    def contains_id(self, student_id: str) -> bool:
        """Return True if a student with this ID exists."""
        i = 0
        found = False
        while i < len(self.__students) and not found:
            found = (get_student_id(self.__students[i]) == target)
            i += 1
        return found

    def contains_name(self, name: str) -> bool:
        """Return True if a student with this name exists."""
        i = 0
        found = False
        while i < len(self.__students) and not found:
            found = (get_name(self.__students[i]) == target)
            i += 1
        return found

    def contains_major(self, major: str) -> bool:
        """Return True if a student with this major exists."""
        i = 0
        found = False
        while i < len(self.__students) and not found:
            found = (get_student_id(self.__students[i]) == target)
            i += 1
        return found
      
    def report(self) -> str:
        """Return a formatted report of all students."""
        output = f"Roster for {self.__course_code} ({len(self)} students)"
        for s in self.__students:
            output += f"\n\t{s.name} - {s.major} ({s.student_id})"
    
        return output

def main():
    course = Roster("COMP271")
    course.add_student("rmax", "Ray Max", "CS")
    course.add_student("ohashem", "Omar Hashim", "CS")
    print(course._Roster__students[0])

if __name__ == "__main__":
    main()
