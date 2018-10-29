from generate_list import unique_first_n
class TestUniqueFirstN:
    def test_removes_duplicate_letters_in_order_provided(self):
        word_list = ['abcdzzz', 'ffffd', 'abcd', 'ffffa', 'abc', 'a', 'g', 'ga']
        modified_list = unique_first_n(word_list)
        assert modified_list == ['abcdzzz', 'ffffd', 'abc', 'a', 'g', 'ga']

    def test_does_not_modify_passed_in_list(self):
        word_list = ['abcdzzz', 'ffffd', 'abcd', 'ffffa', 'abc', 'a', 'g']
        word_list_copy = word_list.copy()
        modified_list = unique_first_n(word_list)
        assert word_list == word_list_copy
