window.onload = () => {
  const navLinks = document.getElementsByClassName('nav-link');
  if (navLinks) {
    for (const element of navLinks) {
      element.classList.remove('active');
      if (element.href === window.location.href) {
        element.classList.add('active');
      }
    }
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const themeToggle = document.getElementById('themeToggle');
  const themeIcon = document.getElementById('themeIcon');
  const currentTheme = localStorage.getItem('theme') || 'light';

  const applyTheme = (theme) => {
    document.documentElement.setAttribute('data-bs-theme', theme);
    themeIcon.className = theme === 'dark' ? 'bi bi-sun-fill' : 'bi bi-moon-fill';
  };

  applyTheme(currentTheme);

  themeToggle.addEventListener('click', () => {
    const newTheme = document.documentElement.getAttribute('data-bs-theme') === 'dark' ? 'light' : 'dark';
    applyTheme(newTheme);
    localStorage.setItem('theme', newTheme);
  });
});