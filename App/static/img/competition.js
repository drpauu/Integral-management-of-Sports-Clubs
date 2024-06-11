const competitionsPerPage = 10;
let currentPage = 1;

document.addEventListener('DOMContentLoaded', function() {
    loadCompetitions(currentPage);

    function loadCompetitions(page) {
        fetch(`get_competitions.php?page=${page}&limit=${competitionsPerPage}`)
            .then(response => response.json())
            .then(data => {
                displayCompetitions(data.competitions);
                setupPagination(data.totalCompetitions, competitionsPerPage, page);
            })
            .catch(error => console.error('Error loading competitions:', error));
    }

    function displayCompetitions(competitions) {
        const competitionList = document.getElementById('competition-list');
        competitionList.innerHTML = '';

        competitions.forEach(competition => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${competition.nom}</td>
                <td>${competition.esport}</td>
                <td>${competition.categoria}</td>
                <td>${competition.any_celebracio}</td>
            `;
            competitionList.appendChild(row);
        });
    }

    function setupPagination(totalCompetitions, competitionsPerPage, currentPage) {
        const pagination = document.getElementById('pagination');
        pagination.innerHTML = '';
        const totalPages = Math.ceil(totalCompetitions / competitionsPerPage);

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
                loadCompetitions(i);
            });

            pagination.appendChild(pageLink);
        }
    }
});