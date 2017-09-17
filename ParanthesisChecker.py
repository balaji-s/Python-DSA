from Stack import Stack

def par_checker(symbol_string):
    stack = Stack()
    balanced = True
    index = 0
    
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        
        if symbol in "({[":
            stack.push(symbol)
        else:
            if stack.is_empty():
                balanced = False
            else:
                sym = stack.pop()
                if not matches(sym,symbol):
                    balanced = False
        
        index = index + 1
        
    if balanced and stack.is_empty():
        return True
    else:
        return False
    
def matches(openp, closep):
    opens="[{("
    closes="]})"
    return opens.index(openp) == closes.index(closep)


def rev_String(String):
    stack =  Stack()
    for char in String:
        stack.push(char)
    while not stack.is_empty():
        print(stack.pop()+" ")


rev_String("balaji")
print(par_checker("()[]"))
print(par_checker('()([])'))


