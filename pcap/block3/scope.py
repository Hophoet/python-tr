number = 7
print("number value before the call of the function", number)
def function():
    global number
    print("number value inside the function", number)
    number = 0
function()
print("number value after the call of the function(using global keywork inside the function)", number)
