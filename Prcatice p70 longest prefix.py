def longest_prefix(lst):
    if not lst:
        return ''
    
    for word in lst:
        if word[0] != lst[0][0]:
            return ''

    prefix = lst[0]
    for word in lst[1:]:
        i = 0
        
        while i < len(prefix) and i < len(word) and prefix[i] == word[i]:
            i += 1

        prefix = prefix[:i]
    return prefix

print(longest_prefix(['monster', 'monument', 'monday', 'monk']))  

# mon
