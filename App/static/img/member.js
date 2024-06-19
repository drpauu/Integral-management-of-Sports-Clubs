const membersPerPage = 10;
let currentPage = 1;

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
            });
        })
        .catch(error => {
            console.error('Error loading the members data:', error);
            alert('Error loading the members data: ' + error.message);
        });
    }

    // Event listener for the search form submission
    document.getElementById('searchForm').addEventListener('submit', function(e) {
        e.preventDefault();
        const searchQuery = this.searchQuery.value;
        fetchMembers(searchQuery);
    });
});
