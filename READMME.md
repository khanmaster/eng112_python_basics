# Python introduction
## Python Variables
### Github set up with HTTPS
#### Github set up with ssh keys

- Python is a dynamic typed language

- add image
![](C:\Users\ahskhan\PycharmProjects\eng122_python\terraform_with_ansible-new.jpg)
  
- Add a block of code
```python
# take user input with method called input()
print("please enter your name")
name = input()
print("welcome dear")
print(name)

```
- To add a line of code
- commands `git add .`
- `git commit -m "logical msg"`
- `git push -u origin main`
- add link to your Git-hub page

### Data types & Operators 
####  2 types operators 
##### Arithmetic operators 
- `+ - * /`
- `+` adds two operands (var) together
- `-` subtract 
- `*` multiply
- `/` divide 

a = 4
b = 2
#### Comparison Operators
- `>` greater than `a > b`
- `<` less than
-`==` 
- `!=`
- `>=`
- `<=`

```python
print(a > b) # true
print(a < b) # false
print(a == b) #false
print(a != b) #true

print(a * b) # 6
```

### Builtin methods
```python
# functions  methods builtin in python
greeting = "Hello World!"

# what options are available in python's builtin library
print(greeting)
# if we wanted to check if the letters are in string
print(greeting.isalpha()) # true or false
# is it in lower case or upper case
print(greeting.islower()) # Boolean
print(greeting.isdigit())
print(greeting.endswith("!"))
print(greeting.startswith("34"))
```

#### Strings Concatenation Casting
- String indexing 
- `Hello World!`
- index in python starts with 0

- Hello World!
  01234567891011
```python
# what options are available in python's builtin library
print(greeting)
# if we wanted to check if the letters are in string
print(greeting.isalpha()) # true or false
# is it in lower case or upper case
print(greeting.islower()) # Boolean
print(greeting.isdigit())
print(greeting.endswith("!"))
print(greeting.startswith("34"))

greeting = "Hello World!"
       #    01234567891011
       #                -1
print(len(greeting))

print(greeting[-5])
print(greeting[:5])


print only `world` in a print statement using slicing
print 4th letter from left to right - use correct indexing for all statements
print 7th index position letter from right to left
print 6 letter from left to right

example_string = "Jame                                                       "
print(example_string)
print(len(example_string))
# strip()
print(len(example_string.strip()))

# welcome user with their name and welcome message - name & message must start with capital
example_text = "here's some text With lot's of text"
print(example_text.count("text"))

# find a method to bring the statement in capital/small letters then first letter capital


# how to replace text within the string

print(example_text.replace("With ", " ,"))
```
