#-*- coding:utf-8 -*-
from gtts import gTTS
import speech_recognition as sr
import os
import time
import pygame
import Adafruit_PCA9685
import RPi.GPIO as GPIO
import hgtk

MATCH_H2B_CHO = {
    u'ㄱ': [[0,0,0,1,0,0]],
    u'ㄴ': [[1,0,0,1,0,0]],
    u'ㄷ': [[0,1,0,1,0,0]],
    u'ㄹ': [[0,0,0,0,1,0]],
    u'ㅁ': [[1,0,0,0,1,0]],
    u'ㅂ': [[0,0,0,1,1,0]],
    u'ㅅ': [[0,0,0,0,0,1]],
    '''u'ㅇ': [[1,1,0,1,1,0]],'''
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

def speak(text):
    tts = gTTS(text=text, lang='ko')
    filename = 'voice.mp3'
    tts.save(filename)
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

speak("좌측 Start 버튼을 누르면 시작합니다.")

# 사용할 GPIO 핀의 번호를 설정
start_pin = 17
yes_pin = 27
no_pin = 22

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM) #핀모드 설정

# 버튼 핀의 입력설정 , 라즈베리파이 내부에 풀다운저항 설정(스위치 안눌렸을 때 off, 눌렸을 때 on) 
GPIO.setup(start_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(yes_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(no_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


pwm = Adafruit_PCA9685.PCA9685()

servo_min = 150
servo_max = 600

def set_servo_pulse(channel, pulse):
    pulse_length = 1000000 # 1,000,000 us per sec
    pulse_length //= 60 #60Hz
    pulse_length //= 4096 #12 bits of resoultion
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel,0,pulse)

pwm.set_pwm_freq(60)

def letter(hangul_letter): #한 글자를 초성,중성,종성으로 분류하고, 점자 데이터로 변환
                
    result1 = []
    result2 = []
    result3 = []

    hangul_decomposed = hgtk.text.decompose(hangul_letter[0], compose_code='/')
            
    for i in range(len(hangul_decomposed)-1):
        hangul = hangul_decomposed[i]
        if i == 0 and hangul in MATCH_H2B_CHO:
            result1.append(MATCH_H2B_CHO[hangul])
            if hangul == 'ㄲ' or hangul == 'ㄸ' or hangul == 'ㅃ' or hangul == 'ㅆ' or hangul == 'ㅉ': #초성이 된소리일 경우
                            
                for i in range(6):
                    if result1[0][0][i] == 0:
                        pwm.set_pwm(i,0,servo_min)
                
                    else:
                        pwm.set_pwm(i,0,servo_max)
                            
                time.sleep(3) #2초 대기 추가
                                
                for j in range(6):
                    pwm.set_pwm(j,0,servo_min)
                                
                            
                time.sleep(2) #점자 초기화 후 1초 대기
                                

                for i in range(6):
                    if result1[0][1][i] == 0:
                        pwm.set_pwm(i,0,servo_min)

                    else:
                        pwm.set_pwm(i,0,servo_max)
                            
                time.sleep(3) #2초 대기 추가
                                
                for j in range(6):
                    pwm.set_pwm(j,0,servo_min)
                    #복구 후
                            
                speak("초성이었습니다") #tts로 초성이었습니다.

            else: #초성이 된소리가 아닐 경우
                for i in range(6):
                    if result1[0][0][i] == 0:
                        pwm.set_pwm(i,0,servo_min)

                    else:
                        pwm.set_pwm(i,0,servo_max)
                            
                time.sleep(3)#2초 대기 추가
                                
                for j in range(6):
                    pwm.set_pwm(j,0,servo_min)                     
                speak("초성이었습니다") #초기화 후 초성이었습니다.(tts)

        if i == 1 and hangul in MATCH_H2B_JOONG:
            result2.append(MATCH_H2B_JOONG[hangul])
            if hangul == 'ㅒ' or hangul == 'ㅙ' or hangul == 'ㅞ' or hangul == 'ㅟ':
                for i in range(6):
                    if result2[0][0][i] == 0:
                        pwm.set_pwm(i,0,servo_min)

                    else:
                        pwm.set_pwm(i,0,servo_max)
                            
                time.sleep(3) #2초 대기 추가
                                
                for j in range(6):
                    pwm.set_pwm(j,0,servo_min)
                                
                            
                time.sleep(2) #점자 초기화 후 1초 대기
                                

                for i in range(6):
                    if result2[0][1][i] == 0:
                        pwm.set_pwm(i,0,servo_min)

                    else:
                        pwm.set_pwm(i,0,servo_max)
                            
                time.sleep(3)#2초 대기 추가
                                
                for j in range(6):
                    pwm.set_pwm(j,0,servo_min)
                    #복구 후
                #tts로 초성이었습니다.
                speak("중성이었습니다")
                        
                            
            else:
                for i in range(6):
                    if result2[0][0][i] == 0:
                        pwm.set_pwm(i,0,servo_min)

                    else:
                        pwm.set_pwm(i,0,servo_max)
                            
                time.sleep(3)#2초 대기 추가
                                
                for j in range(6):
                    pwm.set_pwm(j,0,servo_min)
                          
                #초기화 후 중성이었습니다.(tts)
                speak("중성이었습니다")
                    

        if i == 2 and hangul in MATCH_H2B_JONG:
            result3.append(MATCH_H2B_JONG[hangul])
            if hangul == 'ㄲ' or hangul == 'ㄳ' or hangul == 'ㄵ' or hangul == 'ㄶ' or hangul == 'ㄺ' or hangul == 'ㄻ' or hangul == 'ㄼ' or hangul == 'ㄽ'or hangul == 'ㄾ' or hangul == 'ㄿ' or hangul == 'ㅀ' or hangul == 'ㅄ':
                for i in range(6):
                    if result3[0][0][i] == 0:
                        pwm.set_pwm(i,0,servo_min)

                    else:
                        pwm.set_pwm(i,0,servo_max)
                            
                time.sleep(3) #2초 대기 추가
                                
                for j in range(6):
                    pwm.set_pwm(j,0,servo_min)
                                
                            
                time.sleep(2) #점자 초기화 후 1초 대기
                                

                for i in range(6):
                    if result3[0][1][i] == 0:
                        pwm.set_pwm(i,0,servo_min)

                    else:
                        pwm.set_pwm(i,0,servo_max)
                            
                time.sleep(3)#2초 대기 추가
                                
                for j in range(6):
                    pwm.set_pwm(j,0,servo_min)
                    #복구 후
                            
                speak("종성이었습니다") #tts로 초성이었습니다.
            else:
                for i in range(6):
                    if result3[0][0][i] == 0:
                        pwm.set_pwm(i,0,servo_min)

                    else:
                        pwm.set_pwm(i,0,servo_max)
                            
                time.sleep(3)#2초 대기 추가
                                
                for j in range(6):
                    pwm.set_pwm(j,0,servo_min)
                          
                #초기화 후 종성이었습니다.(tts)
                speak("종성이었습니다")    
    return


def text(hangul_sentence): #한글단어(문장)를 글자별로 분류

    for hangul_letter in hangul_sentence:
        letter(hangul_letter)

    return

while True:      

    while True:
        if GPIO.input(start_pin) == GPIO.HIGH:
            print("start")
            # 맨 처음에 실행할 내용
            speak("단어 말하기")

            while True:
                # microphone에서 audio source를 생성합니다.
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    audio = r.listen(source)

                try:
                    # 음성을 텍스트로 변환합니다.
                    said = r.recognize_google(audio, language='ko-KR')
                    print("You said: " + said)

                    # 말씀하신 단어 출력
                    speak("말씀하신 단어가 " + said + "이면 중앙 YES 버튼, 틀리면 우측 NO 버튼을 눌러주세요.")

                    while True:
                        # GPIO 핀 입력 확인
                        if GPIO.input(yes_pin) == GPIO.HIGH:
                            print("Yes 버튼이 눌렸습니다.")
                            # Yes 버튼 동작에 대한 처리
                            break  # 내부 루프 탈출

                        if GPIO.input(no_pin) == GPIO.HIGH:
                            print("No 버튼이 눌렸습니다.")
                            # No 버튼 동작에 대한 처리
                            break  # 내부 루프 탈출
                    
                    if GPIO.input(yes_pin) == GPIO.HIGH:
                        time.sleep(2)
                        break

                    if GPIO.input(no_pin) == GPIO.HIGH:
                        # 선택하는 부분으로 돌아가기 위해 외부 루프 탈출
                        speak("다시 말씀해 주세요")
                        continue

                    # 선택한 단어에 대한 처리
                    # ...

                except sr.UnknownValueError:
                    speak("인식하지 못했습니다.다시 말씀해 주세요")
                except sr.RequestError as e:
                    print("인식하지 못했습니다.다시 말씀해 주세요".format(e))

            
            

            text(r.recognize_google(audio,language='ko-KR'))

            speak("다시 보고 싶으시면 중앙의 yes버튼, 새로운 단어를 보고 싶으시면 좌측의 start버튼을 눌러주세요")
            
            if GPIO.input(yes_pin) == GPIO.HIGH:
                while True:
                    text(said)
                    speak("다시 보고 싶으시면 중앙의 yes버튼, 새로운 단어를 보고 싶으시면 좌측의 start버튼을 눌러주세요")
                    if GPIO.input(start_pin) == GPIO.HIGH:
                        break
                    else:
                        continue
