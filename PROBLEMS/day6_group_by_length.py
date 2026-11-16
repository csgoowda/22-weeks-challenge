```python
def group_by_length(words):
    groups = {}

    for word in words:
        length = len(word)

        if length in groups:
            groups[length].append(word)
        else:
            groups[length] = [word]

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
