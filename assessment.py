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

   For each instance of a class, the instance gets class attributes set during
   instantiation, and the class variables are shared among all instances of the
   class.  An intance attribute is specific to a particular instance of a class,
   and different instances may have different values of an instance attribute.

   You would use a class attribute when all instances of the class are expected
   to have the attribute, and when they are all expected to have the same value
   of the attribute (though exceptions are possible).  For example, all oranges
   have orange flesh (let's pretend cara cara oranges don't exist for a minute),
   so flesh_color = "orange" could be a good class attribute of the class
   Orange.  However, not all oranges are ripe, and so ripe = True or
   ripe = False might be a good instance attribute for a particular instace of
   Orange.


"""


# Parts 2 through 5:
# Create your classes and class methods
