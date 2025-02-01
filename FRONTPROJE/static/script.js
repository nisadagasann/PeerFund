document.addEventListener('DOMContentLoaded', () => {
    // Kullanıcıları yükle ve tabloya ekle
    fetch('/users')
        .then(response => response.json())
        .then(data => {
            const userList = document.getElementById('user-list');
            userList.innerHTML = '';
            data.forEach(user => {
                const li = document.createElement('li');
                li.textContent = `${user.name} (${user.email})`;
                userList.appendChild(li);
            });
        });

    // Kredi taleplerini yükle
    fetch('/loan_requests')
        .then(response => response.json())
        .then(data => {
            const loanList = document.getElementById('loan-list');
            loanList.innerHTML = '';
            data.forEach(loan => {
                const li = document.createElement('li');
                li.textContent = `ID: ${loan.id}, Miktar: ${loan.amount_requested}, Durum: ${loan.status}`;
                loanList.appendChild(li);
            });
        });

    // Yeni kullanıcı ekleme
    const addUserForm = document.getElementById('add-user-form');
    if (addUserForm) {
        addUserForm.addEventListener('submit', event => {
            event.preventDefault();
            const formData = new FormData(addUserForm);
            const user = {
                name: formData.get('name'),
                email: formData.get('email'),
                password: formData.get('password'),
                user_type: formData.get('user_type'),
            };

            fetch('/users', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(user),
            })
                .then(response => {
                    if (response.ok) {
                        alert('Kullanıcı başarıyla eklendi!');
                        location.reload();
                    } else {
                        alert('Kullanıcı eklenirken bir hata oluştu.');
                    }
                })
                .catch(error => console.error('Hata:', error));
        });
    }
});
