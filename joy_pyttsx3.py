# Python program to show
# how to convert text to speech
import pyttsx3
  
text = "한국 R 사용자회는 데이터 분석 및 통계분야에서 전 세계적으로 사용되고 있는 R 프로그래밍 언어의 사용을 촉진하고, 연구 및 개발 분야에서 R을 활용한 다양한 응용과 기술 발전을 위해 설립된 사단법인입니다..\
한국 R 사용자회는 R 프로그래밍 언어를 사용하는 분야에서의 지식과 정보 교류, 협력과 공유를 위한 다양한 활동을 전개하고 있습니다. 회원들은 R을 활용한 다양한 분석 및 시각화 기술을 공유하고, R 패키지 개발 및 오픈소스 활용, 데이터 과학 분야에서의 협력과 커뮤니케이션 등 다양한 분야에서 활동하며 지식을 공유합니다.. \
한국 R 사용자회는 국내외 R 컨퍼런스 및 세미나 개최, R 교육 및 훈련, R 활용 사례 발표, R 패키지 개발 및 유지 보수 등 다양한 활동을 통해 회원들의 R 활용 능력 향상과 지식 공유를 위한 기반을 제공하고 있습니다. \
회원으로 가입하면 R 언어 및 데이터 분석 분야에서의 최신 정보와 기술 동향을 지속적으로 업데이트 받을 수 있으며, R 패키지 개발 및 활용, 데이터 분석 기술 등에 대한 다양한 교육과 세미나, 워크샵 등을 참여할 수 있습니다.. \
한국 R 사용자회는 R 프로그래밍 언어의 활용과 개발을 통해 데이터 분석 및 통계분야의 발전을 위한 지속적인 노력을 기울이고 있으며, 회원들의 활동과 참여를 통해 R 프로그래밍 언어의 활용과 발전에 기여하고 있습니다."
# Initialize the converter
converter = pyttsx3.init('sapi5')

voices = converter.getProperty('voices')

for voice in voices:
	# to get the info. about various voices in our PC
	print("Voice:")
	print("ID: %s" %voice.id)
	print("Name: %s" %voice.name)
	print("Age: %s" %voice.age)
	print("Gender: %s" %voice.gender)
	print("Languages Known: %s" %voice.languages)

# windows에서만 사용가능함. 
# Set properties before adding
# Things to say
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_KO-KR_HEAMI_11.0"
  
# Use female voice
converter.setProperty('voice', voice_id)
# Sets speed percent 
# Can be more than 100
converter.setProperty('rate', 130)
# Set volume 0-1
#converter.setProperty('volume', 0.7)
  
# Queue the entered text 
# There will be a pause between
# each one like a pause in 
# a sentence
converter.save_to_file(text, 'tts3.mp3') 
# Empties the say() queue
# Program will not continue
# until all speech is done talking
converter.runAndWait()

print('completed')