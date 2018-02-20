'''
PROBLEM:
Elly has a S of uppercase letters and a magic device that can modify the string. The strength of the device is an L.

The device is used in the following way. The user enters a 0-based index i such that 0 <= i <= length(S)-L. The device then performs the following changes:
* It leaves the first i characters (i.e., characters with indices 0 through i-1) untouched.
* It rearranges the next L characters (i.e., characters with indices i through i+L-1) into alphabetical order.
* It erases all the remaining characters (i.e., characters with indices i+L and more). Note that for i=length(S)-L no characters are erased.
The girl can use this "sorting trimmer" as many times as she likes. After each use she is left with the new version of the string.

In the examples below we use brackets to highlight the region that shall be sorted. For example, "ABRA[CADAB]RA" means that L=5 and Elly chose i=4. The device keeps the letters in front of the brackets, sorts the letters in the brackets, and throws away the rest. Here is one way how Elly could have used a device with L = 5, starting with the string S = "ABRACADABRA":
1. "ABRAC[ADABR]A" -> "ABRACAABDR"
2. "ABR[ACAAB]DR" -> "ABRAAABC"
3. "A[BRAAA]BC" -> "AAAABR"
You are given the S and the L. Return the lexicographically smallest string Elly can obtain.
'''
class EllysSortingTrimmer :
    def getMin(self, S, L) :
        return ''.join(sorted((S[0] + ''.join(sorted(S[1:])))[:L]))
