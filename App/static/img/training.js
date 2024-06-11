const trainingsPerPage = 10;
let currentPage = 1;

document.addEventListener('DOMContentLoaded', function() {
    loadTrainings(currentPage);

    function loadTrainings(page) {
        fetch(`get_trainings.php?page=${page}&limit=${trainingsPerPage}`)
            .then(response => response.json())
            .then(data => {
                displayTrainings(data.trainings);
                setupPagination(data.totalTrainings, trainingsPerPage, page);
            })
            .catch(error => console.error('Error loading trainings:', error));
    }

    function displayTrainings(trainings) {
        const trainingList = document.getElementById('training-list');
        trainingList.innerHTML = '';

        trainings.forEach(training => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${training.data}</td>
                <td>${training.hora}</td>
                <td>${training.lloc}</td>
                <td>${training.esport}</td>
                <td>${training.categoria}</td>
                <td>${training.membres_present.join(', ')}</td>
            `;
            trainingList.appendChild(row);
        });
    }

    function setupPagination(totalTrainings, trainingsPerPage, currentPage) {
        const pagination = document.getElementById('pagination');
        pagination.innerHTML = '';
        const totalPages = Math.ceil(totalTrainings / trainingsPerPage);

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
                loadTrainings(i);
            });

            pagination.appendChild(pageLink);
        }
    }
});