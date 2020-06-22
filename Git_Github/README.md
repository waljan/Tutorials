# Git and GitHub
Introductory tutorial on git and GitHub.


## Git
Git is a version control  system that helps managing files within projects. It keeps track of the entire history of things that you are working on. It tracks all changes in the projects and allows us to revert back to a previous version. It also allows to work with several people on the same project, without disturbing each other. Team members can work on different features and easily merge the changes.


## Github
GitHub is a Web Service for version control using Git.


## Basic Terminology
**Working Directory:** The directory you are working in and in which you add, modify and remove files. The changes need to be staged and commited to Git in order to track the project history.

**Git Repository:** A Git Repository is a folder that you’ve told Git to help you track file changes.

**Remote Repository:** a copy of your local Git repo that is saved on a server.

**Branch:** A branch is an independent line of development (like a new copy of the repo in which you can experiment without any risk)

**Master:** The default development branch. Whenever you create a git repo, a branch named “master” is created which becomes the default active branch.

**Fork:** Copy the repo of another user to your account. This is done in order to contribute to a project of another user (to which you would not have writing permission).

**Clone:** Download a repository from GitHub

**Commit:** save changes permanently on local Git repository

**Gitignore:** a .gitignore file specifies all folders/files that should not be staged and commited


## Installation on Ubuntu

```
sudo apt-get update
sudo apt-get install git
```


## Setup and Configuration

Get location of git:
```
which git
```

Get the version of git:
```
git --version
```

Assign username and email:
```
git config --global user.name "[github-username]"
git config --global user.mail "[gitub-mail]"
```

Check configuration:
```
git config --list
```


## Create new Repository / Download Repository
First create a Github Repository (with Readme file) and copy the url.


Clone (download) a repository from github:
```
git clone [url]
```


## Create Repository from existing Folder
First create an empty Github Repo (without Readme file) and copy the url.


Turn current directory into a local git repository:
```
git init
```

Connect local repository with remote repository (github repository). By default the remote repo is called origin.
```
git remote add origin [url]
```

Move files from the working directory to the staging are. Files within the staging area will be commited to the local git repo with the next commit.
```
git add .
```

Commit the files that are staged to your local git repo (-m for adding a comment). This adds the staged files to the project history.
```
git commit -m “initial commit”
```

Push the code to the master branch of the remote repository (called origin). This saves the changes on the GitHub server.
```
git push origin master
```

## Branches
Branches can be used to isolate work without affecting other branches. In the new branch you can work in isolation from changes that other people are making to the repository. Branches are used to develop features, fix bugs and to safely experiment with new ideas.


List all existing branches (a “*“  will appear next to the currently active branch)
```
git branch
```

Create a new branch (eg. in order to work on a new feature):
```
git branch [branch_name]
```

Switch to the specified branch:
```
git checkout [branch_name]
```

### Delete failed Branches
Delete the local copy of your branch:
```
git branch -D [branch_name]
```

Delete the remote branch:
```
git push origin –delete [branch_name]
```

### Merge Branches
Before merging, make sure that both branches are up-to-data with the latest remote commits.


Switch to the branch that should be updated (receiving branch):
```
git checkout [branch_name]
```

Fetch downloads latest changes from the remote repository named “origin”, but does not integrate any of this new data into your working files. It is a very safe way to get a view on the things that happened on the remote repo.  
```
git fetch origin
```

Updates the current branch with the latest changes from the remote server. Thus, pull downloads and integrates data from the remote into your local repo. You should only pull if you do not have any uncomitted local changes.
```
git pull origin master
```

Merges (combines) the specified branch with the current branch (the current branch is the one that gets updated). Brings two histories back together again.
```
git merge [branch_name]
```

Stop merging. To return to the state before you started the merge.
```
git merge --abort
```

Undo a completed merge (eg. in case you have made a mistake while resolving a conflict).
```
git reset --hard 
```

Delete the specified branch after successful merging. Only works if the branch has been merged to the root branch (otherwise you get an error message)
```
git branch -d [branch_name]
```

### Merge Conflicts
If the two branches you are trying to merge both changed the same part of the same file, Git won’t be able to figure out which version to use. The merge will stop right before the merge commit so that you can resolve the conflicts manually.


Shows which files need to be resolved
```
git status
```

Stop merging. To return to the state before you started the merge
```
git merge --abort
```

The affected file contains visual indicators that mark both of the conflicted content. The content before  the ===== marker is the receifvng branch and the part after this is the merging branch (the branch in which you developed a new feature). Resolve the conflict by making the necessary changes.
```
Some content not affected by the conflicts
<<<<<< master
this is conflicted text from master
======
this is conflicted text from feature branch
```

Git add tells git that the conflict has been resolved and git commit generate the merge commit.
```
git add [conflicted_file]
git commit [conflicted_file]
```

## Save changes temporarily
You can temporarily get rid of changes (without losing them) and continue working on them later. This is for example useful if an important bug report comes in which you should fix. Stashing can be useful  before checking out a different branch, before pulling remote changes or before merging a branch.

Put away the local changes so that you have a clean working copy. Discard all local changes, but saves them for later:
```
git stash
```

Get an overview of your current stashes:
```
git stash list
```

This applies the newest stash and removes it from your clipboard:
```
git stash pop
```

Apply the specified stash, but it will remain saved:
```
git stash apply [stash_name]
```

Delete the specified stash:
```
git stash drop [stash_name]
```

## Handling Files
Newly created files first need to be added to the staging area before they are commited to the local git repo. The files that are in the staging will be commited to the local git repo with the next commit. Files that have been commited can be pushed to the remote repo (github).

Create a  new branch:
```
git branch [branch_name]
```

Show modified files in your working directory that are staged for your next commit. Also shows if there are any merge conflicts (unmerged paths).
```
git status
```

Adds changes in the working directory to the staging area:
```
git add
```

Unstage a file while retaing the changes in the working directory:
```
git reset [file_name]
```

Delete the file from the Git repository AND from local file system and push the changes to the remote repo:
```
git rm [file_name]
git commit -m “remove file_name”
git push origin master
```

Remove file from the Git repo and NOT delete it from the local file system:
```
git rm --cached [file_name]
git commit -m “remove file_name”
git push origin master
```

Commit staged files to the local git repository:
```
git commit -m [message]
```

Shows all the commits in one line each:
```
git log --oneline
```

Pull remote repo:
```
git pull origin master
```

Push changes:
```
git push origin master
```







