# Comp 5408 Course Project - Fractional Cascading

student name: Yukang Yin

student email: yinyukang@cmail.carleton.ca and yyin050@uottawa.ca

student number: 300162143 (University of Ottawa)

---

Three search algorithms are implemented in this course project:

- naive binary search
- iterated searh
- fractional cascading

## Structures

1. naive binary search solution is organized in `naive_binary_search.py`

2. iterated search solution is organized in `iterated_search_node.py` and `iterated_search.py`

3. fractional cascading search solution is organized in `fractional_cascading_node.py` and `fractional_cascading.py`

4. execution code is organized in `main.py`

## Run

1. define input arrays in `main.py`

   populate `arr` with valid input arrays, such as `[[4, 6, 7, 8, 12], [1, 2, 5, 11, 15], [3, 9, 10, 13, 14]]`

2. define query key in `main.py`

   populate `query_key` with valid query key, such as `11`

3. initialize a search solution by passing input arrays into solution's constructor, such as

   ```
   naive_binary_search = NaiveBinarySearch(arrs)
   iterated_search = IteratedSearch(arrs)
   fractional_cascading = FractionalCascading(arrs)
   ```

4. invoke search solution's `find` method by passing into query key, such as

   ```
   naive_binary_search.find(query_key)
   iterated_search.find(query_key)
   fractional_cascading.find(query_key)
   ```
