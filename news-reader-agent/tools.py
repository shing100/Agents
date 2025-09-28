from crewai.tools import tool

@tool
def count_letters(text: str) -> int:
    """Count the number of letters in a given text."""
    return sum(c.isalpha() for c in text)