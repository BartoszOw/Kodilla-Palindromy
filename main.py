def palindrom(string):
    if string == reversed(string):
        return True
    else:
        return False
    
palindrom("kajak")