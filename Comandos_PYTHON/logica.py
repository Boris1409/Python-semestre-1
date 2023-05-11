"""OPERADORES BIT A BIT """

# &  (ampersand) ‒ conjunción a nivel de bits;
# |  (barra vertical) - disyunción a nivel de bits;
# ~  (tilde) - negación a nivel de bits;
# ^  (signo de intercalación) - o exclusivo a nivel de bits (xor).

# &  requiere exactamente dos 1 s para proporcionar 1 como resultado;
# |  requiere al menos un 1 para proporcionar 1 como resultado;
# ^  requiere exactamente un 1 para proporcionar 1 como resultado.

i = 15
j = 22

log = i and j 
print(log)
print(type(log))

# x & 1 = x
# x & 0 = 0