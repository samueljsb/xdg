import os
import unittest.mock
from pathlib import Path

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


class TestDataDirs:
    def test_read_from_environment(self) -> None:
        with unittest.mock.patch.dict(
            os.environ, {'XDG_DATA_DIRS': '/my-data:/other-data'}, clear=True
        ):
            data_dirs = xdg.data_dirs()

        assert data_dirs == ('/my-data', '/other-data')

    def test_default_if_empty(self) -> None:
        with unittest.mock.patch.dict(
            os.environ, {'XDG_DATA_DIRS': ''}, clear=True
        ):
            data_dirs = xdg.data_dirs()

        assert data_dirs == ('/usr/local/share/', '/usr/share/')

    def test_default_if_not_set(self) -> None:
        with unittest.mock.patch.dict(os.environ, {}, clear=True):
            data_dirs = xdg.data_dirs()

        assert data_dirs == ('/usr/local/share/', '/usr/share/')

    def test_relative_paths_ignored(self) -> None:
        with unittest.mock.patch.dict(
            os.environ,
            {'XDG_DATA_DIRS': './relative-data:/other-data'},
            clear=True,
        ):
            data_dirs = xdg.data_dirs()

        assert data_dirs == ('/other-data',)

    def test_default_if_all_relative_paths(self) -> None:
        with unittest.mock.patch.dict(
            os.environ,
            {'XDG_DATA_DIRS': './relative-data:./other-relative-data'},
            clear=True,
        ):
            data_dirs = xdg.data_dirs()

        assert data_dirs == ('/usr/local/share/', '/usr/share/')


class TestFindDataFiles:
    def test_finds_files_in_all_dirs(self, tmp_path: Path) -> None:
        # create `foo.txt` in data home and all other data dirs
        (tmp_path / 'data-home').mkdir()
        (tmp_path / 'data-home' / 'foo.txt').touch()
        (tmp_path / 'data-one').mkdir()
        (tmp_path / 'data-one' / 'foo.txt').touch()
        (tmp_path / 'data-two').mkdir()
        (tmp_path / 'data-two' / 'foo.txt').touch()

        with unittest.mock.patch.dict(
            os.environ,
            {
                'XDG_DATA_HOME': str(tmp_path / 'data-home'),
                'XDG_DATA_DIRS': (
                    f'{tmp_path / "data-one"}:{tmp_path / "data-two"}'
                ),
            },
            clear=True,
        ):
            files = xdg.find_data('foo.txt')

        assert files == (
            str(tmp_path / 'data-home' / 'foo.txt'),
            str(tmp_path / 'data-one' / 'foo.txt'),
            str(tmp_path / 'data-two' / 'foo.txt'),
        )

    def test_ignores_missing_files(self, tmp_path: Path) -> None:
        # create `foo.txt` in one data dirs
        (tmp_path / 'data-home').mkdir()
        (tmp_path / 'data-one').mkdir()
        (tmp_path / 'data-one' / 'foo.txt').touch()
        (tmp_path / 'data-two').mkdir()

        with unittest.mock.patch.dict(
            os.environ,
            {
                'XDG_DATA_HOME': str(tmp_path / 'data-home'),
                'XDG_DATA_DIRS': (
                    f'{tmp_path / "data-one"}:{tmp_path / "data-two"}'
                ),
            },
            clear=True,
        ):
            files = xdg.find_data('foo.txt')

        assert files == (str(tmp_path / 'data-one' / 'foo.txt'),)


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


class TestConfigDirs:
    def test_read_from_environment(self) -> None:
        with unittest.mock.patch.dict(
            os.environ,
            {'XDG_CONFIG_DIRS': '/my-config:/other-config'},
            clear=True,
        ):
            config_dirs = xdg.config_dirs()

        assert config_dirs == ('/my-config', '/other-config')

    def test_default_if_empty(self) -> None:
        with unittest.mock.patch.dict(
            os.environ, {'XDG_CONFIG_DIRS': ''}, clear=True
        ):
            config_dirs = xdg.config_dirs()

        assert config_dirs == ('/etc/xdg',)

    def test_default_if_not_set(self) -> None:
        with unittest.mock.patch.dict(os.environ, {}, clear=True):
            config_dirs = xdg.config_dirs()

        assert config_dirs == ('/etc/xdg',)

    def test_relative_paths_ignored(self) -> None:
        with unittest.mock.patch.dict(
            os.environ,
            {'XDG_CONFIG_DIRS': './relative-config:/other-config'},
            clear=True,
        ):
            config_dirs = xdg.config_dirs()

        assert config_dirs == ('/other-config',)

    def test_default_if_all_relative_paths(self) -> None:
        with unittest.mock.patch.dict(
            os.environ,
            {'XDG_CONFIG_DIRS': './relative-config:./other-relative-config'},
            clear=True,
        ):
            config_dirs = xdg.config_dirs()

        assert config_dirs == ('/etc/xdg',)


class TestFindConfigFiles:
    def test_finds_files_in_all_dirs(self, tmp_path: Path) -> None:
        # create `foo.txt` in config home and all other config dirs
        (tmp_path / 'config-home').mkdir()
        (tmp_path / 'config-home' / 'foo.txt').touch()
        (tmp_path / 'config-one').mkdir()
        (tmp_path / 'config-one' / 'foo.txt').touch()
        (tmp_path / 'config-two').mkdir()
        (tmp_path / 'config-two' / 'foo.txt').touch()

        with unittest.mock.patch.dict(
            os.environ,
            {
                'XDG_CONFIG_HOME': str(tmp_path / 'config-home'),
                'XDG_CONFIG_DIRS': (
                    f'{tmp_path / "config-one"}:{tmp_path / "config-two"}'
                ),
            },
            clear=True,
        ):
            files = xdg.find_config('foo.txt')

        assert files == (
            str(tmp_path / 'config-home' / 'foo.txt'),
            str(tmp_path / 'config-one' / 'foo.txt'),
            str(tmp_path / 'config-two' / 'foo.txt'),
        )

    def test_ignores_missing_files(self, tmp_path: Path) -> None:
        # create `foo.txt` in one config dirs
        (tmp_path / 'config-home').mkdir()
        (tmp_path / 'config-one').mkdir()
        (tmp_path / 'config-one' / 'foo.txt').touch()
        (tmp_path / 'config-two').mkdir()

        with unittest.mock.patch.dict(
            os.environ,
            {
                'XDG_CONFIG_HOME': str(tmp_path / 'config-home'),
                'XDG_CONFIG_DIRS': (
                    f'{tmp_path / "config-one"}:{tmp_path / "config-two"}'
                ),
            },
            clear=True,
        ):
            files = xdg.find_config('foo.txt')

        assert files == (str(tmp_path / 'config-one' / 'foo.txt'),)


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
