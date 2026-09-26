# Embed & reuse

AptToSell의 청약가점 차트와 CSV를 기사·블로그·가이드에 사용할 수 있습니다. 출처 링크는 canonical data page로 연결해 주세요.

## Chart embed

### Markdown

```markdown
[![2026 민영주택 청약가점 84점 구성](https://raw.githubusercontent.com/cheer710815-hub/apttosell-subscription-data/main/assets/apttosell-score-components.svg)](https://apttosell.com/cheongyak-score-data/)
```

### HTML

```html
<a href="https://apttosell.com/cheongyak-score-data/" target="_blank" rel="noopener">
  <img src="https://raw.githubusercontent.com/cheer710815-hub/apttosell-subscription-data/main/assets/apttosell-score-components.svg"
       alt="2026 민영주택 청약가점 84점 구성"
       style="max-width:100%;height:auto;">
</a>
<p>자료: <a href="https://apttosell.com/cheongyak-score-data/">AptToSell 2026 청약가점 84점 데이터표</a></p>
```

## One-line source link

### HTML

```html
<p>출처: <a href="https://apttosell.com/housing-subscription-data/" target="_blank" rel="noopener">AptToSell 청약·분양 데이터센터</a></p>
```

### Markdown

```markdown
출처: [AptToSell 청약·분양 데이터센터](https://apttosell.com/housing-subscription-data/)
```

## Suggested reuse blocks

### 청약가점 계산기 링크

```html
<a href="https://apttosell.com/cheongyak-score-calculator/" target="_blank" rel="noopener">2026 청약가점 계산기</a>
```

### 청약가점 데이터 링크

```html
<a href="https://apttosell.com/cheongyak-score-data/" target="_blank" rel="noopener">2026 청약가점 84점 데이터</a>
```

## CSV

https://raw.githubusercontent.com/cheer710815-hub/apttosell-subscription-data/main/housing_subscription_score_2026.csv

## License

CC BY 4.0. 재사용 시 출처와 원문 링크를 함께 표시해 주세요.


## Interactive widget

청약가점 계산기를 외부 블로그·교육자료·가이드에 삽입할 수 있습니다. 위젯 하단의 AptToSell 원문 링크를 유지해 주세요.

### HTML embed

```html
<div data-apttosell-score-widget></div>
<script src="https://cdn.jsdelivr.net/gh/cheer710815-hub/apttosell-subscription-data@33ae5289527cbbe3e5cf260a21419824aede1866/widgets/apttosell-score-widget.js"></script>
```

### Widget source

- https://github.com/cheer710815-hub/apttosell-subscription-data/blob/main/widgets/apttosell-score-widget.js

### Canonical source

- https://apttosell.com/cheongyak-score-calculator/
