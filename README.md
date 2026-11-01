# 弹丸论破1自动扭蛋机win系统

> 用于《弹丸论破：希望的学园与绝望的高中生》的自动扭蛋机脚本，**仅支持 Windows**。
> Auto gacha (capsule machine) script for *Danganronpa: Trigger Happy Havoc* — **Windows only**.

[中文](#中文说明) | [English](#english-readme)

---

## 中文说明

### 这个脚本能做什么

在扭蛋机界面里自动完成「投币（S）→ 确认（Enter）」的循环，直到用完你设定的次数。中途可以随时按 `F9` 停止。

脚本只负责按时发送按键，不读画面、不修改游戏文件，也不联网。

### 完全开源

本项目的代码**完全开源**，任何人都可以自由使用、修改、分发、商用，**无需署名**，也无需征得同意。详见 [LICENSE](LICENSE)（MIT No Attribution）。

仅供个人娱乐使用，请自行承担风险。

### 环境要求

- Windows 10 / 11（本脚本依赖 `pydirectinput` 的 Win32 DirectInput 接口，**不能在 macOS / Linux 上运行**）
- Python 3.8 及以上（[python.org](https://www.python.org/downloads/) 下载，安装时勾选 “Add Python to PATH”）
- 两个第三方库：`pynput`、`pydirectinput`

### 安装依赖（在 CMD 里执行）

```bat
pip install pynput pydirectinput
```

或者在本目录下执行：

```bat
pip install -r requirements.txt
```

如果 `pip` 提示找不到命令，可以改用：

```bat
python -m pip install pynput pydirectinput
```

### 使用方法

1. 启动游戏，进入扭蛋机（胶囊玩具机）的操作界面。
2. 打开 CMD，切换到本脚本所在目录，例如：

   ```bat
   cd /d "C:\Users\AAA\Desktop\danganronpa"
   ```

3. 运行脚本：

   ```bat
   python gacha.py
   ```

4. 按提示输入要抽的次数（例如 `10`），回车。
5. **点击游戏窗口让它处于前台**，然后按 `F9` 开始自动扭蛋。
6. 想提前停止时，再按一次 `F9`。
7. 次数用完后脚本会自动停止。之后请回到游戏里把扭蛋逐个拆开。

> 小提示：开始后不要切换到别的窗口，也不要用鼠标点别的地方，否则按键会跑到别的程序里。

### 配置说明

打开 `gacha.py`，文件顶部的「配置区」可以调整：

```python
COIN_KEY = 's'            # 投币键
CONFIRM_KEY = 'enter'     # 确认键
WAIT_AFTER_COIN = 1.0     # 投币后等待秒数
WAIT_AFTER_CONFIRM = 7.5  # 确认后等待秒数（等扭蛋动画播完）
TOGGLE_KEY = Key.f9       # 开始 / 停止热键
```

如果你的电脑较慢或游戏动画较长，可以适当**增大** `WAIT_AFTER_CONFIRM`；如果按键没反应，先检查游戏键位是否与 `COIN_KEY` / `CONFIRM_KEY` 一致。

### 常见问题

- **按 F9 没反应**：用「以管理员身份运行」打开 CMD 再启动脚本；部分游戏需要管理员权限才能接收模拟按键。
- **按键发到了别的窗口**：游戏窗口必须处于前台，脚本不会自动切换窗口。
- **节奏对不上（提前确认或等太久）**：调整配置区里的两个等待时间。
- **能不能在 Mac / Linux 用**：不能。`pydirectinput` 是 Windows 专用库；在其它系统上需要改用 `pyautogui` 等方案。
- **会被封号吗**：这是单机游戏，但仍然属于自动化操作，使用风险自负。

---

## English README

### What it does

Automates the capsule-toy (gacha) machine in *Danganronpa: Trigger Happy Havoc* by repeatedly pressing the coin key (`S`) and the confirm key (`Enter`) for a number of pulls you choose. Press `F9` at any time to stop.

The script only sends timed keystrokes — it does not read the screen, modify game files, or access the network.

### Fully open source

This project is **completely open source**. Anyone may use, modify, redistribute, or sell it, **with or without attribution**, and without asking for permission. See [LICENSE](LICENSE) (MIT No Attribution).

For personal entertainment only. Use at your own risk.

### Requirements

- Windows 10 / 11 (it relies on `pydirectinput`'s Win32 DirectInput API and **does not run on macOS or Linux**)
- Python 3.8+ (from [python.org](https://www.python.org/downloads/); tick “Add Python to PATH” during installation)
- Two third-party packages: `pynput` and `pydirectinput`

### Install dependencies (in CMD)

```bat
pip install pynput pydirectinput
```

Or, from this folder:

```bat
pip install -r requirements.txt
```

If `pip` is not recognized, use:

```bat
python -m pip install pynput pydirectinput
```

### Usage

1. Launch the game and open the gacha machine screen.
2. Open CMD and `cd` into this folder, e.g.:

   ```bat
   cd /d "C:\Users\AAA\Desktop\danganronpa"
   ```

3. Run the script:

   ```bat
   python gacha.py
   ```

4. Enter how many coins/pulls to use (e.g. `10`) and press Enter.
5. **Click the game window to bring it to the foreground**, then press `F9` to start.
6. Press `F9` again to stop early.
7. The script stops automatically when the count reaches zero. Open your capsules in-game afterwards.

> Tip: once started, don't switch windows or click elsewhere — the keystrokes would go to whatever window is focused.

### Configuration

The block at the top of `gacha.py` is editable:

```python
COIN_KEY = 's'            # key that inserts a coin
CONFIRM_KEY = 'enter'     # confirm key
WAIT_AFTER_COIN = 1.0     # seconds to wait after inserting a coin
WAIT_AFTER_CONFIRM = 7.5  # seconds to wait after confirming (capsule animation)
TOGGLE_KEY = Key.f9       # start / stop hotkey
```

On slower machines or with longer animations, **increase** `WAIT_AFTER_CONFIRM`. If keys never register, first check that the in-game bindings match `COIN_KEY` / `CONFIRM_KEY`.

### FAQ

- **F9 does nothing**: run CMD as Administrator before starting the script — some games only accept injected keys from an elevated process.
- **Keys go to another window**: the game window must stay focused; the script never switches windows for you.
- **Timing is off (confirms too early or waits too long)**: adjust the two delay values in the config block.
- **Can I run it on macOS/Linux?**: No. `pydirectinput` is Windows-only; you'd need to rewrite the input layer (e.g. with `pyautogui`).
- **Will I get banned?**: This is a single-player game, but it is still automation — use at your own risk.

---

## 文件说明 / Files

| 文件 | 说明 / Description |
| --- | --- |
| `gacha.py` | 主脚本 / main script |
| `requirements.txt` | 依赖清单 / dependency list |
| `LICENSE` | MIT No Attribution 许可证 / license |
