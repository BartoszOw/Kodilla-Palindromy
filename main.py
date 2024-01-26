

#  Funkcja sprawdzająca palindromy
def palindrom(string):
    if string == string[::-1]:
        return True
    else:
        return False
    
print(palindrom("lewel"))