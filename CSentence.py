from Cstring import Cstring

class CSentence:
    """
    A class to represent a sentence composed of multiple Cstring objects,
    mimicking an array of strings to construct sentences.

    Attributes:
        string (list[Cstring]): A list of Cstring objects representing words in a sentence.
    """
    def __init__(self, cstrings: list[Cstring] = None):
        """
        Initializes the CSentence with an optional list of Cstring objects.

        Args:
            cstrings (list[Cstring], optional): A list of Cstring objects that make up the sentence.
                                                Defaults to None, which will initialize an empty sentence.
        """
        self.__cstrings = cstrings

    def get_sentence(self) -> str:
        """
        Constructs and returns the sentence as a concatenated string of words.

        Returns:
            str: The full sentence constructed from the Cstring objects,
                 where each word is separated by a space.
        """
        for index in range(0, len(self.__cstrings)):
            if type(self.__cstrings[index]) == list:
                sub_lst = self.__cstrings[index]
                for sub_index in range(len(sub_lst)):
                    sub_lst = sub_lst[sub_index] + sub_lst[sub_index + 1]
            else:
                self.__cstrings[index] + self.__cstrings[index + 1]


