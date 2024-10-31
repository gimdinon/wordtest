#22okt.py문서 10월31일 목요일 작성
from wordcloud import WordCloud, STOPWORDS
from konlpy.tag import Okt
import time

print('koNLpy test')
okt = Okt()
print(' Okt() 정보 ', okt) #<konlpy.tag._okt.Okt object at 0x0000018DF3870D10>

msg = '파인애플* 사과★ 귤@ 추출 워드 클라우드로 그려봅시다'
print(msg)
print()

result1 = okt.nouns(msg)
print(result1)
print()
time.sleep(0.5)

result2 = okt.pos(msg)
print(result2) #시간이 걸려요
print()
print('- ' * 50)
time.sleep(0.5)

result3 = okt.morphs(msg)
print(result3) # 
print()
time.sleep(0.5)


print()
print()