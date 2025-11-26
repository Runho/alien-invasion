import os


class GameStats:
    """Track statistics for Alien Invasion, with persistent high score."""

    # Store high score in a file next to this module by default.
    HIGH_SCORE_FILENAME = os.path.join(os.path.dirname(__file__), 'high_score.txt')

    def __init__(self, ai_game):
        """Initialize statistics and load persisted high score."""
        self.settings = ai_game.settings
        self.reset_stats()

        # High score should never be reset; load from file if available.
        self.high_score = self._load_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _load_high_score(self):
        """Read the high score from a file. Return 0 if not available."""
        try:
            with open(self.HIGH_SCORE_FILENAME, 'r', encoding='utf-8') as f:
                return int(f.read().strip() or 0)
        except Exception:
            return 0

    def save_high_score(self):
        """Write the current high score to the high score file.

        Errors are swallowed so saving never crashes the game.
        """
        try:
            with open(self.HIGH_SCORE_FILENAME, 'w', encoding='utf-8') as f:
                f.write(str(self.high_score))
        except Exception:
            pass