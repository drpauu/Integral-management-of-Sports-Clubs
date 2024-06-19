document.querySelectorAll('.info-link').forEach(link => {
    link.addEventListener('click', function(event) {
        event.preventDefault();
        const infoType = link.getAttribute('data-info');
        document.querySelectorAll('.info-content').forEach(content => {
            content.style.display = 'none';
        });
        document.getElementById(`${infoType}-info`).style.display = 'block';
        document.getElementById('infoModal').style.display = 'block';
    });
});

document.querySelector('.close').addEventListener('click', function() {
    document.getElementById('infoModal').style.display = 'none';
});

window.addEventListener('click', function(event) {
    if (event.target == document.getElementById('infoModal')) {
        document.getElementById('infoModal').style.display = 'none';
    }
});