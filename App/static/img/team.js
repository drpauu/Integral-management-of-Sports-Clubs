document.addEventListener('DOMContentLoaded', function() {
    fetchTeams();

    function fetchTeams() {
        fetch('../backend/get_equip.php')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById('team-list');
            tableBody.innerHTML = ''; // Clear the table body
            data.forEach(team => {
                const row = tableBody.insertRow();
                const cellName = row.insertCell(0);
                const cellSport = row.insertCell(1);
                const cellViewMembers = row.insertCell(2);

                cellName.textContent = team.nom;
                cellSport.textContent = team.esport;

                const viewMembersButton = document.createElement('button');
                viewMembersButton.textContent = 'Veure Membres';
                viewMembersButton.onclick = () => viewTeamMembers(team.id);
                cellViewMembers.appendChild(viewMembersButton);
            });
        })
        .catch(error => console.error('Error loading team data:', error));
    }

    function viewTeamMembers(teamId) {
        fetch(`../backend/get_team_members.php?teamId=${teamId}`)
        .then(response => response.json())
        .then(data => {
            const modal = document.getElementById('membersModal');
            const tableBody = document.getElementById('members-list');
            tableBody.innerHTML = ''; // Clear previous members

            data.forEach(member => {
                const row = tableBody.insertRow();
                row.insertCell(0).textContent = member.num_soci;
                row.insertCell(1).textContent = member.nom;
                row.insertCell(2).textContent = member.data_naixement;
                row.insertCell(3).textContent = member.sexe;
                row.insertCell(4).textContent = member.email;
            });

            modal.style.display = 'block';
        })
        .catch(error => console.error('Error loading team members:', error));

        // Close modal setup
        document.querySelector('.close').onclick = function() {
            document.getElementById('membersModal').style.display = 'none';
        };
    }

    // Close modal if clicked outside of it
    window.onclick = function(event) {
        const modal = document.getElementById('membersModal');
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    }
});
