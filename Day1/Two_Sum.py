def two_sum(nums, target):
    """
    Find two numbers in the given list that add up to the target value.
    
    This function uses a hash map (dictionary) approach to solve the Two Sum problem 
    with an efficient O(n) time complexity and O(n) space complexity.
    
    Args:
        nums (list): A list of integers to search through
        target (int): The target sum we want to achieve
    
    Returns:
        list: Indices of the two numbers that add up to the target
               Returns an empty list if no solution is found
    """
    # Create a dictionary to store complements and their indices
    complement_map = {}
    
    # Iterate through the list with enumeration to keep track of indices
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - num
        
        # Check if the complement exists in our dictionary
        if complement in complement_map:
            # If found, return the indices of both numbers
            return [complement_map[complement], i]
        
        # Store the current number and its index in the dictionary
        complement_map[num] = i
    
    # If no solution is found, return an empty list
    return []

# Example usage
if __name__ == "__main__":
    # Test cases
    test_nums = [2, 7, 11, 15]
    test_target = 9
    
    # Find and print the solution
    result = two_sum(test_nums, test_target)
    print(f"Indices of two numbers that sum to {test_target}: {result}")