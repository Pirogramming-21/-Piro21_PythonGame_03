import random
import sys
import time
import subwaylist


# 참가자 정보 저장할 클래스
class Player:
    def __init__(self, name, deadline, lose_num):
        self.name = name  # 이름
        self.deadline = deadline  # 치사량
        self.lose_num = lose_num  # 걸린 횟수
        self.left = None  # 왼쪽 플레이어
        self.right = None  # 오른쪽 플레이어

    def status(self):  # 현재 상태 출력
        print(
            f"{self.name}은(는) 지금까지 {self.lose_num}\U0001F37A! 치사량까지 {self.deadline}"
        )

    def lose_game(self):  # 게임에서 걸렸을 때
        self.lose_num += 1  # 걸린 횟수 +1
        self.deadline -= 1  # 치사량 -1

    def is_dead(self):  # 치사량만큼 마셨는지 확인
        if self.deadline == 0:  # 치사량이 0이면
            finish_game(self.name)  # 게임 종료)


def make_friend(my_name, friend_num, player_list):  # 나를 제외한 친구 랜덤 추출
    player_list.remove(my_name)  # 리스트에서 나 삭제
    friend_list = random.sample(
        player_list, friend_num
    )  # 리스트에서 선택한 친구 수만큼 랜덤 추출
    return friend_list


def finish_game(name):  # 게임 종료
    print(f"{name}이(가) 전사했습니다... 꿈나라에서는 편히 쉬시길..zzz")
    sys.exit()


#####################
# 1번 게임
def game_007(current_player, players):
    print("\U0001F52B 공공칠빵\U0001F52B 게임을 시작합니다!")
    
    # 각 플레이어의 양옆 플레이어 지정
    n = len(players)
    for i in range(n):
        players[i].left = players[(i-1)%n]
        players[i].right = players[(i+1)%n]
    
    # 게임 진행
    current_word = ""
    first_turn = True
    while True:
        print(f"\n{current_player.name}의 차례입니다.")
        
        # 자기 자신을 지목한 경우
        if random.random() < 0.2:  # 20% 확률로 자기 자신 지목
            print(f"{current_player.name}: 공공칠빵!")
            
            current_player, losers = who_is_next(current_player)
            if losers:
                return losers
            
            current_word = ""
            first_turn = True
        
        # 다른 플레이어를 지목한 경우
        else:
            if first_turn:
                valid_words = ["공", "공공", "공공칠", "공공칠빵"]
            elif current_word == "":
                valid_words = ["공"]
            elif current_word == "공":
                valid_words = ["공"]
            elif current_word == "공공":
                valid_words = ["칠"]
            elif current_word == "공공칠":
                valid_words = ["빵"]
            
            word = input(f"{current_player.name}, 단어를 말하세요 ({', '.join(valid_words)} 중 하나): ")
            
            if word not in valid_words:
                print(f"{current_player.name}이(가) 잘못된 단어를 말해 졌습니다!")
                return [current_player]
            
            current_word = word if first_turn else current_word + word
            
            if current_word == "공공칠빵":
                print(f"{current_player.name}: 공공칠빵!")
                
                current_player, losers = who_is_next(current_player)
                if losers:
                    return losers
                
                current_word = ""
                first_turn = True
            else:
                current_player = current_player.right  # 다음 플레이어로 넘어감
            
            first_turn = False

def who_is_next(current_player):
    # 양옆 플레이어가 '으악!' 또는 '...' 외치기
    left_shout = '으악!' if random.random() < 0.5 else '...'
    right_shout = '으악!' if random.random() < 0.5 else '...'
    
    print(f"{current_player.left.name}: {left_shout}")
    print(f"{current_player.right.name}: {right_shout}")
    
    losers = []
    if left_shout == '...':
        losers.append(current_player.left)
    if right_shout == '...':
        losers.append(current_player.right)
    
    if losers:
        if len(losers) == 2:
            print(f"모두 : 아 누가 술을 마셔 둘이 같이 마셔 ~ 원~~~샷!")
        else:
            loser = losers[0]
            print(f"모두 : 아 누가 술을 마셔 {loser.name}(이)가 술을 마셔~ {loser.name[0]}! 짝짝짝 짝짝! {loser.name[1]}! 짝짝짝 짝짝! 원~~~샷!")
        
        for loser in losers:
            loser.lose_game()
        
        next_player = current_player.right if right_shout == '...' else current_player.left
    else:
        next_player = current_player
    
    return next_player, losers

# 2번 게임
def like_game_check(str, a, game2_players, player, count, game2_player):
    if str == "좋아!":
        game2_player = next((p for p in game2_players if p.name == a), None)
        game2_players = player.copy()
        count = 0
    else:
        count += 1
        game2_players = [p for p in game2_players if p.name != a]  # "캌 퉤!"를 외친 플레이어 제거(새로운 list생성)
    return game2_player, game2_players, count

def like_game(choice_player,player):
    speak_list = ["좋아!", "캌 퉤!"]
    print("현재 사람들 중 한명을 지목하여 00 좋아!를 입력해주세요. (본인제외) 한번 거절당한 사람에게는 다시시도 못합니다!")
    print("술도 마셨는데~ 좋아 게임할까?")

    game2_player = choice_player  # 시작 플레이어
    game2_players = player.copy()  # 플레이어 목록 복사
    count = 0

    while game2_players:
        if count == 0:
            game2_players.remove(game2_player)
        if me.name == game2_player.name:  # 시작 플레이어가 본인일 경우
            a, b = input(game2_player.name + ": ").split()
            b = random.choice(speak_list)
            print("->", a, " : ", b)
            time.sleep(2)
            game2_player, game2_players, count = like_game_check(b, a, game2_players, player, count,game2_player)
        else:  # 시작 플레이어가 본인이 아닐 경우
            a = random.choice(game2_players).name
            print(game2_player.name + ": " + a + " " + "좋아!")
            time.sleep(2)
            if me.name != a:  # 컴퓨터가 지목되었을 경우
                b = random.choice(speak_list)
                print("->", a, " : ", b)
                time.sleep(2)
                game2_player, game2_players, count = like_game_check(b, a, game2_players, player, count,game2_player)
            else:  # 본인이 지목되었을 경우
                b = input("-> " + a + " : ")
                time.sleep(2)
                game2_player, game2_players, count = like_game_check(b, a, game2_players, player, count,game2_player)
    print(f"아 누가누가 술을 마셔 {game2_player.name}이(가) 술을 마셔 원~~~~~샷! \U0001F61D")
    return game2_player

# 3번 게임
def iam_ground(starter, player):
    print("\U0001F44F 아이엠 그라운드\U0001F44F 자기 이름 대기~")

    for gamer in player:
        print(f"나는 {gamer.name}!")

    print("아이엠 그라운드 지금부터 시작 ~")

    defender = []
    attacker = starter
    while True:
        for gamer in player:  # 공격자 제외 나머지 사람들은 방어
            if gamer.name != attacker.name:
                defender.append(gamer)

        # 공격 부분
        if attacker.name == name:  # 공격자가 나일 경우
            _who, num = input("누구를 몇 번 부를 건지 입력(자신은 지목할 수 없음) : ").split(
                sep=" "
            )  # 이름, 횟수 입력
            for i in defender:
                if i.name == _who:
                    who = i
        else:  # 공격자가 내가 아닐 경우
            who = defender[random.randint(0, len(defender) - 1)]  # 이름 랜덤 선택
            num = random.randint(1, 4)  # 이름 부를 횟수 랜덤 선택
            print(f"{attacker.name} : {who.name}, {num}!")

        # 방어 부분
        weight = []  # 가중치 리스트
        defend = []
        if who.name == name:  # 내가 지목된 경우
            # print("내가 지목됨. 알맞게 방어 : ", end=' ')
            defend = input("내가 지목됨. 알맞게 방어 : ").split(sep=" ")
            if len(defend) != int(num):  # 틀리면 게임 종료
                print(
                    f"모두 : 아 누가 술을 마셔 {name}(이)가 술을 마셔~ {name[0]}! 짝짝짝 짝짝! {name[1]}! 짝짝짝 짝짝! 원~~~샷!"
                )
                return who
        else:  # 다른 사람이 지목된 경우
            for i in range(1, 5):
                if i == int(num):
                    weight.append(0.6)  # 올바르게 대답할 확률 0.7
                else:
                    weight.append(0.2)  # 틀릴 확률 0.1
            answer_num = random.choices(range(1, 5), weight)[
                0
            ]  # 가중치를 적용하여 대답할 횟수 1~4 랜덤 추출
            print(f"{who.name} : ", end=" ")
            for i in range(1, answer_num + 1):  # 대답할 횟수만큼 대답하게 함
                print(f"{who.name}", end=" ")
            print("!", end=" ")
            print()
            if answer_num != int(num):  # 틀렸으면 게임 종료
                print(
                    f"모두 : 아 누가 술을 마셔 {who.name}(이)가 술을 마셔~ {who.name[0]}! 짝짝짝 짝짝! {who.name[1]}! 짝짝짝 짝짝! 원~~~샷!"
                )
                return who
        attacker = who
        defender.clear()
        weight.clear()
        defend.clear()


# 4번 게임
# 여기 구현~~~
def subwaygame(choiced_player, player) -> Player:
    target_player = choiced_player
    is_me = False
    if choiced_player == player[0]:
        is_me = True
    if is_me:
        target_line = input("\U0001F687 지하철~ 지하철! 지하철~ 지하철! 몇호선~ 몇호선? :")
        tmp = target_line
        try:
            target_line = "".join(filter(str.isdigit, target_line))
            target_line = int(target_line)
        except ValueError:
            target_line = 0
        if target_line not in subwaylist.subway_lines.keys():
            print(f"뭔 {tmp}이여~ 바보샷 ~! 바보샷 ~!")
            return target_player
    else:
        target_line = random.choice(list(subwaylist.subway_lines.keys()))
    print(f"{choice_player.name}: {target_line}호선! {target_line}호선!")
    line = subwaylist.subway_lines[int(target_line)]
    print("Game ~ start!")

    while True:
        if target_player == player[0]:  # 본인이면
            selected_station = input(f"{target_line}호선 무슨역? :")
            if selected_station in line:
                print(f"{target_player.name}: {selected_station}!")
                line.remove(selected_station)
                target_player = player[
                    (player.index(target_player) + 1) % 4
                ]  # 다음 사람으로 넘어가기
            else:  # 틀렸을 떄
                print(
                    f"모두: {target_player.name}이(가) 술을마셔 {target_player.name[0]}! 짝짝짝 짝짝! {target_player.name[1]}! 짝짝짝 짝짝! 원 ~ 샷!!"
                )
                break
        else:  # 컴퓨터면
            a = random.randint(0, 9)
            if a == 0:  # 컴퓨터는 10% 확률로 틀림
                b = random.randint(0, 2)
                if b == 0:
                    print(f"{target_player.name}: 흠...")
                elif b == 1:
                    print(f"{target_player.name}: 어...")
                else:
                    print(f"{target_player.name}: 아.")
                print(
                    f"모두: {target_player.name}이(가) 술을마셔 {target_player.name[0]}! 짝짝짝 짝짝! {target_player.name[1]}! 짝짝짝 짝짝! 원 ~ 샷!!"
                )
                break
            else:
                selected_station = random.choice(line)
                print(f"{target_player.name}: {selected_station}!")
                line.remove(selected_station)
                target_player = player[
                    (player.index(target_player) + 1) % 4
                ]  # 다음 사람으로 넘어가기
    return target_player


######################

player_list = ["민석", "연진", "동현", "라현"]  # 전체 인원 명단

# 게임 인트로 정해서 넣기
# 1번
print("게임을 진행할까요? (y/n) : ", end=" ")
answer = input()

if answer == "n":
    sys.exit()

# 2번
while True:
    print("오늘 거하게 취해볼 당신의 이름은? : ", end=" ")
    name = input()
    if name in player_list:
        break
    else:
        print("이름을 정확히 입력해주세요")


# 3번
print(
    "~~~~~~~~~~~~~~~~~~\U0001F37A  소주 기준 당신의 주량은? \U0001F37A~~~~~~~~~~~~~~~~~"
)
print("                   \U0001F37A 1. 소주 반병 (2잔)")
print("                   \U0001F37A 2. 소주 반병에서 한병 (4잔)")
print("                   \U0001F37A 3. 소주 한병에서 한병 반 (6잔)")
print("                   \U0001F37A 4. 소주 한병 반에서 두병 (8잔)")
print("                   \U0001F37A 5. 소주 두병 이상 (10잔)")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

while True:
    try:
        print("당신의 치사량(주량)은 얼마만큼인가요? (1~5를 선택해주세요) : ", end=" ")
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
        else:
            print("1~5를 선택해주세요")
    except:
        print("1~5를 선택해주세요")

me = Player(name, deadline, 0)

# 4번
while True:
    try:
        print(
            "함께 취할 친구들은 얼마나 필요하신가요?(사회적 거리두기로 인해 최대 3명까지 초대할 수 있어요!) : ",
            end=" ",
        )
        friendNum = int(input())
        if 1 <= friendNum <= 3:
            break
        else:
            print("1명에서 3명까지 초대할 수 있습니다")
    except:
        print("1명에서 3명까지 초대할 수 있습니다")

friends = make_friend(name, friendNum, player_list)
player = [me]  # 술게임에 참가하는 총 참가자 명단(객체 저장)
for friend in friends:

    num = random.randint(1, 5)
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
round = 0  # 게임 몇 판째인지 확인
alist = []
while True:  # 게임 시작 반복문
    # print(f"현재 몇 판째? => {round}") // 주석 단 사람 : 라현

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for i in player:  # 게임 전 현재 상태 출력
        i.status()

    for i in player:  # 치사량만큼 마셨는지 확인
        i.is_dead()

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(
        "~~~~~~~~~~~~~~~~~~\U0001F37A  오늘의 Alcohol GAME \U0001F37A~~~~~~~~~~~~~~~~~"
    )
    print("                    1. \U0001F52B 공공칠빵\U0001F52B")
    print("                    2. \U0001F494 좋아\U0001F494")
    print("                    3. \U0001F44F 아이엠 그라운드\U0001F44F")
    print("                    4. \U0001F687 지하철\U0001F687")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    if round == 0:  # 첫 번째 판은 내가 먼저
        choice_player = me
    elif 1 <= round <= len(player) - 1:  # 두 번째 ~ 마지막 사람 차례까지는 랜덤 선택
        a = random.randint(1, len(player) - 1)
        while a in alist:  # 이미 했던 사람이면 다시 선택
            a = random.randint(1, len(player) - 1)
        alist.append(a)
        choice_player = player[a]
    else:  # 한 바퀴 다 돌았는데 아무도 안죽었으면 계속 랜덤 선택
        choice_player = player[random.randint(0, len(player) - 1)]

    if choice_player.name == name:  # 게임을 고르는 사람이 나면 직접 게임 선택
        while True:
            print(
            f"{choice_player.name}(이)가 좋아하는 랜덤 게임 ~ 랜덤 게임 ~ 무슨 게임? : ",
            end=" ",
            )
            num = int(input())
            if 1 <= num <= 4:
                break
            else:
                print("게임은 1~4번 중에서 골라주세요")
    else:  # 내가 아니면 랜덤으로 게임 선택
        print(
            '술게임 진행중 ! 다른 사람의 턴입니다. 그만하고 싶으면 "exit"를, 계속하고 싶으면 아무키나 입력해 주세요 : ',
            end=" ",
        )
        choice = input()
        if choice == "exit":
            sys.exit("게임을 종료합니다")
        num = random.randint(1, 4)
        print(
            f"{choice_player.name}(이)가 좋아하는 랜덤 게임 ~ 랜덤 게임 ~ 무슨 게임? : {num}"
        )

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"{choice_player.name} 님이 게임을 선택하셨습니다!\n")

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    print(f"{round+1}번째 라운드 게임 시작~~~~~~~ 이 부분도 인트로 찾아서 만들기") # 수정 완료 : round -> round + 1
    # 게임 구현

    if num == 1:
        # print("1번 게임 시작")
        # loser = 
        game_007(choice_player, player)

        # 1번 게임 함수 호출
    elif num == 2:
        print("\U0001F494 좋아\U0001F494 게임 시작")
        loser = like_game(choice_player,player)
        loser.lose_game()
        # 2번 게임 함수 호출
    elif num == 3:
        # print("3번 게임 시작")
        loser = iam_ground(choice_player, player)
        loser.lose_game()
        # 3번 게임 함수 호출
    elif num == 4:
        # print("4번 게임 시작")
        # 4번 게임 함수 호출
        loser = subwaygame(choice_player, player)
        loser.lose_game()

    #loser.lose_game()
    print(f"{round+1}번째 라운드 게임 종료~~~~~~ 이 부분도 인트로 찾아서 수정해야함") # 수정 완료 : round -> round + 1
    round += 1