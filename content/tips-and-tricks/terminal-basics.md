Title: Terminal Basics
Slug: tips-and-tricks/terminal-basics
Category: Tips & Tricks
Tags: bash, terminal
Date: 2018-10-13
Modified: 2018-10-13

#### Things to install (optional)
If you're on a Mac, installing [iTerm2](https://www.iterm2.com/) will make your life easier with improved search and autocomplete. Using [oh-my-zsh](https://ohmyz.sh/) on top of this is enough to make you weep tears of joy; [this guide](https://hackernoon.com/oh-my-zsh-made-for-cli-lovers-bea538d42ec1) shows the range of cool stuff it can do.

#### What about Windows?
Save yourself some pain and just don't bother with the Command Prompt or Powershell. Windows commands are awkward and unintuitive and much harder to find support for.

You could try using the [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10) to get used to the terminal, but you'll probably want to install Linux for a native experience eventually.

#### Show the current directory
*Note: You can run terminal commands from a notebook by prefixing them with an exclamation mark (!). This isn't required when running them directly in the terminal.*


```python
!pwd
```

#### Show files in the current directory


```python
!ls
```


```python
#Include hidden files in output
!ls -a
```


```python
# Include hidden files with extra information
!ls -al
```

#### Change directory


```python
!cd subdirectory
```


```python
# Go up a level
!cd ../
```


```python
# Go to home directory
!cd ~
```

#### Moving and renaming


```python
!mv my_file.txt subdirectory/my_file.txt
```


```python
# Rename a file
!mv my_file.txt new_name.txt
```

#### Creating and editing a new file


```python
!touch new_file.txt
```


```python
# Nano is a terminal-based text editor
!nano new_file.txt
```

#### Creating a new directory


```python
!mkdir my_new_directory
```


```python
# Add a new subdirectory
!mkdir my_new_directory/subdirectory
```

#### Deleting files
**Warning**: Use these commands with caution as deleted files are unrecoverable.


```python
!rm new_file.txt
```


```python
# Remove all directories and subdirectories - DON'T RUN THIS IN YOUR ROOT DIRECTORY
!rm -r my_new_directory
```
