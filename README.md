# CQUPT_BBS

（仅供学习，禁止用于商业用途）

## Applications

1. bbs - base
2. home - 主页
3. user - 用户系统
4. write - 编辑

### bbs - base

左边侧边栏left_sidebar：顶部图标，中间两个导航图标，底部用户头像（未登录则不显示头像）。

中间主体内容content。

右侧栏right_sidebar：其中右侧栏有两套，一套是主页/搜索，一套是文章/作者页。

### home - 主页

顶部未登录则提示去登录，已登录则显示Follow People；下面有两列Following和All显示帖子，文章用分割线隔离。

### user - 用户系统

登录 

注册 

Following

Followers

选择有限的头像

E-mail

### write - 编辑

开源github

## Git Development Specification

### Git Workflow

1. If you are new to this project, please enter `git clone https://github.com/sulv9/benchmark.git` in your Git Bash to clone this project to your local computer. Otherwise, skip this step.
2. After cloning, go into the project folder "benchmark" and open Git Bash. Enter `git checkout -b [branchName]` in the Git Bash to create and switch to the new branch where the [branchName] should be in the format of "your name +  taskName", for example "sulv/arch" represents the task of architecture development in the project created by sulv.
3. Then enter `git pull origin main --rebase` to fetch the latest code from the remote main branch and execute the "git rebase" command which is good for clean commits.
4. After that, use the `Android Studio` to open the project and start your development.
5. After your development, enter `git add .` and `git commit -m"[commitMessage]"` in the Git Bash in turn. The [commitMessage] should be in the format of "[Type] commit-message". See [Git Commit Type](https://github.com/sulv9/benchmark#Git Commit Type) for "Type" and the "commit-message" should be in 50 characters.
6. Finally, enter `git push -u origin [branchName]` where the [branchName] is same to that in the second step if you push your code for the first time, otherwise enter `git push` directly in the Git Bash.

### Git Commit Type

- `feat`: Add a new feature to the codebase.
- `fix`: Fix a bug.
- `docs`: Documentation changes.
- `style`: Code style change(Don't affect the execution of the code).
- `refactor`: Refactor code without changing public API.
- `perf`: Update code performances.
- `test`: Add test to an existing feature.