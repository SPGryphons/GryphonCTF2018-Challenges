# Lupusregina

## Question Text

I have intercepted this encrypted EMAIL message sent to Lupusregina, see if you can find any useful intel.

*Creator - PotatoDrug*

### Hints (Optional)
1. What is the first line when you write emails?

## Setup Guide
1. Run `distrib/Lupusregina.py -f generate/plaintext -o distrib/Lupusregina -a 6364136223846793005 -c 12820163 -s 5`

## Distribution
- Lupusregina
    - SHA1: `fab951ae5e3c8a381955da9ec5859e2642d30a2a`
    - Encrypted file
- Lupusregina.py
    - SHA1: `224ddc605748de0cee637653f697feaef1e00866`
    - Source code

## Solution

```python
# Linear Congruential Generator

'''
p is modulo defined as 0 < p
a is the multiplier defined as 0 < a < p
c is the increment 0 <= c < p ( if c = 0 the LCG is called Multiplicative 
'''
def lcg(seed, a, c, p):
    last = (a * seed + c) % p
    while True:
        yield last
        last = (a * last + c) % p
```

[Sample solution](solution/solve.py)

### Flag
`GCTF{8R0k3N_Rn9_M4K35_8r0k3N_C1ph3R2}`
