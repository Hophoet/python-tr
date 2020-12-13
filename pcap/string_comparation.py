
def compare(string1, string2):
    condition = string1 > string2
    if(condition): big = string1
    else: big = string2
    string1_size = [ord(char) for char in string1]
    string2_size = [ord(char) for char in string2]
    print(f"you have just compare {string1} to {string2}")
    print(f"the bigest is {big}")
    print(f"{string1} sizes {string1_size}\n{string2} sizes {string2_size}")

compare("justine", "hophoet")
