git revert types with example

The `git revert` command **undoes changes by creating a new "inverse" commit** rather than erasing or altering history. This makes it perfectly safe for public, shared repositories. [[1](https://www.atlassian.com/git/tutorials/undoing-changes/git-revert), [2](https://www.w3schools.com/git/git_revert.asp?remote=github), [3](https://www.geeksforgeeks.org/git/how-to-revert-a-commit-with-git-revert/)]

While `git revert` is a single command, you can use it in different ways depending on your objective: **reverting a standard single commit, staging changes without committing, or reverting a complex merge commit**. [[1](https://git-scm.com/docs/git-revert.html), [2](https://www.w3schools.com/git/git_revert.asp?remote=github)]

---

1. Standard Commit Revert (Single Commit)

This is the most common use case. It target a specific regular commit, inverts its contents, and automatically creates a new commit. [[1](https://www.cloudbees.com/blog/git-revert-explained), [2](https://www.atlassian.com/git/tutorials/undoing-changes/git-revert)]

- **Command:** `git revert <commit-hash>`
- **When to use:** When you need to undo a specific bug or feature added in a past standalone commit without altering the rest of your history. [[1](https://www.youtube.com/watch?v=FoiVbElm8H8&t=177), [2](https://www.geeksforgeeks.org/git/how-to-revert-a-commit-with-git-revert/), [3](https://www.cloudbees.com/blog/git-revert-explained)]

Example:

Imagine you have three commits on your branch, and `Commit B` added a faulty file named `broken_feature.js`:

text

```
A --- B (Added broken_feature.js) --- C (Current HEAD)
```

Use code with caution.

1. Run `git log --oneline` to find the hash of Commit B (e.g., `b1a2c3f`).
2. Execute the revert:
    
    bash
    
    ```
    git revert b1a2c3f
    ```
    
    Use code with caution.
    
3. Your text editor will pop up asking for a commit message. Save and close it. Your project history will now safely include a brand new commit (`D`): [[1](https://www.youtube.com/watch?v=XJqQPNudPSY&t=173), [2](https://www.youtube.com/watch?v=Q5T0TeC9zbE&t=48), [3](https://www.w3schools.com/git/git_revert.asp?remote=github)]

text

```
A --- B --- C --- D (Revert "Added broken_feature.js")
```

Use code with caution.

The history is preserved, but `broken_feature.js` is gone. [[1](https://www.youtube.com/watch?v=Q5T0TeC9zbE&t=48), [2](https://www.atlassian.com/git/tutorials/undoing-changes/git-revert)]

---

2. No-Commit Revert (Staged Reversion)

This variation applies the exact inverse changes of a commit directly to your working directory and staging area, but **stops short of creating the new commit**. [[1](https://www.atlassian.com/git/tutorials/undoing-changes/git-revert), [2](https://git-scm.com/docs/git-revert.html)]

- **Command:** `git revert -n <commit-hash>` (or `--no-commit`)
- **When to use:** When you want to revert multiple past commits at once into a single new commit, or when you want to inspect and test the reversed code before finalizing it. [[1](https://www.atlassian.com/git/tutorials/undoing-changes/git-revert), [2](https://git-scm.com/docs/git-revert.html), [3](https://www.cloudbees.com/blog/git-revert-explained)]

Example:

If you want to undo changes from two separate commits (`a1b2c3d` and `e5f6g7h`) but group them into a single clean commit message:

bash

```
git revert -n a1b2c3d
git revert -n e5f6g7h
```

Use code with caution.

Your files will change locally and sit in your staging area. Once you test the application, you can finish it manually: [[1](https://www.atlassian.com/git/tutorials/undoing-changes/git-revert), [2](https://git-scm.com/docs/git-revert.html)]

bash

```
git commit -m "Fixing regression by reverting features X and Y"
```

Use code with caution.

---

3. Merge Commit Revert (Mainline Reversion)

Reverting a merge commit is fundamentally different from a regular commit. Because a merge commit links two branches together, Git has no way of knowing which side of the merge should be treated as the "mainline" history. You **must explicitly specify the parent number** using the `-m` flag. [[1](https://git-scm.com/docs/git-revert.html)]

- **Command:** `git revert -m <parent-number> <merge-commit-hash>`
- **When to use:** When a branch feature was merged into `main` or `develop` via a PR, and it immediately broke production, requiring you to undo the entire merge. [[1](https://git-scm.com/docs/git-revert.html)]

Example:

You merged a feature branch into your main branch, resulting in merge commit `m98765`.

- Parent 1 is your main branch history.
- Parent 2 is the feature branch you pulled in.

To strip out the feature branch changes and roll back to the main branch's state (Parent 1): [[1](https://git-scm.com/docs/git-revert.html)]

bash

```
git revert -m 1 m98765
```

Use code with caution.

> ⚠️ **Important Note on Merge Reverts:** Reverting a merge commit does not delete the history of the feature branch. If you try to merge that same feature branch back in later after fixing it, Git will think those changes are already there and ignore them. To fix this, you must first **revert the revert commit** before re-merging.

---

Quick Comparison Summary

|Revert Type|Flag Used|Creates New Commit Immediately?|Best Use Case|
|---|---|---|---|
|**Standard**|None|✅ Yes|Quick fix for an isolated mistake in history.|
|**No-Commit**|`-n` / `--no-commit`|❌ No (Saves to staging area)|Grouping multiple reverts together or checking code before committing.|
|**Merge Commit**|`-m <parent-number>`|✅ Yes|Stripping an entire broken branch integration out of your main line.|

Are you currently trying to fix a **broken production branch**, or are you just looking to clean up a **local typo**? I can give you the exact steps if you let me know whether the commit you want to revert is a **normal commit** or a **merge commit**.

- [](https://git-scm.com/docs/git-revert.html)
    
    ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAAPCAYAAAA71pVKAAACf0lEQVR4AWyQ20tUURTG115773OckbKmMoygRvLJG14g6yHMSxYV3RCCoJf+iAhSZx6DXgNfI/ApeizJxAuEZUokZRSDFZriQxao45yzL6u9JxItD2efc/ba3+9b51sIO1xTTSDz5yuvrl+ofJw/e+QKtYLYQQb/wQSA1fvTLYEQt5MyvFYSJO6a0qouOncs/NdgG7x48VByvStdqwEqgGCOCH4CZ3UoeCZC1jF/4nBiq8Em7A/KdNguA9HPpbixFtsn+UjdU9p8IIRG4QwOpBJtXvfXoAh/aT1aktobtAdS9grOWyTHUxyheln96DfaDIChFY6s+Y9B0Ob13gDJDWdfgnVKzjMub3NsLFiiXZyzphTuqSei9wQ0QpaWEaFBCJmpSGKH53DlQPqyK2SJsSbtaHcDMMY5YjkBO6kYNSilB2Ot7rsI75BjvRQyu1aevoQG8DpnvEERgAUA9yo+LJGNwIYCxRnDxcHVX/FAQZtJJ4qdQSNj2I3WsIfW0mvBivGLsDfwOwQEKXiIDLqD3cGdUPDjwCAwTm81PcKPQ7mnUaR7rbWvvAED15hAa0OLQGbGGL3k4JoSKW65udQ53RQp0zP9fG4QTwPohe/BqBtUHxFNeAM3oIIi+ry6XnipDeUYkRLIEoZgUivb9+mrHPMcukZQMzsblwGMGR1nXNYJZJhgDDpTZYksMtaOiKE2ZiJWUd880bjXe64I+w/2LBeVAh/Lb0RZsvZNUsi6UhneDIWoJQuTG5oyS8THq5zO6/3ahP3GGywtJkfyBZtRxr51XZMu43S+YDIL34LRraDXb4N9wf/SzIvc8GrB9OYj/WAjVj1lQ7lhX/fnW9dvAAAA//8zWEKcAAAABklEQVQDADlNOhh1xoT5AAAAAElFTkSuQmCC)
    
    Git
    
    Git - git-revert Documentation
    
    Command: git-revert records new commits reversing existing commit changes, requiring a clean working tree. Options: -e/--edit (edi...
    
- [](https://www.atlassian.com/git/tutorials/undoing-changes/git-revert)
    
    ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAAPCAYAAAA71pVKAAAB00lEQVR4AaSQu2sUURTGvzOPe+/uLGZB02RUloAOFmvho7EQg6LYxEdhF7WySa9ImgEbo2Dhv+H/oFa2sRBDIJBUeZCw5LHZbLI7c3LuzE5e7EIglzn3zD33/L7vcB2cYw2Eb79j/+ZXDmwepD8Q3rmKu3ttfNyQDDD1E+gL12I2CXBPkEmHMRZNo3Jm2PUwLFaRAFVy8JQ6qPdz7+tMKS4IOCwhDO6kwP3Rz1ktKxXbKVgGfT5T3dpsjDBQ3GlpfuZ1EYHlXg7FVzTk57d/h/xAvWw2GuPcTXbzYrbfIuDB6PRJ92MwU9Wv1rTWk5SmD1ut5pAArQwFlIz+ygNqx90P4Uvv1yu+CZ74Wtc9pa90dttGRv+P3hKhOid4HH05evkezKRcHWqjXytT8kUgYOYVTtM/IlCMr4jxRgRCeUXRQv4oIzFKZRO8UCVzXRsDyeQqb1sEfhLhX8/cpohTjF/+BmMPmXNZIXAcZ8L1fU8JrE1pQ+nyAnjzFwG/QdhBvjwBJkw7H13+gfkZNDoOxpyEQpfdkN3ujbYuf5+PL27BwycXuEZdhDb2CY9sv9XKYPygZGGKVudiWrKxGFdW1mJq2oa5D7Q9O0XLtm7D9tl+e3cAAAD//yPt8RgAAAAGSURBVAMAc8WRH73ehhkAAAAASUVORK5CYII=)
    
    Atlassian
    
    How to Revert a Commit in Git? | Atlassian Git Tutorial
    
    Command: git revert (inverts changes of a specified commit and creates a new "revert commit" without removing history or moving ol...
    
- [](https://www.cloudbees.com/blog/git-revert-explained)
    
    ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAAPCAYAAAA71pVKAAACAElEQVR4AXxSz6tpURhd+1yEDAz9mJqiJGKgriKDW8pAipn8BYqJkSIRIwMTZWBAGd6ZpAxlakDIwExm7vErvPN99V63d723O+v82Huv71trnS1ZrdZ3BV8Wi+VJMJvNTwK9/wdfCuddej6fnwr0CnC73SDLMq7XKx6PB2gOrwft/5SUNT1tJDidTjSbTdRqNfj9fgghuIiy59WlJzJ3jMfj6Pf7sNlscLlcqFQqoDli/UsByYZKpUI2m8VkMkEkEkEqlcJwOORCJpMJ9/udavyARDNvb28wGo1YLBbsebPZYDAY4HA4QK1W43w+s7q/FTCZAlqtVvD5fIhGo3C73QiFQkgkEggEAuyf7FAuBGpIkIQQnGq9XodOp0O1WkU+n4fdbsflckEwGESpVEKxWEQ6nWaLvxVwZ41Gg9FohEKhgEajwcFtt1vQmM1maLfb2O12yGQyCIfDbIMKMFkIAUmSMJ1O0e122S/ZoCxortPpoFwuY7/fsy0iQhlMVp5M1uv1IJCS0+nEYRkMBg5rvV5zR/qmRsyh2yssl0vulMvl+ND0ej04HA6QCiouhMCfzvg2tFot5vM5+z8ej0gmk/B4PKBQ6SwIIXg3pS3z27cbyaKDMx6PEYvFuKPX60Wr1eI/IASTZer8ofB+FBBCgBSQRGWdM6EDQ4WFELKCj18AAAD//2SIlXkAAAAGSURBVAMABUrzEjCZUHwAAAAASUVORK5CYII=)
    
    CloudBees
    
    Git Revert Explained: Safely Undoing Your Changes
    
    Git revert undoes changes in a project commit history without tampering with it. When reverting, this operation takes the specific...
    
    ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEMAAABDCAYAAADHyrhzAAAQAElEQVR4AeyaZ3sdR5JmI7NwL7wnQQsCoHeiEUnN7OzTs+5fb/e2kaallkTvvbcgQZDw9t49JwGo0d0iZ3e/7TMEkaiqrMzIyMgwb0Qxnzj1n5r/9C//o3n2n/5r8/TZ3zS/+ef/1jzH/TmuJ7/+z6XfdydP/0vTPpvjznzzX5pfn/vX8v6bf/7vfzPPMWd5//9by/v27489e/bEvr17o6e7O9rbO6K1tTUWFhZiYX4+uukbGx2N4eHhaGtri5xSbBkcjNGRUa5bor2tPdo72mPr0FBs37Ejai0tMfHuXczOzX26zfJudjZmP9U+N/dz7/49up9aj/65ufnI165ejRfPn0dfX18cOnQoTpw8EUeOHIlBNtxLX093T3R0dJaNHj92LA4cPFiEMjs7g9DqsR9h7tu3L1ZXVuPRw0fxbmIient7I5rNT7ZmsxGNxifaZ+Z9jqbvPkv3U+tt9MNTrjjJN+Pjcf3Gjbh9504U4bx4EfNoxcrySkxMvIv79+/F3bt348WLl/Hu7dt4hvBevnoV82jPi1cv4tHjx/Hu/USsrK5Ek3/zi4uRcv5sy7mKX2+Z/l9v/x7N8r6qIv0/tEgpcien7im9YnOT79/H02fP4jnC+PjxY8zNzcb0zExMfvgQT588jRs3b8SDhw/pnysbVyiPnzyJFy9fxPT0dDRTREtLLVJOsYqkP9WanL5C+9XGO/n5ZPsM3UZAkfmF/v/lNeA9Ly0voe6tkTlJtaSlaonV1dVoNprRgKD3wbVqqaK1Xo86zbGN1UasrKyUeTUEkKsc8MKcRrnG535SipQ+3T439XPvoPhZuikx4jMtu1mdYFVVMT01FauN1fBUMqebWLm5blPcsnFUEGKrCMEx7e3tdsfyynI0EV5iToPr4tJiodFYn/v310C4ZeKv/PFU/378xnMTrdi4/7Vr8zN0f2Wpv+nSJeSurq5ob2+Lbq5bt26NsbGxGN69O3bu2hUDOFEX1bnaBgYHor+vP3bz3tbP89C2bTG4ZUu01GvR3dNTHPBXJ07EsePHuT8Zh3HGI6NEIyLW12fOlD6d8FfHvwppnjx5Mnbt3BknmHP06NHYy/o65ZGRkdhD28Vax6F1EOd+6NDhGIbO7t3D5VqiIA58Y41DRw7H8a+Ox9D2bfEVgaBvoD/OnDsLf4Phu7F9e2Pn7l2ljYyNxpFjR8u4/QcPxOGjRyIfPHAgZOIYkWJ0dCz6evsIlR0x0N8f/TTNoqenN3YhHKON4xxfQvLInti2fXv09fdFGwLt7OosUWcP/WOE6uE9wzHK5hy7F0bs8354eDeheGt0oFmGceJO9Pf1xRhCk74COnXqVJz46kQcgL8R+kdphw8fju2st23HdgS1J3YjmP6BgXIIhvbevr5o7+xcP8gBeNsWXd1dsR1h70GwowhgbO9Y7EIgXUCGWr0eztnBew80v3j5MiZwnFM4wMnJ9zE+/ibe8yzOWF5eRt2bRJa5mCe+v594H2/fjofO9uWrl/EWPGEonZqeicWlpXg/ORn3H9yPe/cfxJOnT+PW7dtcn8Sr169pb3i+xbv75f4l6y5jbob150Sna9evx+UrV3DSN+PatWvh840b1+P2rdtx6eLFuM7729D7gGMfJ6LJ88epj/H6zet48uxp2PeU68NHD8MxDx89Kn03bt6MN+zp0eNHOPo1nsffvosnT5/Ayz0i4aPy/g37ys+ePou7hNQbLHb/wYOy0RdEE0Opm15YXCjRxPuLFy/Ejz/+FJcvX4lbt26VcOsib9+9JczOl3H37t+Pu/fuxtVrV8uGbt66yeauhtfzFy7EBWhcunQpbEYvN7GEIA3ZT4hMj9iEEUue7kNL4b+F+fIeAT97/oyI9gDB3mYz9+M1gn7Hodj/jEj4FkHdAwo85f4RIV+heRU6eDgK5z4H5rqTREkjp4J33ayalvicc7SBPFWfjo6OyFUVqwCpTP8qJ6i51Hnf3dMNqOoBiHXga9pDx6sT9toGQm0Bt+iHnNeDD2ltbQvpt2MSnaiwY7q6OlmrLYxe0m6tt0ah3dUd8qMj9F2uqjCieSAi2im0Qo2VtmMWwTO+l2ZKKQglhaYOmqdwPfnWNzmmgp5za7VayKPoWn6l6YHk+YX5cDMppVghpC7ML0R5gRBylaPKGVwxb9SMzJgam13CfMQVCzBjeHV8gyjiYjI4C7x1gV8Y3hRVmtynlKKl1hICO9c2+kxPTccMqPYDp+U8/YkbcOGUUtTZQK1eC+m7jkJzrmtJp0EUdN4yUKGFsQLCdg5Hc2ywpvPkSX6d5xzn+qxwFFrux+l0ArxaqgrBpshsXmm5aTWlDyeqNsiYCzhZifb3D4Qnav/GHE9CrVILHOM7GdcRbzDvSUrDfpnvkz4aofM15zGqrY1txDz5QoNwOkhUk4br9LOu1yYbdB1P2M20tNSKJnSwFw+nl5TA6DaAg3WtFg5RnjrRevmyuY7vgh8FlPWk2whFquW2oW1hbnL27Nk4dep0GNZG8NjmKiZxEhiAsWNHj8U3587FKcLh6J6R6GUzA719sRuvfOzI0Tj79Zk4RztI2NtHhDrOeN9tHRiMndu2h2H1HPPNdUaJEnp3w6Qh9QSh9jRrG+IHBgfCcD9KJDCqOEZ+PKROTM7k0mjo1TG7iXiDbL6OZhiZHHvu7NnYv29/HCNsH4MPQ/5hwvSB/Qfo3xfbgQadCLCBVRSfsY0OQUdV5ZJ1qkLC8WXMIfhR3fT4nqiqNo7n1aHVchW1SJEwkU6y1wz4rKUc2FvUq5ZYXViO1SXa4lJMT36M5YXFANUVc9NXeKrLOE8356l5IGqA/ZqE6y2S/xiNPO121pC3WVKEirW3im9Ypw2fo0a10DfxbqLQd94qPk8/o3B83yB36iWkdnV2lX3Wa/Wi3T3dXZHZR75/7148xut2dHbAZyP06DdJ2m7dvhWGvad4cL17F6c/RJqu7SmYcZK7K0SVcbz3Er7DRV8ShR4Qka6SCf/0008kdM9KTvOAqDDDBnLO4fUO0esCkcVwqU0Xz08UkZdrV6+VMGoGPA0i1j8ZdR49ekz0uBfjb8Yjs+np6amQj4fkSka+27fvxJs3b0rZYQnhTwADnhI+3dvdu3fi5o2bYcS4e/deoX/nzu2y7ynC8yypvweRG0BYbVfVUdLG/gzTaosmpM21Ak52AHT6sMM1T51K6n7o0MGixrV6PXJVlbR/H+m86FH1k+ZeQI60VPuDpP/D1EWkX+oHzBHp7qGvoF7MLFc53pMB7z+wP0SlRqTAgQ5tG4qTJ07GbgDbmTNfxwjm2QMYVKOMRCklQNb2OAKSPAwS3UFtpa+vPwRpu3ftDvcyDHIdGtoamf2tkltt2TIYotp9AELNLat+npaSkUEBl86kr6+vEOqD4Ar2pHnkqgpDbwuRoA1PPYia6oR0Tl5Fg9vxCT2oYgc2rV07vo2w2s54x/Sub6ADR9ZL6FXbtmzZWlCkm5LRLlKDLdDWCXoQ7ZhHD2PduD5kNxC9D8fru97eHhxnR1H7dlCwZjaIb3LtDopOA9x7GDs4TFGo++kitPcAEbawbh/7dMwAvpAUvqMAl8sAIVFZijCahWoqEhTAqH6qsqYxA1KdoICjKVy8cLGMm0KdFaJzbmNe16/fiLvUPy5dvhx3QI13UOEbmJ4m8ODhgxIeG4TCl5QNLpwHyP30Y0jvAcj1PbSl9cMPP8TP588XFCmocv73338fF+j7y19+jGuY4k2An4BsirBspLt7526c//l8XAHJ3qTcIDB03uUrl38Biprvk8dPYnLyQ9yGtz/+8Y+8u1zmZG1SKZofGI9XCVnFcYE8ZWISiO0pIqOCP4Tdht1pBPDh44eCPD1Nne0EhaAJNjM9Mx2rADU1Ts2bm5+LGbCHdv7xw8cQSyzhWDU5cY7r6osmSQcEV9JzrjTb0ShDpzw1CLPyq/N28/opx3mdI11wrmvNUZiSvnPU6BnSBdcUrcp3wkzqmLY4Y5LUY5oDtmUZ0dvqpVeIHnpYB6aUS/LkO/sdrEB89v0SUcB759ufGe+9PsdNuKDPmp/vNaU6Xt8NNTC7OsxUmJ1CaHIAAjoPpMrgnZxDk3Kcm7VEoICMeF6do4BcI+cUgb/QbG2u4zxNvUmUU88r1vE6hbNsxzyrnAGSs+E4sUhKKaoqR/aUP3LKRoSc6YC4906W4LyIFCGJCJVwA4frqciMvqTWUgs3L4rUP1j0qddqYZEo+HEDCsXxXh2bUkIpGuF69quNthQp/NWhe6opMS6iQHcPJCWeEVwr2uLhqbEzM7Oh75BfhVQEgk9zrVxVUWUagGsVh1mr1UO6TWh6b/hWg3mEn4gsQT38YeoOpsE+WzuQSeH2QXL9IeocO3fuooYwHDoc03mzXCVfteBUiduepGpnJplSKuaTWMXFuwnLClaBOc7TW0E7VGH75cTNWlhKyVmBMKtoQaiZ5ybmkVIqzyZX7TjklFI5BN9rggo9JdYFtUq3Bb6qnEuVX9oKvoGf8n6J4pOCWyQEq3Wr4A/XyHrSf/3Nb8LwZvg7/tVXsWP7jhga2hbDeO1dhCVrDIcJV4dAbvYZrobAHDmn4htcJMOIreI02vD+3hemM2PYuIvLkM1T8zTbOOFV3qkVRh8FJbO2VU5SLVsBOKlNmp/znFPHxJznpjzdzNqua0qhoNvXP3eoZQq03lqPlFK0w5daVcdcPeyN5nMTjc/joMn7ACUjh6BJ0HWLtNu6huZwG3Ci43kEuBHkWP+4B1BbwUFqs6xSooNq67MMFQ1go/oZN7+IM66hqgrHjaEwpf7hHJmvszkd4DxOMKUcOVdkqw1A4GqknKJibvFJCK4dujM4aNeps6kUiYy3HgpK56oJpGRvwuEvl/5gzCLAUA3yW5A8OF4BIIMyptZSiyyDhjM3vsAEN+Di2r/vUkrxgk8EIr1Z7FNCVc4hXPeUNLHdgBkxxgB5gTigr7eX8t3e8hHJJKuU6gBWbaTzOi1pFzwAltiGhjnHueIWwZXNSpsmuYUxa5q4Nfr6+wBdw+WEd6O1vl9BxXtZb5iqmlgiIzw33gt+6Kc1MTE1Tho7d+4oFTvNfCcAT+3uh6b4RU3Ldlqz3EuZzgmiPBMm0aNfzewXpCiYHaC6HZTdRJLdACPnmkAdp+5onVJzEjWeOn06hkGK5gDbyXtMsGQ4+Mk5h+o5RoLmHAGWuclJkj7bTtbYBy+ua/N+3959sdc2trcgX1GrQs4cVIOI0cOHLvk4cOAgtZbeqKFJgyR5W7ZuKXUXNzzKeqdPfx0mgsdI2g6AcEXKO/GF7tsDyH4PuUlpzEqW5vCScp5aYMVKECZ4Up2N4RPAZJMmTcWoYhnwFsDnOlWyx+QOz8xjHjyMB+QizluitiCAsgJljiCm0JTs0+SeP3tOCfB1vCankK5RTSf8nBzH5zdUsay6PaOc9/zF8zLONcQy9stPiuBD10TIs3QbRBv9iznMCzR6lRbPegAADVNJREFUkeTQiPiUPEVeBYXy9pCvf9J4i5sQa4g08wIMv2OTb0i4Mh54BWJL+IMFPO4EIKgD6DojiKGvwQwS03j5+lUYr1vbWkvRRXsWaD3nY9IyajsBUJuiULPEJ4QZikeztHnobSG/2Iaqdvf1xiq0XlGbrGotMULR+A1MXQIpvoWXccqI0pgk5NvewYfvPSijxiK+pYmD7Whtjx4iVVdHZ0y+ex/3SABXl1aiA3M0ZHYSdfqA/+34Fvsb7GH641TMYe7TFpF4fvt6PCYoG741ATyGih+lFN/T1xtzML1C+Nm7f1/soyo9gL1aiXbTnd2dpe/Y8WNhWf0gSdowfqCPHKEFIRrOVnBw2qGV8L0kbP0kQjsxlz1jo3Hy69NxkIi0Y9fOkOYu+reTL+zE9odHhqMbu68IpfqNr8+eidOMP37ieMjLFvxKHce5ykFpcnupkRwm6TtCdDtArWIvJmD4b63VY3BgIMZG+Axw8FB8c+ZcnD51KopZUFvZRi6ybctQaIpDW4diiOd6S0tUCaeNyeUZUuuXnKje/CNSM/9osmgr4QgNJC0eDzcp4hSMzQGtjQCq3jQ5geNVT82oif0Ke3WyXjn8qAi1OieF5bgJ4O8UJz7D6TRx5dJ88fwFiHAu6kQV586SUs/yadMx5kIz8Kj5aK6vqKrr6O3z06d9Vuk1We8d517EQZMfJsmA35ci91tKDlbvpavpuB/HaVINDtG9ZivQ+g2ZkBmJXbt+jYToQmir1huM+zJ+mQTo4sVLJEnXqAlcKxXvJ9RCFIROkQhWPhXcoHZg+HWxh4Rk1/jxxx/XkjHCuP7CPpM//dJ1Pgm8oeTveOsnF/k0cMl1qLAb9s2RBGY6W+kqvLuEdxOtR3wCsE6h/3APUxyo5qR/uASdy5cuh0mo4xWk7ak+iM8T8qEAA60owviI7QySvhomPT0FskQSpVAUQAOzSSmFoU9HU1WZ+N8IN+/YipOXUL1eAxa3ehuajdGnDZ/ygexQWo5vpbquVmUiyiq+RaziWosgwVqtHkYVcYLRIFcVtFLBAPLhnDqa45wmKucBLcOn7xSU+MMIV1WZva0BPTVaXmr1Oml+Z6yiAav4GkPvMrnVAlCijmmaauiI8wpMiRlUOzcOBwVEtVEb6MQxLTFJ7KFZLHLfBopLKbFgjirTsDlPZJVFHJvtq1pCM1EFFZL9bsSr9Ou1erThA9x0xabXhFSxp2bZvExLR0Ydw4uQcTVnlcPROfq+Vq9FguAKKNX3CyVyzBcavlfwLbVaEQLDIuB741DaSdh0/CmlQttDyIIXQZYAxlRegYjumFmINPEDAqo60nXMChGiAUMreGIdmpvynSeTcuKTYUdkrvYPDgyWTUu3k8VlRPtcIvFzvsJa5TAyDC2iHaqsJ73CCRoivQ92azh2bis81I0M+LTS11KDzVTWC35SdnAKBZxSQobNaDJWv6QAV9fpek0J7WEfQoRySEgj76F8Noo3FpW1t3fAfHsc5YOs3zW3UiLr7OoKQZZ5yXEiyUD/AB+pu2OMCLGPiOF316/IZw6T6FmF9nkvoMmr7/sZ79yDeH7pCL7gI/zZYDpXVTEtn92wTYEqlBVOXc1bQfgy7kG5GYWqlmgu9hdNgE6GeIK4c7hgUFGEI+0qo330NDlg3zlW7VEzFTrC2BODoLUKQpbC5vDiFlMlLhSGNhh/ESG1RSvxu47d6zB7gbqenuMG8TkSzFUVFWF2mmKKwEhfMQBt4bmLuwlP1BMnkIRzV9jsAhXwirmOWcCO1RjvpW+/plJVOVYQiHNzzmwpIqUUuarK6ZeOWNMG10gRBQMpFDWfgw9er2k7EF2B2KcwpRn85O+++y5uUKZ7DZB6AxI07MicIfMp32F7AC2GLVGmyZyoUJU3ijzje6aVdCvdV69eAQU+KBXrl4RqfZCo9imo9A5gyKq5KNWw6mZsMuIm6/VaCKY0O/YXCrYDf1Wrtaz5L/xLL3xs5BCqvPau+enYLdC40QZqrzbpHM1/1BgF2sRU2vV1bLjKa4JUqxRYSrkIiFeRjf3a8BAp+8jIaJgvaAL9gCm9u8VUJe3zPtR/FLRoBVqGXWiGct4HIpLOTQa7QYSONQz2AeRcRC1SgOJ/854jfGjSDDWbI4ePhB+pNKMTmNuxY8fL/zwcAmjtJgEcGdlT/ouBIO7MmTPlvyjsxTxHRkcw1bFiwkcOHy45y25AoGur+mq1NA4AHreT73SCpJeXVyKlVJoCUjNSThGqKYzmlHjgZhDk5sJjbFa17+npiTbgbEopWlB9+0yQ/ATY2dkVhk7tN6U11ZRerV6Pvv6+MKFLKYVoUmFCPgYwpR3USXweGOiPPXypM9McIpEz0eru7irj9SkKUmG7MavtHThf33dTdfcrn5s0HLqJCjPp64Pe8J6w1uI7aViht+kPTcTkVecvL85JKRchuHvNyP7yRW2SXMJk7Yfvf4g/fftt+W8H/pcATUFg8o6vVOU9FetLVLxvAJKekWSJ8mSoFSFI7D15hUnQBcCOSdADqt2ax3PMSfB1/sL5UonW3KRx5crVuAawugyYO0+V/Nq1a3GV+6tcH1JFf/ToIR+O7lNpvxO3bt2O3/3ud3Hx4oW4TXIoPYHUNarkP/38U3z73bdxhXvX1USfk+xZJb8EL4/5QDVO7tVJMMhVFQogVwgDptUOhcNt5CUSqJ6e7lCV/K7gN8uxsdHwBJXyCCcolt9GkqV2qH67qH4N4hgVgs5H/KH912v1GCScDqveRCjt2RM+euxY7KR+4IltQxNsFVhkGdzSgy+Qvqc+iPbsJHfxm6m5g2s5x/utpONqzE5SbsuT+olWwmwb/sS5atEg2u2HME1uD5rSg3YvgD3UUCPcCN9s5UfzzviOlFLxF5pMEcYceYD/dUmGhkma3PwYiZCMaQpOMirsggmTnmE+7jpW1dU2A4ISqrfWSy1BAe6g5rHCRk2epOmmLSt+ffp0aN97EJaFF0/EMZpMN6dm8+uX/kQhGMbd3FZqsJrLaeYbUl23l43uJtnT7xwlrHv1v0jtROjS28uXPP3FIMniPnydyZqJZRvRUCebYFpfqGB85jGyKe5HzORnPsx8/2//Fn/BVL7707dx5+at+MD3ygfkAPMkVTeuXY/f//Z3RJ7rZczrl68KctNMtEdD2ywJlR95rBnMkMRJY+r9h3g//i5uX78ZF386H9/94U/x848/xWNylgYOzbT7Kt9sFd6bV69Jw+/GD3/+czwih7nLxyf7Jt6+iyvkGH/4X78PTeAZUc7/JvWC/ML/rnSX76ea8fmff447fLz6M/N//4c/xCPMQ3T9LRHzf/72t/Ez753vIWxos7xXuVIWkVXvZdDfIrF+gcqyWmCmaEbqxFkEYd8sG/3lmXvHp5RQjBT8CYXSBMxsNMfKiCXFCezV9uH9ZFhP2KBvmP3I1/kPZLKGbzf9ntrC9MfpmEdjZ/m44/M4Id8cSg0z5E9NfSz/d6Nk2bwbpy7ie7NYP2e4dmlEOqOc/ItuxSmGWzgOIgdsZxpP/AY/uUimqkJz4E3ZlKqzCkz2+qmm40kJKjYI+dwEzDSI9apyilQ+0vhFfAFBLyJwmWEBfpvIbq0Z71cAXsskXRaSPbEGdFJewwPOm6eYswqU1t5NslyrIsI5zk3OUXxS1V13Bb7FIY5vgi9YCO5csrkG2uyDZ+mnnCK4bxoKIwIZrAnCl+KEtWvyRfj8qZZSgs56i7WfBkQbaIdNZrXtllpLGLpaYN5n73WeHoLPtVotHFPecyjVeivvq5Yo/SSDjrVPNOqcuvPoz9Ua/85LCDDBSkopCt/Zd1U4j40WZylvKWJ9f4k7fpUul+xHFOHvhjQbSE5JsS/cgKM+1ZjtLwPLCK82Z3GynkwDwTgkwxyS803RFk9vhZNurK+VEkxtNCbYvwL0Vmuc50bsWwCqJzbsaYtW5TNFYkaUTNUx9pXGarHefHaOmuK9/PpcJvIHHeVvRC5/N/6kiJTSett8v9G36Ros5ebXG4//+Jsi+I2UUmnBT2GE68ZvSmvvUkprXQyQYbWsuS5MJrtY2fDmTZQJTEsphf/UhoSwSrNvU4v1ewhBohnSt7lWocMfhJ7Dk0tJcvSsb25jILyty1cym9r6ON8z629/oVVo0ut7F7Tx+Ne1HCPjXO23OcbmXBiD/xQKxBPnAZNpKaru2Cpnuni/zkeu2Ede20NigE1aGy0Yl5jDpLKJzf0ML7+5/N30pzC/8QyBjUn/cN0Ys+mawn/B3yg/0pIJ53pVqqWvvIUn6Nvve5v39DpsjUZyYJPutVnJXoTnk4fFCweU5nz7Njf7fmmOcj2vtLTeuPzyuyYMFoj1llLidq1x88vA/6ObxCjmO0+GeQrv/9riH35+Geeb9bne/tJPX0oSXhNT9nQZUDbJNaUE+b9qCF1//eUdL6O0cD5//E38+bt39MSaMLz70r4IY7MOfNGMTdL4IowvwtgkgU23XzTjizA2SWDT7X9Ezdi0/b+9/SKMTfL4IowvwtgkgU23XzTjizA2SWDT7RfN2CSM/w0AAP//QBY7bgAAAAZJREFUAwBxlRR/cC1tdAAAAABJRU5ErkJggg==)
    

Show all

3. Merge Commit Revert (Mainline Reversion) I don't get it

Let’s look at a **merge commit revert** using a simple analogy.

Imagine you are writing a book (the **main branch**).  
Your co-author writes a separate chapter about time travel (the **feature branch**) and copies it into your book.  
This act of combining them is the **merge commit**.

Suddenly, your publisher says, "Time travel ruins the plot, take it out!"

If you use a regular `git revert`, Git gets confused. It looks at the book and sees two distinct histories flowing into that point: your original storyline (Parent 1) and the time travel storyline (Parent 2). Git doesn't know which author's work to erase, so it panics and asks you to choose.

By running `git revert -m 1`, you are telling Git: **"Keep the book exactly how it looked on my storyline (Parent 1) right before the merge, and completely undo everything that came from the other storyline."**

---

Step-by-Step Example

Let's look at what the terminal actually shows when this happens.

1. The Problem

You merged a feature branch into `main`, but it broke the website. You run `git log` to see what happened:

bash

```
git log --oneline
```

Use code with caution.

**Output:**

text

```
f8b3a21 (HEAD -> main) Merge branch 'broken-feature' into main
```

Use code with caution.

2. The Revert Command

Because `f8b3a21` is a _merge commit_, typing just `git revert f8b3a21` will fail with an error (_"error: commit f8b3a21 is a merge but no -m option was given"_).

You must specify `-m 1` (Mainline 1, which almost always means the branch you merged _into_, in this case, `main`):

bash

```
git revert -m 1 f8b3a21
```

Use code with caution.

3. The Result

Git cleanly strips away all files and code changes that were introduced by the `broken-feature` branch and creates a brand-new commit on `main` stating that the merge was reverted.

---

The Hidden Trap (Why people get confused later)

The most confusing part of a merge revert happens **after** you fix the bug.

Imagine you go back to your `broken-feature` branch, fix the code, and try to merge it into `main` again. **Git will say everything is up to date and your code changes won't show up.**

Why? Because Git remembers that it already "played" those commits once during the first merge. It doesn't realize you want them back.

The Fix: "Reverting the Revert"

To bring your feature back into `main` later, you have to undo your undoing.

1. Find the commit hash of the **revert** you did earlier (e.g., `c4d3e21`).
2. Revert that commit to bring the history back:
    
    bash
    
    ```
    git revert c4d3e21
    ```
    
    Use code with caution.
    
3. Now your code is back on `main`, and you can safely merge your new fixes.

To bring your feature back into main later, you have to undo your undoing. so will that be on the main or the feature branch since its not okay to do anything on the main ?

You should do this on a **new feature branch**, not directly on `main`.

Even though you are undoing a commit that happened on `main`, you can safely target that commit hash from a side branch. This keeps your `main` branch protected.

Here is the exact, safe workflow to bring your feature back:

The Safe 4-Step Workflow

1. Create a brand new branch from main

Before doing anything, pull the latest `main` and branch off of it. Let's call it `restore-feature`.

bash

```
git checkout main
git pull
git checkout -b restore-feature
```

Use code with caution.

2. Revert the revert commit _on your new branch_

Find the commit hash of the original revert (run `git log` to find it). Let's pretend the hash is `c4d3e21`. While standing on your `restore-feature` branch, run:

bash

```
git revert c4d3e21
```

Use code with caution.

_What just happened:_ Your new branch now has all of your original feature code back, because you just undid the deletion. `main` remains completely untouched.

3. Add your fixes or new code

If you need to fix the bugs that caused the issue in the first place, make those code changes right now on this branch and commit them.

bash

```
# Fix the bugs...
git add .
git commit -m "Fix bugs that broke the initial release"
```

Use code with caution.

4. Push and open a Pull Request

Now, push your branch to GitHub/GitLab and open a normal Pull Request back into `main`.

bash

```
git push origin restore-feature
```

Use code with caution.

Once your team reviews the Pull Request and merges it, your feature will safely return to `main` without you ever having to touch or commit directly to the protected `main` branch.

Does this workflow match how your team handles **Pull Requests**? If you have a specific **commit hash** you are trying to pull this off with right now, I can help you write out the exact terminal commands.

okay but the initial revert I already need to commit a new changes so will it see that the changes where already applied if Im merging a new merge commit

Yes, ==**Git will absolutely ignore your old changes** if you just try to merge the feature branch again==, even if you add new commits to it.

This is the exact trap that catches most developers.

Why Git Ignores the Old Changes

Git does not look at the final state of the code when merging; it looks at the **history of commits**.

1. When you first merged `feature-branch`, Git noted: _"Commits X, Y, and Z are now part of `main`."_
2. When you ran `git revert -m 1`, you didn't erase Commits X, Y, and Z from `main`'s history. You just added a **new commit** that said, _"Delete the code changes that X, Y, and Z brought in."_
3. If you add a new Commit W to your feature branch and try to merge it, Git compares the histories. It sees that `main` **already contains** Commits X, Y, and Z.
4. Therefore, Git will **only bring in Commit W**. All your original code from X, Y, and Z will stay missing on `main`.

---

The Two Ways to Fix This

Depending on how your team works, you have two options to make Git see the whole picture again.

Option A: Revert the Revert (Recommended)

As shown before, you create a new branch (`restore-feature`) from `main`, run `git revert <hash-of-the-revert>`, and then add your new changes on top. This formally commands Git to "undo the deletion," bringing everything back cleanly.

Option B: Cherry-Pick (The Alternative)

If you do not want to "revert the revert," you can use a fresh branch and **cherry-pick** the specific commits you want back. This generates entirely new commit hashes, tricking Git into seeing them as brand-new changes.

1. Create a fresh branch from `main`:
    
    bash
    
    ```
    git checkout main && git pull
    git checkout -b feature-fixed
    ```
    
    Use code with caution.
    
2. Copy your original feature commits over manually using their hashes:
    
    bash
    
    ```
    git cherry-pick <hash-of-commit-X>
    git cherry-pick <hash-of-commit-Y>
    ```
    
    Use code with caution.
    
3. Add your new fixes, commit them, and open a Pull Request. Git will see these as completely new commits and will not ignore them.

Which option feels easier for you to track—**reverting the revert commit** to bring everything back at once, or **cherry-picking** the specific pieces of work you need?