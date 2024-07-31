def manchester_encode(data):
  enc=[]
  for b in data:
    enc += [0,1]*(b==1) + [1,0]*(b==0)
  return enc
print(manchester_encode([1,0,1]))


def mfm_encode(data):
    prev_enc_bit, enc = 0, []
    for i in range(len(data)):
        bit = data[i]
        if bit == 0:
            if prev_enc_bit == 0:
                enc_bits = [1, 0]
            else:
                enc_bits = [0, 0]
        elif bit == 1:
            enc_bits = [0, 1]
        enc.extend(enc_bits)
        prev_enc_bit = enc_bits[-1]
    return enc
print(mfm_encode([1,0,1]))
