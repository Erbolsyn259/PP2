a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

b = "Hello, World!"
print(b[2:5]) #llo

print(b[:5]) #Hello

print(b[2:]) #llo, World!

print(b[-5:-2]) #orl

print(b.upper())

print(b.lower())

print(b.strip()) # returns "Hello, World!"

a = "Hello"
b = "World"
c = a + " " + b
print(c)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)