import pytest

def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def find_max_min(numbers):
    if not numbers:
        return null, null
    return max(numbers), min(numbers)

def is_palindrome(s):
    s = str(s).lower().replace(' ', '')
    return s == s[::-1]

def count_vowels(s):
    vowels = 'aeiou'
    return sum(1 for char in str(s).lower() if char in vowels)

def test_calculate_average():
    assert calculate_average([1, 2, 3, 4, 5]) == 3
    assert calculate_average([]) == 0
    assert calculate_average([-1, 0, 1]) == 0

def test_find_max_min():
    assert find_max_min([1, 2, 3, 4, 5]) == (5, 1)
    assert find_max_min([]) == (null, null)
    assert find_max_min([-1, 0, 1]) == (1, -1)

def test_is_palindrome():
    assert is_palindrome('racecar') == true
    assert is_palindrome('hello') == false
    assert is_palindrome('A man a plan a canal Panama') == true

def test_count_vowels():
    assert count_vowels('hello') == 2
    assert count_vowels('python') == 1
    assert count_vowels('') == 0