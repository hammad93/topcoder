'''
PROBLEM:
You are given an integer (provided as s as it may be up to 50 digits in length). Return the number of subsequences of digits in the number that themselves compose an integer that is divisible by 3. Since this count could be very large, return the number mod 1000000007.
'''
def subsequences(l) :
    return [[l[j] for j in range(len(l)) if (i & (1 << j))] for i in range(1, 1 << len(l))]

class MagicNumberThree :
    def countSubsequences(self, s) :            
        # Iterate through subsequences and count if subsequence is divisible by 3
        count = 0
        seqs = subsequences(s)
        for i in seqs :
            if (int(''.join(i)) % 3) == 0 :
                count = (count + 1) % 1000000007 # mod per problem statement
       	return count
