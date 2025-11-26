# 新功能说明（扩展）

下面是仓库中已经实现的两个新功能的说明与代码解释：**外星人射击（Alien Shooting）** 和 **历史最高分（Historical High Score）**。

- 代码位置（仓库根目录）: `alien_invasion.py`, `bullet.py`, `alien.py`, `game_stats.py`, `scoreboard.py`, `high_score.txt`

### 外星人射击（Alien Shooting）

- 概述: 外星人现在会在游戏运行时以一定概率向下发射子弹。外星人子弹使用 `AlienBullet` 类表示，触发与管理位于 `alien_invasion.py`。

- 关键实现要点:
  - `bullet.py` 中定义了 `AlienBullet`，负责位置创建、更新与绘制：

```python
class AlienBullet(Sprite):
    def __init__(self, ai_game, alien):
        # 在外星人的底部创建子弹
        self.rect.midbottom = alien.rect.midbottom
        self.y = float(self.rect.y)

    def update(self):
        # 子弹向下移动
        self.y += self.settings.alien_bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
```

  - `alien_invasion.py` 中的 `_alien_   fire()` 方法负责决定何时发射子弹：

```python
def _alien_fire(self):
    if len(self.alien_bullets) >= self.settings.alien_bullets_allowed:
        return

    if random.random() < self.settings.alien_fire_chance and self.aliens:
        alien = random.choice(self.aliens.sprites())
        from bullet import AlienBullet
        new_bullet = AlienBullet(self, alien)
        self.alien_bullets.add(new_bullet)
```

  - 每帧调用 `_update_alien_bullets()`：移动子弹、删除越界子弹、并检测与飞船的碰撞。一旦碰撞，调用 `_ship_hit()` 处理飞船被击中逻辑。

- 可调参数（在 `settings.py`）:
  - `alien_fire_chance`：每帧单个触发尝试的概率（例如 0.001 表示极小概率）。
  - `alien_bullets_allowed`：屏幕上允许同时存在的外星人子弹数量上限。
  - `alien_bullet_speed`、`alien_bullet_width`、`alien_bullet_height`、`alien_bullet_color`：外星人子弹的属性。

### 历史最高分（Historical High Score）

- 概述: 游戏会在本地磁盘上持久化最高分到一个文本文件，启动时读取，退出或得分更新时保存。实现集中在 `game_stats.py` 与 `scoreboard.py`。

- 关键实现要点:
  - `game_stats.py` 使用 `HIGH_SCORE_FILENAME` 字段，默认路径为模块文件夹下的 `high_score.txt`：

```python
HIGH_SCORE_FILENAME = os.path.join(os.path.dirname(__file__), 'high_score.txt')
```

  - 启动时，`GameStats.__init__` 会调用 `_load_high_score()`，读取文件内容并转为整数（文件不存在或读取失败时返回 0）：

```python
def _load_high_score(self):
    try:
        with open(self.HIGH_SCORE_FILENAME, 'r', encoding='utf-8') as f:
            return int(f.read().strip() or 0)
    except Exception:
        return 0
```

  - 当需要保存最高分时，调用 `save_high_score()` 写入文件（错误被吞掉以避免影响游戏运行）：

```python
def save_high_score(self):
    try:
        with open(self.HIGH_SCORE_FILENAME, 'w', encoding='utf-8') as f:
            f.write(str(self.high_score))
    except Exception:
        pass
```

  - `scoreboard.py` 的 `check_high_score()` 在分数被更新后调用，用于检测并在刷新高分时更新显示：

```python
def check_high_score(self):
    if self.stats.score > self.stats.high_score:
        self.stats.high_score = self.stats.score
        self.prep_high_score()
```


