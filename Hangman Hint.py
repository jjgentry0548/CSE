# Changing thing into a list
string1 = "turquoise"
list1 = list(string1)

# Hangman hint
for i in range(len(list1)):  # i goes through all indices
    if list1[i] == "u":  # if we find a "U"
        list1.pop(i)  # Remove the i-th index
        list1.insert(i, "*")  # Put a * there instead

# Changing back into a string (list->string)
print("".join(list1))
