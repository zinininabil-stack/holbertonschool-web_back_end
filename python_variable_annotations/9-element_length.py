i: int
lst: list


def element_length(lst: list[str]) -> list[tuple[str,int]]:
    return [(i, len(i)) for i in lst]
