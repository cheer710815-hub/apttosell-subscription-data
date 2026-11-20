/* AptToSell score widget v0.2 (2026-11-20): educational score arithmetic only. */
(function () {
  'use strict';
  const roots = document.querySelectorAll('[data-apttosell-score-widget], #apttosell-score-widget');
  if (!roots.length) return;
  const homeless = [['해당 없음',0],['1년 미만',2],['1~2년',4],['2~3년',6],['3~4년',8],['4~5년',10],['5~6년',12],['6~7년',14],['7~8년',16],['8~9년',18],['9~10년',20],['10~11년',22],['11~12년',24],['12~13년',26],['13~14년',28],['14~15년',30],['15년 이상',32]];
  const dependents = [['0명',5],['1명',10],['2명',15],['3명',20],['4명',25],['5명',30],['6명 이상',35]];
  const account = [['6개월 미만',1],['6개월~1년',2],['1~2년',3],['2~3년',4],['3~4년',5],['4~5년',6],['5~6년',7],['6~7년',8],['7~8년',9],['8~9년',10],['9~10년',11],['10~11년',12],['11~12년',13],['12~13년',14],['13~14년',15],['14~15년',16],['15년 이상',17]];
  const spouse = [['해당 없음',0],['1점',1],['2점',2],['3점',3]];
  function addSelect(root, labelText, key, arr) {
    const label = document.createElement('label');
    label.textContent = labelText;
    const sel = document.createElement('select');
    sel.setAttribute('data-k', key);
    for (const option of arr) {
      const opt = document.createElement('option');
      opt.value = String(option[1]);
      opt.textContent = option[0] + ' (' + option[1] + '점)';
      sel.appendChild(opt);
    }
    label.appendChild(sel);
    root.appendChild(label);
  }
  roots.forEach(function (root) {
    if (root.getAttribute('data-atsw-initialized') === 'true') return;
    root.setAttribute('data-atsw-initialized','true');
    const card = document.createElement('div');
    card.className = 'atsw-card';
    const title = document.createElement('div');
    title.className = 'atsw-title';
    title.textContent = '청약가점 간편 계산 (교육용)';
    card.appendChild(title);
    addSelect(card,'무주택기간 점수','h',homeless);
    addSelect(card,'부양가족 점수','d',dependents);
    addSelect(card,'본인 청약통장 가입기간 점수','a',account);
    addSelect(card,'배우자 청약통장 인정점수','s',spouse);
    const result = document.createElement('div');
    result.className = 'atsw-result';
    result.setAttribute('role','status');
    result.setAttribute('aria-live','polite');
    card.appendChild(result);
    const note = document.createElement('p');
    note.className='atsw-note';
    note.textContent='가상 입력 구간의 배점 합산만 제공합니다. 배우자 인정점수 포함 통장 항목은 최대 17점이며 실제 신청조건은 최신 모집공고에서 확인하세요.';
    card.appendChild(note);
    // Optional attribution; never enforced or inserted without site owner choice.
    if (root.getAttribute('data-show-source') === 'true') {
      const source = document.createElement('a');
      source.className = 'atsw-source';
      source.href = 'https://apttosell.com/cheongyak-score-calculator/';
      source.target = '_blank';
      source.rel = 'noopener noreferrer';
      source.textContent = 'AptToSell 계산 기준과 공식 출처';
      card.appendChild(source);
    }
    root.appendChild(card);
    const calc = function () {
      const get = function(k){ const el = card.querySelector('select[data-k="' + k + '"]'); return Number(el.value); };
      const h = get('h'), d = get('d'), a = get('a'), s = get('s');
      const accountPoints = Math.min(17,a+s);
      result.textContent = '예상 총점 ' + (h+d+accountPoints) + '점 / 84점 (무주택 ' + h + ' + 가족 ' + d + ' + 통장 ' + accountPoints + ')';
    };
    card.addEventListener('change',calc);
    calc();
  });
  if (!document.getElementById('atsw-style')) {
    const style = document.createElement('style');
    style.id='atsw-style';
    style.textContent='.atsw-card{box-sizing:border-box;max-width:520px;padding:20px;border:1px solid #ddd;border-radius:16px;background:#fff;font-family:Arial,"Noto Sans KR",sans-serif;color:#222}.atsw-card *{box-sizing:border-box}.atsw-title{font-size:20px;font-weight:700;margin-bottom:16px}.atsw-card label{display:block;font-size:14px;font-weight:600;margin:12px 0}.atsw-card select{display:block;width:100%;margin-top:7px;padding:11px;border:1px solid #aaa;border-radius:8px;background:#fff;color:#222;font-size:14px}.atsw-result{margin-top:18px;padding:16px;border-radius:12px;background:#f6f6f6;font-weight:700;line-height:1.6}.atsw-note{margin:12px 0 10px;font-size:12px;line-height:1.6;color:#555}.atsw-source{font-size:12px;color:#245b80;text-decoration:underline}@media(max-width:480px){.atsw-card{padding:14px}.atsw-title{font-size:18px}}';
    document.head.appendChild(style);
  }
})();