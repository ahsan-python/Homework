# The actual class
class  TrainingSession:
    def __init__(self, SessionID, Title, DurationMinutes, IsCompleted):
        self.__sessionID = SessionID
        self.__Name = Title
        self.__Checking = False
# Setting new time
    def setting_time(self, NewTime):
        if  NewTime >240 or NewTime < 15 :
            print("Error : Invalid duration")
        else:
            self.__Time = NewTime
# Getting a Private Attributes
   def getting_SessionID(self):
       return self.__sessionID    

   
