
import random
import pandas as pd


def caesar(string, n):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sis = string.replace("'", '').replace(' ', '').replace(',', '').replace('.', '').upper()
    res = ''
    for i in range(len(sis)):
        res += alpha[(alpha.index(sis[i]) + n) % len(alpha)]
    print(res)
    print(sis)


def bruteforce(text, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    i = 1
    while i != len(alphabet):
        sis = text.upper()
        end = ''
        for j in range(len(text)):
            end += alphabet[(alphabet.index(sis[j]) - i) % len(alphabet)]
        i += 1
        print(end)


def encrypter(text, fro, to):
    lst = []
    while fro < to:
        alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        numbers = [int(i) for i in str(fro)]
        end = ''
        sis = text.upper().replace(' ', '')
        for i in range(len(sis)):
            try:
                end += alphabet[(alphabet.index(sis[i]) - numbers[i % len(numbers)]) % len(alphabet)]
            except ValueError:
                print(sis[i])
        if 'АЛМАЗ' in end or "Дакоста" in end or "ПРЕСТУП" in end or 'ЖАРРИКЕС' in end:
            lst.append(end)
            lst.append(fro)
            lst.append("_____________________________________________________________________________________")

        fro += 1
    print(lst)


def kidds_encryption(text, reverse=False):
    cypher = {'e': '8', 't': ';', 'h': '4', 'o': '‡', 's': ')', 'n': '*', 'a': '5', 'i': '6', 'r': '(', 'f': '1',
              'd': '†', 'l': '0', 'm': '9', 'b': '2', 'y': ':', 'g': '3', 'u': '?', 'v': '¶', 'c': '-', 'p': '.'}
    end = ''
    for i in range(len(text)):
        if reverse == False:
            if text[i] in cypher:
                end += cypher[text[i]]
        else:
            if text[i] in cypher.values():
                for k, v in cypher.items():
                    if v == text[i]:
                        end += k
    return (end)


def mimic_dict(string):
    sis = string.split()
    dct = {"": [sis[0]]}
    for i in range(len(sis) - 1):
        if sis[i] in dct.keys():
            dct[sis[i]].append(sis[i + 1])
        else:
            dct.setdefault(sis[i], [sis[i + 1]])
    return dct

def reflector(symbol, n):
    rotors = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
              1: 'YRUHQSLDPXNGOKMIEBFZCWVJAT',
              2: 'FVPJIAOYEDRZXWGCTKUQSBNMHL',
              3: 'ENKQAUYWJICOPBLMDXZVFTHRGS',
              4: 'RDOBJNTKVEHMLFCWZAXGYIPSUQ',
              }
    end = ''
    for i in range(len(symbol)):
        end += rotors[n][(rotors[0].index(symbol[i]))]
    return (end)


def enigma(text, ref, rot1, shift1, rot2, shift2, rot3, shift3):
    sis = text.upper()
    end = ''
    rotors = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
              1: 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
              2: 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
              3: 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
              4: 'ESOVPZJAYQUIRHXLNFTGKDCMWB',
              5: 'VZBRGITYUPSDNHLXAWMJQOFECK',
              6: 'JPGVOUMFYQBENHZRDKASXLICTW',
              7: 'NZJHGRCXMYSWBOUFAIVLPEKQDT',
              8: 'FKQHTLXOCBJSPDZRAMEWNIUYGV',
              'beta': 'LEYJVCNIXWPBQMDRTAKZGFUHOS',
              'gamma': 'FSOKANUERHMBTIYCWLQPZXVGJD'
              }
    for i in range(1, len(sis) + 1):
        if sis[i - 1] != ' ':
            first = rotors[0][(rotors[0].index(
                rotors[rot3][(rotors[0].index(sis[i - 1]) + shift3 + i) % len(rotors[0])]) - shift3) % len(rotors[0])]
            if (i - 1 + shift2) == 5:
                chsecond = (rotors[0].index(
                    rotors[rot2][(rotors[0].index(first) + shift2 + i + 1) % len(rotors[0])]) - shift2) % len(rotors[0])
                second = rotors[0][chsecond]
                third = rotors[0][(rotors[0].index(
                    rotors[rot1][(rotors[0].index(second) + shift1 + 1) % len(rotors[0])]) - shift1) % len(rotors[0])]
            else:
                chsecond = (rotors[0].index(
                    rotors[rot2][(rotors[0].index(first) + shift2 + i) % len(rotors[0])]) - shift2) % len(rotors[0])
                second = rotors[0][chsecond]
                third = rotors[0][
                    (rotors[0].index(rotors[rot1][(rotors[0].index(second) + shift1) % len(rotors[0])]) - shift1) % len(
                        rotors[0])]

            reflect = reflector(third, ref)
            changethird = rotors[0][((rotors[0].index(reflect) + shift1)) % len(rotors[0])]
            rethird = rotors[0][rotors[rot1].index(changethird)]
            changesecond = rotors[0][(rotors[0].index(rethird) - shift1 + shift2) % len(rotors[0])]
            resecond = rotors[0][rotors[rot2].index(changesecond)]
            changefirst = rotors[0][(rotors[0].index(resecond) - shift2 + shift3) % len(rotors[0])]
            refirst = rotors[0][rotors[rot3].index(changefirst)]
            end += rotors[0][(rotors[0].index(refirst) - shift3) % len(rotors[0])]
            print(first, second, third, reflect, rethird, resecond, refirst)
    print(end)

    # resecond=rotors[0][rotors[0].index(rotors[rot1][rotors[0].index(rethird)-shift1])+shift1]




def print_mimic(text, n):
    end = ''
    word = n
    for i in range(200):
        if i != 199:
            try:
                random.choice(text[word])
                end += word + ' '
                word = random.choice(text[word])
            except KeyError:
                end += word + ' '
                word = random.choice(text[''])
        else:
            try:
                random.choice(text[word])
                end += word
                word = random.choice(text[word])
            except KeyError:
                end += word
                word = random.choice(text[''])
    print(end)

