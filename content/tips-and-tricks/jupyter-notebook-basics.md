Title: Jupyter Notebook Basics
Slug: tips-and-tricks/jupyter-notebook-basics
Category: Tips & Tricks
Tags: jupyter, notebook, lab
Date: 2019-04-02
Modified: 2019-04-02

### Getting started
Start the notebook server by opening a terminal and running `jupyter lab`. The notebook server will start and should open in your web browser automatically.

If you get an error, try running `pip install jupyterlab` first.

**Note**: Some older tutorials will mention `jupyter notebook`. This is just an older version of what we'll be using. Most things below will work there too, but I'd recommend using Jupyter Lab as it will receive more support in future.

### Opening a notebook
The panel on the left is like Explorer in Windows or Finder in MacOS. You can move between folders and view all your files here. 

By default, the launcher page will open. You should see a range of icons that let you create new files (click *File* → *New Launcher* if you don't see this). To create a new notebook, click the *Python 3* under the *Notebook* section.

### Running code
Now you've opened a notebook, it's time to run some code. The first thing you'll see is an empty cell, like this:


```python

```

Type a command and hit shift and enter to run it and move to the next cell:


```python
print("Hello World!")
```

    Hello World!


Most of the time you'll want to use shift-enter to run a cell but there are other ways: 
- control-enter runs the cell without moving to the next one
- option-enter (alt-enter on Windows) runs the cell and inserts a new one below

### Viewing documentation
If you want to find out what a function does, put a question mark in front of it and run the cell, like this:


```python
?print
```


    [0;31mDocstring:[0m
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
    [0;31mType:[0m      builtin_function_or_method



You can also view this quickly while typing by pressing shift-tab.

### Command palette
There are loads of commands for moving cells, editing notebooks and changing your Jupter Lab settings. You can search through them by bringing up the command palette with cmd-shift-C (control-shift-C on Windows).

### Shortcuts
The command palette shows the shortcut if a command has one. To use them, enter command mode by pressing escape, then type the command. Here are a few that I regularly use:
- **A**: insert cell above
- **B**: insert cell below
- **X**: cut cell
- **C**: copy cell
- **V**: paste cell
- **DD**: delete cell
- **Z**: undo last action
- **II**: interrupt execution (if something is taking longer than expected)
- **00**: restart (if things go badly wrong!)

### Saving a notebook
This is done automatically most of the time. If you want to be sure, use cmd-S (control-S on Windows) to save your work.
