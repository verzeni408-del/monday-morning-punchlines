import os

SETUP = "My alarm rang at 6am Monday. I said 'five more minutes.'"
PUNCHLINE = "It called my boss and told him I'm awake."
ENTRY = SETUP + " " + PUNCHLINE

OUT_PATH = "/output/entry.txt"

def main():
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
