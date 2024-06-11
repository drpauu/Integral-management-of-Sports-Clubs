const teamsPerPage = 10;
let currentPage = 1;

document.addEventListener('DOMContentLoaded', function() {
    loadTeams(currentPage);

    function loadTeams(page) {
        fetch(`get_teams.php?page=${page}&limit=${teamsPerPage}`)
            .then(response => response.json())
            .then(data => {
                displayTeams(data.teams);
                setupPagination(data.totalTeams, teamsPerPage, page);
            })
            .catch(error => console.error('Error loading teams:', error));
    }

    function displayTeams(teams) {
        const teamList = document.getElementById('team-list');
        teamList.innerHTML = '';

        teams.forEach(team => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${team.nom}</td>
                <td>${team.categoria}</td>
                <td>${team.esport}</td>
            `;
            teamList.appendChild(row);
        });
    }

    function setupPagination(totalTeams, teamsPerPage, currentPage) {
        const pagination = document.getElementById('pagination');
        pagination.innerHTML = '';
        const totalPages = Math.ceil(totalTeams / teamsPerPage);

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
                loadTeams(i);
            });

            pagination.appendChild(pageLink);
        }
    }
});