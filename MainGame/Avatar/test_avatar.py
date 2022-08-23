import unittest
import avatar as avatar

# Tests to confirm changes made in avatar.py are saved and retrievable across different modules
class TestGlobalSync(unittest.TestCase):
    def test_initial_tickets(self):
        avatar_obj = avatar.AvatarSelect()
        result = avatar_obj.get_tickets()
        assert result == 100
    def test_current_avatar(self):
        avatar_obj = avatar.AvatarSelect()
        result = str(avatar_obj.get_current_avatar())
        assert result == "default_avatar"
