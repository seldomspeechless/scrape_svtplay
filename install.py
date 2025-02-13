import os
import subprocess
import sys

VENV_DIR = "venv"
PIP_PACKAGES = ["requests", "beautifulsoup4"]

# create environment
def create_venv():
    """Creates a virtual environment if it doesn't exist."""
    if not os.path.exists(VENV_DIR):
        print("Creating virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", VENV_DIR], check=True)
    else:
        print("Virtual environment already exists.")

# pip bs4 and requests
def pip_installations():
    """Installs requests inside the virtual environment."""
    pip_executable = os.path.join(VENV_DIR, "bin", "pip") if os.name != "nt" else os.path.join(VENV_DIR, "Scripts", "pip.exe")
    
    print("Upgrading pip...")
    subprocess.run([pip_executable, "install", "--upgrade", "pip"], check=True)

    for package in PIP_PACKAGES:
        print(f"Installing {package}...")
        subprocess.run([pip_executable, "install", package], check=True)

if __name__ == "__main__":
    create_venv()
    pip_installations()
    print("Setup complete! To activate the virtual environment, use:")
    print(f"  source {VENV_DIR}/bin/activate" if os.name != "nt" else f"  {VENV_DIR}\\Scripts\\activate")
