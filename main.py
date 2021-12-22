from fractional_cascading import FractionalCascading
from iterated_search import IteratedSearch
from naive_binary_search import NaiveBinarySearch

# define input sorted arrays
arrs = [[4, 6, 7, 8, 12], [1, 2, 5, 11, 15], [3, 9, 10, 13, 14]]

# define query key
query_key = 11

# Solution 1: Naive Binary Search
naive_binary_search = NaiveBinarySearch(arrs)
answers_1 = naive_binary_search.find(query_key)
print("Naive Binary Search:", answers_1)


# Solution 2: Iterated Search
iterated_search = IteratedSearch(arrs)
iterated_search.merge_input_arrs()
iterated_search.calculate_pointers()
answers_2 = iterated_search.find(query_key)
print("Iterated Search:", answers_2)


# Solution 3: Fractional Cascading
fractional_cascading = FractionalCascading(arrs)
fractional_cascading.merge_input_arrs()
fractional_cascading.calculate_pointers()
answers_3 = fractional_cascading.find(query_key)
print("Fractional Cascading:", answers_3)
