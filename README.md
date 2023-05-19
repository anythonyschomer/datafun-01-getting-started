# datafun-01-getting-started

> Get started with Python for data analytics

We assume no prior programming experience and that you want to 
get productive as quickly as possible.

## IMPORTANT

When working with computers, commands, and Python:

- **Spelling** is critical
- **Capitalization** is critical
- **Spacing** is critical

Computers are pedantic. When things don't work, check spelling, capitalization, and spacing first.

-----

## On the Web (GitHub / Fork)

### Sign Up for GitHub

GitHub is a code hosting platform that manages a vast number of programming projects. 
Join over 100 million developers and browse over 28 million public repositories.

1. Sign up for a free account with [GitHub](https://github.com/).
1. While logged in, you can create/delete your own repositories (project folders). 
1. You can browse public repos - and if you see something you like, you can grab it and copy it into your account.
1. It's called forking (forking just means copying a repo from one account to another).

### Fork Some Free Code

Fork this repo (copy it into your GitHub account)

1. Open a browser (Chrome is recommended) to the URL of this repo: <https://github.com/denisecase/datafun-01-getting-started>.
1. Look at the URL - note the username is denisecase.
1. Look at all the options available for a repo. 
1. Find and click the **Fork** button up top.
1. Keep the defaults and click 'Create Fork'. 
1. When it finishes, check out your new repo. Note the URL and the username (it should be yours).
1. Explore!  GitHub is pretty fun and easy to use. You got it once you can get it again. You can delete your fork and fork it again. Be courageous and try the + in the upper right, and check out the tabs.

-----

## On Your Machine (Install Git, Python, and VS Code)

Install three important tools on your machine: 
[Git](https://denisecase.github.io/datafun-central/tools/git/index.html), 
[Python](https://denisecase.github.io/datafun-central/languages/python/index.html), and 
[VS Code](https://denisecase.github.io/datafun-central/tools/vs-code/index.html).

### Install Git (for managing code and data files)

1. Installing new tools from the web can be a bit painful, but it's a very valuable, widely-used skill. 
1. Read a bit about Git at <https://git-scm.com/>.
1. DO NOT install GitHub Desktop (we'll use VS Code instead) - see the official instructions for your operating system. 
1. Install Git by clicking the recommended download button for your machine. "Standalone installer 64 bit" is a common choice on Windows.
1. This guide has more information (do NOT install GitHub Desktop): <https://github.com/git-guides/install-git>.
1. We typically verify each installation by checking the version with a simple command.  
1. Open a new PowerShell window (on Windows/Mac) or Terminal (Mac/Linux) and type the following, then hit return/enter.

  ```shell
  git version
  ```

### Configure Git with your name and email. 

1. In the commands below,
1. Change "John Doe" to your name.
1. Change johndoe@example.com to your email (the one you used for GitHub).
1. Open PowerShell or Terminal and configure your global username.
1. Configure your global email address.
1. Verify your global username.
1. Verify your global email. 

  ```shell
  git config --global user.name "John Doe"
  git config --global user.email johndoe@example.com
  git config user.name
  git config user.email
  git config --list
  ```

Git is widely used in industry and academia. Congratulations on getting started with this popular tool! 

### Install Python 3

Download and install Python 3.

1. Read a bit about Python at https://www.python.org/ 
1. Click "Downloads" tab and choose (or accept) the best recommendation for your machine. 
1. Start the executable. Important: Click "Add python.exe to PATH" and continue.
1. Verify your installation by checking the default (usually most recent) Python version. 
1. You may have several versions of Python installed on your machine (3.10, 3.11, even earlier if needed for work).

  ```shell
  python --version
  ```

Install some essential Python packages into the default Python environment.

```shell
python -m pip install --upgrade pip build setuptools wheel 
python -m pip install --upgrade black ruff
python -m pip install --upgrade ipykernel jupyterlab
```

### Install VS Code Editor

Download and install VS Code. 
Python is not the only language we need - we'll use Markdown and SQL too.
VS Code is a great editor for many languages. 

1. Read a bit about VS Code at <https://code.visualstudio.com/>.
1. Click "Download" and follow instructions for your machine.
1. If you need more help, use the official VS Code docs. For example, additional Mac instructions are [here](https://code.visualstudio.com/docs/setup/mac).

-----

## On Your Machine (Get code, Run it, Modify it, Push it Back)

### Get Your Code Down To Your Machine

Clone your new GitHub repo down to the Documents folder on your local machine. 

1. Open VS Code. 
1. From the menu: select View / Command Palette.
1. Start typing Git: Clone and select it from the options. Click GitHub repo.
1. Provide the URL for **your** new GitHub repo. It should have YOUR GitHub username in the URL.
1. When it asks where to put it, select your Documents folder.
1. The first time you clone, you'll be guided through a process to sign into GitHub from VS Code. It's may be a slight challenge, but it's just this once. 
1. Follow the recommendations in VS Code. 
1. When complete, verify you have a new folder in your Documents directory: `Documents/datafun-01-getting-started`
1. You don't need VS Code to clone a repo, but most students prefer it. To clone without VS Code, follow instructions [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

### Execute Python Scripts

With your newly cloned repo folder open in VS Code, we can start exploring Python.
Get VS Code ready for Python. 

1. Click acquainted.py (or any .py file).
1. VS Code will ask if you want to install the recommended extension. 
1. Of course! Check the recommendation (Python by Microsoft). 
1. Consider the stars and downloads. Does it look good?
1. Click Install. 

Execute each script in alphabetical order.

1. Click the Explorer (top left) icon to see your files again. 
1. Click menu View / Terminal to open a terminal window.
1. There are many ways to execute scripts. 
1. Type the following commands to execute each script. 

  ```shell
  python acquainted.py
  python basic_expressions.py
  python basic_functions.py
  python circle_calc.py
  python data_io.py
  python easy_stats.py
  ```

Helpful hint: Hit the **up arrow** in the terminal to get the last command. Edit as needed and hit return.

On some machines, you may need to use `python3` instead of `python`.
On some machines, you may need to use `py` instead of `python`.
If all else fails, try clicking the play button 
in the upper right corner of the editor window or 
right-click on the file and select "Run Python File in Terminal".

Verify things are working - when successful, 
running any of these scripts will create a new log file.  
Log files provide information about your Python environment and can be helpful when things don't work

### Read and Modify Python Scripts

Read each script in alphabetical order.

1. Each Python script has a .py file extension.
1. In the Explorer, click each script to open it in the editor. 
1. Read the script.
1. You do NOT need to fully understand the code. 
1. Instead, just see which parts you can figure out. 
1. By the end of the course, these will be very familiar.

Try the TODOs

1. When you see a TODO comment, try to do what it suggests.
1. Treat these as mini puzzles. Creating small syntax errors and fixing them are a great way to learn. 

Optional: Customize the code

1. Edit the author to your name. 
1. Try some new things. 
1. Your repo is YOURS to do with as you like - we'll share them in class. 

Keep .gitignore and the datafun logger as they are

1. .gitignore is a special file that tells Git what to ignore. Keep it as is.
1. util_datafun_logger.py is our custom logger. Keep it as is.

### Commit Your Changes and Push Back Up to GitHub

After making changes to the code, you'll want to get it back up to the cloud (GitHub) where it's safe. 

1. In VS Code, look for the "Source Control" icon down the left side (mouse over to find the right one). 
1. Click "Source Control" icon. 
1. Enter a short message describing the work you did, e.g., "initial exploration"
1. Note the Commit button has a drop-down - select "Commit and Push" (or "Commit and Sync") to send your changes back up to GitHub.

-----

## Skills Checklist

This README.md file is written in [Markdown](https://denisecase.github.io/datafun-central/languages/markdown/index.html) - a super simple markup langage, widely used in Python notebooks.

Every repo has a README.md. Modify this file as you like. 
Delete parts you don't need anymore. 
Add your own notes in the README.md file. 
Markdown skills are valuable. 

If you like, change the open boxes [ ] below to checked boxes [x] as you gain new skills.

- [x] Sign up for GitHub
- [x] Fork a repo into your GitHub
- [x] Install Git
- [x] Configure Git
- [x] Install Python 3
- [x] Install VS Code 
- [x] Clone your new GitHub repository/repo down to your machine
- [x] Explore your local repo in VS Code
- [x] Execute Python scripts
- [x] Edit Python scripts
- [x] Commit changes (with a message!) and push/sync back up to GitHub for sharing

Each time you make changes on your machine, commit and push back up to GitHub. 
When starting it's best to make small changes locally and commit and push often.

## Helpful Resources

<<<<<<< HEAD
VS Code makes it pretty easy. 

1. On the VS Code side panel, click the source control icon (look for a blue bubble with an number in it).
1. Important! Above the Commit button, it will say "Message". You must include a message. 
1. In that message input box, type "initial setup".
1. Click the blue "Commit" button and follow instructions to Commit your code and sync/push it up to your GitHub repo. 

Verify: Open a browser to your GitHub repo and see if the files have appeared. 

In addition to the original files, you should have one or more new files and an edited Markdown file. 

If not, return to VS Code and edit/execute files as needed.

If your computer hangs because you forget the a commit message, 
just enter your message in the top line of the file it shows in the editor.
Then click the checkmark in the upper right to close that file and save your commit message.
"Sync your changes" to push. 

If we didn't use VS Code, the commands are pretty easy in Git Bash or Terminal as well:


```
git add .
git commit -m "initial setup"
git push origin main
```

✅ Git is a powerful tool, widely used in industry. Your skills can facilitate onboarding.


## Checklist

Change the open boxes [ ] below to checked boxes [x] as you complete the tasks.

- [x] Task 1. Sign up for GitHub
- [x] Task 2. Install (and configure) Git
- [x]  Task 3. Install Miniconda3 (or other)
- [x] Task 4. Install VS Code
- [x] Task 5. Install VS Code Extension: Python
- [x] Task 6. Install VS Code Extension: GitHub Repositories
- [x] Task 7. Fork this repo into your account
- [x] Task 8. Clone your new GitHub repo down
- [x] Task 9. Explore the repo in VS Code
- [x] Task 10. Execute a Python script.
- [x] Task 11. Check the boxes (edit a Markdown file)
- [x] Task 12. Commit changes (with a message!) and push to GitHub

Finally - after your initial commit and push, you can check the last box. 
Check the box, commit your changes (with a message!), and push/sync again. 


## Computer View Settings

Update important view settings as needed.

### View File Extensions

When negotiating files and folders, you should be able to view file extensions (e.g, .py, .md). 
If these aren't visible, seach for how to view file extensions on your operating system. 

### See Hidden Files

You may want to see hidden files. 
Find this option in the Windows File Explorer ribbon.
Toggle it in Mac Finder with Command Shift . ("command shift dot").

Your repo has a hidden .git folder that maintains changes to your code.
Do a web search to learn more as needed.

## Tips and Troubleshooting

### Issue: VS Code - No Source Control Icon

Suggestion: If you're in VS Code, and you don't see the Source Control icon with a blue bubble, right-click on the sidebar icons, and make sure "Source Control" is checked.  

### Issue: VS Code - Conda Error on Execute

Suggestion: If you're in VS Code, On Windows, trying to run a script or execute a conda command and you get an error "conda: The term 'conda' is not recognized as a name of a cmdlet, function, script file, or executable program." Your VS Code terminal is likely Powershell (look for a the PS before your path). We want to switch it to "Command Prompt" for Python commands. From the VS Code menu / View / Command Palette. Start typing 'Terminal: Select Default Profile' until it appears, click it and change from Powershell to Command Prompt.

### Issue: VS Code wants to install Pylance extension

Suggestion: Sure. If VS Code suggests an extension, it's often good to go ahead and try it. 
Read up a bit if curious, but the suggestions are usually helpul. 

### Issue: VS Code Extension for GitHub - which one?

Suggestion: VS Code Extension: [GitHub Repositories](https://marketplace.visualstudio.com/items?itemName=GitHub.remotehub) seems to work well and may especially good for beginners. 
If you get a recommendation to use [GitHub Pull Requests and Issues](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github), you can try that. It might be more suitable for experienced developers. [Here's a good article for getting started](https://www.techrepublic.com/article/add-github-vs-code/). You're encouraged to share your thoughts in the discussions.

## Additional Resources

1. For more information about editing Markdown task lists, see [how to mark a task complete](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/about-task-lists).

1. For more information about Git in VS Code, see [Using Git source control in VS Code](https://code.visualstudio.com/docs/sourcecontrol/overview).

1. For more information about editing Markdown in VS Code, see [Markdown and Visual Studio Code](https://code.visualstudio.com/docs/languages/markdown).
=======
Whether working on a home or a project, powerful tools are worth learning. 
Mastering VS Code can provide many happy returns.
>>>>>>> c5486520ca7d79488ccb93343415e51f0764f9b9

1. Scan the article [Programming Languages in VS Code](https://code.visualstudio.com/docs/languages/overview) 
1. Scan the article [Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)
