from base64 import b64decode
from os import urandom

from challenge_18 import AES_CTR_crypt, xor_byte_block
from challenge_6 import bruteforce
from challenge_3 import etaoin_frequency

encoded_texts = """SSBoYXZlIG1ldCB0aGVtIGF0IGNsb3NlIG9mIGRheQ==
    Q29taW5nIHdpdGggdml2aWQgZmFjZXM=
    RnJvbSBjb3VudGVyIG9yIGRlc2sgYW1vbmcgZ3JleQ==
    RWlnaHRlZW50aC1jZW50dXJ5IGhvdXNlcy4=
    SSBoYXZlIHBhc3NlZCB3aXRoIGEgbm9kIG9mIHRoZSBoZWFk
    T3IgcG9saXRlIG1lYW5pbmdsZXNzIHdvcmRzLA==
    T3IgaGF2ZSBsaW5nZXJlZCBhd2hpbGUgYW5kIHNhaWQ=
    UG9saXRlIG1lYW5pbmdsZXNzIHdvcmRzLA==
    QW5kIHRob3VnaHQgYmVmb3JlIEkgaGFkIGRvbmU=
    T2YgYSBtb2NraW5nIHRhbGUgb3IgYSBnaWJl
    VG8gcGxlYXNlIGEgY29tcGFuaW9u
    QXJvdW5kIHRoZSBmaXJlIGF0IHRoZSBjbHViLA==
    QmVpbmcgY2VydGFpbiB0aGF0IHRoZXkgYW5kIEk=
    QnV0IGxpdmVkIHdoZXJlIG1vdGxleSBpcyB3b3JuOg==
    QWxsIGNoYW5nZWQsIGNoYW5nZWQgdXR0ZXJseTo=
    QSB0ZXJyaWJsZSBiZWF1dHkgaXMgYm9ybi4=
    VGhhdCB3b21hbidzIGRheXMgd2VyZSBzcGVudA==
    SW4gaWdub3JhbnQgZ29vZCB3aWxsLA==
    SGVyIG5pZ2h0cyBpbiBhcmd1bWVudA==
    VW50aWwgaGVyIHZvaWNlIGdyZXcgc2hyaWxsLg==
    V2hhdCB2b2ljZSBtb3JlIHN3ZWV0IHRoYW4gaGVycw==
    V2hlbiB5b3VuZyBhbmQgYmVhdXRpZnVsLA==
    U2hlIHJvZGUgdG8gaGFycmllcnM/
    VGhpcyBtYW4gaGFkIGtlcHQgYSBzY2hvb2w=
    QW5kIHJvZGUgb3VyIHdpbmdlZCBob3JzZS4=
    VGhpcyBvdGhlciBoaXMgaGVscGVyIGFuZCBmcmllbmQ=
    V2FzIGNvbWluZyBpbnRvIGhpcyBmb3JjZTs=
    SGUgbWlnaHQgaGF2ZSB3b24gZmFtZSBpbiB0aGUgZW5kLA==
    U28gc2Vuc2l0aXZlIGhpcyBuYXR1cmUgc2VlbWVkLA==
    U28gZGFyaW5nIGFuZCBzd2VldCBoaXMgdGhvdWdodC4=
    VGhpcyBvdGhlciBtYW4gSSBoYWQgZHJlYW1lZA==
    QSBkcnVua2VuLCB2YWluLWdsb3Jpb3VzIGxvdXQu
    SGUgaGFkIGRvbmUgbW9zdCBiaXR0ZXIgd3Jvbmc=
    VG8gc29tZSB3aG8gYXJlIG5lYXIgbXkgaGVhcnQs
    WWV0IEkgbnVtYmVyIGhpbSBpbiB0aGUgc29uZzs=
    SGUsIHRvbywgaGFzIHJlc2lnbmVkIGhpcyBwYXJ0
    SW4gdGhlIGNhc3VhbCBjb21lZHk7
    SGUsIHRvbywgaGFzIGJlZW4gY2hhbmdlZCBpbiBoaXMgdHVybiw=
    VHJhbnNmb3JtZWQgdXR0ZXJseTo=
    QSB0ZXJyaWJsZSBiZWF1dHkgaXMgYm9ybi4="""

def cribdrag(xor_cipher, word):
    #word = word.encode('ascii')
    xor_len = len(xor_cipher)
    word_len = len(word)
    for i in range(0, xor_len - word_len):
        #print("Xor ",xor_cipher[i:], " with ", word)
        a = xor_byte_block(xor_cipher[i:], word)
        print(a)


if __name__ == '__main__':
    BLOCK_SIZE = 16 # no need to set, but oh well
    nonce = (0).to_bytes(8, byteorder="little") # setting to 0
    #key = urandom(BLOCK_SIZE)
    key = b'quickbrownfoxjum'

    plain_text = [b64decode(i) for i in encoded_texts.split()]
    cipher_text = [AES_CTR_crypt(key, nonce, i) for i in plain_text]

    shortest_len = min(map(len, cipher_text))
    print("Shortest length is: ", shortest_len)


    truncated_cipher_text = [cipher[:16] for cipher in cipher_text]
    print(truncated_cipher_text)
    master = bytearray().join(truncated_cipher_text)
