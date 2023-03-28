from functools import reduce
from copy import copy


class BinPoly:
    def __init__(self, coefs):
        assert all(map(lambda x: x in (0,1), coefs)), ValueError("All coefficients must be 1 or 0")

        self._coefs = list(coefs)
        while self._coefs:
            if not self._coefs[0]:
                self._coefs.pop(0)
            else:
                break

        self._degree = len(self._coefs) - 1

    @property
    def degree(self):
        return self._degree

    @property
    def coefficients(self):
        return copy(self._coefs)

    def __str__(self):
        return " + ".join(f"x**{self._degree-i}" for i, coef in enumerate(self._coefs) if coef) if self._coefs \
            else "0"

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        coefs = []
        for i in range(max(self._degree, other._degree)+1):
            coefs.insert(0, self[i] ^ other[i])

        return BinPoly(coefs)

    def __mul__(self, other):
        n = self._degree + other._degree + 1

        coefs = []
        for k in range(n):
            coefs.insert(0, reduce(lambda x, y: x ^ y, (self[i] * other[k-i] for i in range(k+1))))

        return BinPoly(coefs)

    def __mod__(self, other):
        curr = self

        while curr._degree >= other._degree:
            diff = curr._degree - other._degree
            curr = curr + other * BinPoly([1] + [0]*diff)

        return curr

    def __getitem__(self, item):
        assert isinstance(item, int) and item > -1, IndexError("Only non-negative integer indexes are allowed")

        return self._coefs[self._degree - item] if item <= self._degree else 0


class AESFieldElement:
    POLYGON = BinPoly([1, 0, 0, 0, 1, 1, 0, 1, 1])

    def __init__(self, bits):
        assert all(map(lambda x: x in (0, 1), bits)), ValueError("All bits must be 1 or 0")

        self._bits = list(bits)

    @property
    def bin(self):
        return "".join(str(b) for b in self._bits)

    @property
    def hex(self):
        bitstr = "".join(str(b) for b in self._bits)
        return hex(int(bitstr, 2))[2:]

    @property
    def int(self):
        bitstr = "".join(str(b) for b in self._bits)
        return int(bitstr, 2)

    @property
    def poly(self):
        return BinPoly(self._bits)

    def __add__(self, other):
        p1 = BinPoly(self._bits)
        p2 = BinPoly(other._bits)

        res = p1 + p2
        return AESFieldElement(res.coefficients)

    def __mul__(self, other):
        p1 = BinPoly(self._bits)
        p2 = BinPoly(other._bits)

        res = (p1 * p2) % AESFieldElement.POLYGON
        return AESFieldElement(res.coefficients)


def frombin(bitstr):
    return AESFieldElement([int(c) for c in bitstr])


def fromhex(hexstr):
    bitstr = bin(int(hexstr, 16))[2:].zfill(8)
    return AESFieldElement([int(c) for c in bitstr])


def fromint(n):
    bitstr = bin(n)[2:].zfill(8)
    return AESFieldElement([int(c) for c in bitstr])


if __name__ == "__main__":
    p1 = BinPoly([1, 1, 0, 1, 1, 1, 1, 0])
    p2 = BinPoly([1, 1, 0, 1, 1, 1, 1])
    p3 = BinPoly([0, 0, 0])
    print(f"p1 = {p1}\np2 = {p2}\np3 = {p3}")
    print(f"p1 + p2 = {p1 + p2}")
    print(f"p1 + p1 = {p1 + p1}")
    print(f"p2 + p3 = {p2 + p3}")
    print(f"p1 * p2 = {p1 * p2}")
    print(f"p1 * p3 = {p1 * p3}")
    print(f"p2 * p2 = {p2 * p2}")
    print((p1 * p2) % BinPoly([1,0,0,0,1,1,1,0,1]))

    print("\n")

    a = fromhex("d7") + fromhex("3c")
    print(a.int, a.bin, a.hex)

    a = fromint(200) * fromint(100)
    print(a.int, a.bin, a.hex)

    a = frombin("10010111") * frombin("01010111")
    print(a.int, a.bin, a.hex)


