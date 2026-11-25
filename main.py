"""Write one childhood memory sentence to /output/entry.txt.

The memory: catching fireflies in a jar on a summer evening.
"""

import os

SENTENCE = (
    "Every August evening, barefoot in the damp grass, I chased fireflies "
    "into a jam jar with holes punched in the lid, and by bedtime their "
    "light had faded to nothing, so I unscrewed it in the dark and let "
    "them go."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
