const overlay = document.querySelector('.overlay');
const movableText = document.getElementById('movable-text');
let isDragging = false;
let startMouseX = 0;
let startMouseY = 0;
let startElementX = 0;
let startElementY = 0;

movableText.addEventListener('mousedown', startDrag);
movableText.addEventListener('mouseup', stopDrag);
movableText.addEventListener('mousemove', drag);
movableText.addEventListener('mouseleave', stopDrag);

function startDrag(event) {
  isDragging = true;
  startMouseX = event.clientX;
  startMouseY = event.clientY;
  startElementX = parseInt(window.getComputedStyle(movableText).getPropertyValue('left'));
  startElementY = parseInt(window.getComputedStyle(movableText).getPropertyValue('top'));
  movableText.style.cursor = 'grabbing';
}

function stopDrag() {
  isDragging = false;
  movableText.style.cursor = 'move';
}

function drag(event) {
  if (isDragging) {
    const offsetX = event.clientX - startMouseX;
    const offsetY = event.clientY - startMouseY;
    const newLeft = startElementX + offsetX;
    const newTop = startElementY + offsetY;
    movableText.style.left = newLeft + 'px';
    movableText.style.top = newTop + 'px';
  }
}