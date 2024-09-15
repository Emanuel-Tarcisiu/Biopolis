function showSection(sectionId) {
    const sections = document.querySelectorAll('.data-card');
    sections.forEach(section => {
        section.style.display = 'none';
    });

    document.getElementById(sectionId).style.display = 'block';
}


document.addEventListener('DOMContentLoaded', () => {
    showSection('map'); 
});


function validateForm(event) {
    event.preventDefault(); 

    const password = document.getElementById('password').value;
    if (password.length >= 8) {
        alert('Account created successfully! Redirecting to the Map section...');
        showSection('map'); 
    } else {
        alert('Password must be at least 8 characters long.');
    }
}


document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('.signup-card form');
    if (form) {
        form.addEventListener('submit', validateForm);
    }
});
