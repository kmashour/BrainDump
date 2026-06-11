---
tags:
  - GIT
Type: Reference Note
source: https://git-workshop.tecladocode.com/docs/what_is_a_commit
page:
links:
Folgezettel:
---
## Initialize a Git Repo
```
git init
```
## staging environment 

git add . or just specify what you want to add git add modules/app.py
```git
git status

On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   app.py
        modified:   models/user.py

```

unstage user.py
```git
git reset HEAD models/user.py
```
But changes are untouched in the working area 

```git
git checkout -- models/user.py
```
To discard changes in the working directory, first make sure a file is not in the Staging Area. Then, run this command

`--` It ensures that the following argument, `models/user.py`, is interpreted as a file path and not a branch name or other command option


## Undo Local commits 

`git revert` undo the changes of a previous commit and creates a new commit this is a ==safe undo==
`git reset` This is not a **safe undo**. It is not possible to bring back your commit after it's been deleted
	- You are sure you never want the commit you're deleting again.
	- You are not sharing the repository with others.
`git log` you use it to choose which hash you want to revert to 

revert is preferred all day long  
```git
git revert ae77aedd
```

## Setting up Local Repo with Remote Repo

Link remote Repo with the local Repo
`git remote add origin https://github.com/yourusername/your-repo.git`

upload(pushing) commits to remote repo 
`git push -u origin main # or master`

## Pulling from remote to local 

if the local repo became out of sync with the local one 

`git pull`


## To start of a new device 

`git clone https://github.com/yourusername/your-repo folder_name`
This will download the repo in a specified directory
or
`git clone https://github.com/yourusername/your-repo `
This will download the repo in your current directory 

## Branching
`
`git branch`
shows which branch Iam on
### Creating and Switching to a New Branch (Recommended)

`git switch -c <new-branch-name>`
Modern approach

`git checkout -b <new-branch-name>
Old way 
### Creating a branch 
`git branch feature/new-design`
#### switching to a created branch 
`git checkout <branch-name>`
`git switch <branch-name>
`



![[1_two_branch_same_commit-0aa676411f3fc4ef87c7393f9ffc2daa.png]]

There's actually a third label on the current commit called `HEAD`. This label is always on the commit you're on at any given point in time.

![[2_one_branch_ahead-e4b4c7a4b14e9ca7ae1cb3484dc65dde.png]]

Notice that the `master` branch is still at `C3` because we committed in `signup_web`.


![[3_diverging_branches-625bc24e970677ca60ae630581f737aa.png]]

f we go back to the `master` branch and commit there, the branches would now diverge:
- `master` would get `C5`; and
- `signup_web` would not (and still be on `C4`).

## Merging branches 

`git checkout master`
`git merge signup_web
### What if someone else made commits in = `master`
![[1_merging_branches-55f52406fec58b2552c21aa7b6916be7.png]]

Well its same steps as before

```
git checkout master
git merge signup_web
```


However, if both you and the other developer made changes to the **same lines in the same files**, you're going to encounter a **merge conflict**.
That's when Git gets confused because two commits changed the same file at same time, and it doesn't know which one to pick...

## Merge Conflicts 

Study case 
https://git-workshop.tecladocode.com/docs/merge_conflicts

## Stashing 
https://git-scm.com/book/en/v2/Git-Tools-Stashing-and-Cleaning

`$ git stash
if my work is not yet ready I can stash it to my workspace clean and finish what I want from the remote repo then unstash it and start where I left 
- Maybe the changes you've made so far are incomplete, and wouldn't make sense on their own.
- Or maybe you want to pull some changes from the remote repository that someone else has made, but you don't want to make a commit just in case there are merge conflicts.

```
$ git status
# On branch master
nothing to commit, working directory clean
```

`git stash apply`
To unstash and bring back the changes 

`git pull` then `git stash` are used to bring updates from remote repository 

`git stash list` 



## working with Github Forking and PR 
https://git-workshop.tecladocode.com/docs/working_with_github