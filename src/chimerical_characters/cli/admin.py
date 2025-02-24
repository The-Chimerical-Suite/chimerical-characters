from pathlib import Path
from typer import Typer, get_app_dir, launch


app = Typer(no_args_is_help=True)

@app.callback()
def callback():
    """
    Admin tools for the Chimerical Characters application.
    """
    pass

@app.command()
def locate_appdata():
    """
    Locate app data if it exists.
    """
    appdata = Path(get_app_dir("chimerical"))
    if appdata.exists():
        print(f"App data found at: {appdata}")
        launch(str(appdata), locate=True)
    else:
        print(f"App data does not exist. Consider using the `init_appdata` command to generate it at: {appdata}")

@app.command()
def init_appdata():
    """
    Initialise app data if it doesn't exist.
    """
    appdata = Path(get_app_dir("chimerical"))
    if appdata.exists():
        print("App data already exists.")
    else:
        appdata.mkdir()
        print(f"Empty app data has been initialised at: {appdata}")
