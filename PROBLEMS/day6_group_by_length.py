```python
def group_by_length(words):
    groups = {}

    for word in words:
        length = len(word)

         groups.setdefault(length, []).append(word)

    return groups


words = ["cat", "dog", "apple", "bat", "mango", "hi"]

print(group_by_length(words))
```

**Output:**
```text
{
    3: ['cat', 'dog', 'bat'],
    5: ['apple', 'mango'],
    2: ['hi']
}
```
