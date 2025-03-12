import os
import unittest.mock

import xdg


class TestDataHome:
    def test_read_from_environment(self) -> None:
        with unittest.mock.patch.dict(
            os.environ, {'XDG_DATA_HOME': '/my-data'}, clear=True
        ):
            data_home = xdg.data_home()

        assert data_home == '/my-data'

    def test_default_if_empty(self) -> None:
        with unittest.mock.patch.dict(
            os.environ,
            {'HOME': '/home/my-user', 'XDG_DATA_HOME': ''},
            clear=True,
        ):
            data_home = xdg.data_home()

        assert data_home == '/home/my-user/.local/share'

    def test_default_if_not_set(self) -> None:
        with unittest.mock.patch.dict(
            os.environ, {'HOME': '/home/my-user'}, clear=True
        ):
            data_home = xdg.data_home()

        assert data_home == '/home/my-user/.local/share'

    def test_default_if_relative_path(self) -> None:
        with unittest.mock.patch.dict(
            os.environ,
            {'HOME': '/home/my-user', 'XDG_DATA_HOME': './my-data'},
            clear=True,
        ):
            data_home = xdg.data_home()

        assert data_home == '/home/my-user/.local/share'


class TestConfigHome:
    def test_read_from_environment(self) -> None:
        with unittest.mock.patch.dict(
            os.environ, {'XDG_CONFIG_HOME': '/my-config'}, clear=True
        ):
            config_home = xdg.config_home()

        assert config_home == '/my-config'

    def test_default_if_empty(self) -> None:
        with unittest.mock.patch.dict(
            os.environ,
            {'HOME': '/home/my-user', 'XDG_CONFIG_HOME': ''},
            clear=True,
        ):
            config_home = xdg.config_home()

        assert config_home == '/home/my-user/.config'

    def test_default_if_not_set(self) -> None:
        with unittest.mock.patch.dict(
            os.environ, {'HOME': '/home/my-user'}, clear=True
        ):
            config_home = xdg.config_home()

        assert config_home == '/home/my-user/.config'

    def test_default_if_relative_path(self) -> None:
        with unittest.mock.patch.dict(
            os.environ,
            {'HOME': '/home/my-user', 'XDG_CONFIG_HOME': './my-config'},
            clear=True,
        ):
            config_home = xdg.config_home()

        assert config_home == '/home/my-user/.config'


class TestStateHome:
    def test_read_from_environment(self) -> None:
        with unittest.mock.patch.dict(
            os.environ, {'XDG_STATE_HOME': '/my-state'}, clear=True
        ):
            state_home = xdg.state_home()

        assert state_home == '/my-state'

    def test_default_if_empty(self) -> None:
        with unittest.mock.patch.dict(
            os.environ,
            {'HOME': '/home/my-user', 'XDG_STATE_HOME': ''},
            clear=True,
        ):
            state_home = xdg.state_home()

        assert state_home == '/home/my-user/.local/state'

    def test_default_if_not_set(self) -> None:
        with unittest.mock.patch.dict(
            os.environ, {'HOME': '/home/my-user'}, clear=True
        ):
            state_home = xdg.state_home()

        assert state_home == '/home/my-user/.local/state'

    def test_default_if_relative_path(self) -> None:
        with unittest.mock.patch.dict(
            os.environ,
            {'HOME': '/home/my-user', 'XDG_STATE_HOME': './my-state'},
            clear=True,
        ):
            state_home = xdg.state_home()

        assert state_home == '/home/my-user/.local/state'


class TestCacheHome:
    def test_read_from_environment(self) -> None:
        with unittest.mock.patch.dict(
            os.environ, {'XDG_CACHE_HOME': '/my-cache'}, clear=True
        ):
            cache_home = xdg.cache_home()

        assert cache_home == '/my-cache'

    def test_default_if_empty(self) -> None:
        with unittest.mock.patch.dict(
            os.environ,
            {'HOME': '/home/my-user', 'XDG_CACHE_HOME': ''},
            clear=True,
        ):
            cache_home = xdg.cache_home()

        assert cache_home == '/home/my-user/.cache'

    def test_default_if_not_set(self) -> None:
        with unittest.mock.patch.dict(
            os.environ, {'HOME': '/home/my-user'}, clear=True
        ):
            cache_home = xdg.cache_home()

        assert cache_home == '/home/my-user/.cache'

    def test_default_if_relative_path(self) -> None:
        with unittest.mock.patch.dict(
            os.environ,
            {'HOME': '/home/my-user', 'XDG_CACHE_HOME': './my-cache'},
            clear=True,
        ):
            cache_home = xdg.cache_home()

        assert cache_home == '/home/my-user/.cache'
