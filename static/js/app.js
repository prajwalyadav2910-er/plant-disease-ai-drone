document.addEventListener('DOMContentLoaded', () => {
  const input = document.querySelector('input[type="file"]');
  const button = document.querySelector('button');

  if (input && button) {
    input.addEventListener('change', () => {
      if (input.files && input.files.length > 0) {
        button.textContent = `${input.files[0].name}`;
      }
    });
  }
});
