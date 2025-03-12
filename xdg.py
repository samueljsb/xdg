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


def data_dirs() -> tuple[str, ...]:
    """Directories in which to search for user-specific data files.

    This set of directories is defined by the environment variable
    $XDG_DATA_DIRS. The directories in $XDG_DATA_DIRS should be separated with
    a colon ':'. If $XDG_DATA_DIRS is either not set or empty, a value equal to
    /usr/local/share/:/usr/share/ will be used.

    The order of base directories denotes their importance; the first directory
    listed is the most important. When the same information is defined in
    multiple places the information defined relative to the more important base
    directory takes precedent. The base directory defined by $XDG_DATA_HOME is
    considered more important than any of the base directories defined by
    $XDG_DATA_DIRS.

    All paths set in environment variables must be absolute. If $XDG_DATA_DIRS
    contains a relative path it will be ignored.

    See <https://specifications.freedesktop.org/basedir-spec/latest/> for more
    information.
    """
    xdg_data_dirs = os.getenv('XDG_DATA_DIRS')
    if xdg_data_dirs:
        dirs = xdg_data_dirs.split(':')
        dirs = [dir_ for dir_ in dirs if os.path.isabs(dir_)]
        if dirs:
            return tuple(dirs)

    return ('/usr/local/share/', '/usr/share/')


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


def config_dirs() -> tuple[str, ...]:
    """Directories in which to search for user-specific configuration files.

    This set of directories is defined by the environment variable
    $XDG_CONFIG_DIRS. The directories in $XDG_CONFIG_DIRS should be separated
    with a colon ':'. If $XDG_CONFIG_DIRS is either not set or empty, a value
    equal to /usr/local/share/:/usr/share/ will be used.

    The order of base directories denotes their importance; the first directory
    listed is the most important. When the same information is defined in
    multiple places the information defined relative to the more important base
    directory takes precedent. The base directory defined by $XDG_CONFIG_HOME
    is considered more important than any of the base directories defined by
    $XDG_CONFIG_DIRS.

    All paths set in environment variables must be absolute. If
    $XDG_CONFIG_DIRS contains a relative path it will be ignored.

    See <https://specifications.freedesktop.org/basedir-spec/latest/> for more
    information.
    """
    xdg_config_dirs = os.getenv('XDG_CONFIG_DIRS')
    if xdg_config_dirs:
        dirs = xdg_config_dirs.split(':')
        dirs = [dir_ for dir_ in dirs if os.path.isabs(dir_)]
        if dirs:
            return tuple(dirs)

    return ('/etc/xdg',)


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
