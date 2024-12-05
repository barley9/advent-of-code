class TrieNode():
    orda = ord('a')
    alpha = set(chr(i) for i in range(ord('a'), ord('z') + 1))

    def __init__(self):
        self._children = [None] * 26
        self._word_end = [False] * 26

    def insert(self, word: str) -> None:
        if not word:
            return

        i = ord(word[0]) - self.orda
        if not self._children[i]:
            self._children[i] = TrieNode()
        self._children[i].insert(word[1:])

        if len(word) == 1:
            self._word_end[i] = True

    def remove(self, word: str) -> None:
        raise NotImplementedError

    def contains(self, word: str) -> bool:
        i = ord(word[0]) - self.orda
        if not self._children[i]:
            return False
        elif len(word) == 1:
            return self._word_end[i]
        else:
            return self._children[i].contains(word[1:])

    def contains_prefix(self, prefix: str) -> bool:
        if not prefix:
            return True
        i = ord(prefix[0]) - self.orda
        return self._children[i] and self._children[i].contains_prefix(prefix[1:])

    def pretty_print(self, depth=0) -> None:
        for i, c in enumerate(self._children):
            if c:
                print(' ' * depth + chr(i + self.orda) + ('.' if self._word_end[i] else ''))
                c.pretty_print(depth + 1)


if __name__ == '__main__':
    t = TrieNode()
    words = ['abet', 'able', 'abs', 'ab', 'box']
    for word in words:
        t.insert(word)
    t.pretty_print()

    for word in words:
        assert t.contains(word)

    for word in ['a', 'b', 'boxes']:
        assert not t.contains(word)

    assert t.contains(['a', 'b'])  # any iterable of characters also works