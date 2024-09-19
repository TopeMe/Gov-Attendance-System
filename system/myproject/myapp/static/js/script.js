document.addEventListener('DOMContentLoaded', () => {

    // Event listeners for forms
    document.getElementById('show-login').addEventListener('click', () => toggleForm('login-form'));
    document.getElementById('back-btn').addEventListener('click', () => toggleForm('checkin-form'));

    function toggleForm(formId) {
        document.querySelectorAll('.form-container form').forEach(form => {
            form.style.display = form.id === formId ? 'block' : 'none';
        });
        document.querySelector('.dashboard').style.display = 'none';
    }
});

function updateClock() {
    const now = new Date();
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const seconds = String(now.getSeconds()).padStart(2, '0');
    
    const timeString = `${hours}:${minutes}:${seconds}`;
    document.getElementById('time').textContent = timeString;
}

// Update the clock every second
setInterval(updateClock, 1000);

// Initialize the clock
updateClock();
