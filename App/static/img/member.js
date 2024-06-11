const membersPerPage = 10;
let currentPage = 1;

document.addEventListener('DOMContentLoaded', function() {
    loadMembers(currentPage);

    function loadMembers(page) {
        fetch(`get_members.php?page=${page}&limit=${membersPerPage}`)
            .then(response => response.json())
            .then(data => {
                displayMembers(data.members);
                setupPagination(data.totalMembers, membersPerPage, page);
            })
            .catch(error => console.error('Error loading members:', error));
    }

    function displayMembers(members) {
        const memberList = document.getElementById('member-list');
        memberList.innerHTML = '';

        members.forEach(member => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${member.num_soci}</td>
                <td>${member.nom}</td>
                <td>${member.data_naixement}</td>
                <td>${member.sexe}</td>
                <td>${member.email}</td>
            `;
            memberList.appendChild(row);
        });
    }

    function setupPagination(totalMembers, membersPerPage, currentPage) {
        const pagination = document.getElementById('pagination');
        pagination.innerHTML = '';
        const totalPages = Math.ceil(totalMembers / membersPerPage);

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
                loadMembers(i);
            });

            pagination.appendChild(pageLink);
        }
    }
});