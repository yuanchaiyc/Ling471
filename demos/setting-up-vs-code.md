## VS Code settings

<img width="199" alt="Screen Shot 2021-04-22 at 1 42 38 PM" src="https://user-images.githubusercontent.com/10963114/115790461-99b4cd00-a37b-11eb-8049-be20953f9514.png">


### Settings for running programs under the debugger.

Visual studio code is mainly for debugging your code. It is hardly the best choice to simply run programs which had already been debugged. But debugging is crucial for programming, and so in this class I am assuming that most students mostly work "under the debugger", or in the debugging mode.

In VS Code, the debugging mode is accessed via the appropriate menu, but often times you also need to modify the debugging ("running") configuration. The debugging configurations are stored in a file called `launch.json`. That file is created automatically when you create your first configuration, and is located in the folder named `.vscode`.
You need to modify that file to do certain things in VS Code. For example, you might want to pass your program some arguments. For that, you need to specify the `args` variable in the configuration which you intend to use:

```
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "args": [
                "/Users/olzama/Teaching/Ling471/datasets/IMDB/aclImdb/train/pos/1_7.txt"
            ]
        }
    ]
}

```

The `args` variable specifies a list of arguments. In the example above, there is only one argument passed to the program.

In order to be able to **import modules** in the debugging mode in VS Code, you need to perform 2 steps:
1. Create a file called `.env` and put it inside `.vscode`. In that file, write the command adding the path to the **folder containing the module** to PYTHONPATH. For Mac OSX:

`PYTHONPATH=${PYTHONPATH}:/Users/olzama/Ling471/projects/modules`

The command above means **appending** a new path to the existing set of paths stored in PYTHONPATH (it may already be nonempty, depending on your environment). 
For Windows, use semicolon (;) instead of colon (:). 
2. In `launch.json`, you also need to specify the `env` variable:

```
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "env": {
                "PYTHONPATH": "/Users/olzama/Ling471/projects/modules"
            }
        }
    ]
}
```

The above two steps should make the modules which are stored under `/Users/olzama/Ling471/projects/modules` available for import in the debugging mode.

### Settings for non-debugging mode.

Debuggers slow things down. Often times, even as you are working in VS Code, you want to be able to run things quickly without starting the heavy-weight debugger. You can still pass arguments to the program, but you need to do it in another file. The file is called `settings.json` and is located under `.vscode` again.

To pass arguments in non-debugging mode, you need to additionally pass **the program name** as the very first argument. This is confusing because you do not need to do that for the debugging mode. But ultimately it makes sense if you remember the convention for main() arguments (sys.argv). The first element of the argv array is the program name.

```
{
    "python.terminal.launchArgs": [
        "olzama_assignment2.py",
        "/Users/olzama/Teaching/Ling471/datasets/IMDB/aclImdb/train/pos/1_7.txt",        
    ]
}
```

To be able to add modules to PYTHONPATH, you need to add the path to the folder containing the modules to `settings.json` as follows:


```
{
    "terminal.integrated.env.osx": {
        "PYTHONPATH": "${env:PYTHONPATH}:/Users/olzama/projects/modules",
    }
}
```

Put together, the two settings would look like this:

```
{
    "python.terminal.launchArgs": [
        "olzama_assignment2.py",
        "/Users/olzama/Teaching/Ling471/datasets/IMDB/aclImdb/train/pos/1_7.txt",        
    ],
        "terminal.integrated.env.osx": {
        "PYTHONPATH": "${env:PYTHONPATH}:/Users/olzama/projects/modules",
    }
}
```

You can create `settings.json` outside of VS Code or you can bring it up from within VS Code by pressing `command+shift+p` and choosing "Workspace settings".
