# Mini Lessons 迷你課

國中理化與生物迷你課簡報，依 物理 / 化學 / 生物 分類，每類 3 課。介面可切換中文 / English。

**網址：** https://danll737321-beep.github.io/mini-slide-/

## 使用

- 首頁依分類列出課程，點卡片開始播放
- 翻頁：`←` `→`、空白鍵，或點投影片左右兩側；手機左右滑動
- `F` 全螢幕、`N` 講者備註、`Esc` 返回
- 右上角「中文 / EN」切換介面語言；有中文版的課程（電路、波動）會同時切換簡報版本，並停在同一張
- 網址會記住頁數，例如 `#/circuits/7`，可直接分享到某一張

## 結構

```
index.html            App 入口
assets/app.js|css     首頁與播放器
content/catalog.json  分類、課程名稱、各語言版本對應
content/<deck>/       每份簡報的原始檔（deck.json + slides/*.html，1920×1080）
data/decks.js         打包後的資料（由 build.py 產生，勿手改）
tools/build.py        打包腳本
```

## 新增或更新簡報

1. 把簡報資料夾放進 `content/`，例如 `content/osmosis-zh/`（內含 `deck.json` 與 `slides/`）
2. 在 `content/catalog.json` 對應課程的 `versions` 加上 `"zh": "osmosis-zh"`
3. 執行 `python3 tools/build.py`，commit 後推上 GitHub
