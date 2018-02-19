'''
PROBLEM:
  An AND-equation is an equation that looks like this:
    X[0] AND X[1] AND ... AND X[N-1] = Y
  Here X[i] and Y are non-negative integers and the bitwise AND operation is defined in the Notes.
  You are given a A that contains exactly N+1 elements. Your task is to construct an AND-equation using each element of A exactly once. (That is, N of them will be on the left hand side of the AND-equation and the remaining one will be on the right hand side.) If this is possible, return the value of Y in this AND-equation. If no AND-equation can be constructed, return -1. (It can be shown that for each A there is at most one possible value Y, so the return value is always defined correctly.)
NOTES:
  - AND is a binary operation, performed on two numbers in binary notation. First, the shorter number is prepended with leading zeroes until both numbers have the same number of digits (in binary). Then, the result is calculated as follows: for each position where both numbers have 1 in their binary representations, the result also has 1. It has 0 in all other positions.
  - For example 42 AND 7 is performed as follows. First, the numbers are converted to binary: 42 is 101010 and 7 is 111. Then the shorter number is prepended with leading zeros until both numbers have the same number of digits. This means 7 becomes 000111. Then 101010 AND 000111 = 000010 (the result has ones only in the positions where both numbers have ones). Then the result can be converted back to decimal notation. In this case 000010 = 2, so 42 AND 7 = 2.
  - One of the ways to calculate the AND of more than two numbers X[0], X[1], ..., X[N-1] is "X[0] AND (X[1] AND (... AND X[N-1]))..))". Since the function is commutative and associative, you can also express it as "X[0] AND X[1] AND ... AND X[N-1]" and group the operands in any way you like.'
''

def constructAnd(A) :
    if (len(A) == 1) :
        return A[0]
    return A[0] & constructAnd(A[1:])
class ANDEquation :
    def restoreY(self, A) :
        if len(A) <= 2 :
            return -1
        for i, X in enumerate(list(A)) :
            if X == constructAnd(list(set([x for index, x in enumerate(A) if index != i]))) :
                return X
       	return -1
