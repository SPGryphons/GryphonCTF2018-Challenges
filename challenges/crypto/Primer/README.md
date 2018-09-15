# Primer

## Question Text

RSA, so simple!

*Creator - PotatoDrug*

## Distribution
- Primer.txt
    - SHA1: `534e1d259473068a1e60b84b5141e65f29b02296`
    - Contains e,n and c

## Solution
Put `n` into [factordb](https://factordb.com/index.php?query=17969491597941066732916128449573246156367561808012600070888918835531726460341490933493372247868650755230855864199929221814436684722874052065257937495694348389263171152522525654410980819170611742509702440718010364831638288518852689) to get `p` and `q`. Use that to calculate `d` and decrypt the ciphertext.

[Sample solution](solution/solve.py)

### Flag
`GCTF{r54_15_345Y_1F_Y0U_C4n_f4C70r_17}`