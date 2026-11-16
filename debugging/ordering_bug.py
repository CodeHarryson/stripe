def chronological(values: list[str]) -> list[str]:
    """Sort non-negative integer timestamp strings by numeric value."""
    return sorted(values, key=lambda x:int(x))

if __name__ == "__main__":
    # The returned values must remain strings.
    assert chronological([]) == []
    assert chronological(["10", "2", "1"]) == ["1", "2", "10"]
    assert chronological(["100", "2", "11", "2"]) == ["2", "2", "11", "100"]

    result = chronological(["20", "3"])
    assert result == ["3", "20"]
    assert all(isinstance(value, str) for value in result)

    print("All ordering tests passed!")

