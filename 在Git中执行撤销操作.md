### 翻译自[How to undo (almost) anything with Git](https://blog.github.com/2015-06-08-how-to-undo-almost-anything-with-git/)

## 怎样撤销几乎所有的Git版本管理的操作

版本控制工具最具有特色的功能之一就是有能力可以"撤销"你做的更改(错误的更改). 在Git中, 各种"撤销"操作可能有些许不同.

当你做出了新的提交(Commit), Git存储你的仓库的快照[拓展阅读有关Git存储技术](https://stackoverflow.com/questions/8198105/how-does-git-store-files)在特定的时候(PS:例如commit时). 随后,你可以通过Git回到项目(仓库)的早期版本.

本文中, 我将通过一些你可能会遇见的常见的工作场景(你想通过撤销你所做出的更改),介绍你最应该采用的方法, 通过Git实现.(PS:英语的各种从句的表达习惯, 导致中文会用比较长的句子表达,我尽量在通顺的前提下, 仿照原文表达).

### 撤销一个已经公开(Push)的更改

**场景**: 你刚运行了```git push```, 将你的更改提交到GitHub, 现在,你意识到这些更改中有错误, 在其中某一次的commit上. 你想撤销那一次commit(一次push, 可以有很多commit).

**撤销操作**: ```git revert <SHA>``` (每一次commit生成的安全哈希值)

**命令解释**: ```git revert```将会创建一个新的, 与给定的<SHA>值所对应的 commit 相反的commit. 如果旧的commit 是"master"(比喻), 那新的commit就是"anti-master"(后面这有一段,容易混淆,其实就是说老的commit的任何修改都将复原, 个人理解. 原文: anything removed in the old commit will be added in the new commit and anything added in the old commit will be removed in the new commit.)

这是Git最安全, 最基础的撤销操作了, 因为它不改变操作历史(history, commit历史)--因此你可以```git push```这个新的反转commit 去改正你的错误.

### 修改最后一次的提交描述

**场景**: 你最后一次的提交描述有个拼写错误, ```git commit -m "Fxies bug #42"```, 但在**push之前**, 你意识到你应该写```Fixes bug #42```.

**撤销操作**: ```git commit -amend``` or ```git commit -amend -m "Fixes bug #42"```

**命令解释**: ```git commit --amend```将会更新,替换掉最近一次的commit, 用这次提交(这次提交可能包含了之前commit未包含的更改). 如果2次commit之前没有更改, 那就仅仅只是替换了commit 的message.

### 撤销"本地"所做的修改

**场景**: 一只猫走过你的键盘, 有些误更改被保存, 然后编辑器崩了. 你并**没有commit**这些更改, 然后,你也撤销(undo) 这个文件所做的全部更改(回到上次提交时的那样).

**撤销操作**: ```git checkout -- <bad filename>```

**命令解释**: ```git checkout``` 修改工作目录(work directory)下的文件到Git所记录的上一个状态(版本库中所存的)
.


额外补充图:  
![git tree movements visualized](./img/git_tree_movement.jpg)