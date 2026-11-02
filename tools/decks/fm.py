"""Force & Motion slide system: shared layouts so every lesson looks and reads the same.
Each deck script builds a Deck and calls .write('<deck-id>') -> content/<deck-id>/."""
import json, pathlib

CONTENT = pathlib.Path(__file__).resolve().parents[2] / 'content'
INK, BG, TINT, CARD, LINE, MUTED = '#18262B', '#F3F5F2', '#E7EEEA', '#FBFCFA', '#D3DCD8', '#4F5F64'
ACC, ACC_L, ACC_T, BLUE, BLUE_L, BLUE_T = '#B4521F', '#E58A55', '#F7E6DC', '#2463B8', '#7FB0F2', '#E1ECFA'
ON_DARK, DARK_CARD, MYTH, MYTH_INK = '#BFCDC9', '#22343A', '#A84B1B', '#FBF3EE'
MONO = "'JetBrains Mono', 'Courier New', monospace"
FACES = {
    'en': {"nunito-sans": {"family": "Nunito Sans", "href": "https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;700;800;900&display=swap"}},
    'zh': {"noto-sans-tc": {"family": "Noto Sans TC", "href": "https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700;900&display=swap"}},
}
for f in FACES.values():
    f["jetbrains-mono"] = {"family": "JetBrains Mono", "href": "https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500;700&display=swap"}


class Deck:
    def __init__(self, lang, title):
        self.lang, self.title, self.slides = lang, title, []
        self.font = "'Nunito Sans', Arial, sans-serif" if lang == 'en' else "'Noto Sans TC', Arial, sans-serif"
        self.W = 800 if lang == 'en' else 700
        self.LH = 1.1 if lang == 'en' else 1.15

    # ---------- building blocks ----------
    def _id(self, base):
        ids = [i for i, _ in self.slides]
        n, sid = 2, base
        while sid in ids:
            sid, n = f'{base}{n}', n + 1
        return sid

    def _add(self, base, bg, ink, body, aside, section=None, extra='gap:48px', footer_ink=MUTED, footer=True):
        sid = self._id(base)
        ds = f' data-section="{section}"' if section else ''
        foot = (f'<p style="position:absolute;left:128px;bottom:64px;width:900px;font-size:24px;color:{footer_ink}">'
                f'{self.title} · {len(self.slides) + 1}</p>\n') if footer else ''
        self.slides.append((sid, f'<section id="{sid}"{ds} data-transition="fade" style="background:{bg};color:{ink};'
                                 f'font-family:{self.font};padding:128px 128px 160px;display:flex;flex-direction:column;{extra}">\n'
                                 f'{body}\n{foot}<aside>{aside}</aside>\n</section>\n'))

    def _head(self, kicker, h2, size=72, kcolor=ACC):
        return (f'<div style="display:flex;flex-direction:column;gap:16px">\n'
                f'<p style="font-size:24px;font-weight:{self.W};letter-spacing:3px;color:{kcolor}">{kicker}</p>\n'
                f'<h2 style="font-size:{size}px;font-weight:900;line-height:{self.LH}">{h2}</h2>\n</div>')

    def _qlabel(self, i):
        return f'Q{i}' if self.lang == 'en' else f'第 {i} 題'

    # ---------- layouts (mirroring Force & Motion) ----------
    def cover(self, kicker, h1, sub, svg, aside):
        sid = self._id('cover')
        self.slides.append((sid, f'''<section id="{sid}" data-transition="fade" style="background:{INK};color:{BG};font-family:{self.font};padding:128px;display:grid;grid-template-columns:1fr 720px;gap:64px;align-items:center">
<div style="display:flex;flex-direction:column;gap:32px">
<p style="font-size:32px;font-weight:{self.W};letter-spacing:4px;color:{ACC_L}">{kicker}</p>
<h1 style="font-size:120px;font-weight:900;line-height:1.05;color:{BG}">{h1}</h1>
<p style="font-size:36px;line-height:1.45;color:{ON_DARK}">{sub}</p>
</div>
{svg}
<aside>{aside}</aside>
</section>
'''))

    def hook(self, kicker, h2, a, b, closing, aside):
        def card(icon, h3, p, bg, c):
            return (f'<div style="flex:1;display:flex;flex-direction:column;gap:24px;background:{bg};padding:56px;border-radius:24px">\n'
                    f'<x-icon name="{icon}" style="color:{c};width:72px;height:72px"></x-icon>\n'
                    f'<h3 style="font-size:44px;font-weight:{self.W}">{h3}</h3>\n'
                    f'<p style="font-size:32px;line-height:1.5;color:{MUTED}">{p}</p>\n</div>')
        body = (f'{self._head(kicker, h2)}\n<div style="display:flex;gap:40px;flex:1">\n{card(*a, ACC_T, ACC)}\n{card(*b, BLUE_T, BLUE)}\n</div>\n'
                f'<p style="font-size:32px;line-height:1.5">{closing}</p>')
        self._add('hook', BG, INK, body, aside, extra='gap:56px')

    def goals(self, kicker, h2, items, aside):
        cards = '\n'.join(
            f'<div style="display:flex;flex-direction:column;gap:24px;background:{CARD};padding:48px;border:2px solid {LINE};border-radius:24px">\n'
            f'<x-icon name="{ic}" style="color:{ACC};width:64px;height:64px"></x-icon>\n'
            f'<h3 style="font-size:44px;font-weight:{self.W};line-height:1.2">{h3}</h3>\n'
            f'<p style="font-size:32px;line-height:1.5;color:{MUTED}">{p}</p>\n</div>' for ic, h3, p in items)
        self._add('goals', BG, INK, f'{self._head(kicker, h2)}\n<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:40px;flex:1">\n{cards}\n</div>', aside, extra='gap:56px')

    def basics(self, kicker, h2, items, aside, section=None):
        cards = '\n'.join(
            f'<div style="display:flex;flex-direction:column;gap:12px;background:{CARD};padding:40px;border-radius:24px;border-left:12px solid {ACC if k == "o" else BLUE}">\n'
            f'<h3 style="font-size:40px;font-weight:{self.W}">{h3}</h3>\n'
            f'<p style="font-size:30px;line-height:1.5;color:{MUTED}">{p}</p>\n</div>' for k, h3, p in items)
        self._add('basics', TINT, INK, f'{self._head(kicker, h2)}\n<div style="display:grid;grid-template-columns:1fr 1fr;gap:32px;flex:1">\n{cards}\n</div>', aside, section=section)

    def figure_text(self, kicker, h2, svg, caption, paras, callout, aside, tint=False, section=None):
        ps = '\n'.join(f'<p style="font-size:34px;line-height:1.5">{p}</p>' for p in paras)
        body = (f'{self._head(kicker, h2)}\n<div style="display:grid;grid-template-columns:640px 1fr;gap:64px;align-items:center;flex:1">\n'
                f'<div style="display:flex;flex-direction:column;gap:16px;align-items:center">\n{svg}\n'
                f'<p style="font-size:24px;color:{MUTED}">{caption}</p>\n</div>\n'
                f'<div style="display:flex;flex-direction:column;gap:28px">\n{ps}\n'
                f'<p style="font-size:34px;font-weight:{self.W};line-height:1.4;background:{CARD};padding:24px 32px;border-radius:16px">{callout}</p>\n</div>\n</div>')
        self._add('concept', TINT if tint else BG, INK, body, aside, section=section)

    def wide_figure(self, kicker, h2, svg, caption, items, aside, section=None, cards=True):
        cs = '\n'.join(f'<p style="font-size:30px;line-height:1.5;background:{CARD};padding:28px 32px;border:2px solid {LINE};border-radius:20px">{p}</p>' for p in items)
        body = (f'{self._head(kicker, h2)}\n<div style="display:flex;flex-direction:column;gap:12px;align-items:center">\n{svg}\n'
                f'<p style="font-size:24px;color:{MUTED}">{caption}</p>\n</div>\n'
                f'<div style="display:grid;grid-template-columns:repeat({len(items)},1fr);gap:32px">\n{cs}\n</div>')
        self._add('figure', BG, INK, body, aside, section=section, extra='gap:40px')

    def table_figure(self, kicker, h2, svg, header, rows, hi, note, aside):
        trs = '\n'.join(f'<tr{f" style=\"background:{ACC_T}\"" if i == hi else ""}><td>{a}</td><td><b>{b}</b></td></tr>' for i, (a, b) in enumerate(rows))
        body = (f'{self._head(kicker, h2)}\n<div style="display:grid;grid-template-columns:720px 1fr;gap:64px;align-items:center;flex:1">\n{svg}\n'
                f'<table style="font-size:32px;color:{INK}">\n<tr><th style="width:40%;text-align:left">{header[0]}</th><th style="width:60%;text-align:left">{header[1]}</th></tr>\n{trs}\n</table>\n</div>\n'
                f'<p style="font-size:32px;line-height:1.5">{note}</p>')
        self._add('numbers', BG, INK, body, aside)

    def formula(self, kicker, parts, line1, line2, aside, section=None):
        items = []
        for sym, color, label in parts:
            if color is None:
                items.append(f'<p style="font-family:{MONO};font-size:140px;line-height:1.1;color:{ON_DARK}">{sym}</p>')
            else:
                items.append(f'<div style="display:flex;flex-direction:column;align-items:center;gap:8px">\n'
                             f'<p style="font-family:{MONO};font-size:160px;font-weight:700;line-height:1;color:{color}">{sym}</p>\n'
                             f'<p style="font-size:32px;color:{ON_DARK}">{label}</p>\n</div>')
        body = (f'<p style="font-size:32px;font-weight:{self.W};letter-spacing:4px;color:{ACC_L}">{kicker}</p>\n'
                f'<div style="display:flex;align-items:flex-end;gap:48px">\n' + '\n'.join(items) + '\n</div>\n'
                f'<p style="font-size:48px;font-weight:{self.W};line-height:1.4">{line1}</p>\n'
                f'<p style="font-size:28px;line-height:1.5;color:{ON_DARK}">{line2}</p>')
        self._add('formula', INK, BG, body, aside, section=section, extra='gap:48px;justify-content:center', footer_ink=ON_DARK)

    def compare(self, kicker, h2, header, rows, bottom, aside):
        th = (f'<tr><th style="width:34%;text-align:left">{header[0]}</th><th style="width:33%;text-align:left">{header[1]}</th>'
              f'<th style="width:33%;text-align:left">{header[2]}</th></tr>')
        trs = '\n'.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for a, b, c in rows)
        body = (f'{self._head(kicker, h2)}\n<table style="font-size:30px;color:{INK}">\n{th}\n{trs}\n</table>\n<div style="flex:1"></div>\n'
                f'<p style="font-size:32px;line-height:1.5"><b style="color:{ACC}">{"Remember:" if self.lang == "en" else "一句話記住："}</b> {bottom}</p>')
        self._add('compare', BG, INK, body, aside)

    def example(self, kicker, h2, steps, result, aside):
        cards = '\n'.join(
            f'<div style="display:flex;flex-direction:column;gap:20px;background:{CARD};padding:40px;border:2px solid {LINE};border-radius:24px">\n'
            f'<p style="font-family:{MONO};font-size:44px;font-weight:700;color:{ACC}">{i}</p>\n'
            f'<h3 style="font-size:36px;font-weight:{self.W}">{h3}</h3>\n'
            f'<p style="font-family:{MONO};font-size:32px;line-height:1.6">{p}</p>\n</div>' for i, (h3, p) in enumerate(steps, 1))
        body = (f'{self._head(kicker, h2, size=64)}\n<div style="display:grid;grid-template-columns:repeat({len(steps)},1fr);gap:32px;flex:1">\n{cards}\n</div>\n'
                f'<p style="font-size:44px;font-weight:{self.W};background:{BLUE_T};padding:28px 40px;border-radius:20px">{result}</p>')
        self._add('example', BG, INK, body, aside)

    def myth(self, kicker, h2, big, p1, p2, aside, section=None):
        body = (f'{self._head(kicker, h2, kcolor=MYTH_INK)}\n<p style="font-size:160px;font-weight:900;line-height:1.05">{big}</p>\n'
                f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:48px">\n'
                f'<p style="font-size:34px;line-height:1.5">{p1}</p>\n<p style="font-size:34px;line-height:1.5">{p2}</p>\n</div>')
        self._add('myth', MYTH, MYTH_INK, body, aside, section=section, footer_ink=MYTH_INK)

    def quiz(self, kicker, h2, qs, aside):
        cards = '\n'.join(
            f'<div style="display:flex;flex-direction:column;gap:24px;background:{CARD};padding:48px;border:2px solid {LINE};border-radius:24px">\n'
            f'<p style="font-family:{MONO};font-size:44px;font-weight:700;color:{ACC}">{self._qlabel(i)}</p>\n'
            f'<p style="font-size:34px;line-height:1.5">{q}</p>\n</div>' for i, q in enumerate(qs, 1))
        self._add('quiz', BG, INK, f'{self._head(kicker, h2)}\n<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:40px;flex:1">\n{cards}\n</div>', aside)

    def answers(self, h2, items, big, aside):
        cards = '\n'.join(
            f'<div style="display:flex;flex-direction:column;gap:16px;background:{DARK_CARD};padding:40px;border-radius:24px">\n'
            f'<p style="font-family:{MONO};font-size:32px;font-weight:700;color:{ACC_L}">{self._qlabel(i)}</p>\n'
            f'<p style="font-size:44px;font-weight:{self.W}">{a}</p>\n'
            f'<p style="font-size:28px;line-height:1.5;color:{ON_DARK}">{e}</p>\n</div>' for i, (a, e) in enumerate(items, 1))
        body = (f'<h2 style="font-size:72px;font-weight:900;line-height:{self.LH}">{h2}</h2>\n'
                f'<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:40px">\n{cards}\n</div>\n<div style="flex:1"></div>\n'
                f'<p style="font-size:52px;font-weight:900;line-height:1.35">{big}</p>')
        self._add('answers', INK, BG, body, aside, extra='gap:56px', footer_ink=ON_DARK)

    def write(self, deck_id):
        d = CONTENT / deck_id
        (d / 'slides').mkdir(parents=True, exist_ok=True)
        for old in (d / 'slides').glob('*.html'):
            old.unlink()
        for sid, html in self.slides:
            (d / 'slides' / f'{sid}.html').write_text(html)
        plain = self.title.replace('&amp;', '&')
        (d / 'deck.json').write_text(json.dumps({"v": 4, "lists": "css", "title": plain, "order": [s for s, _ in self.slides],
                                                 "faces": FACES[self.lang], "designSystems": []}, ensure_ascii=False))
        print(f'{deck_id}: {len(self.slides)} slides')


# ---------- shared illustrations ----------
def _beaker(ox, top, w, h, fill, level, stroke=BG, sw=8):
    r = 36
    out = (f'<path d="M{ox} {top} V{top + h - r} Q{ox} {top + h} {ox + r} {top + h} H{ox + w - r} Q{ox + w} {top + h} {ox + w} {top + h - r} V{top}" '
           f'fill="none" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round"/>')
    if fill:
        y = top + h - level
        out = (f'<path d="M{ox + 8} {y} H{ox + w - 8} V{top + h - r} Q{ox + w - 8} {top + h - 8} {ox + w - r} {top + h - 8} H{ox + r} '
               f'Q{ox + 8} {top + h - 8} {ox + 8} {top + h - r} Z" fill="{fill}"/>\n') + out
    return out


def svg_cover_beakers(label):
    beakers = '\n'.join(_beaker(ox, 90, 180, 300, c, 170) for ox, c in [(30, ACC_L), (270, '#9AAAA6'), (510, BLUE_L)])
    bubbles = ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{BG}" opacity="0.55"/>' for x, y, r in
                      [(90, 300, 10), (140, 270, 7), (110, 340, 6), (580, 290, 9), (630, 330, 7), (600, 260, 6)])
    return f'''<svg aria-label="{label}" width="720" height="480" viewBox="0 0 720 480">
<defs><linearGradient id="phbar" x1="0" x2="1"><stop offset="0" stop-color="{ACC}"/><stop offset=".35" stop-color="{ACC_L}"/><stop offset=".5" stop-color="#9AAAA6"/><stop offset=".65" stop-color="{BLUE_L}"/><stop offset="1" stop-color="{BLUE}"/></linearGradient></defs>
{beakers}
{bubbles}
<rect x="30" y="430" width="660" height="26" rx="13" fill="url(#phbar)"/>
</svg>'''


def svg_ions(label):
    def ion(x, y, t, c, w=78):
        return (f'<rect x="{x - w / 2}" y="{y - 24}" width="{w}" height="48" rx="24" fill="{c}"/>'
                f'<text x="{x}" y="{y + 10}" text-anchor="middle" font-size="28" font-weight="800" fill="#FFFFFF">{t}</text>')
    h = ''.join(ion(x, y, 'H⁺', ACC) for x, y in [(110, 200), (210, 230), (130, 290), (230, 310), (170, 340)])
    oh = ''.join(ion(x, y, 'OH⁻', BLUE, 96) for x, y in [(440, 200), (550, 240), (460, 290), (560, 320), (500, 350)])
    return f'''<svg aria-label="{label}" width="640" height="380" viewBox="0 0 640 380">
{_beaker(40, 120, 260, 250, BLUE_T, 210, stroke=INK, sw=6)}
{_beaker(360, 120, 260, 250, BLUE_T, 210, stroke=INK, sw=6)}
{h}
{oh}
<text x="170" y="80" text-anchor="middle" font-size="40" font-weight="900" fill="{ACC}">H⁺</text>
<text x="490" y="80" text-anchor="middle" font-size="40" font-weight="900" fill="{BLUE}">OH⁻</text>
</svg>'''


def svg_ph_scale(lang, label):
    x = lambda p: 40 + p * 1520 / 14
    items = ([(2, 'Lemon juice'), (3, 'Vinegar'), (7, 'Pure water'), (9, 'Baking soda'), (10, 'Soapy water'), (13, 'Bleach')] if lang == 'en'
             else [(2, '檸檬汁'), (3, '白醋'), (7, '純水'), (9, '小蘇打水'), (10, '肥皂水'), (13, '漂白水')])
    marks = ''
    for k, (p, t) in enumerate(items):
        y = 30 if k % 2 == 0 else 62
        marks += (f'<line x1="{x(p)}" y1="{y + 8}" x2="{x(p)}" y2="96" stroke="{INK}" stroke-width="3"/>'
                  f'<text x="{x(p)}" y="{y}" text-anchor="middle" font-size="28" font-weight="800" fill="{INK}">{t}</text>')
    ticks = ''.join(f'<text x="{x(p)}" y="190" text-anchor="middle" font-size="28" font-weight="700" fill="{MUTED}">{p}</text>' for p in range(15))
    return f'''<svg aria-label="{label}" width="1600" height="210" viewBox="0 0 1600 210">
<defs><linearGradient id="phscale" x1="0" x2="1"><stop offset="0" stop-color="{ACC}"/><stop offset=".35" stop-color="{ACC_L}"/><stop offset=".5" stop-color="{LINE}"/><stop offset=".65" stop-color="{BLUE_L}"/><stop offset="1" stop-color="{BLUE}"/></linearGradient></defs>
<rect x="40" y="100" width="1520" height="50" rx="25" fill="url(#phscale)"/>
{marks}
{ticks}
</svg>'''


def svg_steps(label):
    cols = ['#D3DCD8', ACC_T, ACC_L, '#C8693A', ACC]
    out = ''
    for i, (ph, c) in enumerate(zip([7, 6, 5, 4, 3], cols)):
        x, h = 60 + i * 130, 60 * (i + 1)
        out += (f'<rect x="{x}" y="{340 - h}" width="96" height="{h}" rx="10" fill="{c}"/>'
                f'<text x="{x + 48}" y="384" text-anchor="middle" font-size="30" font-weight="800" fill="{INK}">{ph}</text>')
        if i:
            out += f'<text x="{x - 17}" y="{320 - h}" text-anchor="middle" font-size="24" font-weight="800" fill="{ACC}">×10</text>'
    return f'''<svg aria-label="{label}" width="720" height="400" viewBox="0 0 720 400">
<line x1="40" y1="340" x2="700" y2="340" stroke="{MUTED}" stroke-width="4"/>
{out}
</svg>'''


def svg_conduct(label):
    ions = ''
    for k, (x, y) in enumerate([(260, 240), (330, 300), (380, 225), (300, 330), (420, 280), (360, 260)]):
        c, t = (ACC, '+') if k % 2 == 0 else (BLUE, '−')
        ions += f'<circle cx="{x}" cy="{y}" r="18" fill="{c}"/><text x="{x}" y="{y + 9}" text-anchor="middle" font-size="28" font-weight="900" fill="#FFFFFF">{t}</text>'
    return f'''<svg aria-label="{label}" width="640" height="380" viewBox="0 0 640 380">
<path d="M220 140 V50 H292 M308 50 H370 M426 50 H470 V140" fill="none" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>
<line x1="292" y1="24" x2="292" y2="76" stroke="{INK}" stroke-width="8"/>
<line x1="308" y1="34" x2="308" y2="66" stroke="{INK}" stroke-width="8"/>
<circle cx="398" cy="50" r="28" fill="#FFC94D" stroke="{INK}" stroke-width="5"/>
<g stroke="#E0A21A" stroke-width="6" stroke-linecap="round"><line x1="398" y1="14" x2="398" y2="2"/><line x1="432" y1="24" x2="444" y2="14"/><line x1="364" y1="24" x2="352" y2="14"/></g>
{_beaker(160, 160, 360, 200, BLUE_T, 150, stroke=INK, sw=6)}
<rect x="212" y="120" width="16" height="200" rx="6" fill="{MUTED}"/>
<rect x="462" y="120" width="16" height="200" rx="6" fill="{MUTED}"/>
{ions}
</svg>'''


def svg_cabbage(lang, label):
    cols = ['#C62828', '#E0457B', '#8E44AD', '#3F51B5', '#2E9E5B', '#E0B020']
    out = ''
    for i, (ph, c) in enumerate(zip([2, 4, 6, 8, 10, 12], cols)):
        x = 60 + i * 245
        out += (f'<path d="M{x + 18} 70 L{x + 34} 180 H{x + 136} L{x + 152} 70 Z" fill="{c}"/>'
                f'<path d="M{x} 20 L{x + 30} 184 H{x + 140} L{x + 170} 20" fill="none" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>'
                f'<text x="{x + 85}" y="228" text-anchor="middle" font-size="28" font-weight="800" fill="{INK}">pH {ph}</text>')
    return f'<svg aria-label="{label}" width="1500" height="240" viewBox="0 0 1500 240">\n{out}\n</svg>'
