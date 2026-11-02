"""Acids, Bases & Salts — Force & Motion layout, zh + en.  Run: python3 tools/decks/chem_acids.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from fm import *  # noqa

def build(lang):
    T = lambda en, zh: en if lang == 'en' else zh
    title = T('Acids, Bases &amp; Salts', '酸、鹼、鹽')
    S = Deck(lang, title)

    # 1 cover
    S.cover(T('CHEMISTRY', '化學'), T('Acids, Bases &amp;<br>Salts', '酸、鹼、鹽'),
            T('Why is lemon juice sour and soap slippery?<br>It comes down to two tiny particles.',
              '檸檬為什麼酸？肥皂為什麼滑？<br>答案在兩種很小的粒子。'),
            svg_cover_beakers(T('Three beakers: an orange acid, a gray neutral and a blue base, above a pH color bar',
                                '三個燒杯：橘色酸性、灰色中性、藍色鹼性，下方是一條 pH 色帶')),
            T('This lesson is for students who have never studied acids and bases. We start from tastes and colors '
              'everyone knows, then explain them with two particles, H⁺ and OH⁻, and finish with what happens when an acid meets a base.',
              '這一課給完全沒學過酸鹼的同學。我們從大家熟悉的味道和顏色出發，用 H⁺ 和 OH⁻ 兩種粒子來解釋，最後看看酸遇到鹼會發生什麼事。'))

    # 2 hook
    S.hook(T('START WITH A PUZZLE', '先想一個謎題'),
           T('Why does purple cabbage juice change color?', '紫甘藍汁為什麼會變色？'),
           ('Droplet', T('Add vinegar', '加入白醋'),
            T('The purple juice turns <b style="color:#18262B">bright pink</b>.', '紫色的汁變成<b style="color:#18262B">鮮豔的粉紅色</b>。')),
           ('Flask', T('Add soapy water', '加入肥皂水'),
            T('The same purple juice turns <b style="color:#18262B">green</b>.', '同樣的紫色汁變成<b style="color:#18262B">綠色</b>。')),
           T('Same juice, opposite colors. Vinegar and soap belong to two opposite families: <b style="color:#B4521F">acids and bases</b>.',
             '同一杯汁，變成相反的顏色。因為白醋和肥皂屬於兩個相反的家族：<b style="color:#B4521F">酸和鹼</b>。'),
           T('If you can, do it live: boil chopped purple cabbage, strain the juice, and pour it into clear cups. Add vinegar to one '
             'and soapy water or baking soda water to another. Ask students to guess before you pour. Optional extension: test soda, '
             'lemon juice and window cleaner too, and line the cups up from pink to green.',
             '可以的話現場示範：把紫甘藍切碎煮水，濾出湯汁倒進透明杯。一杯加白醋，一杯加肥皂水或小蘇打水，倒之前先讓學生猜。'
             '延伸活動：再測汽水、檸檬汁和玻璃清潔劑，把杯子從粉紅排到綠色。'))

    # 3 goals
    S.goals(T('LEARNING GOALS', '學習目標'), T('By the end of this deck, you can:', '看完這份簡報，你會：'), [
        ('Search', T('Tell acids from bases', '分辨酸和鹼'), T('Explain them with H⁺ and OH⁻.', '用 H⁺ 和 OH⁻ 來解釋。')),
        ('Chart', T('Read the pH scale', '看懂 pH 值'), T('Know that each step is 10 times stronger.', '知道每差 1 就差 10 倍。')),
        ('Flask', T('Predict neutralization', '預測中和反應'), T('Write acid + base → salt + water.', '寫出酸 + 鹼 → 鹽 + 水。')),
    ], T('The three goals match the three parts of the deck: what acids and bases are, the pH scale, and neutralization. '
         'We finish with a myth and a three-question quiz.',
         '三個目標對應簡報的三段：什麼是酸和鹼、pH 值、中和反應。最後有一個迷思和三題小測驗。'))

    # 4 basics
    S.basics(T('BEFORE YOU START', '開始之前'), T('Four words you need first', '先認識四個詞'), [
        ('o', T('Acid', '酸'), T('Tastes sour. Lemon juice, vinegar and soda are acidic.', '嚐起來酸。檸檬汁、白醋、汽水都是酸性。')),
        ('b', T('Base', '鹼'), T('Feels slippery. Soap, baking soda and bleach are basic.', '摸起來滑。肥皂、小蘇打、漂白水都是鹼性。')),
        ('o', 'pH', T('A number from <b style="color:#18262B">0 to 14</b> that says how acidic or basic something is.',
                      '從 <b style="color:#18262B">0 到 14</b> 的數字，表示東西有多酸或多鹼。')),
        ('b', T('Indicator', '指示劑'), T('A dye that changes color with pH, like purple cabbage juice.', '顏色會隨 pH 改變的染料，例如紫甘藍汁。')),
    ], T('Orange cards are the acid side; blue cards are the base side. We keep this color code for the rest of the deck. '
         'Safety: never taste or touch unknown chemicals in the lab; the tastes here are only from everyday foods.',
         '橘色卡片是酸那一邊，藍色卡片是鹼那一邊，整份簡報都用這個顏色規則。安全提醒：實驗室裡不明的化學藥品絕對不能嚐或摸，這裡說的味道都來自日常食物。'))

    # 5 H+ / OH-
    S.figure_text(T('WHAT MAKES AN ACID OR A BASE', '酸和鹼的真面目'),
                  T('Acids give off H⁺. Bases give off OH⁻.', '酸放出 H⁺，鹼放出 OH⁻'),
                  svg_ions(T('Two beakers of water: the left one is full of orange H⁺ particles from an acid, the right one is full of blue OH⁻ particles from a base',
                             '兩杯水：左邊滿是酸放出的橘色 H⁺，右邊滿是鹼放出的藍色 OH⁻')),
                  T('Left: acid in water. Right: base in water.', '左：酸溶在水中。右：鹼溶在水中。'),
                  [T('When an acid dissolves in water, it releases <b style="color:#B4521F">H⁺</b> (hydrogen ions).',
                     '酸溶在水裡，會放出 <b style="color:#B4521F">H⁺</b>（氫離子）。'),
                   T('When a base dissolves in water, it releases <b style="color:#2463B8">OH⁻</b> (hydroxide ions).',
                     '鹼溶在水裡，會放出 <b style="color:#2463B8">OH⁻</b>（氫氧根離子）。')],
                  T('More H⁺ → more acidic. More OH⁻ → more basic.', 'H⁺ 越多越酸，OH⁻ 越多越鹼。'),
                  T('The “+” and “−” mean these particles carry an electric charge; they are called ions. Students do not need '
                    'the full ion theory yet, only the rule: acids give H⁺, bases give OH⁻.',
                    '「+」和「−」代表這些粒子帶電，叫做離子。學生現在還不需要完整的離子理論，只要記住：酸放出 H⁺，鹼放出 OH⁻。'),
                  tint=True, section=T('What acids and bases are', '什麼是酸和鹼'))

    # 6 pH scale
    S.wide_figure(T('THE pH SCALE', 'pH 值'), T('From 0 to 14: acidic, neutral, basic', '0 到 14：酸性、中性、鹼性'),
                  svg_ph_scale(lang, T('A pH bar from 0 to 14, orange on the acid side, gray at 7 and blue on the base side, with everyday items marked',
                                       'pH 色帶從 0 到 14，酸性那端是橘色，7 是灰色，鹼性那端是藍色，上面標出生活中的東西')),
                  T('Below 7 is acidic, 7 is neutral, above 7 is basic. The further from 7, the stronger.',
                    '小於 7 是酸性，等於 7 是中性，大於 7 是鹼性。離 7 越遠，越強。'),
                  [T('<b style="color:#B4521F">Below 7</b>: acidic. Lemon juice is about 2.', '<b style="color:#B4521F">小於 7</b>：酸性。檸檬汁大約是 2。'),
                   T('<b>Exactly 7</b>: neutral. Pure water.', '<b>等於 7</b>：中性。純水。'),
                   T('<b style="color:#2463B8">Above 7</b>: basic. Bleach is about 13.', '<b style="color:#2463B8">大於 7</b>：鹼性。漂白水大約是 13。')],
                  T('Values are typical; real products vary. Point out that soda is acidic even though it tastes sweet: the sugar hides the sourness.',
                    '數值是大約值，實際產品會有差異。可以點出汽水是酸性的，雖然喝起來甜，那是糖蓋過了酸味。'),
                  section=T('The pH scale', 'pH 值'))

    # 7 x10 table
    S.table_figure(T('TRY THE NUMBERS', '算算看'), T('Each step on the pH scale is 10 times', 'pH 每差 1，就差 10 倍'),
                   svg_steps(T('Five bars that get taller step by step from pH 7 to pH 3; each step is labeled times ten',
                               '五根柱子從 pH 7 到 pH 3 一階一階變高，每一階標示乘以 10')),
                   [T('pH', 'pH 值'), T('H⁺ compared with water', '和純水比的 H⁺')],
                   [('7', T('1 ×', '1 倍')), ('6', T('10 ×', '10 倍')), ('5', T('100 ×', '100 倍')),
                    ('4', T('1,000 ×', '1,000 倍')), ('3', T('10,000 ×', '10,000 倍'))], hi=4,
                   note=T('Going down 1 on the pH scale multiplies the H⁺ by 10.', 'pH 往下 1，H⁺ 就乘以 10。'),
                   aside=T('Cover the right column and let students fill it in. The bars are drawn on a log scale; if they were drawn to real size, '
                           'the pH 3 bar would be 10,000 times taller than the pH 7 bar.',
                           '先遮住右欄讓學生自己填。柱子是用對數比例畫的；如果照真實比例畫，pH 3 的柱子會是 pH 7 的 10,000 倍高。'))

    # 8 neutralization formula (dark)
    S.formula(T('NEUTRALIZATION', '中和反應'),
              [('H⁺', '#E58A55', T('from the acid', '來自酸')), ('+', None, ''), ('OH⁻', '#7FB0F2', T('from the base', '來自鹼')),
               ('→', None, ''), ('H₂O', '#F3F5F2', T('water', '水'))],
              T('acid + base → salt + water', '酸 + 鹼 → 鹽 + 水'),
              T('Example: HCl + NaOH → NaCl + H₂O (hydrochloric acid + sodium hydroxide → table salt + water)',
                '例：HCl + NaOH → NaCl + H₂O（鹽酸 + 氫氧化鈉 → 食鹽 + 水）'),
              T('The H⁺ from the acid and the OH⁻ from the base join to make water, so the two cancel each other out. The leftover pieces '
                'form a salt. This is why antacid tablets (a base) settle an acidic stomach.',
                '酸的 H⁺ 和鹼的 OH⁻ 結合成水，兩者就互相抵消了，剩下的部分組成鹽。這就是胃藥（鹼性）能中和胃酸的原因。'),
              section=T('Neutralization', '中和反應'))

    # 9 electrolytes
    S.figure_text(T('ELECTROLYTES', '電解質'), T('Acids, bases and salts conduct electricity', '酸、鹼、鹽的水溶液會導電'),
                  svg_conduct(T('A battery wired to two metal rods in a beaker of salt water; charged particles move in the water and the bulb lights up',
                                '電池接上兩根插在鹽水裡的金屬棒，水中的帶電粒子在移動，燈泡亮了')),
                  T('Salt water: the bulb lights up.', '鹽水：燈泡亮了。'),
                  [T('In water, acids, bases and salts split into <b>charged particles</b> (ions).', '酸、鹼、鹽在水中會分成<b>帶電的粒子</b>（離子）。'),
                   T('Moving charges carry electricity, so the bulb lights up.', '帶電粒子移動就能傳電，所以燈泡會亮。')],
                  T('Sugar dissolves but does not split into ions, so sugar water does not conduct.', '糖會溶解，但不會分成離子，所以糖水不導電。'),
                  T('Substances that conduct in water are called electrolytes. Optional demo: a simple conductivity tester with a 9 V battery and an LED, '
                    'tried in tap water, salt water, vinegar and sugar water.',
                    '在水中會導電的物質叫做電解質。可選示範：用 9 V 電池和 LED 做簡單的導電測試器，分別測自來水、鹽水、白醋和糖水。'),
                  tint=True)

    # 10 compare
    S.compare(T('ONE TABLE', '一張表看懂'), T('Acids vs. bases', '酸和鹼，差在哪裡？'),
              [T('Compare', '比較'), T('Acid', '酸'), T('Base', '鹼')], [
                  (T('Releases in water', '在水中放出'), '<span style="color:#B4521F">H⁺</span>', '<span style="color:#2463B8">OH⁻</span>'),
                  (T('pH', 'pH 值'), T('Below 7', '小於 7'), T('Above 7', '大於 7')),
                  (T('Taste or feel', '味道或觸感'), T('Sour', '酸'), T('Bitter, slippery', '苦、滑')),
                  (T('Purple cabbage juice', '紫甘藍汁'), T('Pink to red', '粉紅到紅'), T('Blue to green', '藍到綠')),
                  (T('Everyday examples', '生活例子'), T('Lemon, vinegar, soda', '檸檬、白醋、汽水'), T('Soap, baking soda, bleach', '肥皂、小蘇打、漂白水')),
              ],
              T('acids give H⁺ and sit below 7; bases give OH⁻ and sit above 7.', '酸放出 H⁺，pH 小於 7；鹼放出 OH⁻，pH 大於 7。'),
              T('Ask students to sort five household items into acid or base using the table before you show the last row.',
                '先遮住最後一列，請學生用這張表把五樣家裡的東西分成酸或鹼。'))

    # 11 indicators
    S.wide_figure(T('READ THE COLOR', '看顏色判斷'), T('Indicators show pH as a color', '指示劑用顏色告訴你 pH'),
                  svg_cabbage(lang, T('Six cups of purple cabbage juice from pH 2 to pH 12: red, pink, purple, blue, green, yellow',
                                      '六杯紫甘藍汁從 pH 2 到 pH 12：紅、粉紅、紫、藍、綠、黃')),
                  T('Purple cabbage juice at different pH values.', '紫甘藍汁在不同 pH 下的顏色。'),
                  [T('<b>Purple cabbage juice</b>: a whole rainbow, from red (acid) to green and yellow (base).',
                     '<b>紫甘藍汁</b>：一整道彩虹，從紅色（酸）到綠色、黃色（鹼）。'),
                   T('<b>Litmus paper</b>: turns red in acid, blue in base.', '<b>石蕊試紙</b>：遇酸變紅，遇鹼變藍。'),
                   T('<b>Phenolphthalein</b>: colorless in acid, pink in base.', '<b>酚酞</b>：在酸中無色，在鹼中變粉紅。')],
                  T('Phenolphthalein is used in the quiz. Students often mix up litmus and phenolphthalein: litmus has two colors, '
                    'phenolphthalein is either clear or pink.',
                    '酚酞會出現在小測驗。學生常把石蕊和酚酞搞混：石蕊有兩種顏色，酚酞不是無色就是粉紅。'), cards=True)

    # 12 worked example
    S.example(T('WORKED EXAMPLE', '例題'),
              T('How many times more H⁺ does a pH 2 solution have than a pH 5 solution?', 'pH 2 的溶液，H⁺ 是 pH 5 溶液的幾倍？'), [
                  (T('Find the gap', '算出差距'), '5 − 2 = 3'),
                  (T('Each step ×10', '每差 1 乘 10'), T('3 steps', '差 3 步')),
                  (T('Multiply', '連乘'), '10 × 10 × 10'),
                  (T('Answer', '答案'), '= 1,000'),
              ], T('pH 2 has <span style="color:#2463B8">1,000 times</span> more H⁺', 'pH 2 的 H⁺ 是 <span style="color:#2463B8">1,000 倍</span>'),
              T('The most common wrong answer is 3 times: students subtract and stop. Remind them that every step multiplies by 10.',
                '最常見的錯誤答案是 3 倍：學生相減後就停了。提醒他們每差 1 都要乘以 10。'))

    # 13 myth
    S.myth(T('THE MOST COMMON MYTH', '最常見的迷思'), T('Does “salt” just mean table salt?', '「鹽」就是食鹽嗎？'), T('No.', '不是。'),
           T('In chemistry, a <b>salt</b> is any compound made when an acid and a base neutralize each other. Table salt (NaCl) is only one of them.',
             '在化學裡，<b>鹽</b>是酸和鹼中和後產生的化合物的總稱。食鹽（NaCl）只是其中一種。'),
           T('Baking soda, chalk (calcium carbonate) and many fertilizers are <b>salts</b> too, and most of them don’t taste salty at all.',
             '小蘇打、粉筆（碳酸鈣）和許多肥料也都是<b>鹽</b>，而且大部分吃起來一點也不鹹。'),
           T('Link back to neutralization: change the acid or the base and you get a different salt. HCl + KOH makes KCl, a salt substitute.',
             '回扣中和反應：換一種酸或鹼，就會產生不同的鹽。HCl + KOH 會產生 KCl，就是低鈉鹽的成分。'),
           section=T('Myth, quiz and summary', '破解迷思、小測驗與總結'))

    # 14 quiz
    S.quiz(T('QUICK CHECK', '小測驗'), T('Answer first, then check the next slide', '先自己作答，再翻下一張對答案'), [
        T('True or false: pH 3 is only a little more acidic than pH 4.', '是非題：pH 3 只比 pH 4 酸一點點。'),
        T('Write the products: HCl + NaOH → ?', '寫出生成物：HCl + NaOH → ？'),
        T('Phenolphthalein is added to soapy water. What color do you see, and why?', '在肥皂水裡加入酚酞，會看到什麼顏色？為什麼？'),
    ], T('Let students answer on their own first. For Q1, remind them that each step is 10 times.', '先讓學生自己作答。第 1 題提醒他們每差 1 就差 10 倍。'))

    # 15 answers
    S.answers(T('Answers and the big idea', '答案與一句話總結'), [
        (T('False', '錯'), T('pH 3 has 10 times more H⁺ than pH 4.', 'pH 3 的 H⁺ 是 pH 4 的 10 倍。')),
        ('NaCl + H₂O', T('Acid + base → salt + water.', '酸 + 鹼 → 鹽 + 水。')),
        (T('Pink', '粉紅色'), T('Soapy water is basic, and phenolphthalein turns pink in a base.', '肥皂水是鹼性，酚酞遇鹼變粉紅。')),
    ], T('Acids give H⁺, bases give OH⁻.<br><span style="color:#E58A55">Each pH step is 10×; together they make salt + water.</span>',
         '酸放出 H⁺，鹼放出 OH⁻。<br><span style="color:#E58A55">pH 每差 1 就差 10 倍；酸鹼相遇變成鹽和水。</span>'),
       T('Optional exit ticket: “How many times more H⁺ does pH 2 have than pH 4?” (Answer: 100 times.)',
         '可選出場單：「pH 2 的 H⁺ 是 pH 4 的幾倍？」（答案：100 倍。）'))
    return S

if __name__ == '__main__':
    for lang in ('en', 'zh'):
        build(lang).write(f'chem-acids-{lang}')
