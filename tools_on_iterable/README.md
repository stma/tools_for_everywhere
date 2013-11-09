tools_on_iterable
=================

This module try to give some useful function to handle some rare but inconvenient cases with iterables.

flatten
-------

```python
flatten(nth_deep_list)
```

This function takes the argument and flatten it.

Flatten means in this case that if the given object iterable than it yield all the element from
this and check all the element as well and yield their child as well.

The depth of the object is maximum the call stack limit in python.

When you use it consider if you need performance because this solution use recursion and
exception handling which much more expensive then a loop.

For example:
```python
>>> list(flatten([[[7,7],6,7],8,9,[4,[4,4,[5, [5,[6],7], 6]]],9]))
[7, 7, 6, 7, 8, 9, 4, 4, 4, 5, 5, 6, 7, 6, 9]
```

But for example this kind of list can be flattened with better performance:

```python
l=[[1,2,3],[4,5,6], [7], [8,9]]

sum(l, [])
# or
list(itertools.chain.from_iterable(l)) 
```