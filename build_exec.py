import subprocess


def run_pyinstaller_command():
    command = [
        'pyinstaller',
        '.\\app\\main.py',
        '--name', 'FilePartner',
        '--icon', '"./app/assets/icon/logo.ico"',
        '--add-data', '"./app/assets;app/assets"',
        '--add-data', '"./app/config.json;app"',
        '--windowed',
        '--noconfirm',
        '--version-file', '"./file_version_info.txt"'
    ]

    # Joining the command elements into a single string
    command_str = ' '.join(command)

    # Running the command using subprocess
    subprocess.run(command_str, shell=True)


if __name__ == '__main__':
    run_pyinstaller_command()
