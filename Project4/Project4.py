class TermNode:

    def __init__(self, coefficient=0, exponent=0, next=None):
        self._coefficient = coefficient
        self._exponent = exponent
        self._next = next

    def __eq__(self, other):
        if type(other) is not TermNode:
            return False
        return self._coefficient == other._coefficient and self._exponent == other._exponent

    def __ne__(self, other):
        return not (self == other)


class Polynomial:

    def __init__(self, coefficient, exponent):
        self._first_node = TermNode(coefficient, exponent)

    def __add__(self, other):
        result = Polynomial(self._first_node._coefficient, self._first_node._exponent)
        self_current_term_node = self._first_node._next
        while self_current_term_node is not None:
            result._addTermNodeInDescendingOrder(TermNode(self_current_term_node._coefficient, self_current_term_node._exponent))
            self_current_term_node = self_current_term_node._next
        other_current_term_node = other._first_node
        while other_current_term_node is not None:
            result._addTermNodeInDescendingOrder(TermNode(other_current_term_node._coefficient, other_current_term_node._exponent))
            other_current_term_node = other_current_term_node._next

        return result

    def _addTermNodeInDescendingOrder(self, termNode):
        if termNode._exponent > self._first_node._exponent:
            termNode._next = self._first_node
            self._first_node = termNode
        elif termNode._exponent == self._first_node._exponent:
            self._first_node._coefficient += termNode._coefficient
        else:
            current_node = self._first_node
            while current_node._next is not None:
                if termNode._exponent > current_node._next._exponent:
                    termNode._next = current_node._next
                    current_node._next = termNode
                    break
                elif termNode._exponent == current_node._next._exponent:
                    current_node._next._coefficient += termNode._coefficient
                    break
                else:
                    current_node = current_node._next
            else:
                current_node._next = termNode

    def __mul__(self, other):
        result = None

        self_current_node = self._first_node
        while self_current_node is not None:
            other_current_node = other._first_node
            while other_current_node is not None:
                if result is None:
                    result = Polynomial(self_current_node._coefficient * other_current_node._coefficient,self_current_node._exponent + other_current_node._exponent)
                else:
                    new_term = TermNode(self_current_node._coefficient * other_current_node._coefficient,self_current_node._exponent + other_current_node._exponent)
                    result._addTermNodeInDescendingOrder(new_term)
                other_current_node = other_current_node._next
            self_current_node = self_current_node._next
        return result

    def differentiate(self):
        result = Polynomial(self._first_node._coefficient * self._first_node._exponent, self._first_node._exponent - 1)
        self_current_term_node = self._first_node._next
        while self_current_term_node is not None:
            new_term = TermNode(self_current_term_node._coefficient * self_current_term_node._exponent, self_current_term_node._exponent - 1)
            result._addTermNodeInDescendingOrder(new_term)
            self_current_term_node = self_current_term_node._next
        return result

    def integrate(self):
        result = Polynomial(self._first_node._coefficient / (self._first_node._exponent + 1), self._first_node._exponent + 1)
        self_current_term_node = self._first_node._next
        while self_current_term_node is not None:
            if self_current_term_node._exponent + 1 != 0:
                new_term = TermNode(self_current_term_node._coefficient / (self_current_term_node._exponent + 1),
                                    self_current_term_node._exponent + 1)
                result._addTermNodeInDescendingOrder(new_term)
            self_current_term_node = self_current_term_node._next
        return result

    def __str__(self):
        result = ""
        current_node = self._first_node
        while current_node is not None:
            if current_node._coefficient != 0:
                result += "{:.2f}".format(current_node._coefficient)
                if current_node._exponent != 0:
                    result += "x^" + str(current_node._exponent) + " "
                if current_node._next is not None:
                    if current_node._next._coefficient > 0:
                        result += "+ "
            current_node = current_node._next
        return result

    def __eq__(self, other):
        if type(other) is not Polynomial:
            return False
        self_current_node = self._first_node
        other_current_node = other._first_node
        while self_current_node is not None and other_current_node is not None:
            if self_current_node != other_current_node:
                return False
            self_current_node = self_current_node._next
            other_current_node = other_current_node._next
        return self_current_node is None and other_current_node is None


poly2 = Polynomial(2,3)
poly3 = Polynomial(3,4)
poly1 = poly2 + poly3
poly4 = Polynomial(4,5)
poly5 = Polynomial(5,6)
poly6 = poly4 + poly5
poly7 = poly1 * poly6

print(poly7)
print("differentiate")
poly8 = poly7.differentiate()
print(poly8)
print("integrate")
poly9 = poly8.integrate()
print(poly9)
print("does poly7 == poly9", poly7 == poly9)