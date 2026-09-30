// Segmented control: builds the clipped overlay and keeps it on the selected option.
// Plain script (works from file://): exposes window.initSegmented. Copy into a module and `export` it in a bundled app.
// Markup: <div class="segmented" role="radiogroup" aria-label="…"> <button class="segmented__option" role="radio" aria-checked="true">…</button> … </div>
function initSegmented(root, { onChange } = {}) {
  const options = [...root.querySelectorAll('.segmented__option')];
  const overlay = document.createElement('div');
  overlay.className = 'segmented__active';
  overlay.setAttribute('aria-hidden', 'true');
  for (const option of options) {
    const label = document.createElement('span');
    label.textContent = option.textContent;
    overlay.append(label);
  }
  root.append(overlay);
  root.dataset.ready = 'false';

  let current = 0;
  const place = () => {
    const option = options[current];
    const left = option.offsetLeft - overlay.offsetLeft;
    const right = overlay.offsetWidth - left - option.offsetWidth;
    overlay.style.setProperty('--clip-left', `${left}px`);
    overlay.style.setProperty('--clip-right', `${right}px`);
  };

  const select = (index, { focus = false, silent = false } = {}) => {
    current = index;
    options.forEach((option, i) => {
      option.setAttribute('aria-checked', String(i === index));
      option.tabIndex = i === index ? 0 : -1;
    });
    place();
    if (focus) options[index].focus();
    if (!silent) onChange?.(index, options[index]);
  };

  options.forEach((option, i) => {
    option.addEventListener('click', () => select(i));
    option.addEventListener('keydown', (e) => {
      const step = { ArrowRight: 1, ArrowDown: 1, ArrowLeft: -1, ArrowUp: -1 }[e.key];
      if (!step) return;
      e.preventDefault();
      select((i + step + options.length) % options.length, { focus: true });
    });
  });

  select(Math.max(0, options.findIndex((o) => o.getAttribute('aria-checked') === 'true')), { silent: true });
  requestAnimationFrame(() => { root.dataset.ready = 'true'; }); // no animation on first paint
  new ResizeObserver(place).observe(root);
  return { select };
}

globalThis.initSegmented = initSegmented;
