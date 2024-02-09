class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
  
  def add_grade(self, grade):
    if type(grade) == Grade:
      self.grades.append(grade)

  def get_average(self):
      if self.grades:
          total_score = sum(grade.score for grade in self.grades)
          return total_score / len(self.grades)
      else:
          return 0
      
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

class Grade:
  minimum_passing = 65

  def __init__(self, score):
    self.score = score

  def is_passing(self):
    return self.score >= Grade.minimum_passing
  

pieter.add_grade(Grade(100))
pieter.add_grade(Grade(50))

print(pieter.get_average())
print(Grade(70).is_passing())
print(Grade(60).is_passing())