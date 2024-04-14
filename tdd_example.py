
import sys
class TDDExample():
    def __init__(self):
        pass

    def reverse_string(self, input_str: str) -> str:
        """
        Reverses order of characters in string input_str.
        """
        if input_str is not None:
            return input_str[::-1]
        else:
            return None

    def find_longest_word(self, sentence: str) -> str:
        """
        Returns the longest word in string sentence.
        In case there are several, return the first.
        """
        list1=sentence.split(' ')
        longest_word=''
        if list1 is not None:
            for word in list1:
                if len(word)>len(longest_word):
                    longest_word=word
            return longest_word
        else:
            return None

    def reverse_list(self, input_list: list) -> list:
        """
        Reverses order of elements in list input_list.
        """
        if input_list is not None:
            return input_list[::-1]
        else:
            return []

    def count_digits(self, input_list: list, number_to_be_counted: int) -> int:
        """
        Return count of digits
        """
        count=0
        for num in input_list:
            if num == number_to_be_counted:
                count+=1
        return count
