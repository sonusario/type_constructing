# "OOP" from scratch in Python

In my study of programming languages, and in particular writing an interpreter
for one of my own design, I've noticed that you can mimic object-oriented
behavior by utilizing match case statements and closures.

Making use of Python's
ability to manipulate the global scope (👻), I've defined a function that acts
as a class constructor, called `car`. This function takes in a make, model, year, and instance name, and adds to the global environment the instance of the "car class" with the given instance name and its associated attributes.

Instances of this "car class" are, like the "class constructor" `car`, just functions. Here, they accept an attribute name, which will result in the return of the associated value of that attribute, and an assignment statement (e.g. `"make = Toyota"`), which with update the value of the specified attribute.

## Car Class Constructor Implementation

Here is a rough outline of what the constructor looks like (as opposed to the actual gangly code):

```
DEFINE new_car(make, model, year, instance_name):
    GLOBAL instance_name
    DEFINE instance_name(getSet_field):
        MATCH getSet_field:
            CASE "make":
                RETURN make
            CASE "model":
                RETURN model
            CASE "year":
                RETURN year
            CASE "make =" x:
                new_car(x, model, year, instance_name)
            CASE "model =" x:
                new_car(make, x, year, instance_name)
            CASE "year =" x:
                new_car(make, model, x, instance_name)
            CASE _:
                PRINT "Attribute not found"
            RETURN
    RETURN
```