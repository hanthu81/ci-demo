import os

version = os.getenv("VERSION", "dev")
print(f"Hello CI/CD - version {version}")
