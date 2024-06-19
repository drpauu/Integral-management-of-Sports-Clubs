document.addEventListener('DOMContentLoaded', function() {
    // Initial fetch to load members
    fetchMembers();

    // Fetch members function definition
    function fetchMembers(query = '') {
        const url = query ?
            `../backend/search_members.php?searchQuery=${encodeURIComponent(query)}` :
            '../backend/get_members.php';

        fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            const table = document.getElementById('membersTableBody');
            table.innerHTML = ''; // Clear table for new data
            data.forEach(item => {
                const row = table.insertRow();
                row.insertCell(0).textContent = item.num_soci;
                row.insertCell(1).textContent = item.nom;
                row.insertCell(2).textContent = item.data_naixement;
                row.insertCell(3).textContent = item.sexe;
                row.insertCell(4).textContent = item.email;
                
                // Delete button
                const deleteCell = row.insertCell(5);
                const deleteButton = document.createElement('button');
                deleteButton.textContent = 'Eliminar';
                deleteButton.classList.add('delete-button'); // Add a class for styling
                deleteButton.onclick = function() {
                    deleteMember(item.num_soci);
                };
                deleteCell.appendChild(deleteButton);
            });
        })
        .catch(error => {
            console.error('Error al carregar les dades dels membres:', error);
            alert('Error al carregar les dades dels membres: ' + error.message);
        });
    }

    // Event listener for the search form submission
    document.getElementById('searchForm').addEventListener('submit', function(e) {
        e.preventDefault();
        const searchQuery = this.searchQuery.value;
        fetchMembers(searchQuery);
    });

    // Event listener for the add member form submission
    const addMemberForm = document.getElementById('addMemberForm');
    if (addMemberForm) {
        addMemberForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = new FormData(this);
    
            fetch('../backend/add_member.php', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
                alert('Membre afegit amb èxit');
                fetchMembers(); // Reload the list to include the new member
            })
            .catch(error => {
                console.error('Error al afegir el membre:', error);
                alert('Error al afegir el membre: ' + error.message);
            });
        });
    }

    function deleteMember(num_soci) {
        if(confirm('Segur que vols eliminar aquest membre?')) {
            fetch(`../backend/delete_member.php`, {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ num_soci: num_soci })
            })
            .then(response => response.json())
            .then(data => {
                console.log('Delete Success:', data);
                fetchMembers(); // Reload the list to reflect the deletion
            })
            .catch(error => {
                console.error('Error al eliminar el membre:', error);
                alert('Error al eliminar el membre: ' + error.message);
            });
        }
    }
});
