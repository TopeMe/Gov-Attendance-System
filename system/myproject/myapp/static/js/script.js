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
