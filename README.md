# 项目说明 — 外星人入侵（Alien Invasion）

这是一个完整的外星人入侵小游戏实现，基于《Python 编程 从入门到实践》一书第 14 章的示例代码，并对该示例进行了若干完善与扩展。仓库包含游戏源码、设置和简单说明，适合用来学习 Pygame 基本用法与项目结构。

**主要文件**
- `alien_invasion.py`：程序入口，游戏主循环与事件处理。
- `settings.py`：所有可配置项（屏幕大小、速度、子弹与外星人参数等）。
- `game_stats.py`：游戏统计（得分、最高分、剩余飞船等）。
- `scoreboard.py`：负责在屏幕上绘制得分、最高分、等级与飞船剩余数。
- `ship.py`、`alien.py`、`bullet.py` 等：游戏实体类与行为实现。

**如何运行（Windows cmd 示例）**

```cmd
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python alien_invasion.py
```

**在 PowerShell 中（示例）**

如果你在 PowerShell 中遇到执行策略限制，可以先按需调整策略，或直接以管理员运行一次。下面为无需 `&` 符号的等效命令示例（在多数环境中路径直接执行也有效）：

```powershell
python -m venv .venv
# 可选：激活虚拟环境（仅当你愿意在当前会话内使用虚拟环境时）
. .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python .\alien_invasion.py
```

**不激活虚拟环境也可直接使用解释器**

```cmd
.venv\Scripts\python.exe -m pip install --upgrade pip
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe .\alien_invasion.py
```

**说明与建议**
- `requirements.txt` 当前仅包含 `pygame==2.6.1`。
