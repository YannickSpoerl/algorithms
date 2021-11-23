def huffman(letters: dict[str, float]) -> dict[str, str]:
    """given a dictionary of letters and their frequencie, compute minimal prefix-free coding
    :param letters: dictionary of letters with their respective frequencies (0 < f < 1)
    :return: a dictionary with the letters and their computed coding
    """
    coding = {}
    for letter in letters:
        coding[letter] = ""
    while len(letters) > 1:
        min1 = None
        min1_freq = None
        for letter in letters:
            if min1 is None or letters[letter] < letters[min1]:
                min1 = letter
                min1_freq = letters[min1]
        letters.pop(min1)
        min2 = None
        min2_freq = None
        for letter in letters:
            if min2 is None or letters[letter] < letters[min2]:
                min2 = letter
                min2_freq = letters[min2]
        letters.pop(min2)

        for character in min1:
            coding[character] = "1" + coding[character]
        for character in min2:
            coding[character] = "0" + coding[character]

        letters[f"{min2}{min1}"] = min1_freq + min2_freq

    return coding
