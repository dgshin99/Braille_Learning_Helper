from gtts import gTTS
import speech_recognition as sr
import os
import time
import pygame 
# 모듈 가져오기

def speak_first(text):
     tts = gTTS(text=text, lang='ko')
     filename='start.mp3'
     tts.save(filename)
     pygame.mixer.init()
     pygame.mixer.music.load(filename)
     pygame.mixer.music.play()
     while pygame.mixer.music.get_busy() == True:
        continue  
     # 끝까지 재생할 때까지 기다린다.(중간에 끊김 방지)

speak_first("단어 말하기")
# 점자 출력을 원하는 단어를 사용자에게로부터 음성으로 받기 위한 안내메시지


# microphone에서 audio source를 생성합니다
r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)

# 구글 웹 음성 API로 인식하기 (하루에 제한 50회)
try:
    print("You said: " + r.recognize_google(audio,language='ko-KR'))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

# 예외 처리


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
# 사용자가 말한 단어 음성으로 되물어서 확인


# 초성, 중성, 종성의 유니코드, 초성 ㅇ 예외처리
import hgtk
MATCH_H2B_CHO = {
    u'ㄱ': [[0,0,0,1,0,0]],
    u'ㄴ': [[1,0,0,1,0,0]],
    u'ㄷ': [[0,1,0,1,0,0]],
    u'ㄹ': [[0,0,0,0,1,0]],
    u'ㅁ': [[1,0,0,0,1,0]],
    u'ㅂ': [[0,0,0,1,1,0]],
    u'ㅅ': [[0,0,0,0,0,1]],
    u'ㅇ': [[0,0,0,0,0,0]],
    #u'ㅇ': [[1,1,0,1,1,0]],
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


#한 글자를 초성,중성,종성으로 분류하고, 점자 데이터로 변환
def letter(hangul_letter):
    #리스트에 추가시키기 위해 빈 리스트 준비
    result = []
    result1 = []
    result2 = []
    result3 = []

    #한 글자 자모분리 ex)ㄲㅏㅁ/
    hangul_decomposed = hgtk.text.decompose(hangul_letter[0], compose_code='/')
    for i in range(len(hangul_decomposed)):
        hangul = hangul_decomposed[i]
        #초성에 맞는 유니코드 리스트 가져와서 출력
        if i == 0 and hangul in MATCH_H2B_CHO:
            result1.append(MATCH_H2B_CHO[hangul])
            # ex)ㄲ-> print(result1) => [[[0,0,0,0,0,1], [0,0,0,1,0,0]]]
            #초성이 된소리일 경우(indexerror 보완한 코드)와 아닐경우 구분
            if hangul == 'ㄲ' or hangul == 'ㄸ' or hangul == 'ㅃ' or hangul == 'ㅆ' or hangul == 'ㅉ':
                #여기서 모터 간 delay가 길까봐 걱정
                #result1[0][0]출력 : 초성의 첫번째 리스트 출력
                for i in range(6):
                    if result1[0][0][i] == 0:
                        kit.servo[i].angle = 0
                    else:
                        kit.servo[i].angle = 180

                sleep(2) #2초 대기, 사용자가 점자 인식하기 위한 시간
                   
                for j in range(6):
                    kit.servo[j].angle = 0
               
                sleep(1) #점자 초기화 및 1초 대기, 초성의 두번째 리스트와 구분하기 위해
                   
                #result1[0][1]출력 : 초성의 두번째 리스트 출력   
                for i in range(6):
                    if result1[0][1][i] == 0:
                        kit.servo[i].angle = 0

                    else:
                        kit.servo[i].angle = 180
               
                sleep(2) #2초 대기, 사용자가 점자 인식하기 위한 시간
                   
                for j in range(6):
                    kit.servo[j].angle = 0
                    #복구 후
                sleep(1) #점자 초기화 및 1초 대기, 중성의 첫번째 리스트와 구분하기 위해
                speak("초성이었습니다") #tts로 초성이었습니다.알려주기
               
               
            else: #초성이 된소리가 아닐 경우 ex) 'ㄱ': print(result1)=[[[0,0,0,1,0,0]]] 이므로 result[0][1][0~5]없는거 유의 
                for i in range(6):
                    if result1[0][0][i] == 0:
                        kit.servo[i].angle = 0

                    else:
                        kit.servo[i].angle = 180
               
                sleep(2) #2초 대기 추가, 사용자가 점자 인식하기 위한 시간
                   
                for j in range(6):
                    kit.servo[j].angle = 0
                
                sleep(1) #점자 초기화 및 1초 대기, 중성의 첫번째 리스트와 구분하기 위해
                speak("초성이었습니다") #초기화 후 초성이었습니다.(tts)
     

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


def text(hangul_sentence): #한글단어(문장)를 글자별로 분류 ex) 깜깜해 => '깜' "깜' '해'
    result = []

    for hangul_letter in hangul_sentence:
        #result.append([hangul_letter, letter(hangul_letter)])
        result.append(letter(hangul_letter))
    return result

motor_input=(text(r.recognize_google(audio,language='ko-KR')))