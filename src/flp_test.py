
from flp import *

EQUAL_0 = do(cons(identity, cst(0)), equal)
SUB_1 = do(cons(identity, cst(1)), sub)

def fact(x):
    return cond(EQUAL_0,
        cst(1),
        do(
            cons(identity, do(SUB_1, fact)),
            mul
        )
    )(x)

if __name__ == '__main__':
    class Gender(object):
        MALE = "MALE"
        FEMALE = "FEMALE"

    class Person(object):
        def __init__(self, name, age, gender):
            self.age = age
            self.name = name
            self.gender = gender

        def __repr__(self):
            return "Person(%s, %s, %s)" % (self.name, self.age, self.gender)

    IS_ADULT = lambda p: p.age >= 18
    IS_FEMALE = lambda p: p.gender == Gender.FEMALE
    IS_MALE = lambda p: p.gender == Gender.MALE
    persons = [
        Person("A", 20, Gender.MALE),
        Person("B", 16, Gender.FEMALE),
        Person("C", 50, Gender.MALE),
        Person("D", 30, Gender.FEMALE)
    ]
    print("adult males:",
        filter(
            # AND o [IS_ADULT, IS_MALE], filter
            compose(_and)(cons(IS_ADULT, IS_MALE))
        )
        (persons)
    )
    print("avg of ages:",
        do(
            cons(
                do(apply(lambda p: p.age), add),
                len
            ),
            div
        )
        (persons))

    print("fact:", do(_range, mul)(4))

    result = do(
        transpose,
        apply(mul),
        foldLeft(add)
    )([[1, 2, 3], [6, 5, 4]])
    print("intern product:", result)
