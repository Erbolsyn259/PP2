import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))


print(json.dumps(x, indent=4, separators=(". ", " = ")))

print(json.dumps(x, indent=4, sort_keys=True))