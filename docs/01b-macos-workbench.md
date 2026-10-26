# macOS workbench — Terminal + editor + practical keyboard fluency

**Course position:** Do this **before writing the first Python function** (Day 2), then revisit history shortcuts on Day 3 and environment/Git on Day 7. **Estimated time:** 60–100 minutes including a hands-on change.

## Learning outcomes

By the end, the learner can tell *Terminal.app*, *zsh*, *VS Code* and *Python* apart; open a project folder in the editor; use the terminal to run a Python file; find, fix, and re-run a mistake; navigate a command line and command history without retyping; and copy/paste safely on macOS.

## 1. The four components

```text
macOS
  ├─ Terminal.app  ← window for text commands (or VS Code integrated terminal)
  │   └─ zsh       ← reads commands, has history and line editing
  │       └─ python3 hello.py  ← process you run
  └─ VS Code       ← editor where you save hello.py
```

macOS supplies **zsh** as the default login shell. **No shell framework is required** to do this lesson. The same shell commands work in Terminal.app and VS Code's integrated terminal when both use zsh. Keyboard shortcuts differ when focus is in the editor rather than the terminal.

## 2. Prepare macOS once

1. Open **Terminal** using Spotlight (`Command + Space`, then type “Terminal”).
2. Install a supported Python from [python.org for macOS](https://www.python.org/downloads/macos/). Avoid modifying macOS' bundled Python. Install the [Apple Silicon build of VS Code](https://code.visualstudio.com/docs/setup/mac).
3. In Terminal, inspect the machine and current working directory:

   ```sh
   uname -m                # expect arm64 in a native Apple Silicon terminal
   echo "$SHELL"           # normally /bin/zsh
   python3 --version
   pwd
   ls
   ```

4. Launch VS Code from Applications. Press **Command + Shift + P** (Command Palette), run **Shell Command: Install 'code' command in PATH**, and open a new Terminal window. Enter `code --version` to verify. Adding a Copilot CLI is **optional and not needed for the course**.

If `code` is unavailable, open VS Code normally, select **File → Open Folder…** and choose the folder in the next step. The learner should not get stuck on a PATH issue.

## 3. One project, two windows: first edit–run loop

In Terminal.app:

```sh
mkdir -p ~/Projects/python-ai-playground
cd ~/Projects/python-ai-playground
pwd
code .
```

If the command-line launcher is unavailable, open the same folder with VS Code's File menu. In the VS Code Explorer, create `hello.py`:

```python
name = "friend"
print(f"Hello, {name}!")
```

**Save with Command + S**. In Terminal.app, run:

```sh
python3 hello.py
```

Return to VS Code, change the name and add a second `print` statement. Save and rerun the same command. **Do not paste an entire finished solution; type at least one line yourself.**

Try the integrated terminal via **Terminal → New Terminal** in VS Code. It should be in your opened folder. Keep Terminal.app available while learning so it is clear the editor and shell are separate programs.

### Shortcuts depend on what has focus

**Command (⌘)** shortcuts belong to macOS/applications: copy, paste, save, new tab. **Control (⌃)** shortcuts at a shell prompt generally edit the shell command line or send signals to a running process. `Control + A` in a shell is **not** `Command + A` (Select All).

## 4. Essential zsh command-line shortcuts

Use these at an **idle zsh prompt**, not in the VS Code text editor:

| Shortcut | Meaning | Try it |
| --- | --- | --- |
| **Control + A** | Cursor to **start** of command line | Write `echo one two` without Enter, jump left |
| **Control + E** | Cursor to **end** of command line | From start jump to right edge |
| **Control + P** | **Previous** command in history | Run two `echo` commands; recall the older |
| **Control + N** | **Next** command in history | After Control-P, step forward |
| **Control + R** | **Reverse** incremental search | Type `echo`, find and run a past command |
| **Control + C** | Interrupt current command (SIGINT) | Run `sleep 30`, then stop it |
| **Control + L** | Clear the visible terminal display | Use after the practice session |
| **Control + U** | Delete command text before cursor | Recover from a badly typed command |
| **Control + K** | Delete command text after cursor | Change the trailing part |
| **Tab** | Attempt completion | Type `pyth` then Tab (availability varies) |

With *standard* zsh Emacs-style bindings, Control-P/N navigate history and Control-R searches backward. Shell plugins, different ZLE keymaps, or terminal configurations can customize these commands. If the shortcuts don't work, first verify focus is in Terminal and that `echo "$SHELL"` reports zsh. See Apple's [Terminal keyboard guide](https://support.apple.com/guide/terminal/keyboard-shortcuts-trmlshtcts/mac).

### Two-minute keyboard drill

1. Run `echo APPLES`, then `echo BANANAS`.
2. Press **Control + P**: what appears? Press again; use **Control + N** to advance.
3. Press **Control + R**, type `APPLES`, press Enter (if a matching command is found).
4. Type `echo good morning` **without Enter**; press **Control + A**, then **Control + E**, then Enter.
5. Type a long command, move the cursor left a few positions, try **Control + K** and **Control + U**.
6. Run `sleep 30`, stop it with **Control + C**.

**Exit ticket:** Demonstrate Control-A, E, P, N and R without consulting the table.

## 5. Copy and paste — macOS Terminal vs shell

| In Terminal.app or VS Code integrated terminal | Shortcut |
| --- | --- |
| Select output with mouse/trackpad, then **copy** | **Command + C** |
| **Paste** copied text at the prompt | **Command + V** |
| **Interrupt** a running command | **Control + C** |
| **Save** source file in the VS Code editor | **Command + S** |
| Select all text in VS Code editor | **Command + A** |
| Open a new Terminal.app tab | **Command + T** |

The distinction matters: **Control-C does not copy the terminal output**; it interrupts a process. **Command-C does not send SIGINT**.

### Copy/paste drill (and safety rule)

1. In VS Code, type `print("Hello from the editor")`, save it, then run `python3 hello.py` in Terminal.
2. Select the terminal output with the pointer; press **Command + C**. Paste it into a scratch note in VS Code with **Command + V**.
3. Copy this *single safe command* from the course into Terminal, **inspect it before pressing Enter**, then execute:

   ```sh
   printf 'Copied safely into Terminal\n'
   ```

4. Now try `sleep 30` and **Control + C** — not Command-C — to stop it.

**Never blindly paste and execute multiline commands from an unknown website, chat or repository.** Pasted newlines may execute commands. Read and understand every command first, especially `curl | sh`, `sudo`, `rm`, or commands that edit shell startup files.

Apple's [Terminal shortcuts](https://support.apple.com/guide/terminal/keyboard-shortcuts-trmlshtcts/mac) and [VS Code terminal guide](https://code.visualstudio.com/docs/terminal/basics) document the macOS Command-C/V bindings.

## 6. Continue with the downloaded course

The public presentation's first two slides offer a **ZIP of all course materials**. One reproducible Terminal workflow, after downloading it into `~/Downloads`, is:

```sh
mkdir -p ~/Projects
cd ~/Projects
unzip ~/Downloads/py-ai-studyplan-materials.zip
cd py-ai-studyplan
code .
python3 examples/rule_bot.py
```

If Finder already unpacked it, **do not unzip again**. Use Finder's “Copy as Pathname” or drag the extracted folder onto the Terminal window after typing `cd ` to avoid mistyping the path.

This is the actual course root: `examples/`, `docs/`, `build-revealjs/`. Use your own extracted folder path when running commands.

## 7. Zsh for Humans (z4h): macOS-compatible, *optional*

[Zsh for Humans](https://github.com/romkatv/zsh4humans) works on macOS, bundling autosuggestions, command completion, history search, fzf and prompt customization. Its [usage/tips documentation](https://github.com/romkatv/zsh4humans/blob/master/tips.md) explicitly describes macOS key variations.

However, the maintainer currently says the project has **very limited support, no planned features, and most bugs will go unfixed**. It can change your key bindings and rewrites Zsh startup files after offering backups. **Do not install it just to learn Control-A/E/P/N/R.** macOS already includes zsh, which is enough for the entire curriculum.

**Suggested timing:** Optional *after* the core shortcut drill, preferably after Day 7. Discuss the tradeoff, read the upstream installation instructions before using any remote installer, back up existing `~/.zshrc`/`~/.zshenv` files, and understand the upstream rollback steps. Never silently run a `curl | sh` installer in a teaching session.

### Workbench mastery check

From Terminal.app, start in `~/Projects`; navigate into the course folder with `cd`; open it in VS Code; edit/save a Python file; run it; recall the same command with Control-P; search old history with Control-R; copy its output with Command-C; interrupt a deliberate `sleep` with Control-C. Explain **which program** handled each key.

## 8. Bonus after Day 7: Markdown as a file, HTML as a reading page

The course provides **two views of the same lesson**:

- **Read in a browser:** [formatted HTML lesson](https://study.fkr.dev/docs/01-ai-intuition.html) — headings, links, code blocks and navigation.
- **Edit as source:** [original Markdown lesson](01-ai-intuition.md) — plain text with simple formatting markers.

Once you know `cd`, `code .`, filenames and `curl`, practise bringing a real lesson into your editor. This is an **optional** exercise for Day 7, not a prerequisite for the Day 1 theory discussion.

```sh
cd ~/Projects/python-ai-playground
curl --fail --location --show-error \
  --output lesson.md \
  https://study.fkr.dev/docs/01-ai-intuition.md
head -n 12 lesson.md
code lesson.md
```

*What happened?* `curl` fetched **data** from a URL and saved it as `lesson.md`; `head` showed its first lines; VS Code opened it as editable text. `curl` does not execute the Markdown. Compare VS Code's built-in Markdown preview (Command+Shift+V) with the ordinary text editor, and compare both with the HTML reading page.

If the custom domain is temporarily unavailable, the repository also serves the [original file](https://raw.githubusercontent.com/fkr-0/py-ai-studyplan/main/docs/01-ai-intuition.md).

**Safety:** Downloading a document into a file is very different from running a downloaded shell script. Never pipe unknown network content into a shell interpreter.

[Next: Python foundations](02-python-foundations.md) · [Daily learning schedule](21-day-mac-track.md)
