class NameBins:
    def __init__(self, n: int) -> None:
        self.__n = n
        self.__bins: list[list[str]] = [[] for _ in range(n)]

        self.LETTERS_PER_BIN = 26 // n # convention of last bin being biggest because // is floor division
        self.__ranges = []
        for i in range(n):
            start_char = chr(ord('A') + (i * self.LETTERS_PER_BIN)) # converting to ascii
            if i < n-1:
                end_char = chr(ord('A') + (i + 1) * self.LETTERS_PER_BIN - 1)
            else:
                end_char = 'Z'
            self.__ranges.append([start_char, end_char])

    def add_name(self, name: str) -> None:
        """ adds the name to the appropriate bin """
        letter_index = ord(name[0]) - ord("A") # convert to ascii
        bin_index = min(letter_index // self.LETTERS_PER_BIN, self.__n - 1)
        self.__bins[bin_index].append(name)

    def size(self) -> int:
        """ returns the total number of names in all bins """
        size = 0
        for i in range(len(self.__bins)):
            size += len(self.__bins[i])
        return size

    __HEADER = "this is bin #{}, with {} names:"
    def __str__(self) -> str:
        """ returns a formatted string representing the bins """
        output = ""
        for i in range(len(self.__bins)):
            output += f"\n{self.__HEADER.format(i, len(self.__bins[i]))}"
            for j in range(len(self.__bins[i])):
                output += f"\n\t{self.__bins[i][j]}"
        return output


def main() -> None:
    bins = NameBins(3)

    bins.add_name("Adam")
    bins.add_name("Lauren")
    bins.add_name("Sadie")
    bins.add_name("Michael")
    bins.add_name("Bobby")

    print(bins.__str__())
    print(bins.size())


if __name__ == "__main__":
    main()