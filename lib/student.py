class Student:
    def hello(self):
        # Print a greeting for a student
        print("Hey there! I'm so excited to learn stuff.")

    def raise_hand(self):
        # Print a message indicating the student is raising their hand
        print("Pick me!")
    pass

class ChattyStudent(Student):
    def hello(self):
        # Call the hello method of the parent class (Student)
        super().hello()
        # Add additional information for the chatty student
        print("How are you doing today? I'm okay, but I'm kind of tired. "
              "Did you watch The Walking Dead last night? You didn't?! "
              "Oh man, it was so crazy! What, you don't want any spoilers? "
              "Okay well let me just tell you who died...")

    def raise_hand(self):
        # Repeat the raising hand message multiple times
        for _ in range(10):
            super().raise_hand()
    pass
