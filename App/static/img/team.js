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
                <td><button onclick="viewMembers('${team.nom}')">Veure Membres</button></td>
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

function viewMembers(teamName) {
    fetch(`get_team_members.php?equip_nom=${teamName}`)
        .then(response => response.json())
        .then(data => {
            displayMembers(data.members);
            document.getElementById('membersModal').style.display = 'block';
        })
        .catch(error => console.error('Error loading team members:', error));
}

function displayMembers(members) {
    const membersList = document.getElementById('members-list');
    membersList.innerHTML = '';

    members.forEach(member => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${member.num_soci}</td>
            <td>${member.nom}</td>
            <td>${member.data_naixement}</td>
            <td>${member.sexe}</td>
            <td>${member.email}</td>
        `;
        membersList.appendChild(row);
    });
}

document.querySelector('.close').addEventListener('click', function() {
    document.getElementById('membersModal').style.display = 'none';
});

window.addEventListener('click', function(event) {
    if (event.target == document.getElementById('membersModal')) {
        document.getElementById('membersModal').style.display = 'none';
    }
});