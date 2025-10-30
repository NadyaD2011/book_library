document.getElementById('id_poster').addEventListener('change', function(e) {
    const status = document.getElementById('file-status');
    if (e.target.files.length > 0) {
        status.textContent = 'Файл выбран';
        status.style.color = 'var(--accent-red)';
    } else {
        status.textContent = 'Файл не выбран';
        status.style.color = 'var(--text-gray)';
    }
});