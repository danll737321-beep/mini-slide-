(() => {
  const CATALOG = window.CATALOG, DECKS = window.DECKS;
  const app = document.getElementById('app');
  const W = 1920, H = 1080;

  const T = {
    zh: {
      title: 'Mini Lessons 迷你課', sub: '國中理化與生物 · 每課 15 分鐘', all: '全部',
      slides: n => `${n} 張投影片`, lessons: n => `${n} 課`, lesson: n => `第 ${n} 課`,
      both: '中文 · English', enOnly: '僅英文版', back: '返回', notes: '講者備註', full: '全螢幕',
      noNotes: '這張沒有備註。', prev: '上一張', next: '下一張',
      help: '鍵盤：<kbd>←</kbd> <kbd>→</kbd> 翻頁 · <kbd>F</kbd> 全螢幕 · <kbd>N</kbd> 備註 · <kbd>Esc</kbd> 返回',
    },
    en: {
      title: 'Mini Lessons', sub: 'Middle school science · 15 minutes each', all: 'All',
      slides: n => `${n} slides`, lessons: n => `${n} lessons`, lesson: n => `Lesson ${n}`,
      both: '中文 · English', enOnly: 'English only', back: 'Back', notes: 'Speaker notes', full: 'Fullscreen',
      noNotes: 'No notes for this slide.', prev: 'Previous', next: 'Next',
      help: 'Keys: <kbd>←</kbd> <kbd>→</kbd> navigate · <kbd>F</kbd> fullscreen · <kbd>N</kbd> notes · <kbd>Esc</kbd> back',
    },
  };

  const store = {
    get(k, d) { try { return localStorage.getItem(k) ?? d; } catch { return d; } },
    set(k, v) { try { localStorage.setItem(k, v); } catch {} },
  };
  const state = {
    lang: store.get('ml.lang', (navigator.language || '').toLowerCase().startsWith('en') ? 'en' : 'zh'),
    filter: store.get('ml.filter', 'all'),
    notes: store.get('ml.notes', '0') === '1',
  };
  const t = () => T[state.lang];
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

  const lessons = {};
  CATALOG.categories.forEach(cat => cat.lessons.forEach((l, i) => { lessons[l.id] = { ...l, cat, index: i + 1 }; }));
  const deckFor = l => DECKS[l.versions[state.lang] || l.versions.en || Object.values(l.versions)[0]];

  const icons = {
    back: '<path d="M15 18l-6-6 6-6"/>',
    notes: '<path d="M4 4h16v12H8l-4 4z"/><path d="M8 9h8M8 12h5"/>',
    full: '<path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5"/>',
    prev: '<path d="M15 18l-6-6 6-6"/>',
    next: '<path d="M9 18l6-6-6-6"/>',
  };
  const svg = n => `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${icons[n]}</svg>`;
  const langToggle = (disabledZh = false) => `
    <div class="lang" role="group" aria-label="Language">
      <button data-lang="zh" aria-pressed="${state.lang === 'zh'}">中文</button>
      <button data-lang="en" aria-pressed="${state.lang === 'en'}">EN</button>
    </div>`;

  function fit(root, box) {
    const r = box.getBoundingClientRect();
    const s = Math.min(r.width / W, r.height / H);
    root.style.transform = `scale(${s})`;
    root.style.left = `${(r.width - W * s) / 2}px`;
    root.style.top = `${(r.height - H * s) / 2}px`;
  }

  /* ---------------- Home ---------------- */
  function renderHome() {
    document.title = t().title;
    document.documentElement.lang = state.lang === 'zh' ? 'zh-Hant' : 'en';
    const cats = CATALOG.categories;
    const tabs = [{ id: 'all', name: { zh: T.zh.all, en: T.en.all } }, ...cats];
    const total = cats.reduce((n, c) => n + c.lessons.length, 0);
    app.innerHTML = `
      <main class="home">
        <header class="topbar">
          <div class="brand"><h1>${esc(t().title)}</h1><p>${esc(t().sub)} · ${t().lessons(total)}</p></div>
          ${langToggle()}
        </header>
        <nav class="tabs" aria-label="Categories">
          ${tabs.map(c => `<button data-filter="${c.id}" aria-pressed="${state.filter === c.id}" style="--c:var(--${c.id})">
            ${c.id === 'all' ? '' : '<span class="dot"></span>'}${esc(c.name[state.lang])}</button>`).join('')}
        </nav>
        ${cats.filter(c => state.filter === 'all' || state.filter === c.id).map(c => `
          <section class="cat" style="--c:var(--${c.id})">
            <h2>${esc(c.name[state.lang])} <small>${esc(c.name[state.lang === 'zh' ? 'en' : 'zh'])} · ${t().lessons(c.lessons.length)}</small></h2>
            <div class="grid">
              ${c.lessons.map((l, i) => {
                const d = deckFor(l); const L = lessons[l.id];
                const hasZh = !!l.versions.zh;
                return `<a class="card" href="#/${l.id}/1" style="--c:var(--${c.id})">
                  <div class="thumb"><div class="slide-root">${d.slides[0].html}</div></div>
                  <div class="card-body">
                    <span class="card-kicker">${esc(c.name[state.lang])} · ${t().lesson(i + 1)}</span>
                    <h3 class="card-title">${esc(l.name[state.lang])}</h3>
                    <p class="card-sub">${esc(l.name[state.lang === 'zh' ? 'en' : 'zh'])}</p>
                    <div class="badges">
                      <span class="badge">${t().slides(d.slides.length)}</span>
                      <span class="badge ${hasZh ? 'on' : ''}">${hasZh ? t().both : t().enOnly}</span>
                    </div>
                  </div></a>`;
              }).join('')}
            </div>
          </section>`).join('')}
        <p class="foot">${t().help}</p>
      </main>`;
    const thumbs = [...app.querySelectorAll('.thumb')];
    const sizeThumbs = () => thumbs.forEach(b => {
      const s = b.clientWidth / W; const r = b.firstElementChild; r.style.transform = `scale(${s})`;
    });
    sizeThumbs();
    new ResizeObserver(sizeThumbs).observe(app.querySelector('.home'));
    app.querySelectorAll('[data-filter]').forEach(b => b.onclick = () => {
      state.filter = b.dataset.filter; store.set('ml.filter', state.filter); renderHome();
    });
    bindLang(renderHome);
  }

  function bindLang(rerender) {
    app.querySelectorAll('[data-lang]').forEach(b => b.onclick = () => {
      if (state.lang === b.dataset.lang) return;
      state.lang = b.dataset.lang; store.set('ml.lang', state.lang); rerender();
    });
  }

  /* ---------------- Viewer ---------------- */
  let cleanup = null;
  function renderViewer(id, n) {
    const l = lessons[id];
    if (!l) { location.hash = ''; return; }
    const deck = deckFor(l);
    const total = deck.slides.length;
    let i = Math.min(Math.max(1, n || 1), total) - 1;
    document.documentElement.lang = deck.lang === 'zh' ? 'zh-Hant' : 'en';

    app.innerHTML = `
      <div class="viewer" tabindex="-1">
        <div class="vbar">
          <button class="ibtn" data-act="back" aria-label="${t().back}">${svg('back')}<span class="hide-sm">${t().back}</span></button>
          <div class="title">${esc(l.name[state.lang])}<small>${esc(l.cat.name[state.lang])} · ${t().lesson(l.index)}${l.versions.zh ? '' : ' · ' + t().enOnly}</small></div>
          ${langToggle()}
          <button class="ibtn" data-act="notes" aria-pressed="${state.notes}" aria-label="${t().notes}" title="${t().notes} (N)">${svg('notes')}</button>
          <button class="ibtn" data-act="full" aria-label="${t().full}" title="${t().full} (F)">${svg('full')}</button>
        </div>
        <div class="stage-wrap">
          <div class="stage">
            <div class="slide-root"></div>
            <button class="navzone prev" aria-label="${t().prev}"></button>
            <button class="navzone next" aria-label="${t().next}"></button>
          </div>
          <aside class="notes" ${state.notes ? '' : 'hidden'}><h3>${t().notes}</h3><p></p></aside>
        </div>
        <div class="vfoot">
          <button class="ibtn" data-act="prev" aria-label="${t().prev}">${svg('prev')}</button>
          <div class="progress"><i></i></div>
          <span class="count"></span>
          <button class="ibtn" data-act="next" aria-label="${t().next}">${svg('next')}</button>
        </div>
      </div>`;

    const viewer = app.querySelector('.viewer');
    const stage = app.querySelector('.stage');
    const root = app.querySelector('.stage .slide-root');
    const notes = app.querySelector('.notes');
    const show = () => {
      root.innerHTML = deck.slides[i].html;
      notes.querySelector('p').textContent = deck.slides[i].note || t().noNotes;
      app.querySelector('.count').textContent = `${i + 1} / ${total}`;
      app.querySelector('.progress i').style.width = `${((i + 1) / total) * 100}%`;
      history.replaceState(null, '', `#/${id}/${i + 1}`);
      fit(root, stage);
    };
    const go = d => { const j = Math.min(Math.max(0, i + d), total - 1); if (j !== i) { i = j; show(); } };
    const toggleNotes = () => {
      state.notes = !state.notes; store.set('ml.notes', state.notes ? '1' : '0');
      notes.hidden = !state.notes; app.querySelector('[data-act="notes"]').setAttribute('aria-pressed', state.notes);
      fit(root, stage);
    };
    const toggleFull = () => {
      if (document.fullscreenElement) document.exitFullscreen?.();
      else viewer.requestFullscreen?.().catch(() => {});
    };
    const back = () => { if (document.fullscreenElement) document.exitFullscreen?.(); location.hash = ''; };

    app.querySelector('.navzone.prev').onclick = () => go(-1);
    app.querySelector('.navzone.next').onclick = () => go(1);
    app.querySelector('[data-act="prev"]').onclick = () => go(-1);
    app.querySelector('[data-act="next"]').onclick = () => go(1);
    app.querySelector('[data-act="notes"]').onclick = toggleNotes;
    app.querySelector('[data-act="full"]').onclick = toggleFull;
    app.querySelector('[data-act="back"]').onclick = back;
    bindLang(() => renderViewer(id, i + 1));

    const onKey = e => {
      if (e.metaKey || e.ctrlKey || e.altKey) return;
      if (['ArrowRight', 'PageDown', ' ', 'Enter'].includes(e.key)) { e.preventDefault(); go(1); }
      else if (['ArrowLeft', 'PageUp', 'Backspace'].includes(e.key)) { e.preventDefault(); go(-1); }
      else if (e.key === 'Home') { i = 0; show(); }
      else if (e.key === 'End') { i = total - 1; show(); }
      else if (e.key === 'f' || e.key === 'F') toggleFull();
      else if (e.key === 'n' || e.key === 'N') toggleNotes();
      else if (e.key === 'Escape' && !document.fullscreenElement) back();
    };
    let x0 = null;
    const onTouchStart = e => { x0 = e.touches[0].clientX; };
    const onTouchEnd = e => {
      if (x0 === null) return; const dx = e.changedTouches[0].clientX - x0; x0 = null;
      if (Math.abs(dx) > 40) go(dx < 0 ? 1 : -1);
    };
    const ro = new ResizeObserver(() => fit(root, stage)); ro.observe(stage);
    document.addEventListener('keydown', onKey);
    stage.addEventListener('touchstart', onTouchStart, { passive: true });
    stage.addEventListener('touchend', onTouchEnd);
    cleanup = () => { document.removeEventListener('keydown', onKey); ro.disconnect(); };
    show();
    viewer.focus();
  }

  function route() {
    cleanup?.(); cleanup = null;
    const m = location.hash.match(/^#\/([\w-]+)(?:\/(\d+))?/);
    if (m && lessons[m[1]]) renderViewer(m[1], +m[2] || 1);
    else renderHome();
  }
  window.addEventListener('hashchange', route);
  document.fonts?.ready.then(() => { if (!location.hash) renderHome(); });
  route();
})();
