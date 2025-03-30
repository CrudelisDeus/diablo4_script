import subprocess

subprocess.run("pip freeze > requirements.txt", shell=True)
subprocess.run("pyside6-uic ui/main.ui -o ui_main.py", shell=True)
subprocess.run("pyside6-rcc rc.qrc -o rc_rc.py", shell=True)
cmd = [
    "pyinstaller",
    "--name", "D4 script",
    "--onefile",
    "--windowed",
    "--add-data", "rc_rc.py;.",
    "--add-data", "keyboard.json;.",
    "--icon", "ui/logo.ico",
    "main.py"
]
subprocess.run(cmd)