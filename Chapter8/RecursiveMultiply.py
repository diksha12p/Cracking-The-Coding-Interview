class Multiplication:
    def recursive_multiply(self, a: int, b: int) -> int:
        # smaller = a if a < b else b
        # larger = b if a < b else a
        smaller = min(a, b)
        larger = a+b-smaller
        return self._helper(smaller, larger)

    def _helper(self, small: int, big: int) -> int:
        if small == 0: return 0
        if small == 1: return big
        about_half = self._helper(small >> 1, big)
        return 2 * about_half if not small % 2 else 2 * about_half + big


if __name__ == '__main__':
    mul = Multiplication()
    assert (mul.recursive_multiply(3,4)) == 12
    assert (mul.recursive_multiply(4,4)) == 16
    assert (mul.recursive_multiply(99,4)) == 396
    assert (mul.recursive_multiply(13,0)) == 0
    assert (mul.recursive_multiply(1, 1)) == 1

