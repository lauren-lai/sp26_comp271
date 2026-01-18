class IsomorphicStrings:
    S = ""
    T = ""

    def are_isomorphic(word1, word2) -> bool:
        S = word1
        T = word2
        to_return = False

        if (len(T) != (len(S))) or (1 <= len(S) <= 500):
            to_return = False

        return to_return
    
class InterleavingStrings:      
    S1 = ""
    S2 = ""
    S3 = ""

    def is_interleaved(s1, s2, s3):
        S1 = s1
        S2 = s2
        S3 = s3

class LongestBalancedSubarray:
    _BINARY_ARRAY = []
    
    def count_continuous(self, num, to_search) -> int:
        prev_count = 0
        current_count = 0
        to_return = 0

        # counts longest continuous streak of num in to_search and updates when the current streak ends
        for i in range(len(to_search)):
            if to_search[i] == num:
                current_count +=1
            if (to_search[i] != num) and (current_count != 0): 
                prev_count = current_count
                current_count = 0

        # to_return is the longer streak
        if (current_count > prev_count):
            to_return = current_count
        else:
            to_return = prev_count

        return to_return
    
    def contiguous_length(self, binarr) -> list:
        BINARY_ARRAY = binarr
        to_return = 0
        zeros_streak = self.count_continuous(0, BINARY_ARRAY)
        ones_streak = self.count_continuous(1, BINARY_ARRAY)
        # sets max to the shorter streak length
        max = zeros_streak if zeros_streak < ones_streak else ones_streak
        to_return = max * 2
        return to_return

class Main():
    isomorphicStrings = IsomorphicStrings()
    interleavingStrings = InterleavingStrings()
    longestBalancedSubarray = LongestBalancedSubarray()

    _lbs_array = [0, 1, 0, 0, 1, 1]
    print(f"with the array {_lbs_array}, the longest balanced subarray is {longestBalancedSubarray.contiguous_length(_lbs_array)}")
