"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
   The three main advantages of OO are:
   a. abstraction
   b. encapsulation
   c. polymorphism

   Abstraction: a code user doesn't have to know the details of what happens
   inside a method - they just need to understand the method signature and
   generally what the general behavior is, in order to use it.  Complexity is
   hidden away.

   Encapsulation: object orientation is modular - broken into sections that are
   self-contained, with all relevant info/code found in the same place.

   Polymorphism: pieces that should be interchangeable are interchangeable.

2. What is a class?
    A class is a type of thing, and a template to create instances of that thing.

3. What is an instance attribute?
    An instance attribute is a characteristic that is particular to a specific
    instance of an object.  It's a post-it on the instance.

4. What is a method?
    A method is like a function for a class.

5. What is an instance in object orientation?
    An instance is an instantiation of a class - a particular instance of the
    class.  So for the class Cat, I might have an instance which is a particular
    cat named "fluffy".

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   For each instance of a class, the instance may get class attributes set
   during instantiation, and the class attributes are shared among all instances
   of the class.  An intance attribute is specific to a particular instance of
   a class, and different instances likely have different values of an instance
   attribute.

   You would use a class attribute when all instances of the class are expected
   to have the attribute, and when they are all expected to have the same value
   of the attribute (though exceptions are possible).  For example, all oranges
   have orange flesh (let's pretend cara cara oranges don't exist for a minute),
   flesh_color = "orange" could be a good class attribute of the class Orange.
   However, not all oranges are ripe, and so ripe = True or ripe = False might
   be a good instance attribute for a particular instance of Orange.


"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
    """A student"""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """A question"""

    def __init__(self, question, answer):
        self.question = question
        self.correct_answer = answer

    def ask_and_evaluate(self):
        """Ask a question and return True if the answer is correct (else False)"""
        user_answer = raw_input(self.question + " > ")
        if user_answer.lower() == self.correct_answer.lower():
            return True
        else:
            return False


class Exam(object):
    """An exam"""

    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        """Adds a question to an exam"""
        new_question = Question(question, correct_answer)
        self.questions.append(new_question)

    def administer(self):
        """Asks each question in an exam and returns the score as a decimal"""
        score = 0.0
        for question in self.questions:
            if question.ask_and_evaluate():
                score += 1

# todo: format the score better
        return round(score/(len(self.questions)), 2)


class Quiz(Exam):
    """A quiz"""
    def administer(self):
        if super(Quiz, self).administer() >= 0.5:
            return True
        else:
            return False


def take_test(exam, student):
    """Administers a score for a student and prints the result"""
    student.score = exam.administer()

    print "{}'s score on {} is {}.".format(student.first_name,
                                           exam.name,
                                           student.score)


def example():
    """Create a sample exam and student, and take_test"""
    ex_test = Exam("example_test")

    ex_test.add_question("What's 2+2?", "4")
    ex_test.add_question("What's 1+5?", "6")
    ex_test.add_question("What's 3+0?", "3")

    ex_student = Student("Pupil", "McStudentson", "123 main st")

    take_test(ex_test, ex_student)

# print ""
# print "Creating and administering an example exam..."
# print ""

# #example()
