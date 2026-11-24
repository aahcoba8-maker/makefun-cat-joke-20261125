"""One-line cat joke entry for make.fun.

Writes the joke to entry.txt in the output directory.
"""

import os

JOKE = "My cat stopped meowing at me \u2014 now he just sighs, like a landlord who found out the rent is late."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(JOKE)

if __name__ == "__main__":
    main()
