"""The Most Honest Outage Line.

Writes a single honest status-page line for a total outage to
/output/entry.txt. The line is written by the reporting service
itself, which is also down, so it states what is down and admits
what cannot be verified: no cause is invented, and no ETA is given.
"""

ENTRY = (
    "All services are down. I am the service that reports outages, "
    "and I am also down. I do not know when we will be back."
)


def main() -> None:
    """Write the entry line to /output/entry.txt (UTF-8, one line)."""
    import os

    os.makedirs("/output", exist_ok=True)
    # Write the entry verbatim, as a single line, with nothing added.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
