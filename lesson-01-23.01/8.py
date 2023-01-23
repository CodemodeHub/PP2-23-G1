# chr - returns ascii symbol by giving integer
# ord - return ascii code by giving symbol

a = 'a'
b = 97

print(ord(a))
print(chr(b))

a, b = b, a

print(a, b)

# cout << "Hello " << name;
name = "Anita"
print("Hello,", name, sep='') 