#!/usr/bin/python3
def sum_unique_integers(data):
      """Sums all unique integers in a list.

        Args:
            data: a list of integers

        Returns:
            The sum of all unique integers in the list
        """
        # Use set to remove all duplicates and sum the numbers
        return sum(set(data))
