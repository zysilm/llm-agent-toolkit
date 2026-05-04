"""Tool output truncation via middle-elision."""


def truncate_output(text: str, max_chars: int = 10000) -> str:
    """Truncate *text* to at most *max_chars* using middle-elision.

    If the text fits within the budget it is returned unchanged.  Otherwise the
    first ``max_chars // 2`` characters and the last ``max_chars - left``
    characters are kept, separated by a marker that reports the number of
    removed characters.

    Python strings are sequences of Unicode code-points, so character-level
    slicing is inherently unicode-safe.
    """
    if not text or len(text) <= max_chars:
        return text

    left = max_chars // 2
    right = max_chars - left
    removed = len(text) - left - right
    marker = (
        f"\n<response clipped>\n"
        f"<NOTE>{removed} characters were elided. "
        f"Use head/tail/grep to get specific parts, "
        f"or redirect output to a file.</NOTE>\n"
    )
    return text[:left] + marker + text[len(text) - right:]
