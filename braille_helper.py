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
     while pygame.mixer.music.get_busy() == True:   # 끝까지 재생할 때까지 기다린다.
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
    u'ㅉ': [[0,0,0,0,0,1], [0,0,0,1,0,1]]
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

def letter(hangul_letter): #한 글자를 초성,중성,종성으로 분류하고, 점자 데이터로 변환
    """
    Convert a hangul letter to 6-dot braille
    :param str hangul: a hangul chracter to convert to braille
    :return: braille data (6-int list with the value 0 or 1)
    :rtype: list[str, list[int]]
    """
    result = []
    result1 = []
    result2 = []
    result3 = []

    hangul_decomposed = hgtk.text.decompose(hangul_letter[0], compose_code='/')
    #hangul_decomposed = \
    #    hangul_decomposed.replace(hgtk.text.DEFAULT_COMPOSE_CODE, '')
    for i in range(len(hangul_decomposed)):
        hangul = hangul_decomposed[i]
        if i == 0 and hangul in MATCH_H2B_CHO:
            result1.append(MATCH_H2B_CHO[hangul])
            if hangul == 'ㄲ' or hangul == 'ㄸ' or hangul == 'ㅃ' or hangul == 'ㅆ' or hangul == 'ㅉ': #초성이 된소리일 경우
                
                for i in range(6):
                    if result1[0][0][i] == 0:
                        kit.servo[i].angle = 0

                    else:
                        kit.servo[i].angle = 180
                
                sleep(2) #2초 대기 추가
                    
                for j in range(6):
                    kit.servo[j].angle = 0
                    
                
                sleep(1) #점자 초기화 후 1초 대기
                    

                for i in range(6):
                    if result1[0][1][i] == 0:
                        kit.servo[i].angle = 0

                    else:
                        kit.servo[i].angle = 180
                
                #2초 대기 추가
                    
                for j in range(6):
                    kit.servo[j].angle = 0
                    #복구 후
                #tts로 초성이었습니다.
                
                
            else: #초성이 된소리가 아닐 경우
                for i in range(6):
                    if result1[0][0][i] == 0:
                        kit.servo[i].angle = 0

                    else:
                        kit.servo[i].angle = 180
                
                #2초 대기 추가
                    
                for j in range(6):
                    kit.servo[j].angle = 0
              
                #초기화 후 초성이었습니다.(tts)
     

            #result.append([hangul, MATCH_H2B_CHO[hangul]])
            #for i in range(6):
                #result1.append(MATCH_H2B_CHO[hangul])
                #print(result1[0][0][i])
        if i == 1 and hangul in MATCH_H2B_JOONG:
            #result.append([hangul, MATCH_H2B_JOONG[hangul]])
            result2.append(MATCH_H2B_JOONG[hangul])
            if hangul == 'ㅒ' or hangul == 'ㅙ' or hangul == 'ㅞ' or hangul == 'ㅟ':
                for b in range(2):
                    for c in range(6):
                        print(result2[0][b][c])
                
            else:
                for c in range(6):
                    print(result2[0][0][c])
            
        if i == 2 and hangul in MATCH_H2B_JONG:
            #result.append([hangul, MATCH_H2B_JONG[hangul]])
            result3.append(MATCH_H2B_JONG[hangul])
            if hangul == 'ㄲ' or hangul == 'ㄳ' or hangul == 'ㄵ' or hangul == 'ㄶ' or hangul == 'ㄺ' or hangul == 'ㄻ' or hangul == 'ㄼ' or hangul == 'ㄽ'or hangul == 'ㄾ' or hangul == 'ㄿ' or hangul == 'ㅀ' or hangul == 'ㅄ':
                for b in range(2):
                    for c in range(6):
                        print(result3[0][b][c])
                
            else:
                for c in range(6):
                    print(result3[0][0][c])
            
    if result == []:
        result.append([hangul, [[0,0,0,0,0,0]]])
    return #result


def text(hangul_sentence): #한글단어(문장)를 글자별로 분류
    result = []

    for hangul_letter in hangul_sentence:
        #result.append([hangul_letter, letter(hangul_letter)])
        result.append(letter(hangul_letter))
    return result

motor_input=(text(r.recognize_google(audio,language='ko-KR')))
