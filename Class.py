class Student:
   def __initi__(self,student_name,student_id):
       self.__name = student_name
       self.__student_id = student_id
       self.__marks = 0

  def get_name(self):
      return self.__name
  def get_marks(self):
      return self.__marks 
  def set_marks(score,self):
     if 0 <= score <= 100:
