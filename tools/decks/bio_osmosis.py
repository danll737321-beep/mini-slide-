"""Cells: Osmosis — Force & Motion layout, zh + en."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from fm import *  # noqa

SALT = INK

def _cell(cx, cy, r, inside_salt, color=ACC):
    s = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{CARD}" stroke="{color}" stroke-width="6"/>'
    pts = [(-0.35, -0.3), (0.3, -0.25), (0, 0.05), (-0.25, 0.35), (0.3, 0.35)][:inside_salt]
    return s + ''.join(f'<circle cx="{cx + dx * r:.0f}" cy="{cy + dy * r:.0f}" r="7" fill="{SALT}"/>' for dx, dy in pts)

def svg_cover_cell(label):
    inner = (f'<circle cx="360" cy="240" r="170" fill="#22343A" stroke="{ACC_L}" stroke-width="10"/>'
             f'<circle cx="400" cy="210" r="46" fill="{ACC_L}" opacity=".85"/>'
             + ''.join(f'<path d="M{x} {y} q14 -26 0 -40 q-14 14 0 40z" fill="{BLUE_L}"/>' for x, y in [(80, 120), (110, 400), (640, 150), (620, 380)])
             + ''.join(arrow(x1, y1, x2, y2, BLUE_L, 6, 18) for x1, y1, x2, y2 in [(110, 150, 200, 190), (140, 380, 215, 330), (610, 170, 520, 200), (590, 370, 505, 320)]))
    return svg(label, 720, 480, inner)

def svg_diffusion(lang, label):
    T = lambda en, zh: en if lang == 'en' else zh
    left = ''.join(f'<circle cx="{40 + (i * 23) % 90}" cy="{80 + (i * 41) % 220}" r="9" fill="{ACC}"/>' for i in range(24))
    right = ''.join(f'<circle cx="{350 + (i * 61) % 250}" cy="{70 + (i * 47) % 230}" r="9" fill="{ACC}"/>' for i in range(24))
    inner = (f'<rect x="20" y="50" width="260" height="270" rx="18" fill="{BLUE_T}" stroke="{INK}" stroke-width="5"/>{left}'
             f'<rect x="340" y="50" width="280" height="270" rx="18" fill="{BLUE_T}" stroke="{INK}" stroke-width="5"/>{right}'
             + arrow(150, 185, 260, 185, MUTED, 5, 16) + text(150, 30, T('Start', '開始'), 26, INK, 800) + text(480, 30, T('Later', '一段時間後'), 26, INK, 800))
    return svg(label, 640, 380, inner)

def svg_three_cells(lang, label):
    T = lambda en, zh: en if lang == 'en' else zh
    def panel(x, r, salt_out, arrows_in, arrows_out, title, result):
        s = f'<rect x="{x}" y="10" width="420" height="250" rx="20" fill="{BLUE_T}"/>'
        s += ''.join(f'<circle cx="{x + 40 + (i * 97) % 340}" cy="{40 + (i * 59) % 190}" r="7" fill="{SALT}"/>' for i in range(salt_out))
        s += _cell(x + 210, 135, r, 3)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if arrows_in:
                s += arrow(x + 210 + dx * (r + 60), 135 + dy * (r + 40), x + 210 + dx * (r + 12), 135 + dy * (r + 10), BLUE, 6, 18)
            if arrows_out:
                s += arrow(x + 210 + dx * (r + 10), 135 + dy * (r + 8), x + 210 + dx * (r + 58), 135 + dy * (r + 38), BLUE, 6, 18)
        return s + text(x + 210, 300, title, 30, INK, 800) + text(x + 210, 340, result, 26, MUTED, 700)
    return svg(label, 1500, 360, panel(20, 80, 0, True, False, T('Pure water', '清水'), T('water moves in → swells', '水往內 → 脹大'))
               + panel(540, 62, 3, False, False, T('Same saltiness', '濃度相同'), T('no net change', '大小不變'))
               + panel(1060, 46, 12, False, True, T('Salt water', '鹽水'), T('water moves out → shrinks', '水往外 → 縮小')))

def svg_strips(lang, label):
    T = lambda en, zh: en if lang == 'en' else zh
    rows = [(T('Start', '開始'), 5.0, '#E8D9A8'), (T('Plain water', '清水'), 5.3, '#F2E3B0'), (T('Strong salt', '濃鹽水'), 4.6, '#D4C08A')]
    inner = ''
    for i, (name, L, c) in enumerate(rows):
        y = 70 + i * 100
        inner += f'<rect x="200" y="{y}" width="{L * 70:.0f}" height="44" rx="10" fill="{c}" stroke="{INK}" stroke-width="3"/>'
        inner += text(180, y + 32, name, 26, INK, 800, 'end') + text(212 + L * 70, y + 32, f'{L} cm', 26, MUTED, 700, 'start')
    inner += f'<line x1="550" y1="50" x2="550" y2="330" stroke="{ACC}" stroke-width="3" stroke-dasharray="8 8"/>'
    return svg(label, 720, 400, inner)

def svg_rbc(lang, label):
    T = lambda en, zh: en if lang == 'en' else zh
    def rbc(cx, r, ry, burst=False):
        s = f'<ellipse cx="{cx}" cy="170" rx="{r}" ry="{ry}" fill="#D84B4B"/>'
        if not burst:
            s += f'<ellipse cx="{cx}" cy="170" rx="{r * 0.45:.0f}" ry="{ry * 0.4:.0f}" fill="#B83232"/>'
        else:
            s += ''.join(f'<line x1="{cx + dx}" y1="{170 + dy}" x2="{cx + dx * 1.5:.0f}" y2="{170 + dy * 1.5:.0f}" stroke="#D84B4B" stroke-width="5" stroke-linecap="round"/>' for dx, dy in [(70, -50), (-70, -50), (80, 40), (-80, 40)])
        return s
    return svg(label, 640, 380, rbc(110, 82, 82, True) + rbc(320, 75, 52) + f'<path d="M500 140 q20 -20 40 0 q20 20 40 0 q-10 40 -40 50 q-30 -10 -40 -50z" fill="#D84B4B"/>'
               + text(110, 300, T('Pure water', '清水'), 26, INK, 800) + text(110, 334, T('swells, may burst', '脹大，可能破裂'), 22, MUTED)
               + text(320, 300, T('Saline', '生理食鹽水'), 26, INK, 800) + text(320, 334, T('stays normal', '維持正常'), 22, MUTED)
               + text(540, 300, T('Salty water', '濃鹽水'), 26, INK, 800) + text(540, 334, T('shrivels', '皺縮'), 22, MUTED))


def build(lang):
    T = lambda en, zh: en if lang == 'en' else zh
    S = Deck(lang, T('Cells: Osmosis', '細胞：滲透作用'))

    S.cover(T('BIOLOGY', '生物'), T('Cells:<br>Osmosis', '細胞：<br>滲透作用'),
            T('How does water get in and out of a cell?<br>It always heads for the saltier side.', '水是怎麼進出細胞的？<br>它總是往比較鹹的那邊跑。'),
            svg_cover_cell(T('A cell with water drops moving toward it from every side', '一個細胞，四周的水滴正朝它移動')),
            T('This lesson is for students who have never studied cells in detail. We start with salted cucumbers, build up the idea of diffusion, '
              'and finish with why vegetables stay crisp and why hospitals use saline.',
              '這一課給沒有深入學過細胞的同學。我們從撒鹽的小黃瓜開始，建立擴散的概念，最後解釋蔬菜為什麼能保持爽脆、醫院為什麼用生理食鹽水。'))

    S.hook(T('START WITH A PUZZLE', '先想一個謎題'), T('Why does salted cucumber get watery?', '小黃瓜撒鹽後，為什麼會出水？'),
           ('Droplet', T('Salt on cucumber', '小黃瓜撒鹽'),
            T('Ten minutes later, <b style="color:#18262B">water pools on the plate</b> and the slices go limp.', '十分鐘後，<b style="color:#18262B">盤子上積了一灘水</b>，小黃瓜也變軟了。')),
           ('Leaf', T('Water on lettuce', '生菜噴水'),
            T('Stores spray vegetables so they stay <b style="color:#18262B">crisp and firm</b>.', '超市在蔬菜上噴水，讓它們保持<b style="color:#18262B">爽脆硬挺</b>。')),
           T('In both cases, water is moving <b style="color:#B4521F">in or out of the vegetable’s cells</b>.', '兩種情況裡，水都在<b style="color:#B4521F">進出蔬菜的細胞</b>。'),
           T('Demo: at the start of class, sprinkle salt on cucumber slices and leave them on a plate. Show the water at the end of this slide. '
             'Ask: did the water come from the salt, the air, or inside the cucumber?',
             '示範：上課一開始就在小黃瓜片上撒鹽，放在盤子上。講完這張讓學生看盤子裡的水，問他們：水是來自鹽、空氣，還是小黃瓜裡面？'))

    S.goals(T('LEARNING GOALS', '學習目標'), T('By the end of this deck, you can:', '看完這份簡報，你會：'), [
        ('Activity', T('Explain diffusion', '說明擴散'), T('Say why particles spread out.', '解釋粒子為什麼會散開。')),
        ('Droplet', T('Predict osmosis', '預測滲透方向'), T('Tell which way water will move.', '判斷水會往哪邊移動。')),
        ('Leaf', T('Explain everyday cases', '解釋生活現象'), T('Crisp vegetables, saline drips.', '爽脆的蔬菜、生理食鹽水點滴。')),
    ], T('The goals match the three parts: diffusion, the osmosis rule, and what osmosis does to plant and animal cells.',
         '三個目標對應三段：擴散、滲透規則、滲透對植物和動物細胞的影響。'))

    S.basics(T('BEFORE YOU START', '開始之前'), T('Four words you need first', '先認識四個詞'), [
        ('o', T('Cell membrane', '細胞膜'), T('The thin skin around a cell. Water passes through; salt hardly does.', '包住細胞的薄膜。水可以通過，鹽很難通過。')),
        ('b', T('Concentration', '濃度'), T('How much stuff (like salt) is in a set amount of water.', '一定量的水裡含有多少東西（例如鹽）。')),
        ('o', T('Diffusion', '擴散'), T('Particles spreading from <b style="color:#18262B">crowded to less crowded</b>.', '粒子從<b style="color:#18262B">擁擠的地方往空曠的地方</b>散開。')),
        ('b', T('Osmosis', '滲透'), T('Diffusion of <b style="color:#18262B">water</b> across a membrane.', '<b style="color:#18262B">水</b>穿過細胞膜的擴散。')),
    ], T('Point out that osmosis is a special case of diffusion: same idea, but only water is moving.', '點出滲透是擴散的一種特例：道理相同，只是移動的是水。'))

    S.figure_text(T('DIFFUSION', '擴散'), T('Particles spread out until they’re even', '粒子會一直散開，直到平均'),
                  svg_diffusion(lang, T('Left: orange particles crowded at one side of a tank of water. Right: later, the particles are spread evenly through the tank',
                                        '左：橘色粒子擠在水槽一邊。右：一段時間後，粒子平均分散在整個水槽')),
                  T('A drop of food coloring in still water.', '一滴食用色素滴進靜止的水裡。'),
                  [T('Particles are always jiggling and bumping.', '粒子一直在晃動、互相碰撞。'),
                   T('Over time they move from where they’re <b>crowded</b> (high concentration) to where they’re <b>spread out</b> (low concentration).',
                     '時間久了，它們會從<b>擁擠</b>的地方（濃度高）移到<b>空曠</b>的地方（濃度低）。')],
                  T('No push needed: diffusion just happens.', '不需要推它：擴散會自己發生。'),
                  T('Quick demo: one drop of food coloring in a clear cup of still water, or spray air freshener at the front of the room and ask students to raise a hand when they smell it.',
                    '快速示範：在一杯靜止的清水裡滴一滴食用色素；或在教室前面噴芳香劑，請學生聞到時舉手。'),
                  tint=True, section=T('Diffusion', '擴散'))

    S.wide_figure(T('OSMOSIS', '滲透'), T('Which way does the water go?', '水會往哪邊走？'),
                  svg_three_cells(lang, T('Three cells: in pure water, arrows point in and the cell swells; in water as salty as the cell, no change; in salt water, arrows point out and the cell shrinks',
                                          '三個細胞：在清水裡，箭頭朝內、細胞脹大；在和細胞一樣鹹的水裡，沒有變化；在鹽水裡，箭頭朝外、細胞縮小')),
                  T('Black dots = salt. Blue arrows = which way water moves.', '黑點 = 鹽。藍色箭頭 = 水移動的方向。'),
                  [T('<b>Pure water</b> outside: the cell is saltier, so water moves <b>in</b>.', '外面是<b>清水</b>：細胞比較鹹，水往<b>內</b>走。'),
                   T('<b>Same saltiness</b>: water moves both ways equally, so nothing changes.', '<b>濃度相同</b>：水進出一樣多，所以沒有變化。'),
                   T('<b>Salt water</b> outside: the outside is saltier, so water moves <b>out</b>.', '外面是<b>鹽水</b>：外面比較鹹，水往<b>外</b>走。')],
                  T('Draw one cell on the board and add salt dots inside and outside; ask students to predict the arrows before revealing.',
                    '在黑板畫一個細胞，裡外各點幾個鹽點，先請學生預測箭頭方向再揭曉。'),
                  section=T('The osmosis rule', '滲透規則'))

    S.rule(T('THE RULE', '規則'), T('Water moves toward<br>the saltier side.', '水會往<br>比較鹹的一邊移動。'),
           T('The membrane lets water through, but salt can’t easily cross. So the water does the moving.', '細胞膜讓水通過，但鹽不容易穿過。所以移動的是水。'),
           T('Back to the hook: the salt was on the outside of the cucumber, so water left the cucumber’s cells and pooled on the plate.',
             '回到開場：鹽在小黃瓜外面，所以水離開了小黃瓜的細胞，積在盤子上。'))

    S.table_figure(T('TRY THE NUMBERS', '看看數據'), T('Potato strips after 40 minutes', '馬鈴薯條泡 40 分鐘後'),
                   svg_strips(lang, T('Three potato strips: the starting strip is 5.0 cm, the one from plain water is 5.3 cm, the one from strong salt water is 4.6 cm',
                                      '三條馬鈴薯條：一開始 5.0 公分，泡清水後 5.3 公分，泡濃鹽水後 4.6 公分')),
                   [T('Soaked in', '泡在'), T('Result', '結果')],
                   [(T('Plain water', '清水'), T('5.3 cm, firm: gained water', '5.3 cm，變硬：吸水')),
                    (T('Weak salt water', '淡鹽水'), T('5.0 cm, no change', '5.0 cm，沒變')),
                    (T('Strong salt water', '濃鹽水'), T('4.6 cm, soft: lost water', '4.6 cm，變軟：失水'))], hi=2,
                   note=T('Longer and firmer = gained water. Shorter and floppy = lost water.', '變長變硬 = 吸了水。變短變軟 = 失去水。'),
                   aside=T('Typical results; yours will vary. Optional lab: soak equal potato strips for at least 40 minutes before class (3 in plain water, 3 in 10% salt water), '
                           'then have pairs measure and bend them. A 15-minute soak in class will not show a difference.',
                           '數據是典型結果，實際會有差異。可選實驗：上課前至少 40 分鐘，把一樣大的馬鈴薯條分別泡清水和 10% 鹽水各 3 條，課堂上讓兩人一組量長度、彎一彎。課堂上只泡 15 分鐘看不出差別。'))

    S.figure_text(T('ANIMAL VS. PLANT CELLS', '動物細胞和植物細胞'), T('Too much water can burst a red blood cell', '水太多，紅血球會脹破'),
                  svg_rbc(lang, T('Three red blood cells: swollen and bursting in pure water, normal in saline, shriveled in salty water',
                                  '三個紅血球：在清水中脹大破裂，在生理食鹽水中正常，在濃鹽水中皺縮')),
                  T('Red blood cells in three liquids.', '紅血球放在三種液體裡。'),
                  [T('<b>Animal cells</b> have only a thin membrane, so too much water can make them burst.', '<b>動物細胞</b>只有一層薄膜，水進太多就可能脹破。'),
                   T('<b>Plant cells</b> have a stiff cell wall, so they get firm instead of bursting. That’s why sprayed lettuce is crisp.',
                     '<b>植物細胞</b>有堅硬的細胞壁，水進來只會變硬，不會破。所以噴過水的生菜很爽脆。')],
                  T('That’s why IV drips use saline (salt water), never pure water.', '所以醫院的點滴用生理食鹽水，絕不用純水。'),
                  T('Saline is about 0.9% salt, the same saltiness as blood, so water moves in and out equally.',
                    '生理食鹽水大約含 0.9% 的鹽，跟血液一樣鹹，所以水進出一樣多。'), tint=True)

    S.compare(T('ONE TABLE', '一張表看懂'), T('Diffusion vs. osmosis', '擴散和滲透，差在哪裡？'),
              [T('Compare', '比較'), T('Diffusion', '擴散'), T('Osmosis', '滲透')], [
                  (T('What moves', '誰在移動'), T('Any particles', '任何粒子'), T('Only water', '只有水')),
                  (T('Needs a membrane?', '需要細胞膜嗎？'), T('No', '不需要'), T('Yes', '需要')),
                  (T('Direction', '方向'), T('Crowded → less crowded', '擁擠 → 空曠'), T('Toward the saltier side', '往比較鹹的一邊')),
                  (T('Example', '例子'), T('Perfume spreading in a room', '香水味散滿房間'), T('Salted cucumber going limp', '撒鹽的小黃瓜變軟')),
              ],
              T('osmosis is diffusion of water through a membrane.', '滲透就是水穿過細胞膜的擴散。'),
              T('Ask students to add one more example to each column.', '請學生在每一欄各補一個例子。'))

    S.example(T('WORKED EXAMPLE', '例題'), T('A cell with 1% salt is placed in 5% salt water. What happens?', '含鹽 1% 的細胞放進 5% 的鹽水，會發生什麼事？'), [
        (T('Compare', '比較'), T('in 1%<br>out 5%', '內 1%<br>外 5%')),
        (T('Saltier side', '比較鹹的一邊'), T('outside', '外面')),
        (T('Water moves', '水往哪走'), T('out', '往外')),
        (T('Result', '結果'), T('cell shrinks', '細胞縮小')),
    ], T('Water leaves, so the cell <span style="color:#2463B8">shrinks</span>', '水跑出去，細胞<span style="color:#2463B8">縮小</span>'),
       T('Students often stop at “the outside is saltier.” Push them to finish the chain: so water moves out, so the cell shrinks.',
         '學生常常只說到「外面比較鹹」就停了。引導他們說完整：所以水往外走，所以細胞縮小。'))

    S.myth(T('THE MOST COMMON MYTH', '最常見的迷思'), T('Does the salt move into the cell?', '是鹽跑進細胞裡嗎？'), T('No.', '不是。'),
           T('The membrane lets <b>water</b> through easily, but salt hardly crosses. The salt stays put; the <b>water</b> is what moves.',
             '細胞膜讓<b>水</b>輕鬆通過，但鹽幾乎過不去。鹽留在原地，移動的是<b>水</b>。'),
           T('That’s why salted cucumber gets watery instead of salty inside: water comes <b>out</b> to the salt.', '所以撒鹽的小黃瓜是出水，而不是裡面變鹹：是水<b>跑出來</b>找鹽。'),
           T('Students read “more salt” as “the salt moves.” Close it with one line: the salt stays; the water travels.', '學生常把「鹽比較多」理解成「鹽在移動」。用一句話收尾：鹽不動，水在跑。'),
           section=T('Myth, quiz and summary', '破解迷思、小測驗與總結'))

    S.quiz(T('QUICK CHECK', '小測驗'), T('Answer first, then check the next slide', '先自己作答，再翻下一張對答案'), [
        T('A red blood cell is put in pure water. Which way does water move, and what happens?', '把紅血球放進清水，水往哪個方向移動？會發生什麼事？'),
        T('Why do grocery stores spray water on fresh vegetables?', '為什麼超市要在新鮮蔬菜上噴水？'),
        T('True or false: in osmosis, salt moves across the membrane.', '是非題：滲透作用中，鹽會穿過細胞膜。'),
    ], T('Let students answer on their own first. For Q1, remind them to find the saltier side.', '先讓學生自己作答。第 1 題提醒他們先找出比較鹹的一邊。'))

    S.answers(T('Answers and the big idea', '答案與一句話總結'), [
        (T('In; it swells', '往內；脹大'), T('The cell is saltier, so it may even burst.', '細胞比較鹹，甚至可能脹破。')),
        (T('To keep them crisp', '保持爽脆'), T('Water moves into the cells and makes them firm.', '水進入細胞，讓它們變硬挺。')),
        (T('False', '錯'), T('Water moves; the salt stays put.', '移動的是水，鹽留在原地。')),
    ], T('Water moves toward the saltier side.<br><span style="color:#E58A55">The salt stays; the water travels.</span>',
         '水往比較鹹的一邊移動。<br><span style="color:#E58A55">鹽不動，水在跑。</span>'),
       T('Optional sentence frames: “The water moves ___ the cell because the concentration outside is ___.” “The strip in ___ became ___ because it ___ water.”',
         '可選句型練習：「水會往細胞___移動，因為外面的濃度比較___。」「泡在___裡的薯條變___了，因為它___了水。」'))
    return S

if __name__ == '__main__':
    for lang in ('en', 'zh'):
        build(lang).write(f'bio-osmosis-{lang}')
