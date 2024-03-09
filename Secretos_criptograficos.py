from typing import List
from bsvlib.hd import mnemonic_from_entropy, Xprv, derive_xprvs_from_mnemonic,derive_xkeys_from_xkey
from bsvlib import Key,verify_signed_text

#
# HD derivation
#
entropy = 'cd9b819d9c62f0027116c1849e7d497f'

# snow swing guess decide congress abuse session subway loyal view false zebra
mnemonic: str = mnemonic_from_entropy(entropy)
#print(mnemonic)

keys: List[Xprv] = derive_xprvs_from_mnemonic(mnemonic, path="m/44'/0'/0'", change=1, index_start=0, index_end=5)
for key in keys:
    #print(key.address(), key.private_key().wif())
    print(key)


