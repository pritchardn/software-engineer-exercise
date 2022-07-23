# General instructions

1. Fork or clone this repository into your own github account.
1. All your work will be done in your repository.
1. Inspect the code and understand what it's doing.
1. When going through the steps below,
   create git commits, making a history of
   changes that can be inspected later on.
1. At the end of the exercise you will *have* to push your code.
   You can also push regularly before that if you want.

# Steps
1. Both functions in the `object_analysis` module have a problem.
  1. Write a test for each function that demonstrates the problem.
  1. Fix the function and ensure the test passes.
1. Both functions' performance can be improved
   for performance and readability
  1. Describe how you would go about
     increasing the performance.
     What steps would you take?
     How do you determine what to improve?
  1. Try to increase the performance of both functions.
     Use only built-in python modules and types,
     don't bother trying to use external packages
     or writing code in lower-level languages.
  1. Try to improve the readibility of the functions.
1. The `object_analysis` module contains not only functions
  but also some little examples/mini-tests.
  Can you re-organise this?
1. The code has no comments nor descriptions. Add as appropriate.
1. Create a GitHub Action (or any other CI script)
   that runs automatic tasks after each commit.
   Add the tasks you think are relevant.

# Increasing Performance
How to assess what should be improved:
1. Reasoning about algorithmic complexity for 'low-hanging fruit':
   1. How many loops are being conducted? Could they be merged?
   2. How often is data being read/written? Could operations be merged?
   3. Is there a more efficient algorithm to tackle the task at hand?
   4. Are there more efficient data-structured to provide the type of access required?
2. After making straightforward algorithmic improvements, consider measuring code performance
depending on how often this code will be used; if frequently, on large volumes of data, as a core 
routine or time-sensitive function, absolutely, otherwise perhaps not:
   1. For these examples, I will assume that a linear time approach is enough with few constant 
   factors

## Improving most_common_type
This function is, in essence, calculating the most frequent field entry in a list of dictionaries 
- It loops through the entire list of objects for each type of object considered
  - This can be collapsed into a single pass through the objects 
- The final comparison routine is effectively sorting a list of `sum_x` variables, which can be 
handled as an explicit sort of mapped counts. This incidentally allows the function to become more 
general
- To keep compatibility with the original code outputs, the function contains a list of expected 
types and their corresponding plural forms. If the objects argument contains a maximal number of 
unexpected objects, an appropriate error is raised (this is also tested).
- Further optimisation could include changing the data structure a struct-of-arrays rather than
array-of-structs style, but that either changes the expected input (which I will for now assume is
not expected) or result in one additional pass through the data, which defeats the purpose of the
optimisation in the first place.

## Improving Farthest
This function returns the fist object in a list with the largest "redshift" value.
- Similar to most_common_type, the original code loops thorugh the objects twice, once to compute / locate
the maxium and a second to find it again
  - This can easily be merged into a single pass through the data structure
- Also similar to most_common_type, a struct-of-arrays style would remove the dictionary lookups for each
comparison, but withot changing input signature, that would be redundant.

# A Note on improving readability
- Changing the expected outputs of a function is usually something that needs discussing before 
implementation, if the original intention was to only consider 'valid' object types and return their
plural form if most abundant, I would modify `most_common_type` as follows:
```python
def most_common_type(objects, expected_types: set, expected_plurals: dict):
    type_counts = defaultdict(int)
    for o in objects:
        type_counts[o['type']] += 1
    abundant_type = max(type_counts, key=lambda x: type_counts[x])
    if abundant_type in expected_types:
        return expected_plurals[abundant_type]
    else:
        raise ValueError("Object list contains a large number of unidentified objects")
```
Which is more in line with my original changes, but dropping this requirement makes for a much
simpler, generalised and ultimately readable function.
