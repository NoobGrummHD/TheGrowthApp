import random
import json
import time
import sys
import os
from colorama import Fore, Back, Style

with open('config.txt', 'r', encoding = 'utf-8') as f:
    txt = f.read()
    lines = f.readlines()

print(lines)

def ls(name):
    ls = []
    line = ''
    i = 0

    

    for linex in lines:
        print(linex)
        # linex.rstrip()
        var = linex.startswith(name)
        if var == True:
            line = linex
            line += ','
            break
        else:
            pass

        # print(linex, var)

    for sym in line:
        if sym == '=':
            break
        i += 1

    ls = line[i:-1].split(',')
    return ls


timel = ls('time')

dol = []
wherel = []
diedl = []
namesl = []
be = []
facel = []
sayl = []


print(timel)

# variables
# timel = ['朝の４時', '朝の１０時', '朝１２時', '昼の２時', '昼の５時', '昼の６時', '昼の８時', '昼の１０時', '夜の１２時', '夜の３時']
# dol = ['ゲーム', 'ユーチューブ', '勉強', '殺し合い',  'コーヒーを作っている', '美味しくないものを食べている', '犯罪で逃げている', '秘密', 'ポテトチップスを食べてる', 'ポテトチップスを買ってる', 'ヨガ', 'はっきょう', '４人につめられている', '逃げている', 'エンドラたおしている', 'Roblox', 'おこげ食べている', 'けいれんしている']
# wherel = ['秘密', 'トイレ', '家', '誰かの家', 'ベッド', '便所', 'ホテル', 'スクランブル交差点', 'ホワイトハウス', 'はるきの家', '外', '学校', '学校のトイレ', 'さいばん所', '病院', 'ロッカー', 'GANTZの世界', 'ネザー', '胃の中', 'シャワー室']
# diedl = ['交通事故', 'トラックにひかれているビニール袋と猫を間違えて死亡', '誘拐にあった', 'わざとやった', 'はんぺん食べて食中毒', '犯罪でしけい', 'なおきの腹に圧縮されて脂肪']
# namesl = ['りょうた', 'よしさと', '志村', '金ちゃんせん', 'あさみ', 'ありま', 'アルセン', 'さくら', 'はるき', 'るいと', 'なおき', 'レオ', 'だいちゃん777', 'さとる', 'ルカ', '美しいおおえ先生']
# be = ['ストリートクリーナー', 'クリーナー', '先生', 'ハッカー', '平和主義者', '殺人者', '医者', '農家', '怖い医者', '危険な先生', 'ししむらテックサーービス', 'ユーチューバー', 'どろぼう', 'ふしんしゃ', '日本大統領']
# facel = ['😁', '😋', '😎', '🥰', '🤩', '🤨', '😥', '🥱', '🥵', '😳', '🥴', '🤕', '🤢', '🥺', '💀', '😂']
# sayl = ['おいしいいいいいい', 'やば', 'アハハハハハ', 'うん', 'まあいいでしょう', 'ちょっと', 'やめて', 'いいよ', 'はっ！？！？', 'えええええ', 'そんな', 'やだやだやだやだやだあああああああ', 'あっ..', '何で']


diedT = ''

def get_data(fn):
    with open(fn, 'r', encoding = 'utf-8') as f:
        data = json.load(f)
    return data
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
def live_age(id_, data, fn):
    # data = get_data()

    x = 0
    y = random.randint(30, 100)
    while x <= y:
        data[id_]['今年'] += 1
        data[id_]['歳'] += 1
        data[id_]['時間'] = random.choice(timel)
        x+=1
        va = random.choice([False, True, False])
        va2 = random.choice([False, True])
        va3 = random.choice([False, False, False, False, True])
        do = random.choice(dol)
        face = random.choice(facel)
        where = random.choice(wherel)
        srif = random.choice(sayl)
        bbb = random.choice(be)
        if va == True:
            data[id_]['今やっていること'] = do
            data[id_]['顔'] = face
            data[id_]['今言っていること'] = srif
        
        if va2 == True:
            data[id_]['場所'] = where
        if va3 == True:
            try:
                data[id_]['今の職業'] = bbb
            except:
                pass
            
        # va = random.choice([False, True])
        if data[id_]['歳'] >= 6:
            if data[id_]['歳'] >= 18:
                try:
                    del data[id_]['評価']
                    data[id_]['今の職業']
                except:
                    pass
                
            else:
                data[id_]['評価'] = random.randint(-1, 5)


        time.sleep(random.randint(2, 5))
        with open(fn, 'w', encoding = 'utf-8') as f:
            json.dump(data, f, indent = 4, ensure_ascii = False)
        cls()
        datatext = str(data)
        newtext = ''
        for i in datatext:
            if i == ',':
                newtext += f'{i}\n    '
            elif i == '{':
                newtext += f'{i}\n    '
            elif i == '}':
                newtext += f'\n{i}'
            else:
                newtext += i
# from colorama import Fore, Back, Style
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')

        print(Fore.BLACK + Back.GREEN + newtext + Style.RESET_ALL)
    cls()
    

    sai = data[id_]['歳']
    riyuu = random.choice(diedl)
    koto = data[id_]['今やっていること']
    data[id_]['今やっていること'] = f'({koto})'
    kotosi = data[id_]['今年']
    
    data[id_]['歳'] = f'- ({sai})'
    data[id_]['今年'] = f'{kotosi}'
    data[id_]['死んだ理由'] = riyuu
    with open(fn, 'w', encoding = 'utf-8') as f:
        json.dump(data, f, indent = 4, ensure_ascii = False)
    datatext = str(data)
    newtext = ''
    ntnew = ''
    ntold = ''
    for i in datatext:
        if i == ',':
            newtext += f'{i}\n    '
        elif i == '{':
            newtext += f'{i}\n    '
        elif i == '}':
            newtext += f'\n{i}'
        else:
            newtext += i

    print(Fore.WHITE + Back.RED + newtext + Style.RESET_ALL)

def create_people(a = 1, fn = 0):
    data = get_data(fn)
    for i in range(a):
        names = random.choice(namesl)
        
        # names = '美しいおおえ先生'
        name = f'{names}{random.randint(1000, 5000)}号'
        age = random.randint(0, 5)
        id_ = random.randint(10000, 50000)
        # data = {}
        data[id_] = {}
        data[id_]['今年'] = random.randint(1500, 2024)
        data[id_]['時間'] = random.choice(timel)
        data[id_]['名前'] = name
        data[id_]['歳'] = 0
        with open(fn, 'w', encoding = 'utf-8') as f:
            json.dump(data, f, indent = 4, ensure_ascii = False)
        live_age(id_, data, fn)
# from colorama import Fore, Back, Style
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')
print("成長アプリ by アルセン - v11.0.1 Alpha\n\n")
time.sleep(2)
dtu = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']
ok__ = False
while True:
    filename = input('ファイル名(\\, /, :, *, ?, ", <, >, | は使用しないでください): ')
    if filename == '':
        filename = 'data'
        break
    else:
        # text = ''
        j = 0
        for sym in filename:
            for i in dtu:
                if sym == i:
                    print(f'ノー 「{sym}」 ですよーー！')
                    break
                else:
                    ok__ = True


    if ok__ == True:
        break
    else:
        pass 

filename += '.json'
print(f'\nファイル名は 「{filename}」 になりました！\n\n')

change = input('設定は変えますか？: ')
# change = 'a'
# timel = ['朝の４時', '朝の１０時', '朝１２時', '昼の２時', '昼の５時', '昼の６時', '昼の８時', '昼の１０時', '夜の１２時', '夜の３時']
# dol = ['ゲーム', 'ユーチューブ', '勉強', '殺し合い',  'コーヒーを作っている', '美味しくないものを食べている', '犯罪で逃げている', '秘密', 'ポテトチップスを食べてる', 'ポテトチップスを買ってる', 'ヨガ', 'はっきょう', '４人につめられている', '逃げている', 'エンドラたおしている', 'Roblox', 'おこげ食べている', 'けいれんしている']
# wherel = ['秘密', 'トイレ', '家', '誰かの家', 'ベッド', '便所', 'ホテル', 'スクランブル交差点', 'ホワイトハウス', 'はるきの家', '外', '学校', '学校のトイレ', 'さいばん所', '病院', 'ロッカー', 'GANTZの世界', 'ネザー', '胃の中', 'シャワー室']
# diedl = ['交通事故', 'トラックにひかれているビニール袋と猫を間違えて死亡', '誘拐にあった', 'わざとやった', 'はんぺん食べて食中毒', '犯罪でしけい', 'なおきの腹に圧縮されて脂肪']
# namesl = ['りょうた', 'よしさと', '志村', '金ちゃんせん', 'あさみ', 'ありま', 'アルセン', 'さくら', 'はるき', 'るいと', 'なおき', 'レオ', 'だいちゃん777', 'さとる', 'ルカ', '美しいおおえ先生']
# facel = ['😁', '😋', '😎', '🥰', '🤩', '🤨', '😥', '🥱', '🥵', '😳', '🥴', '🤕', '🤢', '🥺', '💀', '😂']
# sayl = ['おいしいいいいいい', 'やば', 'アハハハハハ', 'うん', 'まあいいでしょう', 'ちょっと', 'やめて', 'いいよ', 'はっ！？！？', 'えええええ', 'そんな', 'やだやだやだやだやだあああああああ', 'あっ..', '何で']
def get_(arg):
    text = ''
    for x in arg:
        text += f'{x}\n'
    return text
if change == 'はい':
    while True:
        print(f"今の設定:\n(1)時間: \n{get_(timel)}\n(2)今やっていること:\n{get_(dol)}\n(3)場所: \n{get_(wherel)}\n(4)死んだ理由:\n{get_(diedl)}\n(5)名前:\n{get_(namesl)}\n(6)顔のひょうじょう:\n{get_(facel)}\n(7)今言っていること:\n{get_(sayl)}")
        print('変え方： add 2 卵を生んでいる, del 2 ゲーム\n\n')
        inp = input('(add <int> <text> | del <int> <text>): ')
        inp += 'x'
        if inp[0:4] == 'add ':
            # 1 time
            # 2 do
            # 3 where
            # 4 died reasons
            # 5 names
            # 6 face
            # 7 saing
            if inp[4] == '1':
                timel.append(inp[6:-1])
            elif inp[4] == '2':
                dol.append(inp[6:-1])
            elif inp[4] == '3':
                wherel.append(inp[6:-1])
            elif inp[4] == '4':
                diedl.append(inp[6:-1])
            elif inp[4] == '5':
                namesl.append(inp[6:-1])
            elif inp[4] == '6':
                facel.append(inp[6:-1])
            elif inp[4] == '7':
                sayl.append(inp[6:-1])
            else:
                print('ええ。　ないよーーー!!')
        elif inp[0:4] == 'del ':
            # 1 time
            # 2 do
            # 3 where
            # 4 died reasons
            # 5 names
            # 6 face
            # 7 saing
            i = 0
            

            if inp[4] == '1':
                if inp[6:-1] in timel:
                    for x in timel:
                        if x == inp[6:-1]:
                            break
                        i+=1
                    timel.pop(i)
                else:
                    print('ないよーー')
            elif inp[4] == '2':
                if inp[6:-1] in dol:
                    for x in dol:
                        if x == inp[6:-1]:
                            break
                        i+=1
                    dol.pop(i)
                else:
                    print('ないよーー')
                # dol.append(inp[6:-1])
            elif inp[4] == '3':
                if inp[6:-1] in wherel:
                    for x in wherel:
                        if x == inp[6:-1]:
                            break
                        i+=1
                    wherel.pop(i)
                else:
                    print('ないよーー')
                # wherel.append(inp[6:-1])
            elif inp[4] == '4':
                if inp[6:-1] in diedl:
                    for x in diedl:
                        if x == inp[6:-1]:
                            break
                        i+=1
                    diedl.pop(i)
                else:
                    print('ないよーー')
                # diedl.append(inp[6:-1])
            elif inp[4] == '5':
                if inp[6:-1] in namesl:
                    for x in namesl:
                        if x == inp[6:-1]:
                            break
                        i+=1
                    namesl.pop(i)
                else:
                    print('ないよーー')
                # namesl.append(inp[6:-1])
            elif inp[4] == '6':
                if inp[6:-1] in facel:
                    for x in facel:
                        if x == inp[6:-1]:
                            break
                        i+=1
                    facel.pop(i)
                else:
                    print('ないよーー')
                # facel.append(inp[6:-1])
            elif inp[4] == '7':
                if inp[6:-1] in sayl:
                    for x in sayl:
                        if x == inp[6:-1]:
                            break
                        i+=1
                    sayl.pop(i)
                else:
                    print('ないよーー')
                # sayl.append(inp[6:-1])
            else:
                print(f'ええ。 "{inp[6:-1]}" ないよーーー!!')
        else:
            print('\n\n設定が終わりました！！！！やったあああああああああーーーーーーーーーー！！！！\nじゃあ、始めるよお！！！')
            break
else:
    print("オッケー")
time.sleep(1)
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)
print('始め！！！！'*500)
time.sleep(2)

with open(filename, 'w') as f:
    f.write("{}")
create_people(1000, filename)