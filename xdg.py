"""Find files using the XDG Base Directory Specification.

See <https://specifications.freedesktop.org/basedir-spec/latest/>.
"""

import os
import os.path


def data_home() -> str:
    """A directory for user-specific data files.

    This directory is defined by the environment variable $XDG_DATA_HOME. If
    $XDG_DATA_HOME is either not set or empty, a default equal to
    $HOME/.local/share will be used.

    All paths set in environment variables must be absolute. If $XDG_DATA_HOME
    contains a relative path it will be ignored.

    See <https://specifications.freedesktop.org/basedir-spec/latest/> for more
    information.
    """
    xdg_data_home = os.getenv('XDG_DATA_HOME')
    if xdg_data_home and os.path.isabs(xdg_data_home):
        return xdg_data_home

    return os.path.expanduser('~/.local/share')


def config_home() -> str:
    """A directory for user-specific configuration files.

    This directory is defined by the environment variable $XDG_CONFIG_HOME. If
    $XDG_CONFIG_HOME is either not set or empty, a default equal to
    $HOME/.config will be used.

    All paths set in environment variables must be absolute. If
    $XDG_CONFIG_HOME contains a relative path it will be ignored.

    See <https://specifications.freedesktop.org/basedir-spec/latest/> for more
    information.
    """
    xdg_config_home = os.getenv('XDG_CONFIG_HOME')
    if xdg_config_home and os.path.isabs(xdg_config_home):
        return xdg_config_home

    return os.path.expanduser('~/.config')


def state_home() -> str:
    """A directory for user-specific state data.

    This directory is defined by the environment variable $XDG_STATE_HOME. If
    $XDG_STATE_HOME is either not set or empty, a default equal to
    $HOME/.local/state will be used.

    All paths set in environment variables must be absolute. If $XDG_STATE_HOME
    contains a relative path it will be ignored.

    See <https://specifications.freedesktop.org/basedir-spec/latest/> for more
    information.
    """
    xdg_state_home = os.getenv('XDG_STATE_HOME')
    if xdg_state_home and os.path.isabs(xdg_state_home):
        return xdg_state_home

    return os.path.expanduser('~/.local/state')


def cache_home() -> str:
    """A directory for user-specific non-essential (cached) data.

    This directory is defined by the environment variable $XDG_CACHE_HOME. If
    $XDG_CACHE_HOME is either not set or empty, a default equal to $HOME/.cache
    will be used.

    All paths set in environment variables must be absolute. If $XDG_CACHE_HOME
    contains a relative path it will be ignored.

    See <https://specifications.freedesktop.org/basedir-spec/latest/> for more
    information.
    """
    xdg_cache_home = os.getenv('XDG_CACHE_HOME')
    if xdg_cache_home and os.path.isabs(xdg_cache_home):
        return xdg_cache_home

    return os.path.expanduser('~/.cache')
