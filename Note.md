# **PYTHON FUNDAMENTALS**

Python is a very powerful and widely-used language that will allow us to quickly build fairly complicated web applications.

Let's start where we start with many programming languages: Hello,world. This program, written in Python, would look like this:

```
Print("Hello,world!");
```

1. To break down what's going on in that line, there is a **print** function built in to the python language, that takes an argument in parentheses, and displays that argument on the command line.
2. To actually write and run this program on your computers, you'll first type this line into your text editor of choice, and then save the file as **something.py**. Next, you'll head over to your terminal, navigate to the directory containing your file, and type **python something.py**. In the case of the above program , the words "Hello, world!" will then be displayed in the terminal.

3. Depending on how your computer is set up, you may have to type **python3** instead of python before the file name, and you may even have to download Python if you haven't already. After installing Python, we recommend that you also download Pip, as you'll need that later in the course.
4. When you type **python file.py** in your terminal, a program called an interpreter, which you downloaded together with Python, reads through your file line by line, and executes each line of the code. This is different than languages like C or Java, which need to be compiled into machine code before they can be run.

# **VARIABLES**

A key part of any programming language is the ability to create manipulate variables. In order to assign a value to a variable in Python, the syntax looks like this:

```
a = 28
b = 1.5
c = "Hello!"
d = True
e = None
```

Each of these lines is taking the value to the right of the =, and storing it in the variable name to the left.

Unlike in some other programming languages, Python variable types are inferred, meaning that while each variable does have a type, we do not have to explicity state which type it is when we create the variable.Some of the most common variable types are:

**int:** An integer.
**float:** A decimal number.
**chr:** A single character.
**str:** A string, or sequence of characters.
**bool:** A value that is either True or False.
**NoneType:** A special value (None) indicating the absence of a value.

Now, we'll work on writing a more interesting program that can take input from the use and say hello to that user. To do this, we'll use another built in function called **input** which displays a prompt to the user, and returns to the user, and returns whatever the user provides as input. For example, we can write the following in a file called **name.py**:

```
name = input("Name: ")
print("Hello, " + name)

```

When run on the terminal, this is what the program looks like:

```
(base) python hello.py
Name: Connor
Hello: Connor
```

A couple of things to point out here:

1. In the first line, instead of assigning the variable name to an explicit value, we're assigning it to whatever the **input** function returns.
2. In the second line, we're using the **+** operator to combine, or **concatenate**, two strings. In python, the **+** operator can be used to add numbers or concatenate strings and lists.

# **FORMATTING STRINGS**

1. While we can use the **+** operator to combine strings as we did above, in the latest versions of pythonm there are even easier ways to work with strings, known as **formatted strings**, or **f-strings** for short.

2. To indicate that we're using formatted strings, we simply add an f before the quotation marks. For example, instead of using "Hello, " + name as we did above, we could write f"Hello,{name}" for the same result. We can even plug a function into this string if we want, and turn our program above into the single line:

```
print(f"Hello, {input("Name: ")}")
```

# **CONDITIONS**

1. Just like in other programming languages, Python give us the ability to run different segments of code based on different conditions. For Example, in the program below, we'll change our output depending on the number a user types in:

```
num = input("Number: ")
if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
else:
    print("Number is 0")

```

2. Getting into how the above program works, conditionals in python contain a keyword **(if, elif, or else)** and then (except in the **else** case) a boolean expression, or an expression that evaluates to either True or False. Then, all the code we want to run if a certain expression in true is **indented** directly below the statement. Indentation is required as part of the Python syntax.

3. However, when we run this program, we run into an exception that looks like this:

```
TypeError: '>' not supported between instances of 'str' and 'int'
```

4. An exception is what happens when an error occurs while we're running our python code, and over time you'll get better and better at interpreting these errors, which is a very valuable skill to have.
5. Let's look a bit more closely at this specific exception: If we look at the bottom, we'll see that we ran into a TypeError, which generally means Python expected a certain variable to be of one type, but found it to be of another type. In this case, the exception tells us that we cannot use the > symbol to compare a str and int, and then above we can see that this comparison occurs on line 2.

6. In this case, it's obvious that 0 is an integer, so it must be the case that our num variable is a string . this is happening it turns out that the input function always returns a string, and we have to specify that it should be turned into(or cast into) an integer using the int function. This means our first line would now look like:

```
num = int(input("Number: "))

```

# **SEQUENCES**

1. One of the most powerful parts of the python language it its ability to work with sequences of data in addition to individual variables.

There are several types of sequences that are similar in some ways, but different in others. When explaining those differences, we'll use the terms **mutable/immutable** and **ordered/unordered.** Mutable means that once a sequence has been defined, we can change individual elements of that sequence, and **ordered** means that the order of the objects matters.

**STRINGS**

**:Ordered:Yes**
**Mutable** : No

We've already looked at strings a little bit, but instead of just variables, we can think of a string as a sequence of characters. This means we can access individual elements within the string! For example:

```
name = "Harry"
print(name[0])
print(name[1])

```

prints out the first (or index-0) character in the string, which in this case happens to be H, and the prints out the second (or index-1) character, which is a.

# **LIST**

**:Ordered:Yes**
**Mutable** : Yes

A **Python list** allows you to store any variable types. We create a list using square brackets and commas, as shown below. Similarly to strings, we can print an entire list, or some individual elements. We can also add elements to a list using **append**, and sort a list using **sort**.

```
names = ["Harry","Ron","Hermaione"];

#Print the entire list:

print(names)

#Print the second element of the list:

print(names[1]);

#Add a new name to the list:

names.append("Draco")

#Print the new list

print(names)

#Result = ['Draco','Harry','Hermaione','Ron']

```

# **TUPLES**

**:Ordere: Yes**
**Mutable**: No

**Tuples** are generally used when you need to store just two or three values together, such as the x and y values for a point. In Python code, we use parentheses:

`point = (12.5, 10.6)`

# **SETS**

**:Ordered:No**
**Mutable**: N/A

**Sets** are different from lists and tuples in that they are **unordered**. They are also different because while you can have two or more of the same elements within a list/tuple, a set will only store each value once. We can define an empty set using the **set** function. We can then use **add** and **remove** to add and remove elements from that set, and the **len** function to find the set's size. Note that the **len** function works on all sequences in python. Also note that despite adding **4** and **3** to the set twice, each item can only appear once in a set.

**Create an empty set**
s = set()

**Add some elements**
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
s.add(6)

#Remove 2 from the set.
s.remove(2)

#Print the set:
print(s)

#Find the size of the set:
print(f"The set has {len(s)} elements.)
