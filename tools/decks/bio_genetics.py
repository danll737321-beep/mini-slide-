"""Genetics: Dominant & Recessive — Force & Motion layout, zh + en."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from fm import *  # noqa

PURPLE, WHITE_F = '#8E5BC2', '#F3F5F2'

def flower(cx, cy, r, color, stroke=INK):
    petals = ''.join(f'<circle cx="{cx + r * dx:.0f}" cy="{cy + r * dy:.0f}" r="{r * 0.62:.0f}" fill="{color}" stroke="{stroke}" stroke-width="3"/>'
                     for dx, dy in [(0, -0.75), (0.72, -0.23), (0.45, 0.62), (-0.45, 0.62), (-0.72, -0.23)])
    return petals + f'<circle cx="{cx}" cy="{cy}" r="{r * 0.35:.0f}" fill="#E0B020"/>'

def svg_cover(label):
    inner = (flower(170, 150, 70, PURPLE, '#22343A') + flower(400, 150, 70, PURPLE, '#22343A')
             + f'<text x="285" y="170" text-anchor="middle" font-size="56" font-weight="900" fill="{ON_DARK}">×</text>'
             + arrow(285, 250, 285, 320, ON_DARK, 6, 20)
             + flower(120, 400, 48, PURPLE, '#22343A') + flower(240, 400, 48, PURPLE, '#22343A')
             + flower(360, 400, 48, PURPLE, '#22343A') + flower(480, 400, 48, WHITE_F, '#22343A')
             + f'<rect x="560" y="60" width="140" height="140" rx="12" fill="none" stroke="{ACC_L}" stroke-width="5"/>'
             + f'<line x1="630" y1="60" x2="630" y2="200" stroke="{ACC_L}" stroke-width="4"/><line x1="560" y1="130" x2="700" y2="130" stroke="{ACC_L}" stroke-width="4"/>')
    return svg(label, 720, 480, inner)

def svg_gametes(lang, label):
    T = lambda en, zh: en if lang == 'en' else zh
    def parent(x, name):
        return (box(x, 40, 200, 80, 'Aa', CARD, INK, LINE, 40, 18, 900) + text(x + 100, 30, name, 24, MUTED, 800)
                + arrow(x + 70, 124, x + 40, 200, MUTED, 5, 16) + arrow(x + 130, 124, x + 160, 200, MUTED, 5, 16)
                + dot(x + 40, 230, 30, ACC, 'A', '#FFFFFF', 30) + dot(x + 160, 230, 30, BLUE, 'a', '#FFFFFF', 30))
    inner = (parent(20, T('Mother', '母本')) + parent(420, T('Father', '父本'))
             + arrow(220, 290, 290, 330, ACC, 5, 16) + arrow(420, 290, 350, 330, ACC, 5, 16)
             + box(250, 320, 140, 56, T('A or a', 'A 或 a'), ACC_T, INK, ACC, 28, 14, 800))
    return svg(label, 640, 380, inner)

def svg_punnett(label):
    cells = [('AA', PURPLE), ('Aa', PURPLE), ('Aa', PURPLE), ('aa', WHITE_F)]
    inner = (box(150, 10, 220, 60, 'A', ACC_T, INK, ACC_T, 34, 12, 900) + box(380, 10, 220, 60, 'a', BLUE_T, INK, BLUE_T, 34, 12, 900)
             + box(20, 80, 120, 140, 'A', ACC_T, INK, ACC_T, 34, 12, 900) + box(20, 230, 120, 140, 'a', BLUE_T, INK, BLUE_T, 34, 12, 900))
    for i, (g, c) in enumerate(cells):
        x, y = 150 + (i % 2) * 230, 80 + (i // 2) * 150
        inner += f'<rect x="{x}" y="{y}" width="220" height="140" rx="14" fill="{CARD}" stroke="{ACC if g == "aa" else LINE}" stroke-width="{5 if g == "aa" else 3}"/>'
        inner += flower(x + 60, y + 70, 30, c) + text(x + 155, y + 84, g, 40, INK, 900)
    return svg(label, 640, 380, inner)

def svg_coins(lang, label):
    T = lambda en, zh: en if lang == 'en' else zh
    data = [('AA', 104, 100), ('Aa', 196, 200), ('aa', 100, 100)]
    inner = f'<line x1="60" y1="330" x2="700" y2="330" stroke="{MUTED}" stroke-width="4"/>'
    for i, (g, got, exp) in enumerate(data):
        x = 100 + i * 210
        inner += f'<rect x="{x}" y="{330 - got}" width="70" height="{got}" rx="8" fill="{ACC}"/>'
        inner += f'<rect x="{x + 80}" y="{330 - exp}" width="70" height="{exp}" rx="8" fill="{LINE}"/>'
        inner += text(x + 75, 372, g, 30, INK, 900)
    inner += (f'<rect x="440" y="20" width="24" height="24" rx="4" fill="{ACC}"/>' + text(474, 40, T('class result', '全班結果'), 22, INK, 700, 'start')
              + f'<rect x="440" y="56" width="24" height="24" rx="4" fill="{LINE}"/>' + text(474, 76, T('expected', '預期'), 22, INK, 700, 'start'))
    return svg(label, 720, 400, inner)

def svg_hidden(lang, label):
    T = lambda en, zh: en if lang == 'en' else zh
    inner = (flower(140, 140, 70, PURPLE) + flower(480, 140, 70, PURPLE)
             + box(70, 250, 140, 64, 'AA', CARD, INK, LINE, 36, 14, 900) + box(410, 250, 140, 64, 'Aa', CARD, INK, ACC, 36, 14, 900)
             + text(140, 350, T('two purple genes', '兩個紫色基因'), 24, MUTED) + text(480, 350, T('white gene hiding', '藏著白色基因'), 24, ACC, 800)
             + text(310, 160, '=', 64, MUTED, 900))
    return svg(label, 640, 380, inner)


def build(lang):
    T = lambda en, zh: en if lang == 'en' else zh
    S = Deck(lang, T('Genetics: Dominant &amp; Recessive', '遺傳：顯性與隱性'))

    S.cover(T('BIOLOGY', '生物'), T('Dominant &amp;<br>Recessive', '顯性<br>與隱性'),
            T('Why do children sometimes show a trait<br>neither parent has?', '為什麼孩子有時會出現<br>爸媽都沒有的特徵？'),
            svg_cover(T('Two purple pea flowers cross to make four offspring: three purple and one white, next to a two-by-two grid',
                        '兩朵紫色豌豆花雜交，生出四個後代：三朵紫色、一朵白色，旁邊是一個 2×2 方格')),
            T('This lesson is for students who have never studied genetics. We follow Mendel’s pea plants: one hidden gene, a simple grid, and the ratios that come out of it.',
              '這一課給完全沒學過遺傳的同學。我們跟著孟德爾的豌豆走：一個藏起來的基因、一個簡單的方格，以及從中算出來的比例。'))

    S.hook(T('START WITH A PUZZLE', '先想一個謎題'), T('Can two purple flowers have a white baby?', '兩朵紫花，能生出白花嗎？'),
           ('Leaf', T('The parents', '親代'), T('Both pea plants have <b style="color:#18262B">purple</b> flowers.', '兩株豌豆都開<b style="color:#18262B">紫色</b>的花。')),
           ('Search', T('The offspring', '後代'), T('About <b style="color:#18262B">1 in 4</b> seedlings grows white flowers.', '大約<b style="color:#18262B">每 4 株就有 1 株</b>開白花。')),
           T('The white color was <b style="color:#B4521F">hiding inside the purple parents</b>. Let’s find out how.', '白色其實<b style="color:#B4521F">一直藏在紫花親代裡</b>。來看看是怎麼回事。'),
           T('Take a vote before revealing the answer. Avoid examples like eyelid folds or tongue rolling; they are controlled by several genes, not a simple dominant–recessive pair.',
             '揭曉前先投票。避免用單雙眼皮或捲舌當例子，它們由多個基因控制，不是單純的顯隱性。'))

    S.goals(T('LEARNING GOALS', '學習目標'), T('By the end of this deck, you can:', '看完這份簡報，你會：'), [
        ('Link', T('Read A and a', '看懂 A 和 a'), T('Tell dominant from recessive.', '分辨顯性和隱性。')),
        ('Search', T('Fill a Punnett square', '畫棋盤方格'), T('Combine one letter from each parent.', '把親代各一個字母組合起來。')),
        ('Chart', T('Find the ratios', '算出比例'), T('Get 1 : 2 : 1 and 3 : 1.', '算出 1 : 2 : 1 和 3 : 1。')),
    ], T('The goals match the three parts: what the letters mean, how to fill the square, and what the ratios tell us.',
         '三個目標對應三段：字母代表什麼、方格怎麼填、比例告訴我們什麼。'))

    S.basics(T('BEFORE YOU START', '開始之前'), T('Four words you need first', '先認識四個詞'), [
        ('o', T('Gene', '基因'), T('An instruction for one trait, like flower color. You get <b style="color:#18262B">two copies</b>, one from each parent.', '控制一個性狀（例如花色）的指令。每個生物有<b style="color:#18262B">兩份</b>，爸媽各給一份。')),
        ('b', T('Dominant (A)', '顯性（A）'), T('Shows up if you have <b style="color:#18262B">at least one</b> copy. Written as a capital letter.', '只要有<b style="color:#18262B">一份</b>就會表現出來。用大寫字母表示。')),
        ('o', T('Recessive (a)', '隱性（a）'), T('Shows up only with <b style="color:#18262B">two copies</b> (aa). Written in lowercase.', '要有<b style="color:#18262B">兩份</b>（aa）才會表現出來。用小寫字母表示。')),
        ('b', T('Genotype / phenotype', '基因型／表現型'), T('The letters (Aa) / the trait you can see (purple).', '字母組合（Aa）／看得到的性狀（紫色）。')),
    ], T('Stress the notation: a capital letter is dominant, the same letter in lowercase is recessive. Genotype is what you write; phenotype is what you see.',
         '強調寫法：大寫是顯性，同一個字母的小寫是隱性。基因型是寫出來的，表現型是看得到的。'))

    S.figure_text(T('PASSING ON GENES', '基因怎麼傳下去'), T('Each parent passes on one letter', '親代各傳一個字母給後代'),
                  svg_gametes(lang, T('A mother and a father, both Aa, each split into an A or an a; the offspring gets one letter from each',
                                      '母本和父本都是 Aa，各自分成 A 或 a；後代從雙方各拿到一個字母')),
                  T('Each parent is Aa. Each passes on A or a, 50/50.', '親代都是 Aa，各自有一半機會傳 A、一半機會傳 a。'),
                  [T('A parent has two letters but passes on <b>only one</b>.', '親代有兩個字母，但只會傳<b>一個</b>下去。'),
                   T('Which one is pure chance, like flipping a coin.', '傳哪一個完全靠機率，就像擲硬幣。')],
                  T('Offspring = one letter from mom + one from dad.', '後代 = 媽媽的一個字母 + 爸爸的一個字母。'),
                  T('The cells that carry one letter are called gametes (egg and sperm, or pollen and ovule in plants). The word is optional at this level.',
                    '只帶一個字母的細胞叫做配子（卵和精子，植物則是胚珠和花粉）。這個名詞在這個階段可以不教。'),
                  tint=True, section=T('How genes are passed on', '基因怎麼傳下去'))

    S.figure_text(T('THE PUNNETT SQUARE', '棋盤方格'), T('A 2 × 2 grid shows every possible offspring', '一個 2 × 2 方格列出所有可能的後代'),
                  svg_punnett(T('A Punnett square for Aa times Aa: AA purple, Aa purple, Aa purple, aa white', 'Aa × Aa 的棋盤方格：AA 紫、Aa 紫、Aa 紫、aa 白')),
                  'Aa × Aa',
                  [T('Mother’s letters across the top, father’s down the side.', '母本的字母寫在上方，父本的寫在左側。'),
                   T('Fill each box with one letter from the top and one from the side.', '每一格填入上方一個字母和左側一個字母。')],
                  T('Only <b>aa</b> shows the white, recessive trait.', '只有 <b>aa</b> 會表現白色的隱性性狀。'),
                  T('Back to the hook: yes, two purple Aa parents can have a white aa offspring, with a 1 in 4 chance each time.',
                    '回到開場：是的，兩株 Aa 紫花親代可以生出 aa 白花，每次的機率是 4 分之 1。'))

    S.formula(T('THE RATIOS', '比例'),
              [('AA', ACC_L, '1'), (':', None, ''), ('Aa', BLUE_L, '2'), (':', None, ''), ('aa', BG, '1')],
              T('Purple : white = 3 : 1', '紫花 : 白花 = 3 : 1'),
              T('Genotype ratio 1 : 2 : 1. Phenotype ratio 3 : 1, because AA and Aa both look purple. Chance of white = 1 in 4 = 25%.',
                '基因型比例 1 : 2 : 1。表現型比例 3 : 1，因為 AA 和 Aa 看起來都是紫色。開白花的機率 = 4 分之 1 = 25%。'),
              T('Mendel counted 705 purple and 224 white plants: about 3 to 1.', '孟德爾數了 705 株紫花和 224 株白花：大約 3 比 1。'))

    S.table_figure(T('TRY IT WITH COINS', '用硬幣試試看'), T('Flip two coins to model two parents', '擲兩枚硬幣，模擬兩個親代'),
                   svg_coins(lang, T('Bar chart of a class’s 400 coin flips: AA 104, Aa 196, aa 100, each close to the expected 100, 200, 100',
                                     '全班擲 400 次的長條圖：AA 104、Aa 196、aa 100，都接近預期的 100、200、100')),
                   [T('Pair', '組合'), T('Class result (400 flips)', '全班結果（400 次）')],
                   [('AA', T('104 (expected 100)', '104（預期 100）')), ('Aa', T('196 (expected 200)', '196（預期 200）')), ('aa', T('100 (expected 100)', '100（預期 100）'))], hi=-1,
                   note=T('Heads = A, tails = a. A few flips can be lopsided; many flips get close to 1 : 2 : 1.', '正面 = A，反面 = a。擲幾次可能差很多，擲很多次就會接近 1 : 2 : 1。'),
                   aside=T('Optional activity: pairs flip two labeled coins 20 times and tally AA, Aa and aa, then add up the class total on the board. '
                           'Remind them that A + a and a + A both count as Aa. The numbers here are a sample class result.',
                           '可選活動：兩人一組，擲兩枚貼了標籤的硬幣 20 次，記錄 AA、Aa、aa 的次數，再把全班結果加總寫在黑板上。提醒學生 A + a 和 a + A 都算 Aa。這裡的數字是一個示範班級的結果。'))

    S.figure_text(T('HIDDEN GENES', '藏起來的基因'), T('Same look, different letters', '看起來一樣，字母卻不同'),
                  svg_hidden(lang, T('Two purple flowers that look identical; one is AA and the other is Aa, carrying a hidden white gene',
                                     '兩朵看起來一模一樣的紫花；一朵是 AA，另一朵是 Aa，藏著白色基因')),
                  T('You can’t tell them apart by looking.', '光用看的分不出來。'),
                  [T('AA and Aa are both purple: same <b>phenotype</b>, different <b>genotype</b>.', 'AA 和 Aa 都是紫色：<b>表現型</b>相同，<b>基因型</b>不同。'),
                   T('An Aa plant is a <b>carrier</b>: it hides the white gene and can pass it on.', 'Aa 植物是<b>帶因者</b>：它藏著白色基因，還能傳給後代。')],
                  T('To find out, cross it with a white (aa) plant and see if any white flowers appear.', '想知道的話，讓它和白花（aa）雜交，看看會不會出現白花。'),
                  T('This is called a test cross. If the purple parent is AA, all offspring are purple; if it is Aa, about half are white.',
                    '這叫做試交。紫花親代如果是 AA，後代全是紫花；如果是 Aa，大約一半會是白花。'), tint=True)

    S.compare(T('ONE TABLE', '一張表看懂'), T('Genotype vs. phenotype', '基因型和表現型，差在哪裡？'),
              [T('Compare', '比較'), T('Genotype', '基因型'), T('Phenotype', '表現型')], [
                  (T('What it is', '是什麼'), T('The pair of letters', '一對字母'), T('The trait you can see', '看得到的性狀')),
                  (T('Example', '例子'), 'AA, Aa, aa', T('Purple, white', '紫色、白色')),
                  (T('Can you see it?', '看得到嗎？'), T('<span style="color:#B4521F">No</span>', '<span style="color:#B4521F">看不到</span>'), T('<span style="color:#2463B8">Yes</span>', '<span style="color:#2463B8">看得到</span>')),
                  (T('Ratio for Aa × Aa', 'Aa × Aa 的比例'), '1 : 2 : 1', '3 : 1'),
              ],
              T('genotype is what you write; phenotype is what you see.', '基因型是寫出來的，表現型是看得到的。'),
              T('Ask students why the two ratios have a different number of parts: AA and Aa merge into one phenotype.',
                '問學生為什麼兩個比例的項數不同：因為 AA 和 Aa 合併成同一種表現型。'))

    S.example(T('WORKED EXAMPLE', '例題'), T('Father Aa × mother aa: what is the chance of a white (aa) offspring?', '父本 Aa × 母本 aa：後代開白花（aa）的機率是多少？'), [
        (T('Letters', '寫出字母'), T('A, a<br>a, a', 'A、a<br>a、a')),
        (T('Fill square', '填方格'), 'Aa Aa<br>aa aa'),
        (T('Count aa', '數 aa'), T('2 of 4', '4 格中 2 格')),
        (T('Chance', '機率'), '2/4 = 1/2'),
    ], T('Chance of white = <span style="color:#2463B8">1/2 (50%)</span>', '開白花的機率 = <span style="color:#2463B8">1/2（50%）</span>'),
       T('Students who answer 1/4 probably reused the Aa × Aa result. Insist they draw the square first.', '答 1/4 的學生可能直接套用了 Aa × Aa 的結果。堅持要他們先畫方格。'))

    S.myth(T('THE MOST COMMON MYTH', '最常見的迷思'), T('After 3 purple plants, must the 4th be white?', '已經生了 3 株紫花，第 4 株一定是白花嗎？'), T('No.', '不一定。'),
           T('Every offspring is a <b>new chance</b>. Each one has its own 1 in 4 chance of being white, no matter what came before.',
             '每個後代都是<b>新的機會</b>。不管前面生了什麼，每一株開白花的機率都是 4 分之 1。'),
           T('It’s like flipping a coin: three heads in a row doesn’t make the fourth flip more likely to be tails.', '就像擲硬幣：連續三次正面，第四次出現反面的機率也不會變大。'),
           T('A 3 : 1 ratio is what you approach over many offspring, not a guarantee for every group of four.', '3 : 1 是後代很多時才會接近的比例，不是每四個就一定照這個比例。'),
           section=T('Myth, quiz and summary', '破解迷思、小測驗與總結'))

    S.quiz(T('QUICK CHECK', '小測驗'), T('Answer first, then check the next slide', '先自己作答，再翻下一張對答案'), [
        T('A purple AA plant is crossed with a white aa plant. What color are the offspring?', '紫花 AA 和白花 aa 雜交，後代是什麼顏色？'),
        T('Two Aa plants are crossed. What is the chance of an aa offspring?', '兩株 Aa 雜交，生出 aa 後代的機率是多少？'),
        T('True or false: two white (aa) plants can have a purple offspring.', '是非題：兩株白花（aa）可以生出紫花後代。'),
    ], T('Let students answer on their own first, and let them draw a square for each.', '先讓學生自己作答，每題都可以畫方格。'))

    S.answers(T('Answers and the big idea', '答案與一句話總結'), [
        (T('All purple', '全是紫色'), T('Every offspring is Aa.', '每個後代都是 Aa。')),
        ('1/4 (25%)', T('One box out of four is aa.', '四格中有一格是 aa。')),
        (T('False', '錯'), T('aa × aa can only give aa.', 'aa × aa 只會生出 aa。')),
    ], T('One letter from each parent.<br><span style="color:#E58A55">Aa × Aa gives 1 : 2 : 1, or 3 purple : 1 white.</span>',
         '親代各給一個字母。<br><span style="color:#E58A55">Aa × Aa 得到 1 : 2 : 1，也就是 3 紫 : 1 白。</span>'),
       T('Optional exit ticket: “Why didn’t 20 coin flips give exactly 1 : 2 : 1, while the class total came closer?” (Probability only gets close with many trials.)',
         '可選出場單：「為什麼擲 20 次沒有剛好得到 1 : 2 : 1，全班合計卻比較接近？」（機率要在試驗次數很多時才會接近預期。）'))
    return S

if __name__ == '__main__':
    for lang in ('en', 'zh'):
        build(lang).write(f'bio-genetics-{lang}')
