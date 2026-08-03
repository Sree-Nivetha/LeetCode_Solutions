class Solution:
    def minimumPushes(self, word: str) -> int:
        letter_counter = Counter(word)
        frequencies = list(letter_counter.values())
        frequencies.sort(reverse = True)
        min_push = 0
        for i in range(len(frequencies)):
            min_push += frequencies[i] * ((i//8) + 1)

        return min_push