""" Урок 2, завдання 3
Створіть ієрархію класів із використанням множинного успадкування. Виведіть на екран порядок
вирішення методів для кожного класу. Поясніть, чому лінеаризація цих класів виглядає саме так.
"""


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(A):
    pass


class E(B, C, D):
    pass


class F(E):
    pass


print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())
print(E.mro())
print(F.mro())

# This is "C3 superclass linearization" for Method Resolution Order