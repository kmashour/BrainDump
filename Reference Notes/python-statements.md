### enumerate -> returns iterator for a list of tuples

For loop is used to unpack list of tuples
```python
	str="abcd
	for index,letter in enumerate(str)
	print(f "the index {index} and letter is {letter}")
```




### zip -> used to create list of tuples by zipping two lists together
```python
	list1=["a","b","c","d"]
	no=["1","2","3","4","5","6"]
	zip(list1,no)
```

### list comprehension (Tip)
Using `all()` or `any()` for a single boolean result 
If the goal is to check if _all_ items meet a condition and get a single `True` or `False` for the entire list, you should combine a generator expression (which is similar to list comprehension but more memory efficient for this purpose) with the built-in `all()` or `any()` functions.
```python
numbers = [2, 4, 6, 8]
all_even = all(num % 2 == 0 for num in numbers)
```
 Result: True



random
	- shuffle
	- randint 

