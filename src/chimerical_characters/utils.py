import os
from pathlib import Path
import sys


def _posixify(name: str) -> str:
    return "-".join(name.split()).lower()


def get_app_dir(app_name: str, roaming: bool = True, force_posix: bool = False) -> Path:
    r"""Returns the config folder for the application.  The default behavior
    is to return whatever is most appropriate for the operating system.

    To give you an idea, for an app called ``"Foo Bar"``, something like
    the following folders could be returned:

    Mac OS X:
      ``~/Library/Application Support/Foo Bar``
    Mac OS X (POSIX):
      ``~/.foo-bar``
    Unix:
      ``~/.config/foo-bar``
    Unix (POSIX):
      ``~/.foo-bar``
    Windows (roaming):
      ``C:\Users\<user>\AppData\Roaming\Foo Bar``
    Windows (not roaming):
      ``C:\Users\<user>\AppData\Local\Foo Bar``

    .. versionadded:: 2.0

    :param app_name: the application name.  This should be properly capitalized
                     and can contain whitespace.
    :param roaming: controls if the folder should be roaming or not on Windows.
                    Has no effect otherwise.
    :param force_posix: if this is set to `True` then on any POSIX system the
                        folder will be stored in the home folder with a leading
                        dot instead of the XDG config home or darwin's
                        application support folder.
    """
    if sys.platform.startswith("win"):
        key = "APPDATA" if roaming else "LOCALAPPDATA"
        folder = os.environ.get(key)
        if folder is None:
            folder = Path.home()
        return Path(folder, app_name)
    if force_posix:
        return Path(Path.home(), f".{_posixify(app_name)}")
    if sys.platform == "darwin":
        return Path(Path.home(), "Library/Application Support", app_name)
    return Path(
        os.environ.get("XDG_CONFIG_HOME", os.path.expanduser("~/.config")),
        _posixify(app_name),
    )


if __name__ == "__main__":
    import click
    print(click.get_app_dir("test"))
    print(get_app_dir("test"))
    assert Path(click.get_app_dir("test")) == get_app_dir("test")
