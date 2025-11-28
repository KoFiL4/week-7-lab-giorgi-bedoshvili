import subprocess
from pathlib import Path

source_file = Path("week 7 lab bedoshvili 3.py")
output_file = Path("week 7 lab bedoshvili 4.py")

with open(output_file, "w") as f:
    subprocess.run([
        "pyminifier",   # აქ უნდა იყოს pyminifier, არა pyminifier3
        "--obfuscate-builtins",
        "--replacement-length=3",
        str(source_file)
    ], stdout=f)

print(f"[OK] Obfuscation complete. Obfuscated file saved as: {output_file.resolve()}")
