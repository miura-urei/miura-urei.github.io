'use strict';

// Filtering progressively enhances the complete, readable HTML bibliography.
const filters = document.querySelector('.publication-filters');
if (filters) {
  const buttons = [...filters.querySelectorAll('button')];
  const papers = [...document.querySelectorAll('.publication')];
  const count = document.querySelector('#publication-count');
  filters.hidden = false;
  filters.addEventListener('click', (event) => {
    const selected = event.target.closest('button[data-filter]');
    if (!selected) return;
    const kind = selected.dataset.filter;
    buttons.forEach((button) => button.setAttribute('aria-pressed', String(button === selected)));
    papers.forEach((paper) => { paper.hidden = kind !== 'all' && paper.dataset.kind !== kind; });
    const visible = papers.filter((paper) => !paper.hidden).length;
    count.textContent = document.documentElement.lang === 'ja' ? `${visible} 件を表示` : `${visible} works shown`;
  });
}

// Keep the current section when moving between the two language editions.
document.querySelectorAll('[data-language-link]').forEach((link) => {
  const destination = link.getAttribute('href');
  const syncHash = () => { link.href = destination + window.location.hash; };
  syncHash();
  window.addEventListener('hashchange', syncHash);
});
