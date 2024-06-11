const sportsPerPage = 10;
let currentPage = 1;

document.addEventListener('DOMContentLoaded', function() {
    loadSports(currentPage);

    function loadSports(page) {
        fetch(`get_sports.php?page=${page}&limit=${sportsPerPage}`)
            .then(response => response.json())
            .then(data => {
                displaySports(data.sports);
                setupPagination(data.totalSports, sportsPerPage, page);
            })
            .catch(error => console.error('Error loading sports:', error));
    }

    function displaySports(sports) {
        const sportList = document.getElementById('sport-list');
        sportList.innerHTML = '';

        sports.forEach(sport => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${sport.nom}</td>
                <td>${sport.descripcio}</td>
            `;
            sportList.appendChild(row);
        });
    }

    function setupPagination(totalSports, sportsPerPage, currentPage) {
        const pagination = document.getElementById('pagination');
        pagination.innerHTML = '';
        const totalPages = Math.ceil(totalSports / sportsPerPage);

        for (let i = 1; i <= totalPages; i++) {
            const pageLink = document.createElement('a');
            pageLink.href = '#';
            pageLink.innerText = i;
            pageLink.classList.add('page-link');
            if (i === currentPage) {
                pageLink.classList.add('active');
            }

            pageLink.addEventListener('click', function(event) {
                event.preventDefault();
                loadSports(i);
            });

            pagination.appendChild(pageLink);
        }
    }
});