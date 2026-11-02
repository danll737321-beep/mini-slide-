"""Oxidation & Reduction — Force & Motion layout, zh + en."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from fm import *  # noqa

RUST, IRON, COPPER = '#A0522D', '#8C989C', '#C8693A'

def svg_nail(label):
    inner = (f'<g transform="rotate(-28 360 240)">'
             f'<rect x="110" y="215" width="470" height="50" rx="8" fill="{IRON}"/>'
             f'<rect x="80" y="190" width="40" height="100" rx="8" fill="{IRON}"/>'
             f'<polygon points="580,215 680,240 580,265" fill="{IRON}"/>'
             + ''.join(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{c}"/>' for x, y, rx, ry, c in
                       [(220, 232, 40, 18, RUST), (330, 250, 54, 16, ACC_L), (450, 228, 34, 14, RUST), (520, 252, 30, 12, ACC_L)])
             + '</g>'
             + ''.join(dot(x, y, 26, ACC_L, 'O') for x, y in [(560, 90), (630, 150), (150, 380)])
             + ''.join(arrow(x1, y1, x2, y2, ON_DARK, 5, 16) for x1, y1, x2, y2 in [(540, 110, 470, 170), (605, 165, 520, 205), (175, 360, 240, 320)]))
    return svg(label, 720, 480, inner)

def svg_swap(lang, label):
    T = lambda en, zh: en if lang == 'en' else zh
    inner = (dot(80, 190, 40, COPPER, 'Cu') + dot(150, 190, 30, ACC, 'O') + text(115, 120, 'CuO', 30, INK, 800)
             + text(260, 202, '+', 48, MUTED, 700) + dot(350, 190, 38, '#2F3B40', 'C') + text(350, 120, 'C', 30, INK, 800)
             + arrow(150, 240, 330, 250, ACC, 5, 16)
             + f'<path d="M150 230 Q240 330 340 236" fill="none" stroke="{ACC}" stroke-width="5" stroke-dasharray="10 8"/>'
             + arrow(410, 190, 470, 190, MUTED, 7, 22)
             + dot(530, 120, 36, COPPER, 'Cu') + text(530, 70, 'Cu', 30, INK, 800)
             + dot(530, 270, 34, '#2F3B40', 'C') + dot(588, 270, 26, ACC, 'O')
             + text(560, 340, 'CO₂', 30, INK, 800)
             + text(115, 300, T('loses O', '失去 O'), 26, BLUE, 800) + text(350, 300, T('gains O', '得到 O'), 26, ACC, 800))
    return svg(label, 640, 380, inner)

def svg_series(lang, label):
    els = ['K', 'Na', 'Ca', 'Mg', 'Al', 'C', 'Zn', 'Fe', 'Sn', 'Pb', 'H', 'Cu', 'Hg', 'Ag', 'Pt', 'Au']
    hi = {'C', 'Fe', 'H', 'Cu'}
    T = lambda en, zh: en if lang == 'en' else zh
    inner = ''
    for i, e in enumerate(els):
        x = 40 + i * 96
        fill = ACC if e in hi else (ACC_T if i < 8 else BLUE_T)
        ink = '#FFFFFF' if e in hi else INK
        inner += box(x, 60, 84, 84, e, fill, ink, fill if e in hi else LINE, 34, 14, 900)
    inner += arrow(60, 190, 1540, 190, MUTED, 6, 22)
    inner += text(60, 236, T('more reactive', '活性大'), 28, ACC, 800, 'start') + text(1540, 236, T('less reactive', '活性小'), 28, BLUE, 800, 'end')
    return svg(label, 1600, 250, inner)

def svg_nail_cuso4(lang, label):
    T = lambda en, zh: en if lang == 'en' else zh
    def tube(x, liquid, coated, title):
        return (f'<path d="M{x} 40 V300 Q{x} 340 {x + 50} 340 Q{x + 100} 340 {x + 100} 300 V40" fill="none" stroke="{INK}" stroke-width="5"/>'
                f'<path d="M{x + 5} 140 H{x + 95} V298 Q{x + 95} 334 {x + 50} 334 Q{x + 5} 334 {x + 5} 298 Z" fill="{liquid}"/>'
                f'<rect x="{x + 40}" y="20" width="20" height="270" rx="6" fill="{IRON}"/>'
                + (f'<rect x="{x + 38}" y="140" width="24" height="150" rx="6" fill="{COPPER}"/>' if coated else '')
                + text(x + 50, 380, title, 26, INK, 800))
    return svg(label, 720, 400, tube(140, '#5B8DEF', False, T('Start', '開始')) + arrow(290, 200, 400, 200, MUTED, 6, 20)
               + tube(450, '#A9C4F5', True, T('After 2 min', '2 分鐘後')))

def svg_rust(lang, label):
    T = lambda en, zh: en if lang == 'en' else zh
    def tube(x, water, oil, rusty, title):
        s = f'<path d="M{x} 50 V280 Q{x} 320 {x + 45} 320 Q{x + 90} 320 {x + 90} 280 V50" fill="none" stroke="{INK}" stroke-width="5"/>'
        if water:
            s += f'<path d="M{x + 5} 200 H{x + 85} V278 Q{x + 85} 314 {x + 45} 314 Q{x + 5} 314 {x + 5} 278 Z" fill="{BLUE_T}"/>'
        if oil:
            s += f'<rect x="{x + 5}" y="186" width="80" height="16" fill="#E0B020"/>'
        s += f'<rect x="{x + 36}" y="70" width="18" height="230" rx="5" fill="{IRON}"/>'
        if rusty:
            s += ''.join(f'<ellipse cx="{x + 45}" cy="{y}" rx="12" ry="8" fill="{RUST}"/>' for y in (170, 205, 240))
        return s + text(x + 45, 350, title, 22, INK, 800)
    return svg(label, 640, 380, tube(40, True, False, True, T('Air + water', '空氣 + 水'))
               + tube(270, False, False, False, T('Dry air', '乾燥空氣')) + tube(500, True, True, False, T('No air', '隔絕空氣')))


def build(lang):
    T = lambda en, zh: en if lang == 'en' else zh
    S = Deck(lang, T('Oxidation &amp; Reduction', '氧化與還原'))

    S.cover(T('CHEMISTRY', '化學'), T('Oxidation &amp;<br>Reduction', '氧化<br>與還原'),
            T('Why does iron rust, and how do we get iron from rock?<br>Follow the oxygen.', '鐵為什麼會生鏽？鐵又是怎麼從石頭裡來的？<br>跟著氧走就知道。'),
            svg_nail(T('A rusty iron nail with oxygen atoms arrowing toward it', '一根生鏽的鐵釘，旁邊的氧原子正朝它靠近')),
            T('This lesson is for students who have never studied oxidation and reduction. At this level we define both by gaining or '
              'losing oxygen; electron transfer comes later in high school.',
              '這一課給完全沒學過氧化還原的同學。在這個階段，我們只用「得到或失去氧」來定義，電子轉移到高中再學。'))

    S.hook(T('START WITH A PUZZLE', '先想一個謎題'), T('Why does a nail turn red in a blue liquid?', '鐵釘放進藍色溶液，為什麼會變紅？'),
           ('Flask', T('Nail in copper sulfate', '鐵釘泡硫酸銅'),
            T('After a few minutes the nail is coated in <b style="color:#18262B">red copper</b> and the blue fades.', '幾分鐘後，鐵釘表面附著<b style="color:#18262B">紅色的銅</b>，藍色也變淡了。')),
           ('Warning', T('Bike left in the rain', '腳踏車淋雨'),
            T('The chain slowly turns <b style="color:#18262B">orange-brown</b> and flaky.', '鏈條慢慢變成<b style="color:#18262B">橘褐色</b>，還會剝落。')),
           T('Both changes are the same kind of reaction: something <b style="color:#B4521F">gains or loses oxygen</b>.', '這兩種變化是同一類反應：有東西<b style="color:#B4521F">得到或失去了氧</b>。'),
           T('Demo: sand an iron nail clean and drop it into copper(II) sulfate solution, or show a short video. Let students write a prediction first.',
             '示範：把鐵釘用砂紙磨乾淨，放進硫酸銅溶液，或播一段短片。先請學生寫下預測。'))

    S.goals(T('LEARNING GOALS', '學習目標'), T('By the end of this deck, you can:', '看完這份簡報，你會：'), [
        ('Search', T('Spot oxidation', '判斷氧化還原'), T('Tell who gains and who loses oxygen.', '分辨誰得到氧、誰失去氧。')),
        ('Link', T('Name the agents', '找出氧化劑和還原劑'), T('Find who gives and who takes oxygen.', '找出誰給氧、誰搶氧。')),
        ('Chart', T('Use the series', '會用活性大小'), T('Predict whether a metal reacts.', '預測金屬會不會反應。')),
    ], T('The goals match the three parts: gain and loss of oxygen, the reactivity series, and real-world uses such as smelting and rust prevention.',
         '三個目標對應三段：得氧與失氧、活性大小、生活應用（煉鐵和防鏽）。'))

    S.basics(T('BEFORE YOU START', '開始之前'), T('Four words you need first', '先認識四個詞'), [
        ('o', T('Oxidation', '氧化'), T('A substance <b style="color:#18262B">gains oxygen</b>. Iron rusting is oxidation.', '物質<b style="color:#18262B">得到氧</b>。鐵生鏽就是氧化。')),
        ('b', T('Reduction', '還原'), T('A substance <b style="color:#18262B">loses oxygen</b>. Getting iron from ore is reduction.', '物質<b style="color:#18262B">失去氧</b>。從鐵礦取出鐵就是還原。')),
        ('o', T('Oxidizing agent', '氧化劑'), T('Gives its oxygen away (and is reduced).', '把自己的氧給出去（自己被還原）。')),
        ('b', T('Reducing agent', '還原劑'), T('Takes oxygen from something else (and is oxidized).', '把別人的氧搶過來（自己被氧化）。')),
    ], T('Orange cards are the oxygen-gaining side; blue cards are the oxygen-losing side. The agent names are backward on purpose: '
         'the reducing agent is the one that gets oxidized.',
         '橘色卡片是得到氧的一方，藍色卡片是失去氧的一方。名稱看起來是反的：還原劑自己是被氧化的那個。'))

    S.figure_text(T('ALWAYS A PAIR', '一定成對'), T('One loses oxygen, another gains it', '一個失去氧，另一個就得到氧'),
                  svg_swap(lang, T('Copper oxide gives its oxygen atom to carbon; copper is left alone and carbon becomes carbon dioxide',
                                   '氧化銅把氧原子交給碳；銅被留下來，碳變成二氧化碳')),
                  '2CuO + C → 2Cu + CO₂',
                  [T('CuO <b style="color:#2463B8">loses</b> oxygen → it is <b>reduced</b> to copper.', 'CuO <b style="color:#2463B8">失去</b>氧 → 被<b>還原</b>成銅。'),
                   T('C <b style="color:#B4521F">gains</b> oxygen → it is <b>oxidized</b> to CO₂.', 'C <b style="color:#B4521F">得到</b>氧 → 被<b>氧化</b>成 CO₂。')],
                  T('Oxidation and reduction always happen at the same time.', '氧化和還原一定同時發生。'),
                  T('Trace the oxygen atom with your finger: it starts on copper and ends on carbon. Whatever the oxygen leaves is reduced; whatever it joins is oxidized.',
                    '用手指追著氧原子走：它從銅身上出發，最後到了碳身上。氧離開的那個被還原，氧加入的那個被氧化。'),
                  tint=True, section=T('Gaining and losing oxygen', '得氧與失氧'))

    S.wide_figure(T('REACTIVITY SERIES', '活性大小'), T('Some elements grab oxygen harder than others', '有些元素搶氧的力氣比較大'),
                  svg_series(lang, T('Sixteen elements in a row from most reactive potassium to least reactive gold, with carbon, iron, hydrogen and copper highlighted',
                                     '十六種元素排成一列，從活性最大的鉀到活性最小的金，碳、鐵、氫、銅特別標示')),
                  T('K &gt; Na &gt; Ca &gt; Mg &gt; Al &gt; C &gt; Zn &gt; Fe &gt; Sn &gt; Pb &gt; H &gt; Cu &gt; Hg &gt; Ag &gt; Pt &gt; Au',
                    'K &gt; Na &gt; Ca &gt; Mg &gt; Al &gt; C &gt; Zn &gt; Fe &gt; Sn &gt; Pb &gt; H &gt; Cu &gt; Hg &gt; Ag &gt; Pt &gt; Au'),
                  [T('A <b>more reactive</b> element can take oxygen away from a less reactive one.', '<b>活性大</b>的元素可以把活性小的元素的氧搶走。'),
                   T('<b>Carbon sits above iron</b>, so carbon can pull oxygen out of iron ore.', '<b>碳排在鐵前面</b>，所以碳能把鐵礦裡的氧拉出來。'),
                   T('<b>Gold and platinum</b> hardly react, which is why they are found as pure metal.', '<b>金和白金</b>幾乎不反應，所以在自然界以純金屬的樣子出現。')],
                  T('Students don’t need to memorize the whole list; they should be able to use it. Highlighted: C, Fe, H and Cu, the four used most in this lesson.',
                    '學生不必背整串，只要會使用。特別標示的 C、Fe、H、Cu 是這一課最常用到的四個。'),
                  section=T('The reactivity series', '活性大小'))

    S.table_figure(T('WILL IT REACT?', '會不會反應？'), T('A more reactive metal pushes a weaker one out', '活性大的金屬會把活性小的擠出來'),
                   svg_nail_cuso4(lang, T('An iron nail in blue copper sulfate solution; two minutes later the nail is coated in copper and the solution is paler',
                                          '鐵釘放進藍色硫酸銅溶液；兩分鐘後鐵釘表面附著銅，溶液顏色變淡')),
                   [T('Metal + solution', '金屬 + 溶液'), T('Reacts?', '會反應嗎？')],
                   [('Fe + CuSO₄', T('Yes: Fe &gt; Cu', '會：Fe &gt; Cu')), ('Zn + CuSO₄', T('Yes: Zn &gt; Cu', '會：Zn &gt; Cu')),
                    ('Cu + FeSO₄', T('No: Cu &lt; Fe', '不會：Cu &lt; Fe')), ('Cu + AgNO₃', T('Yes: Cu &gt; Ag', '會：Cu &gt; Ag'))], hi=2,
                   note=T('Check the series: the metal going in must be <b>more reactive</b> than the metal in the solution.', '查活性大小：放進去的金屬必須比溶液裡的金屬<b>活性大</b>。'),
                   aside=T('This is the opening puzzle explained: iron is more reactive than copper, so iron takes copper’s place and red copper metal forms on the nail. '
                           'The highlighted row is the case that does not react.',
                           '這就是開場謎題的答案：鐵的活性比銅大，所以鐵取代了銅，紅色的銅就附著在鐵釘上。標示的那一列是不會反應的情況。'))

    S.formula(T('SMELTING IRON', '煉鐵'),
              [('Fe₂O₃', ACC_L, T('iron ore', '鐵礦')), ('+', None, ''), ('C', BLUE_L, T('carbon', '碳')), ('→', None, ''), ('Fe', BG, T('iron', '鐵'))],
              T('Carbon takes the oxygen; iron is left behind.', '碳把氧搶走，鐵就留下來了。'),
              T('In a blast furnace: Fe₂O₃ + 3CO → 2Fe + 3CO₂. Iron ore is reduced; carbon (as CO) is oxidized.',
                '在高爐中：Fe₂O₃ + 3CO → 2Fe + 3CO₂。鐵礦被還原，碳（以 CO 的形式）被氧化。'),
              T('The big formula is the idea, not a balanced equation; the balanced version is underneath. Smelting works only because carbon is above iron in the series.',
                '大字公式表達的是概念，不是平衡的反應式；平衡的版本寫在下面。煉鐵之所以可行，就是因為碳的活性比鐵大。'))

    S.figure_text(T('RUSTING', '生鏽'), T('Iron needs both air and water to rust', '鐵要同時碰到空氣和水才會生鏽'),
                  svg_rust(lang, T('Three test tubes with nails: the one with air and water rusts; the ones with only dry air or with water under an oil layer do not',
                                   '三支試管裡各有一根鐵釘：有空氣又有水的那支生鏽了；只有乾燥空氣、或水面蓋了一層油的都沒有生鏽')),
                  T('Only the left nail rusts.', '只有最左邊的鐵釘生鏽。'),
                  [T('Rusting is <b>slow oxidation</b>: iron + oxygen + water → rust (iron oxide).', '生鏽是<b>緩慢的氧化</b>：鐵 + 氧 + 水 → 鐵鏽（氧化鐵）。'),
                   T('Take away air or water and rusting stops.', '拿掉空氣或水，生鏽就停止。')],
                  T('Paint, oil and zinc coatings keep oxygen and water away.', '油漆、上油、鍍鋅，都是把氧和水隔開。'),
                  T('Optional activity: set up the three tubes at the start of the week and check them a few days later. The oil layer stops air from dissolving into the boiled water.',
                    '可選活動：週一架好三支試管，幾天後再觀察。煮過的水上面加一層油，可以防止空氣再溶進水裡。'),
                  tint=True)

    S.compare(T('ONE TABLE', '一張表看懂'), T('Oxidizing agent vs. reducing agent', '氧化劑和還原劑，差在哪裡？'),
              [T('Compare', '比較'), T('Oxidizing agent', '氧化劑'), T('Reducing agent', '還原劑')], [
                  (T('Oxygen', '氧'), T('<span style="color:#2463B8">Gives it away</span>', '<span style="color:#2463B8">給出去</span>'), T('<span style="color:#B4521F">Takes it</span>', '<span style="color:#B4521F">搶過來</span>')),
                  (T('It becomes', '自己變成'), T('Reduced', '被還原'), T('Oxidized', '被氧化')),
                  ('2CuO + C', 'CuO', 'C'),
                  (T('Smelting iron', '煉鐵'), T('Iron ore (Fe₂O₃)', '鐵礦（Fe₂O₃）'), T('Carbon (CO)', '碳（CO）')),
              ],
              T('the reducing agent takes oxygen and gets oxidized; the oxidizing agent gives oxygen and gets reduced.', '還原劑搶氧，自己被氧化；氧化劑給氧，自己被還原。'),
              T('Ask students to fill in the last two rows before revealing them.', '最後兩列先遮住，讓學生自己填。'))

    S.example(T('WORKED EXAMPLE', '例題'), T('2Mg + O₂ → 2MgO: who is oxidized, and what is the oxidizing agent?', '2Mg + O₂ → 2MgO：誰被氧化？誰是氧化劑？'), [
        (T('Follow the O', '追著氧走'), 'O₂ → MgO'),
        (T('Who gains O?', '誰得到氧？'), T('Mg', 'Mg')),
        (T('So Mg is', '所以 Mg'), T('oxidized', '被氧化')),
        (T('O₂ gives O', 'O₂ 給出氧'), T('oxidizing<br>agent', '是氧化劑')),
    ], T('Mg is <span style="color:#2463B8">oxidized</span>; O₂ is the <span style="color:#2463B8">oxidizing agent</span>', 'Mg <span style="color:#2463B8">被氧化</span>；O₂ 是<span style="color:#2463B8">氧化劑</span>'),
       T('Burning magnesium ribbon gives a bright white flash; if you show it, remind students not to look straight at it.',
         '燃燒鎂帶會發出很亮的白光；如果示範，提醒學生不要直視。'))

    S.myth(T('THE MOST COMMON MYTH', '最常見的迷思'), T('Is rusting just a color change?', '生鏽只是顏色改變嗎？'), T('No.', '不是。'),
           T('Rust (iron oxide) is a <b>new substance</b>: flaky, weak and orange-brown. That makes rusting a chemical change, and an oxidation.',
             '鐵鏽（氧化鐵）是<b>新的物質</b>：易碎、脆弱、橘褐色。所以生鏽是化學變化，也是一種氧化。'),
           T('A rusty nail actually gets <b>heavier</b>, because it has gained oxygen atoms from the air.', '生鏽的鐵釘其實會變<b>重</b>，因為它從空氣中得到了氧原子。'),
           T('Contrast with a physical change such as bending a nail or melting ice: no new substance forms.', '可以對比物理變化，例如把鐵釘折彎或冰融化：沒有產生新物質。'),
           section=T('Myth, quiz and summary', '破解迷思、小測驗與總結'))

    S.quiz(T('QUICK CHECK', '小測驗'), T('Answer first, then check the next slide', '先自己作答，再翻下一張對答案'), [
        T('True or false: oxidation can happen without reduction.', '是非題：氧化可以單獨發生，不需要還原。'),
        T('Will a copper strip react with iron(II) sulfate solution? Why?', '銅片放進硫酸亞鐵溶液會反應嗎？為什麼？'),
        T('In 2CuO + C → 2Cu + CO₂, which substance is the reducing agent?', '在 2CuO + C → 2Cu + CO₂ 中，哪一個是還原劑？'),
    ], T('Let students answer on their own first. For Q2, point them to the reactivity series.', '先讓學生自己作答。第 2 題提醒他們查活性大小。'))

    S.answers(T('Answers and the big idea', '答案與一句話總結'), [
        (T('False', '錯'), T('They always happen together.', '兩者一定同時發生。')),
        (T('No', '不會'), T('Copper is less reactive than iron.', '銅的活性比鐵小。')),
        ('C', T('It takes oxygen from CuO.', '它把 CuO 的氧搶走。')),
    ], T('Gain oxygen = oxidation; lose oxygen = reduction.<br><span style="color:#E58A55">The more reactive element wins the oxygen.</span>',
         '得到氧是氧化，失去氧是還原。<br><span style="color:#E58A55">活性大的元素會把氧搶走。</span>'),
       T('Optional exit ticket: “Use the reactivity series to explain why red copper appeared on the nail.”', '可選出場單：「用活性大小解釋，為什麼鐵釘上出現了紅色的銅？」'))
    return S

if __name__ == '__main__':
    for lang in ('en', 'zh'):
        build(lang).write(f'chem-redox-{lang}')
