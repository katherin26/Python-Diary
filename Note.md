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
