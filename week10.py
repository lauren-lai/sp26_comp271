class NameBins:
    def __init__(self, n: int) -> None:
        self.__bin_list = list[[None] * n]
        self.__num_bins = n
        self.__alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
        'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def add_name(self, name: str) -> None:
        """ adds the name to the appropriate bin """
        first_letter = name[0]
        index = self.get_letter_index(first_letter)
        print(self.get_bin_range())

    def size(self) -> int:
        """ returns the total number of names in all bins """
        size = 0

        for list in self.__bin_list():
            size += list.length()
        return size

    def __str__(self) -> str:
        """ returns a formatted string representing the bins """
        return "hello world"

    def get_letter_index(self, letter:str) -> int: 
        index = 0
        found = False
        i = 0
        while not found and i in range(len(self.__alphabet)):
            if letter == self.__alphabet[i]: # allowed because this isn't in add_name
                index = i
            i += 1
        return index

    def get_bin_range(self) -> int:
        bin_range = 0
        if (26 % self.__num_bins) == 0:
            bin_range = 26 // self.__num_bins
        else:
            

        return bin_range

def main() -> None:
    bins = NameBins(3)
    print(bins.__str__())

    bins.add_name("Adam")
    bins.add_name("Lauren")
    bins.add_name("Sadie")

    print(bins.__str__())
    bins.size()


if __name__ == "__main__":
    main()