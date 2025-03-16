document.addEventListener('DOMContentLoaded', function() {
    const sidebar = document.getElementById('sidebar');
    const toggle = document.getElementById('toggle');

    // Sidebar hover effect
    sidebar.addEventListener('mouseenter', function() {
        sidebar.style.width = '200px';
    });

    sidebar.addEventListener('mouseleave', function() {
        sidebar.style.width = '60px';
    });

    // Theme switching
    toggle.addEventListener('change', function() {
        if (toggle.checked) {
            document.body.classList.add('dark-mode');
        } else {
            document.body.classList.remove('dark-mode');
        }
    });

    // Add more event listeners for other interactions
}); 