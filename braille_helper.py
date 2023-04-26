from gtts import gTTS
import speech_recognition as sr
import os
import time
import pygame



def speak_first(text):
     tts = gTTS(text=text, lang='ko')
     filename='start.mp3'
     tts.save(filename)
     pygame.mixer.init()
     pygame.mixer.music.load(filename)
     pygame.mixer.music.play()
     while pygame.mixer.music.get_busy() == True:
        continue

speak_first("단어 말하기")

# microphone에서 auido source를 생성합니다
r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)

# 구글 웹 음성 API로 인식하기 (하루에 제한 50회)
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("You said: " + r.recognize_google(audio,language='ko-KR'))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


def speak(text):
     tts = gTTS(text=text, lang='ko')
     filename='voice.mp3'
     tts.save(filename)
     pygame.mixer.init()
     pygame.mixer.music.load(filename)
     pygame.mixer.music.play()
     while pygame.mixer.music.get_busy() == True:
        continue

speak("말씀하신 단어는 " + r.recognize_google(audio,language='ko-KR') + " 맞습니까?")



'''
#초성 유니코드 점자
unicode_braille_cho = {
    0x1100 : [[0,0,0,1,0,0]], #'ㄱ'
    0x1101 : [[0,0,0,0,0,1],[0,0,0,1,0,0]], #'ㄲ'
    0x1102 : [[1,0,0,1,0,0]], #'ㄴ'
    0x1103 : [[0,1,0,1,0,0]], #'ㄷ'
    0x1104 : [[0,0,0,0,0,1],[0,1,0,1,0,0]], #'ㄸ'
    0x1105 : [[0,0,0,0,1,0]], #'ㄹ'
    0x1106 : [[1,0,0,0,1,0]], #'ㅁ'
    0x1107 : [[0,0,0,1,1,0]], #'ㅂ'
    0x1108 : [[0,0,0,0,0,1],[0,0,0,1,1,0]], #'ㅃ'
    0x1109 : [[0,0,0,0,0,1]], #'ㅅ'
    0x110A : [[0,0,0,0,0,1],[0,0,0,0,0,1]], #'ㅆ'
    0x110B : [], #'ㅇ'
    0x110C : [[0,0,0,1,0,1]], #'ㅈ'
    0x110D : [[0,0,0,0,0,1],[0,0,0,1,0,1]], #'ㅉ'
    0x110E : [[0,0,0,0,1,1]], #'ㅊ'
    0x110F : [[1,1,0,1,0,0]], #'ㅋ'
    0x1110 : [[1,1,0,0,1,0]], #'ㅌ'
    0x1111 : [[1,0,0,1,1,0]], #'ㅍ'
    0x1112 : [[0,1,0,1,1,0]], #'ㅎ'
}


unicode_braille_jung = {
    0x1161 : [[1,1,0,0,0,1]], #'ㅏ'
    0x1162 : [[1,1,1,0,1,0]], #'ㅐ'
    0x1163 : [[0,0,1,1,1,0]], #'ㅑ'
    0x1164 : [[0,0,1,1,1,0]], #'ㅒ'
    0x1165 : [[0,1,1,1,0,0]], #'ㅓ'
    0x1166 : [[1,0,1,1,1,0]], #'ㅔ'
    0x1167 : [[1,0,0,0,1,1]], #'ㅕ'
    0x1168 : [[0,0,1,1,0,0]], #'ㅖ'
    0x1169 : [[1,0,1,0,0,1]], #'ㅗ'
    0x116A : [[1,1,1,0,0,1]], #'ㅘ'
    0x116B : [[1,1,1,0,0,1],[1,1,1,0,1,0]], #'ㅙ'
    0x116C : [[1,0,1,1,1,1]], #'ㅚ'
    0x116D : [[0,0,1,1,0,1]], #'ㅛ'
    0x116E : [[1,0,1,1,0,0]], #'ㅜ'
    0x116F : [[1,1,1,1,0,0]], #'ㅝ'
    0x1170 : [[1,1,1,1,0,0],[1,1,1,0,1,0]], #'ㅞ'
    0x1171 : [[1,0,1,1,0,0],[1,1,1,0,1,0]], #'ㅟ'
    0x1172 : [[1,0,0,1,0,1]], #'ㅠ'
    0x1173 : [[0,1,0,1,0,1]], #'ㅡ'
    0x1174 : [[0,1,0,1,1,1]], #'ㅢ'
    0x1175 : [[1,0,1,0,1,0]], #'ㅣ'
}


unicode_braille_jong = {
    0x11A8 : [[1,0,0,0,0,0]], #'ㄱ'
    0x11A9 : [[0,0,0,0,0,1],[1,0,0,0,0,0]], #'ㄲ'
    0x11AA : [[1,0,0,0,0,0],[0,0,1,0,0,0]], #'ㄳ'
    0x11AB : [[0,1,0,0,1,0]], #'ㄴ'
    0x11AC : [[0,1,0,0,1,0],[1,0,1,0,0,0]], #'ㄵ'
    0x11AD : [[0,1,0,0,1,0],[0,0,1,0,1,1]], #'ㄶ'
    0x110E : [[0,0,1,0,1,0]], #'ㄷ'
    0x110F : [[0,1,0,0,0,0]], #'ㄹ'
    0x11B0 : [[0,1,0,0,0,0],[1,0,0,0,0,0]], #'ㄺ'
    0x11B1 : [[0,1,0,0,0,0],[0,1,0,0,0,1]], #'ㄻ'
    0x11B2 : [[0,1,0,0,0,0],[1,1,0,0,0,0]], #'ㄼ'
    0x11B3 : [[0,1,0,0,0,0],[0,0,1,0,0,0]], #'ㄽ'
    0x11B4 : [[0,1,0,0,0,0],[0,1,1,0,0,1]], #'ㄾ'
    0x11B5 : [[0,1,0,0,0,0],[0,1,0,0,1,1]], #'ㄿ'
    0x11B6 : [[0,1,0,0,0,0],[0,0,1,0,1,1]], #'ㅀ'
    0x11B7 : [[0,1,0,0,0,1]], #'ㅁ'
    0x11B8 : [[1,1,0,0,0,0]], #'ㅂ'
    0x11B9 : [[1,1,0,0,0,0],[0,0,1,0,0,0]], #'ㅄ'
    0x11BA : [[0,0,1,0,0,0]], #'ㅅ'
    0x11BB : [[0,0,0,0,0,1],[0,0,1,0,0,0]], #'ㅆ'
    0x11BC : [[0,1,1,0,1,1]], #'ㅇ'
    0x11BD : [[1,0,1,0,0,0]], #'ㅈ'
    0x11BE : [[0,1,1,0,0,0]], #'ㅊ'
    0x11BF : [[0,1,1,0,1,0]], #'ㅋ'
    0x11C0 : [[0,1,1,0,0,1]], #'ㅌ'
    0x11C1 : [[0,1,0,0,1,1]], #'ㅍ'
    0x11C2 : [[0,0,1,0,1,1]], #'ㅎ'
}


def string_to_braille(text):
    braille = []
    for c in text:
        # Convert character to Unicode code point
        code_point = ord(c)
        # Check if character is a Hangul syllable
        if 0xAC00 <= code_point <= 0xD7A3:
            # Calculate index of the character in the Hangul syllable table
            index = code_point - 0xAC00
            # Calculate the initial, medial, and final Jamo for the syllable
            initial = index // (21 * 28)
            medial = (index // 28) % 21
            final = index % 28
            # Convert Jamo to Braille
            braille_initial = unicode_braille_cho.get(0x1100 + initial)
            braille_medial = unicode_braille_jung.get(0x1161 + medial)
            braille_final = unicode_braille_jong.get(0x11A7 + final) if final != 0 else []
            # Concatenate Braille for initial, medial, and final Jamo
            braille_syllable = braille_initial + braille_medial + braille_final
            # Append Braille for syllable to list of Braille for string
            braille.append(braille_syllable)
        else:
            # Convert non-Hangul character to Braille
            braille_character = unicode_braille.get(code_point, [])
            braille.append(braille_character)
    return braille


print("단어는 '" + r.recognize_google(audio,language='ko-KR') + "' 입니다")
braille = string_to_braille(r.recognize_google(audio,language='ko-KR'))
print(braille)
'''
import hgtk

MATCH_H2B_CHO = {
    u'ㄱ': [[0,0,0,1,0,0]],
    u'ㄴ': [[1,0,0,1,0,0]],
    u'ㄷ': [[0,1,0,1,0,0]],
    u'ㄹ': [[0,0,0,0,1,0]],
    u'ㅁ': [[1,0,0,0,1,0]],
    u'ㅂ': [[0,0,0,1,1,0]],
    u'ㅅ': [[0,0,0,0,0,1]],
    u'ㅇ': [[1,1,0,1,1,0]],
    u'ㅈ': [[0,0,0,1,0,1]],
    u'ㅊ': [[0,0,0,0,1,1]],
    u'ㅋ': [[1,1,0,1,0,0]],
    u'ㅌ': [[1,1,0,0,1,0]],
    u'ㅍ': [[1,0,0,1,1,0]],
    u'ㅎ': [[0,1,0,1,1,0]],

    u'ㄲ': [[0,0,0,0,0,1], [0,0,0,1,0,0]],
    u'ㄸ': [[0,0,0,0,0,1], [0,1,0,1,0,0]],
    u'ㅃ': [[0,0,0,0,0,1], [0,0,0,1,1,0]],
    u'ㅆ': [[0,0,0,0,0,1], [0,0,0,0,0,1]],
    u'ㅉ': [[0,0,0,0,0,1], [0,0,0,1,0,1]],
}

MATCH_H2B_JOONG = {
    u'ㅏ': [[1,1,0,0,0,1]],
    u'ㅑ': [[0,0,1,1,1,0]],
    u'ㅓ': [[0,1,1,1,0,0]],
    u'ㅕ': [[1,0,0,0,1,1]],
    u'ㅗ': [[1,0,1,0,0,1]],
    u'ㅛ': [[0,0,1,1,0,1]],
    u'ㅜ': [[1,0,1,1,0,0]],
    u'ㅠ': [[1,0,0,1,0,1]],
    u'ㅡ': [[0,1,0,1,0,1]],
    u'ㅣ': [[1,0,1,0,1,0]],
    u'ㅐ': [[1,1,1,0,1,0]],
    u'ㅔ': [[1,0,1,1,1,0]],
    u'ㅒ': [[0,0,1,1,1,0], [1,1,1,0,1,0]],
    u'ㅖ': [[0,0,1,1,0,0]],
    u'ㅘ': [[1,1,1,0,0,1]],
    u'ㅙ': [[1,1,1,0,0,1], [1,1,1,0,1,0]],
    u'ㅚ': [[1,0,1,1,1,1]],
    u'ㅝ': [[1,1,1,1,0,0]],
    u'ㅞ': [[1,1,1,1,0,0], [1,1,1,0,1,0]],
    u'ㅟ': [[1,0,1,1,0,0], [1,1,1,0,1,0]],
    u'ㅢ': [[0,1,0,1,1,1]],
}

MATCH_H2B_JONG = {
    u'ㄱ': [[1,0,0,0,0,0]],
    u'ㄴ': [[0,1,0,0,1,0]],
    u'ㄷ': [[0,0,1,0,1,0]],
    u'ㄹ': [[0,1,0,0,0,0]],
    u'ㅁ': [[0,1,0,0,0,1]],
    u'ㅂ': [[1,1,0,0,0,0]],
    u'ㅅ': [[0,0,1,0,0,0]],
    u'ㅇ': [[0,1,1,0,1,1]],
    u'ㅈ': [[1,0,1,0,0,0]],
    u'ㅊ': [[0,1,1,0,0,0]],
    u'ㅋ': [[0,1,1,0,1,0]],
    u'ㅌ': [[0,1,1,0,0,1]],
    u'ㅍ': [[0,1,0,0,1,1]],
    u'ㅎ': [[0,0,1,0,1,1]],

    u'ㄲ': [[1,0,0,0,0,0], [1,0,0,0,0,0]],
    u'ㄳ': [[1,0,0,0,0,0], [0,0,1,0,0,0]],
    u'ㄵ': [[0,1,0,0,1,0], [1,0,1,0,0,0]],
    u'ㄶ': [[0,1,0,0,1,0], [0,0,1,0,1,1]],
    u'ㄺ': [[0,1,0,0,0,0], [1,0,0,0,0,0]],
    u'ㄻ': [[0,1,0,0,0,0], [0,1,0,0,0,1]],
    u'ㄼ': [[0,1,0,0,0,0], [1,1,0,0,0,0]],
    u'ㄽ': [[0,1,0,0,0,0], [0,0,1,0,0,0]],
    u'ㄾ': [[0,1,0,0,0,0], [0,1,1,0,0,1]],
    u'ㄿ': [[0,1,0,0,0,0], [0,1,0,0,1,1]],
    u'ㅀ': [[0,1,0,0,0,0], [0,0,1,0,1,1]],
    u'ㅄ': [[1,1,0,0,0,0], [0,0,1,0,0,0]],
    u'ㅆ': [[0,0,1,1,0,0]],
}

MATCH_H2B_ALPHABET = {
    'a': [[1,0,0,0,0,0]],
    'b': [[1,1,0,0,0,0]],
    'c': [[1,0,0,1,0,0]],
    'd': [[1,0,0,1,1,0]],
    'e': [[1,0,0,0,1,0]],
    'f': [[1,1,0,1,0,0]],
    'g': [[1,1,0,1,1,0]],
    'h': [[1,1,0,0,1,0]],
    'i': [[0,1,0,1,0,0]],
    'j': [[0,1,0,1,1,0]],
    'k': [[1,0,1,0,0,0]],
    'l': [[1,1,1,0,0,0]],
    'm': [[1,0,1,1,0,0]],
    'n': [[1,0,1,1,1,0]],
    'o': [[1,0,1,0,1,0]],
    'p': [[1,1,1,1,0,0]],
    'q': [[1,1,1,1,1,0]],
    'r': [[1,1,1,0,1,0]],
    's': [[0,1,1,1,0,0]],
    't': [[0,1,1,1,1,0]],
    'u': [[1,0,1,0,0,1]],
    'v': [[1,1,1,0,0,1]],
    'w': [[0,1,1,1,1,1]],
    'x': [[1,0,1,1,0,1]],
    'y': [[1,0,1,1,1,1]],
    'z': [[1,0,1,0,1,1]],

    'A': [[0,0,0,0,0,1], [1,0,0,0,0,0]],
    'B': [[0,0,0,0,0,1], [1,1,0,0,0,0]],
    'C': [[0,0,0,0,0,1], [1,0,0,1,0,0]],
    'D': [[0,0,0,0,0,1], [1,0,0,1,1,0]],
    'E': [[0,0,0,0,0,1], [1,0,0,0,1,0]],
    'F': [[0,0,0,0,0,1], [1,1,0,1,0,0]],
    'G': [[0,0,0,0,0,1], [1,1,0,1,1,0]],
    'H': [[0,0,0,0,0,1], [1,1,0,0,1,0]],
    'I': [[0,0,0,0,0,1], [0,1,0,1,0,0]],
    'J': [[0,0,0,0,0,1], [0,1,0,1,1,0]],
    'K': [[0,0,0,0,0,1], [1,0,1,0,0,0]],
    'L': [[0,0,0,0,0,1], [1,1,1,0,0,0]],
    'M': [[0,0,0,0,0,1], [1,0,1,1,0,0]],
    'N': [[0,0,0,0,0,1], [1,0,1,1,1,0]],
    'O': [[0,0,0,0,0,1], [1,0,1,0,1,0]],
    'P': [[0,0,0,0,0,1], [1,1,1,1,0,0]],
    'Q': [[0,0,0,0,0,1], [1,1,1,1,1,0]],
    'R': [[0,0,0,0,0,1], [1,1,1,0,1,0]],
    'S': [[0,0,0,0,0,1], [0,1,1,1,0,0]],
    'T': [[0,0,0,0,0,1], [0,1,1,1,1,0]],
    'U': [[0,0,0,0,0,1], [1,0,1,0,0,1]],
    'V': [[0,0,0,0,0,1], [1,1,1,0,0,1]],
    'W': [[0,0,0,0,0,1], [0,1,1,1,1,1]],
    'X': [[0,0,0,0,0,1], [1,0,1,1,0,1]],
    'Y': [[0,0,0,0,0,1], [1,0,1,1,1,1]],
    'Z': [[0,0,0,0,0,1], [1,0,1,0,1,1]],

    '1': [[0,0,1,1,1,1], [1,0,0,0,0,0]],
    '2': [[0,0,1,1,1,1], [1,1,0,0,0,0]],
    '3': [[0,0,1,1,1,1], [1,0,0,1,0,0]],
    '4': [[0,0,1,1,1,1], [1,0,0,1,1,0]],
    '5': [[0,0,1,1,1,1], [1,0,0,0,1,0]],
    '6': [[0,0,1,1,1,1], [1,1,0,1,0,0]],
    '7': [[0,0,1,1,1,1], [1,1,0,1,1,0]],
    '8': [[0,0,1,1,1,1], [1,1,0,0,1,0]],
    '9': [[0,0,1,1,1,1], [0,1,0,1,0,0]],
    '0': [[0,0,1,1,1,1], [0,1,0,1,1,0]],

    ',': [[0,1,0,0,0,0]],
    '.': [[0,1,0,0,1,1]],
    '-': [[0,1,0,0,1,0]],
    '?': [[0,1,1,0,0,1]],
    '_': [[0,0,1,0,0,1]],
    '!': [[0,1,1,0,1,0]],
}


def letter(hangul_letter):
    """
    Convert a hangul letter to 6-dot braille
    (alphabet, number, and some special chracter supported)
    :param str hangul: a hangul chracter to convert to braille
    :return: braille data (6-int list with the value 0 or 1)
    :rtype: list[str, list[int]]
    """
    result = []
    hangul_decomposed = hgtk.text.decompose(hangul_letter[0])
    hangul_decomposed = \
        hangul_decomposed.replace(hgtk.text.DEFAULT_COMPOSE_CODE, '')
    for i in range(len(hangul_decomposed)):
        hangul = hangul_decomposed[i]
        if i == 0 and hangul in MATCH_H2B_CHO:
            result.append([hangul, MATCH_H2B_CHO[hangul]])
        if i == 0 and hangul in MATCH_H2B_ALPHABET:
            result.append([hangul, MATCH_H2B_ALPHABET[hangul]])
        if i == 1 and hangul in MATCH_H2B_JOONG:
            result.append([hangul, MATCH_H2B_JOONG[hangul]])
        if i == 2 and hangul in MATCH_H2B_JONG:
            result.append([hangul, MATCH_H2B_JONG[hangul]])
    if result == []:
        result.append([hangul, [[0,0,0,0,0,0]]])
    return result


def text(hangul_sentence):
    """
    Convert hangul sentence to list of 6-dot braille
    :param str hangul: hangul text to convert to braille
    :return: list of braille data (list of 6-int list with the value 0 or 1)
    :rtype: list[str, list[str, list[int]]]
    """
    result = []

    for hangul_letter in hangul_sentence:
        result.append([hangul_letter, letter(hangul_letter)])
    return result