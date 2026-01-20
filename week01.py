class IsomorphicStrings:
    S = ""
    T = ""

    def are_isomorphic(self, word1, word2) -> bool:
        S = word1
        T = word2
        word_map = [[0 for _ in range(len(S))] for _ in range(2)]
        to_return = False

        # constraints on S and T: need to be same length, between 1 and 500 characters, and don't contain numbers
        # TODO: find a way to exclude punctuation marks too??
        if (len(word1) != len(word2)) or ((len(S) <= 1) or (500 <= len(S))) or not (word1.isalpha() or word2.isalpha()):
            to_return = False
        else:
            for i in range(len(word1)):
                # if this is a new letter in S
                if (word1[i] not in word_map[0]):
                    word_map[0][i] = word1[i]
                    word_map[1][i] = word2[i]
                # if this is a previously used letter in S
                elif (word1[i] in word_map[0]):
                    index = word_map[0].index(word1[i]) # find previous equivalent and use that
                    word_map[1][i] = word2[index]
                    word_map[0][i] = word1[i]     

            word2_list = list(word2)
            if word2_list == word_map[1]: 
                to_return = True
    
        return to_return
    
class InterleavingStrings:      
    _S1 = ""
    _S2 = ""
    _S3 = ""

    def is_interleaved(self, s1, s2, s3):
        _S1 = s1
        _S2 = s2
        _S3 = s3
        interleaved1 = ""
        interleaved2 = ""
        to_return = False

        for i in range(len(s1)):
            interleaved1 = interleaved1 + s1[i] + s2[i]
            interleaved2 = interleaved2 + s2[i] + s1[i]
        to_return = interleaved1 == _S3 or interleaved2 == _S3

        if (0 >= len(_S1)) or (0 >= len(_S2)) or (100 <= len(_S1)) or (100 <= len(_S1)):
            to_return = False
        if (0 >= len(_S3)) or (200 <= len(_S3)):
            to_return = False

        return to_return

        

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

    _iso_string1 = "add"
    _iso_string2 = "bee"
    _lbs_array = [0, 1, 0, 0, 1, 1]
    _inter_string1 = "abc"
    _inter_string2 = "def"
    _inter_string3 = "adbecf"

    isomorphic_boolean = isomorphicStrings.are_isomorphic(_iso_string1, _iso_string2)
    iso_str = "are" if isomorphic_boolean else "are not"
    print(f"the strings {_iso_string1} and {_iso_string2} {iso_str} isomorphic")
   
    subarray_length = longestBalancedSubarray.contiguous_length(_lbs_array)
    print(f"the longest balanced subarray is {subarray_length} characters long")

    interleave_boolean = interleavingStrings.is_interleaved(_inter_string1, _inter_string2, _inter_string3)
    inter_str = "can" if interleave_boolean else "cannot"
    print(f"the strings {_inter_string1} and {_inter_string2} {inter_str} form {_inter_string3}")