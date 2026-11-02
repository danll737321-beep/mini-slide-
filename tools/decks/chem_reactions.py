"""Chemical Reactions & Conservation of Mass — Force & Motion layout, zh + en."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from fm import *  # noqa

C_, H_, O_ = '#2F3B40', '#9AAAA6', ACC

def svg_balance(label):
    inner = (f'<polygon points="360,420 320,470 400,470" fill="{ON_DARK}"/>'
             f'<line x1="360" y1="420" x2="360" y2="150" stroke="{ON_DARK}" stroke-width="10"/>'
             f'<line x1="120" y1="150" x2="600" y2="150" stroke="{BG}" stroke-width="10" stroke-linecap="round"/>'
             f'<line x1="150" y1="150" x2="150" y2="300" stroke="{ON_DARK}" stroke-width="4"/><line x1="570" y1="150" x2="570" y2="300" stroke="{ON_DARK}" stroke-width="4"/>'
             f'<path d="M70 300 H230 L210 330 H90 Z" fill="{ON_DARK}"/><path d="M490 300 H650 L630 330 H510 Z" fill="{ON_DARK}"/>'
             f'<path d="M125 300 V220 L140 200 V170 H160 V200 L175 220 V300 Z" fill="{BLUE_L}"/>'
             f'<ellipse cx="150" cy="150" rx="30" ry="38" fill="{ACC_L}"/>'
             f'<rect x="525" y="250" width="90" height="50" rx="8" fill="{ACC_L}"/><rect x="545" y="215" width="50" height="35" rx="6" fill="{ACC_L}"/>')
    return svg(label, 720, 480, inner)

def svg_rearrange(label):
    def ch4(x, y):
        return dot(x, y, 34, C_, 'C') + ''.join(dot(x + dx, y + dy, 18, H_, 'H', INK, 18) for dx, dy in [(-44, -30), (44, -30), (-44, 30), (44, 30)])
    def o2(x, y):
        return dot(x - 22, y, 26, O_, 'O') + dot(x + 22, y, 26, O_, 'O')
    def co2(x, y):
        return dot(x - 50, y, 26, O_, 'O') + dot(x, y, 32, C_, 'C') + dot(x + 50, y, 26, O_, 'O')
    def h2o(x, y):
        return dot(x, y, 28, O_, 'O') + dot(x - 34, y + 26, 18, H_, 'H', INK, 18) + dot(x + 34, y + 26, 18, H_, 'H', INK, 18)
    inner = (ch4(90, 110) + o2(90, 240) + o2(90, 320) + arrow(190, 210, 330, 210, MUTED, 8, 26)
             + co2(480, 110) + h2o(440, 240) + h2o(540, 300)
             + text(90, 30, 'CH₄ + 2O₂', 30, INK, 800) + text(480, 30, 'CO₂ + 2H₂O', 30, INK, 800))
    return svg(label, 640, 380, inner)

def svg_open_closed(lang, label):
    T = lambda en, zh: en if lang == 'en' else zh
    def setup(x, closed, before, after, title):
        s = (f'<rect x="{x}" y="170" width="300" height="24" rx="6" fill="{MUTED}"/>'
             f'<rect x="{x + 30}" y="194" width="240" height="40" rx="8" fill="{INK}"/>'
             + text(x + 150, 223, after, 28, '#7FE0A0' if before == after else ACC_L, 800, 'middle'))
        if closed:
            s += (f'<path d="M{x + 110} 170 V100 L{x + 125} 80 V60 H{x + 175} V80 L{x + 190} 100 V170 Z" fill="{BLUE_T}" stroke="{INK}" stroke-width="5"/>'
                  f'<ellipse cx="{x + 150}" cy="30" rx="36" ry="30" fill="{ACC_L}"/>')
        else:
            s += (f'<path d="M{x + 95} 80 V170 H{x + 205} V80" fill="{BLUE_T}" stroke="{INK}" stroke-width="5"/>'
                  + ''.join(arrow(x + dx, 70, x + dx + 10, 20, BLUE, 4, 12) for dx in (115, 150, 185)))
        s += text(x + 150, 270, title, 28, INK, 800) + text(x + 150, 306, f'{before} → {after}', 26, MUTED, 700)
        return s
    inner = (setup(180, False, '250.0 g', '248.6 g', T('Open cup', '開口杯')) +
             setup(900, True, '250.0 g', '250.0 g', T('Sealed bottle + balloon', '密封瓶 + 氣球')))
    return svg(label, 1400, 320, inner)

def svg_mole(lang, label):
    T = lambda en, zh: en if lang == 'en' else zh
    eggs = ''.join(f'<ellipse cx="{70 + (i % 6) * 50}" cy="{110 + (i // 6) * 60}" rx="20" ry="26" fill="{ACC_T}" stroke="{ACC}" stroke-width="3"/>' for i in range(12))
    dots = ''.join(f'<circle cx="{430 + (i * 37) % 240}" cy="{80 + (i * 53) % 130}" r="7" fill="{BLUE}"/>' for i in range(40))
    inner = (f'<rect x="30" y="60" width="320" height="140" rx="16" fill="none" stroke="{LINE}" stroke-width="4"/>{eggs}'
             f'<rect x="400" y="60" width="300" height="140" rx="16" fill="none" stroke="{LINE}" stroke-width="4"/>{dots}'
             + text(190, 250, T('1 dozen = 12', '1 打 = 12 個'), 30, INK, 800) + text(550, 250, T('1 mole = 6 × 10²³', '1 莫耳 = 6 × 10²³ 個'), 30, INK, 800)
             + text(190, 290, T('eggs', '雞蛋'), 24, MUTED) + text(550, 290, T('particles', '粒子'), 24, MUTED))
    return svg(label, 720, 400, inner)


def build(lang):
    T = lambda en, zh: en if lang == 'en' else zh
    S = Deck(lang, T('Chemical Reactions &amp; Conservation of Mass', '化學反應與質量守恆'))

    S.cover(T('CHEMISTRY', '化學'), T('Chemical<br>Reactions', '化學反應與<br>質量守恆'),
            T('When substances react, does anything get lost?<br>Count the atoms and find out.', '物質反應之後，有東西不見嗎？<br>數一數原子就知道。'),
            svg_balance(T('A balance holding a bottle with a balloon on one side and weights on the other, perfectly level',
                          '天平一邊放著套了氣球的瓶子，另一邊放砝碼，兩邊剛好平衡')),
            T('This lesson is for students who have never studied chemical reactions. We start with a fizzing experiment, then count atoms '
              'to see why mass never disappears, and finish with balancing equations and the mole.',
              '這一課給完全沒學過化學反應的同學。我們從一個冒泡實驗開始，再數原子看看質量為什麼不會消失，最後學平衡反應式和莫耳。'))

    S.hook(T('START WITH A PUZZLE', '先想一個謎題'), T('Does a reaction make things lighter?', '化學反應會讓東西變輕嗎？'),
           ('Flask', T('In an open cup', '在開口杯裡'),
            T('Baking soda + vinegar fizz, and the scale reading <b style="color:#18262B">drops</b>.', '小蘇打加白醋冒泡，秤上的數字<b style="color:#18262B">變小了</b>。')),
           ('Scale', T('In a sealed bottle', '在密封瓶裡'),
            T('The same reaction under a balloon, and the reading <b style="color:#18262B">stays the same</b>.', '同樣的反應，瓶口套上氣球，數字<b style="color:#18262B">完全沒變</b>。')),
           T('Same reaction, different result. So where did the missing mass go?', '同樣的反應，結果卻不同。不見的質量到底跑去哪了？'),
           T('Demo if you can: two identical setups on two digital scales. Put baking soda in a balloon and stretch it over a bottle of vinegar; '
             'tip it in. Do the open version in a cup. Let students predict before you start.',
             '可以的話現場示範：兩組一樣的器材放在兩台電子秤上。把小蘇打裝進氣球、套在裝白醋的瓶口再倒進去；另一組在開口杯裡做。開始前先讓學生預測。'))

    S.goals(T('LEARNING GOALS', '學習目標'), T('By the end of this deck, you can:', '看完這份簡報，你會：'), [
        ('Scale', T('Explain conservation', '說明質量守恆'), T('Say why total mass stays the same.', '解釋為什麼總質量不變。')),
        ('Search', T('Balance equations', '平衡反應式'), T('Use coefficients so atoms add up.', '用係數讓兩邊原子數相等。')),
        ('Chart', T('Use the mole', '會用莫耳'), T('Turn grams into particle counts.', '把公克換算成粒子數量。')),
    ], T('The three goals match the three parts: why mass is conserved, how to balance an equation, and how chemists count with moles.',
         '三個目標對應三段：為什麼質量守恆、怎麼平衡反應式、化學家怎麼用莫耳數粒子。'))

    S.basics(T('BEFORE YOU START', '開始之前'), T('Four words you need first', '先認識四個詞'), [
        ('o', T('Reactant', '反應物'), T('What you start with. In CH₄ + O₂, both are reactants.', '反應開始時的物質。CH₄ + O₂ 裡兩者都是反應物。')),
        ('b', T('Product', '生成物'), T('The new substances that form, written after the arrow.', '反應後產生的新物質，寫在箭頭右邊。')),
        ('o', T('Coefficient', '係數'), T('The big number in front: <b style="color:#18262B">2</b>H₂O means two water molecules.', '寫在前面的大數字：<b style="color:#18262B">2</b>H₂O 代表兩個水分子。')),
        ('b', T('Subscript', '下標'), T('The small number inside: H<b style="color:#18262B">₂</b>O has two H atoms.', '寫在裡面的小數字：H<b style="color:#18262B">₂</b>O 有兩個 H 原子。')),
    ], T('Orange cards are about what goes in; blue cards are about what comes out or how it is written. Coefficient vs. subscript '
         'comes back in the comparison table.',
         '橘色卡片講反應前，藍色卡片講反應後或寫法。係數和下標的差別，後面的對照表會再整理一次。'))

    S.figure_text(T('WHAT A REACTION REALLY IS', '化學反應的真面目'), T('Atoms only change partners', '原子只是換了搭檔'),
                  svg_rearrange(T('Methane and two oxygen molecules on the left rearrange into carbon dioxide and two water molecules on the right; the same atoms appear on both sides',
                                  '左邊是甲烷和兩個氧分子，重新排列成右邊的二氧化碳和兩個水分子；兩邊的原子完全相同')),
                  T('Count them: 1 C, 4 H, 4 O on each side.', '數數看：兩邊都是 1 個 C、4 個 H、4 個 O。'),
                  [T('In a reaction, atoms are <b>not created or destroyed</b>.', '化學反應中，原子<b>不會被創造，也不會消失</b>。'),
                   T('They break apart and join up in new ways, making new substances.', '它們拆開、再用新的方式組合，變成新的物質。')],
                  T('Same atoms before and after → same total mass.', '反應前後原子一樣 → 總質量也一樣。'),
                  T('Use LEGO bricks if you have them: build CH₄ and two O₂, then rebuild into CO₂ and two H₂O without adding or removing a brick.',
                    '有樂高的話可以示範：先拼出 CH₄ 和兩個 O₂，再拆開重組成 CO₂ 和兩個 H₂O，過程中一塊都不多、不少。'),
                  tint=True, section=T('Conservation of mass', '質量守恆'))

    S.wide_figure(T('BACK TO THE PUZZLE', '回到謎題'), T('The mass didn’t vanish. It escaped.', '質量沒有消失，是跑掉了'),
                  svg_open_closed(lang, T('Two scales: the open cup lets gas bubble out and drops from 250.0 to 248.6 grams; the sealed bottle traps the gas in a balloon and stays at 250.0 grams',
                                          '兩台秤：開口杯的氣體冒出去，從 250.0 克變成 248.6 克；密封瓶的氣體被氣球留住，維持 250.0 克')),
                  T('Typical readings from a classroom demo.', '課堂示範的典型讀數。'),
                  [T('<b>Open cup</b>: the reaction makes CO₂ gas, which floats away into the air.', '<b>開口杯</b>：反應產生 CO₂ 氣體，飄到空氣中了。'),
                   T('<b>Sealed bottle</b>: the balloon traps the CO₂, so nothing leaves.', '<b>密封瓶</b>：氣球把 CO₂ 留住，什麼都沒跑掉。'),
                   T('Weigh <b>everything</b>, including gases, and the total never changes.', '把<b>所有東西</b>都秤進去，包括氣體，總質量就不會變。')],
                  T('The numbers are illustrative; the drop depends on how much baking soda you use. The balloon inflating is the visible clue that gas was made.',
                    '數字僅供參考，減少多少取決於小蘇打的用量。氣球鼓起來，就是有氣體產生的證據。'))

    S.formula(T('CONSERVATION OF MASS', '質量守恆定律'),
              [(T('mass', '質量'), ACC_L, T('before', '反應前')), ('=', None, ''), (T('mass', '質量'), BLUE_L, T('after', '反應後'))],
              T('Total mass of reactants = total mass of products', '反應物總質量 = 生成物總質量'),
              T('Antoine Lavoisier showed this in the 1780s by weighing reactions inside sealed containers.', '法國化學家拉瓦節在 1780 年代，把反應放在密封容器裡秤重，證明了這件事。'),
              T('This is why chemical equations must be balanced: the equation has to show the same atoms on both sides.',
                '這就是化學反應式一定要平衡的原因：反應式兩邊必須有相同的原子。'))

    S.example(T('BALANCE IT STEP BY STEP', '一步一步平衡'), 'CH₄ + O₂ → CO₂ + H₂O', [
        (T('Count C', '數 C'), '1 = 1 ✓'),
        (T('Fix H', '平衡 H'), T('4 H left<br>→ 2H₂O', '左邊 4 個 H<br>→ 2H₂O')),
        (T('Fix O', '平衡 O'), T('4 O right<br>→ 2O₂', '右邊 4 個 O<br>→ 2O₂')),
        (T('Check', '檢查'), 'C 1=1<br>H 4=4<br>O 4=4'),
    ], 'CH₄ + <span style="color:#2463B8">2</span>O₂ → CO₂ + <span style="color:#2463B8">2</span>H₂O',
       T('Always balance by changing coefficients (the big numbers in front). Balance H and O last if they appear in more than one place.',
         '平衡時只改係數（前面的大數字）。H 和 O 如果出現在好幾個地方，就留到最後再平衡。'))

    S.compare(T('ONE TABLE', '一張表看懂'), T('Coefficient vs. subscript', '係數和下標，差在哪裡？'),
              [T('Compare', '比較'), T('Coefficient', '係數'), T('Subscript', '下標')], [
                  (T('Where it goes', '寫在哪裡'), T('In front: <b>2</b>H₂O', '前面：<b>2</b>H₂O'), T('Inside: H<b>₂</b>O', '裡面：H<b>₂</b>O')),
                  (T('What it counts', '代表什麼'), T('How many molecules', '有幾個分子'), T('Atoms in one molecule', '一個分子裡有幾個原子')),
                  (T('Change it to balance?', '平衡時可以改嗎？'), T('<span style="color:#2463B8">Yes</span>', '<span style="color:#2463B8">可以</span>'), T('<span style="color:#B4521F">Never</span>', '<span style="color:#B4521F">絕對不行</span>')),
                  (T('If you change it', '改了會怎樣'), T('More or fewer of the same thing', '同一種物質變多或變少'), T('A different substance: H₂O → H₂O₂', '變成另一種物質：H₂O → H₂O₂')),
              ],
              T('change the big number in front, never the small number inside.', '只改前面的大數字，不要動裡面的小數字。'),
              T('H₂O₂ is hydrogen peroxide, a bleach. Changing a subscript turns drinking water into a disinfectant, which makes the point memorable.',
                'H₂O₂ 是過氧化氫，也就是消毒用的雙氧水。改一個下標，喝的水就變成消毒水，學生會記得很清楚。'))

    S.table_figure(T('COUNTING WITH MOLES', '用莫耳來數'), T('A mole is a chemist’s “dozen”', '莫耳是化學家的「一打」'),
                   svg_mole(lang, T('A box of 12 eggs labeled one dozen next to a box of many tiny particles labeled one mole, 6 times 10 to the 23rd',
                                    '一盒 12 顆雞蛋標示 1 打，旁邊一盒很多小粒子標示 1 莫耳 = 6 × 10²³ 個')),
                   [T('Substance', '物質'), T('1 mole weighs', '1 莫耳重')],
                   [('CH₄', '16 g'), ('H₂O', '18 g'), ('O₂', '32 g'), ('CO₂', '44 g')], hi=-1,
                   note=T('<b>mass (g) = moles × molecular mass</b>. Atomic masses: C = 12, H = 1, O = 16.', '<b>質量（g）= 莫耳數 × 分子量</b>。原子量：C = 12、H = 1、O = 16。'),
                   aside=T('Show how each row is built: H₂O = 2 × 1 + 16 = 18. A mole is just a counting number, like a dozen, but enormous.',
                           '示範每一列怎麼算：H₂O = 2 × 1 + 16 = 18。莫耳只是一個計數單位，就像「一打」，只是大得多。'))

    S.example(T('WORKED EXAMPLE', '例題'), T('How many grams of O₂ are needed to burn 16 g of CH₄?', '要讓 16 g 的 CH₄ 完全燃燒，需要多少克 O₂？'), [
        (T('Moles of CH₄', 'CH₄ 的莫耳數'), T('16 ÷ 16<br>= 1 mol', '16 ÷ 16<br>= 1 莫耳')),
        (T('Read the ratio', '看係數比'), 'CH₄ : O₂<br>= 1 : 2'),
        (T('Moles of O₂', 'O₂ 的莫耳數'), T('1 × 2<br>= 2 mol', '1 × 2<br>= 2 莫耳')),
        (T('Grams of O₂', 'O₂ 的質量'), '2 × 32<br>= 64 g'),
    ], T('Answer: <span style="color:#2463B8">64 g</span> of O₂', '答案：需要 <span style="color:#2463B8">64 g</span> 的 O₂'),
       T('Use the balanced equation from earlier. The coefficients give the ratio of moles, never the ratio of grams.',
         '用前面平衡好的反應式。係數代表莫耳數的比，不是質量的比。'))

    S.myth(T('THE MOST COMMON MYTH', '最常見的迷思'), T('A candle gets lighter as it burns. Is mass lost?', '蠟燭越燒越輕，質量消失了嗎？'), T('No.', '沒有。'),
           T('The wax reacts with oxygen and turns into <b>CO₂ and water vapor</b>. Both are gases, so they float away and the scale can’t see them.',
             '蠟和氧氣反應，變成 <b>CO₂ 和水蒸氣</b>。兩者都是氣體，飄走了，秤就秤不到。'),
           T('Burn a candle inside a <b>sealed jar</b> on a scale and the reading stays the same. The atoms are all still there.',
             '把蠟燭放在<b>密封罐</b>裡、放在秤上燒，讀數就不會變。所有原子都還在。'),
           T('The opposite surprise: steel wool gets heavier when it burns, because it gains oxygen from the air. Both cases follow the same rule.',
             '相反的驚喜：鋼絲絨燃燒後會變重，因為它從空氣中得到了氧。兩種情況遵守的是同一條規則。'),
           section=T('Myth, quiz and summary', '破解迷思、小測驗與總結'))

    S.quiz(T('QUICK CHECK', '小測驗'), T('Answer first, then check the next slide', '先自己作答，再翻下一張對答案'), [
        T('Steel wool burns and gets heavier. Does this break conservation of mass?', '鋼絲絨燃燒後變重了。這違反質量守恆嗎？'),
        T('Balance this equation: H₂ + O₂ → H₂O', '平衡這個反應式：H₂ + O₂ → H₂O'),
        T('How many grams is 2 moles of H₂O?', '2 莫耳的 H₂O 是多少克？'),
    ], T('Let students answer on their own first. For Q2, remind them to change coefficients only.', '先讓學生自己作答。第 2 題提醒他們只能改係數。'))

    S.answers(T('Answers and the big idea', '答案與一句話總結'), [
        (T('No', '沒有'), T('It gains oxygen atoms from the air.', '它從空氣中得到了氧原子。')),
        ('2H₂ + O₂ → 2H₂O', T('H 4 = 4, O 2 = 2.', 'H 4 = 4，O 2 = 2。')),
        ('36 g', T('2 × 18 = 36', '2 × 18 = 36')),
    ], T('Atoms rearrange; they never vanish.<br><span style="color:#E58A55">Balance with coefficients, count with moles.</span>',
         '原子只會重新排列，不會消失。<br><span style="color:#E58A55">用係數平衡，用莫耳計數。</span>'),
       T('Optional exit ticket: “In one sentence, explain why the sealed bottle’s mass did not change.” Ask students to use the words atoms and conservation of mass.',
         '可選出場單：「用一句話說明，為什麼密封瓶的質量沒有改變？」請學生用到「原子」和「質量守恆」兩個詞。'))
    return S

if __name__ == '__main__':
    for lang in ('en', 'zh'):
        build(lang).write(f'chem-reactions-{lang}')
