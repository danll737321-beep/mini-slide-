"""Ecology: Food Webs & Energy Pyramids — Force & Motion layout, zh + en."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from fm import *  # noqa

GREEN, GREEN_T = '#5B8C3A', '#E3EDD6'

def svg_cover(label):
    inner = (f'<circle cx="610" cy="90" r="56" fill="#FFC94D"/>'
             f'<polygon points="360,70 230,200 490,200" fill="{ACC}"/>'
             f'<polygon points="230,210 490,210 590,330 130,330" fill="{ACC_L}"/>'
             f'<polygon points="130,340 590,340 690,460 30,460" fill="{GREEN}"/>'
             + arrow(560, 130, 470, 230, '#FFC94D', 6, 18))
    return svg(label, 720, 480, inner)

def svg_chain(lang, label):
    T = lambda en, zh: en if lang == 'en' else zh
    items = [(T('Sun', '太陽'), '#FFC94D', INK), (T('Grass', '草'), GREEN, '#FFFFFF'), (T('Rabbit', '兔子'), ACC_L, INK), (T('Wolf', '狼'), ACC, '#FFFFFF')]
    inner = ''
    for i, (name, fill, ink) in enumerate(items):
        y = 20 + i * 92
        inner += box(170, y, 300, 66, name, fill, ink, fill, 30, 16, 900)
        if i:
            inner += arrow(320, y - 24, 320, y - 2, MUTED, 6, 16)
    inner += text(475, 220, T('energy flows', '能量流向'), 24, BLUE, 800, 'start') + arrow(540, 250, 540, 330, BLUE, 5, 16)
    return svg(label, 640, 380, inner)

def svg_web(lang, label):
    T = lambda en, zh: en if lang == 'en' else zh
    N = {'grass': (760, 330, T('Grass', '草'), GREEN, '#FFFFFF'), 'rabbit': (380, 200, T('Rabbit', '兔子'), ACC_T, INK),
         'deer': (760, 200, T('Deer', '鹿'), ACC_T, INK), 'mouse': (1140, 200, T('Mouse', '老鼠'), ACC_T, INK),
         'snake': (1240, 70, T('Snake', '蛇'), ACC_L, INK), 'hawk': (900, 70, T('Hawk', '老鷹'), ACC, '#FFFFFF'),
         'wolf': (480, 70, T('Wolf', '狼'), ACC, '#FFFFFF')}
    edges = [('grass', 'rabbit'), ('grass', 'deer'), ('grass', 'mouse'), ('rabbit', 'wolf'), ('rabbit', 'hawk'), ('deer', 'wolf'),
             ('mouse', 'hawk'), ('mouse', 'snake'), ('snake', 'hawk')]
    inner = ''
    for a, b in edges:
        x1, y1 = N[a][0], N[a][1]; x2, y2 = N[b][0], N[b][1]
        if y1 == y2:
            sg = 1 if x2 > x1 else -1
            inner += arrow(x1 + 100 * sg, y1, x2 - 102 * sg, y2, MUTED, 4, 14)
        else:
            dx = x2 - x1
            inner += arrow(x1 + dx * 0.12, y1 - 30, x2 - dx * 0.12, y2 + 32, MUTED, 4, 14)
    for x, y, name, fill, ink in N.values():
        inner += box(x - 100, y - 30, 200, 60, name, fill, ink, fill, 28, 14, 900)
    return svg(label, 1500, 370, inner)

def svg_pyramid(lang, label):
    T = lambda en, zh: en if lang == 'en' else zh
    rows = [(T('Wolf', '狼'), '100 kJ', ACC, 220), (T('Rabbit', '兔子'), '1,000 kJ', ACC_L, 400), (T('Grass', '草'), '10,000 kJ', GREEN_T, 620)]
    inner = ''
    for i, (name, kj, fill, w) in enumerate(rows):
        y = 40 + i * 110
        inner += f'<rect x="{360 - w / 2:.0f}" y="{y}" width="{w}" height="90" rx="12" fill="{fill}"/>'
        inner += text(360, y + 40, name, 28, '#FFFFFF' if i == 0 else INK, 900) + text(360, y + 74, kj, 24, '#FFFFFF' if i == 0 else INK, 700)
    return svg(label, 720, 400, inner)

def svg_yellowstone(lang, label):
    T = lambda en, zh: en if lang == 'en' else zh
    steps = [(T('Wolves', '狼'), '↓', ACC), (T('Elk', '麋鹿'), '↑', BLUE), (T('Trees', '河邊的樹'), '↓', ACC)]
    inner = ''
    for i, (name, d, c) in enumerate(steps):
        y = 20 + i * 120
        inner += box(120, y, 280, 84, name, CARD, INK, LINE, 32, 16, 900) + text(470, y + 62, d, 64, c, 900)
        if i:
            inner += arrow(260, y - 32, 260, y - 4, MUTED, 6, 16)
    return svg(label, 640, 380, inner)


def build(lang):
    T = lambda en, zh: en if lang == 'en' else zh
    S = Deck(lang, T('Ecology: Food Webs &amp; Energy Pyramids', '生態：食物網與能量金字塔'))

    S.cover(T('BIOLOGY', '生物'), T('Food Webs &amp;<br>Energy', '食物網與<br>能量金字塔'),
            T('Who eats whom, and where does the energy go?<br>Follow it from the sun to the wolf.', '誰吃誰？能量去了哪裡？<br>從太陽一路追到狼。'),
            svg_cover(T('An energy pyramid with green producers at the bottom, then orange levels above, and the sun shining on it', '一座能量金字塔：底層是綠色的生產者，上面是橘色的各層，太陽照在上面')),
            T('This lesson is for students who have never studied ecology. We start with a real story from Yellowstone, build food chains and webs, '
              'and finish with the 10% rule for energy.',
              '這一課給完全沒學過生態的同學。我們從黃石公園的真實故事開始，建立食物鏈和食物網的概念，最後學能量的 10% 規則。'))

    S.hook(T('START WITH A PUZZLE', '先想一個謎題'), T('Removing wolves made the riverside trees disappear. Why?', '狼被移除後，河邊的樹不見了。為什麼？'),
           ('Warning', T('Wolves removed', '狼被移除'), T('By the 1920s, every wolf in Yellowstone had been hunted. <b style="color:#18262B">Elk numbers boomed.</b>', '到 1920 年代，黃石公園的狼全被獵光了。<b style="color:#18262B">麋鹿數量暴增。</b>')),
           ('Leaf', T('Trees vanished', '樹不見了'), T('Willows and aspens along the rivers were <b style="color:#18262B">eaten down</b> to stumps.', '河岸邊的柳樹和白楊被<b style="color:#18262B">啃到只剩樹樁</b>。')),
           T('Taking away one animal changed the whole park. <b style="color:#B4521F">Food webs</b> explain why.', '只拿走一種動物，整座公園都變了。<b style="color:#B4521F">食物網</b>可以解釋為什麼。'),
           T('Let students guess with a partner first. Wolves were brought back to Yellowstone in 1995, and the riverside trees began to recover.',
             '先讓學生兩人一組猜猜看。1995 年狼被重新引入黃石公園，河邊的樹開始恢復。'))

    S.goals(T('LEARNING GOALS', '學習目標'), T('By the end of this deck, you can:', '看完這份簡報，你會：'), [
        ('Link', T('Build a food chain', '畫出食物鏈'), T('Draw arrows the right way.', '箭頭方向畫對。')),
        ('Users', T('Read a food web', '看懂食物網'), T('Predict what happens when one species disappears.', '預測某種生物消失後會怎樣。')),
        ('Chart', T('Use the 10% rule', '會用 10% 規則'), T('Work out energy at each level.', '算出每一層的能量。')),
    ], T('The goals match the three parts: food chains, food webs, and energy pyramids.', '三個目標對應三段：食物鏈、食物網、能量金字塔。'))

    S.basics(T('BEFORE YOU START', '開始之前'), T('Four words you need first', '先認識四個詞'), [
        ('o', T('Producer', '生產者'), T('Makes its own food from sunlight, like grass and trees.', '利用陽光自己製造養分，例如草和樹。')),
        ('b', T('Consumer', '消費者'), T('Gets energy by eating other living things, like rabbits and wolves.', '吃其他生物來獲得能量，例如兔子和狼。')),
        ('o', T('Decomposer', '分解者'), T('Breaks down dead things and returns nutrients to the soil: bacteria, fungi.', '分解死去的生物，把養分還給土壤：細菌、真菌。')),
        ('b', T('Food web', '食物網'), T('Many food chains linked together, because most animals eat more than one thing.', '許多食物鏈連在一起，因為大多數動物不只吃一種東西。')),
    ], T('Decomposers are often forgotten; remind students they break down every organism in the web once it dies.', '分解者常被忘記；提醒學生，食物網裡的每種生物死後都由分解者分解。'))

    S.figure_text(T('FOOD CHAINS', '食物鏈'), T('Arrows follow the energy', '箭頭跟著能量走'),
                  svg_chain(lang, T('A food chain from top to bottom: sun, grass, rabbit, wolf, with arrows pointing from each to the next', '由上到下的食物鏈：太陽、草、兔子、狼，箭頭從前一個指向下一個')),
                  T('Sun → grass → rabbit → wolf', T('Sun → grass → rabbit → wolf', '太陽 → 草 → 兔子 → 狼')),
                  [T('Energy starts with the <b>sun</b>; producers capture it.', '能量從<b>太陽</b>開始，由生產者接住。'),
                   T('Each arrow means <b>“is eaten by”</b>: grass is eaten by the rabbit.', '每個箭頭代表<b>「被……吃」</b>：草被兔子吃。')],
                  T('Arrows point from the food to the eater.', '箭頭從食物指向吃牠的生物。'),
                  T('Have students read each arrow out loud as “is eaten by” or “gives energy to.”', '請學生把每個箭頭大聲讀成「被……吃」或「把能量給」。'),
                  tint=True, section=T('Food chains and food webs', '食物鏈與食物網'))

    S.wide_figure(T('FOOD WEBS', '食物網'), T('Most animals eat more than one thing', '大多數動物不只吃一種東西'),
                  svg_web(lang, T('A food web: grass feeds rabbit, deer and mouse; rabbit feeds wolf and hawk; deer feeds wolf; mouse feeds hawk and snake; snake feeds hawk',
                                  '食物網：草被兔子、鹿、老鼠吃；兔子被狼和老鷹吃；鹿被狼吃；老鼠被老鷹和蛇吃；蛇被老鷹吃')),
                  T('Every arrow points from food to eater.', '每個箭頭都從食物指向吃牠的生物。'),
                  [T('A <b>food web</b> links many chains together.', '<b>食物網</b>把許多條食物鏈連在一起。'),
                   T('Remove one species and the change <b>ripples</b> through the web.', '拿掉一種生物，影響會<b>擴散</b>到整張網。'),
                   T('Webs with more links are <b>more stable</b>: eaters can switch food.', '連結越多的網越<b>穩定</b>：掠食者可以換別的食物吃。')],
                  T('Optional activity: eight students hold role cards (Sun, Grass, Rabbit, Deer, Mouse, Snake, Hawk, Wolf) and pass yarn from each food to its eater. '
                    'Say “the wolf is gone” and have the wolf let go; ask who feels the yarn go slack.',
                    '可選活動：八位同學拿角色卡（太陽、草、兔子、鹿、老鼠、蛇、老鷹、狼），把毛線從食物傳給吃牠的生物。老師說「狼不見了」，扮演狼的同學放手，問誰感覺到毛線鬆了。'))

    S.figure_text(T('BACK TO THE PUZZLE', '回到謎題'), T('One missing link changes the whole web', '少了一個環節，整張網都會變'),
                  svg_yellowstone(lang, T('Chain reaction: wolves go down, elk go up, riverside trees go down', '連鎖反應：狼減少、麋鹿增加、河邊的樹減少')),
                  T('Yellowstone, 1920s to 1995', T('Yellowstone, 1920s to 1995', '黃石公園，1920 年代到 1995 年')),
                  [T('No wolves → elk had no predator → <b>elk numbers boomed</b>.', '沒有狼 → 麋鹿沒有天敵 → <b>麋鹿數量暴增</b>。'),
                   T('More elk → young trees eaten → <b>riverbanks washed away</b>.', '麋鹿變多 → 小樹被吃光 → <b>河岸被沖刷</b>。')],
                  T('Wolves returned in 1995, and the trees began to recover.', '1995 年狼回來了，樹開始恢復。'),
                  T('Scientists still debate how much of the recovery is due to wolves alone, but the chain reaction is a classic example of a food web at work.',
                    '科學家還在討論恢復有多少是單靠狼的功勞，但這個連鎖反應是食物網運作的經典例子。'))

    S.formula(T('THE 10% RULE', '10% 規則'),
              [('100%', GREEN_T, T('grass', '草')), ('→', None, ''), ('10%', ACC_L, T('rabbit', '兔子')), ('→', None, ''), ('1%', BG, T('wolf', '狼'))],
              T('Only about 10% of the energy passes up each level.', '每往上一層，只有大約 10% 的能量傳上去。'),
              T('The other 90% is used for living (breathing, moving, keeping warm) and lost as heat, or stays in parts that aren’t eaten.',
                '另外 90% 用在生活（呼吸、活動、保持體溫），以熱的形式散失，或留在沒被吃掉的部分。'),
              T('10% is an approximation; real values range from about 5 to 20%. It is the standard figure in textbooks and tests.',
                '10% 是近似值，實際大約在 5% 到 20% 之間。這是課本和考試使用的標準數字。'),
              section=T('Energy pyramids', '能量金字塔'))

    S.table_figure(T('TRY THE NUMBERS', '算算看'), T('An energy pyramid gets narrow fast', '能量金字塔越往上越窄'),
                   svg_pyramid(lang, T('Energy pyramid: grass 10,000 kJ at the bottom, rabbit 1,000 kJ in the middle, wolf 100 kJ at the top',
                                       '能量金字塔：底層草 10,000 kJ，中層兔子 1,000 kJ，頂層狼 100 kJ')),
                   [T('Level', '層級'), T('Energy', '能量')],
                   [(T('1 · Grass', '1 · 草'), '10,000 kJ'), (T('2 · Rabbit', '2 · 兔子'), '1,000 kJ'), (T('3 · Wolf', '3 · 狼'), '100 kJ'), (T('4 · ?', '4 · ？'), '10 kJ')], hi=3,
                   note=T('That’s why there are <b>far fewer</b> top predators than plants.', '所以頂層掠食者的數量<b>遠少於</b>植物。'),
                   aside=T('Cover the energy column and let students fill it in. Ask what could be at level 4, and why it would struggle to survive.',
                           '先遮住能量欄，讓學生自己填。問他們第 4 層可能是什麼生物，為什麼很難生存。'))

    S.compare(T('ONE TABLE', '一張表看懂'), T('Food chain vs. food web', '食物鏈和食物網，差在哪裡？'),
              [T('Compare', '比較'), T('Food chain', '食物鏈'), T('Food web', '食物網')], [
                  (T('Shape', '形狀'), T('One straight line', '一條直線'), T('Many crossing links', '很多交錯的連線')),
                  (T('Shows', '呈現'), T('One path of energy', '一條能量路徑'), T('All the paths together', '所有路徑合在一起')),
                  (T('If one species vanishes', '某種生物消失時'), T('<span style="color:#B4521F">The chain breaks</span>', '<span style="color:#B4521F">整條鏈斷掉</span>'), T('<span style="color:#2463B8">Others may switch food</span>', '<span style="color:#2463B8">其他生物可能改吃別的</span>')),
                  (T('Real ecosystems', '真實的生態系'), T('Too simple', '太簡化'), T('Closer to reality', '比較接近真實')),
              ],
              T('a food web is many food chains linked together.', '食物網是許多條食物鏈連在一起。'),
              T('Ask students to trace three separate chains inside the food web from earlier.', '請學生從前面的食物網裡找出三條不同的食物鏈。'))

    S.example(T('WORKED EXAMPLE', '例題'), T('Grass stores 50,000 kJ. How much reaches a hawk that eats rabbits?', '草儲存了 50,000 kJ，吃兔子的老鷹能得到多少？'), [
        (T('Level 1: grass', '第 1 層：草'), '50,000 kJ'),
        (T('Level 2: rabbit', '第 2 層：兔子'), '× 10%<br>= 5,000 kJ'),
        (T('Level 3: hawk', '第 3 層：老鷹'), '× 10%<br>= 500 kJ'),
        (T('Answer', '答案'), '500 kJ'),
    ], T('The hawk gets about <span style="color:#2463B8">500 kJ</span>', '老鷹大約得到 <span style="color:#2463B8">500 kJ</span>'),
       T('Students who answer 5,000 skipped a level. Have them write out every level first.', '答 5,000 的學生少算了一層。請他們先把每一層都寫出來。'))

    S.myth(T('THE MOST COMMON MYTH', '最常見的迷思'), T('Do arrows point to what gets eaten?', '箭頭是指向被吃的一方嗎？'), T('No.', '不是。'),
           T('Arrows show the <b>flow of energy</b>: from the food to the eater. So it’s grass → rabbit → wolf, not wolf → rabbit → grass.',
             '箭頭代表<b>能量的流向</b>：從食物指向吃牠的生物。所以是草 → 兔子 → 狼，不是狼 → 兔子 → 草。'),
           T('Read every arrow as <b>“is eaten by”</b> and you’ll never get it backward.', '把每個箭頭都讀成<b>「被……吃」</b>，就不會畫反。'),
           T('When students draw their own webs, have them check that every arrow points up from the producers.', '學生自己畫食物網時，請他們檢查每個箭頭都是從生產者往上指。'),
           section=T('Myth, quiz and summary', '破解迷思、小測驗與總結'))

    S.quiz(T('QUICK CHECK', '小測驗'), T('Answer first, then check the next slide', '先自己作答，再翻下一張對答案'), [
        T('In “grass → rabbit,” what does the arrow mean?', '「草 → 兔子」的箭頭代表什麼？'),
        T('All the mice disappear from a field. What happens to the snakes?', '田裡的老鼠全部消失了，蛇會怎樣？'),
        T('Why do food chains rarely have more than 4 or 5 levels?', '為什麼食物鏈很少超過 4 或 5 層？'),
    ], T('Let students answer on their own first. For Q2, have them look back at the food web.', '先讓學生自己作答。第 2 題請他們回頭看食物網。'))

    S.answers(T('Answers and the big idea', '答案與一句話總結'), [
        (T('Is eaten by', '被……吃'), T('Energy flows from grass to rabbit.', '能量從草流向兔子。')),
        (T('They decline', '數量減少'), T('Snakes lose a main food source.', '蛇失去了主要的食物來源。')),
        (T('Energy runs out', '能量不夠'), T('About 90% is lost at each level.', '每一層大約損失 90%。')),
    ], T('Arrows follow the energy, from food to eater.<br><span style="color:#E58A55">Only about 10% passes up each level.</span>',
         '箭頭跟著能量走，從食物指向吃牠的生物。<br><span style="color:#E58A55">每往上一層，只剩大約 10%。</span>'),
       T('Optional sentence frames: “If the ___ disappears, the ___ will increase because ___.” “Only about ___% of the energy in ___ passes to ___.”',
         '可選句型練習：「如果___消失了，___會增加，因為___。」「___裡的能量，只有大約___% 會傳給___。」'))
    return S

if __name__ == '__main__':
    for lang in ('en', 'zh'):
        build(lang).write(f'bio-ecology-{lang}')
