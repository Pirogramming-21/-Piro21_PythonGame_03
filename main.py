import random
import sys

#참가자 정보 저장할 클래스
class Player :
    def __init__(self, name, deadline, lose_num) :
        self.name = name # 이름
        self.deadline = deadline # 치사량
        self.lose_num = lose_num # 걸린 횟수

    def status(self): # 현재 상태 출력
        print(f"{self.name}은(는) 지금까지 {self.lose_num}\U0001F37A! 치사량까지 {self.deadline}")

    def is_dead(self): #치사량만큼 마셨는지 확인
        if self.deadline == 0: # 치사량이 0이면
            finish_game(self.name) # 게임 종료)

    def lose_game(self): # 게임에서 걸렸을 때
        self.lose_num += 1 # 걸린 횟수 +1
        self.deadline -= 1 # 치사량 -1
    

def make_friend(my_name, friend_num, player_list) : #나를 제외한 친구 랜덤 추출
    player_list.remove(my_name)# 리스트에서 나 삭제
    friend_list = random.sample(player_list, friend_num) # 리스트에서 선택한 친구 수만큼 랜덤 추출
    return friend_list

def finish_game(name): # 게임 종료
    print(f"{name}이(가) 전사했습니다... 꿈나라에서는 편히 쉬시길..zzz")
    sys.exit()

#####################
# 1번 게임
    #여기 구현~~~

# 2번 게임
    #여기 구현~~~

# 3번 게임
    #여기 구현~~~

# 4번 게임



######################

player_list = ["민석", "연진", "동현", "라현"] #전체 인원 명단

# 게임 인트로 정해서 넣기
# 1번
print("게임을 진행할까요? (y/n) : ", end=' ')
answer = input()

if answer == 'n':
    sys.exit()

# 2번

print("오늘 거하게 취해볼 당신의 이름은? : ", end=' ')
name = input()

# 3번
print("~~~~~~~~~~~~~~~~~~\U0001F37A  소주 기준 당신의 주량은? \U0001F37A~~~~~~~~~~~~~~~~~")
print("                   \U0001F37A 1. 소주 반병 (2잔)")
print("                   \U0001F37A 2. 소주 반병에서 한병 (4잔)")
print("                   \U0001F37A 3. 소주 한병에서 한병 반 (6잔)")
print("                   \U0001F37A 4. 소주 한병 반에서 두병 (8잔)")
print("                   \U0001F37A 5. 소주 두병 이상 (10잔)")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

while True:
    try:
        print("당신의 치사량(주량)은 얼마만큼인가요? (1~5를 선택해주세요) : ", end=' ')
        num = int(input())
        if 1 <= num <= 5:
            if num == 1:
                deadline = 2
                break
            if num == 2:
                deadline = 4
                break
            if num == 3:
                deadline = 6
                break
            if num == 4:
                deadline = 8
                break
            if num == 5:
                deadline = 10
                break
        else :
            print("1~5를 선택해주세요")
    except:
        print("1~5를 선택해주세요")

me = Player(name, deadline, 0)

# 4번
while True:
    try:
        print("함께 취할 친구들은 얼마나 필요하신가요?(사회적 거리두기로 인해 최대 3명까지 초대할 수 있어요!) : ", end=' ')
        friendNum = int(input())
        if 1 <= friendNum <= 3:
            break
        else :
            print("1명에서 3명까지 초대할 수 있습니다")
    except:
        print("1명에서 3명까지 초대할 수 있습니다")

friends = make_friend(name, friendNum, player_list)
player = [me] # 술게임에 참가하는 총 참가자 명단(객체 저장)
for friend in friends:
    num = random.randint(1,6)
    if 1 <= num <= 5:
        if num == 1:
            deadline = 2
        if num == 2:
            deadline = 4
        if num == 3:
            deadline = 6
        if num == 4:
            deadline = 8
        if num == 5:
            deadline = 10
    print(f"오늘 함께 취할 친구는 {friend}입니다! (치사량 : {deadline})")
    player_obj = Player(friend, deadline, 0)
    player.append(player_obj)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
round = 0 # 게임 몇 판째인지 확인
while True: # 게임 시작 반복문
    print(f"현재 몇 판째? => {round}")

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for i in player: # 게임 전 현재 상태 출력
        i.status()

    for i in player: # 치사량만큼 마셨는지 확인
        i.is_dead()

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~\U0001F37A  오늘의 Alcohol GAME \U0001F37A~~~~~~~~~~~~~~~~~")
    print("                   \U0001F37A 1. 1번 게임 이름")
    print("                   \U0001F37A 2. 2번 게임 이름")
    print("                   \U0001F37A 3. 3번 게임 이름")
    print("                   \U0001F37A 4. 4번 게임 이름")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    choice_player = player[round%(len(player))] # 몇 번째 사람이 게임을 고를 차례인지 확인용
    
    if choice_player.name == name : # 게임을 고르는 사람이 나면 직접 게임 선택
        print(f"{choice_player.name}(이)가 좋아하는 랜덤 게임 ~ 랜덤 게임 ~ 무슨 게임? : ", end=' ')
        num = int(input())
    else : # 내가 아니면 랜덤으로 게임 선택
        print("술게임 진행중 ! 다른 사람의 턴입니다. 그만하고 싶으면 \"exit\"를, 계속하고 싶으면 아무키나 입력해 주세요 : ", end=' ')
        choice = input()
        if choice == "exit":
            sys.exit("게임을 종료합니다")
        num = random.randint(1,5)
        print(f"{choice_player.name}(이)가 좋아하는 랜덤 게임 ~ 랜덤 게임 ~ 무슨 게임? : {num}")
    
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"{choice_player.name} 님이 게임을 선택하셨습니다!\n")
    
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    print(f"{round}번째 라운드 게임 시작~~~~~~~ 이 부분도 인트로 찾아서 만들기")
    # 게임 구현
    # if num == 1 ~
    # if num == 2 ~
    # if num == 3 ~
    # if num == 4 ~

    for i in player: # 
        i.lose_game()
    print(f"{round}번째 라운드 게임 종료~~~~~~")
    round += 1
