// format table adminLTE3
$(function () {
    $('#tbl-admin').DataTable({
        "paging": true,
        "lengthChange": false,
        "searching": false,
        "ordering": true,
        "info": true,
        "autoWidth": false,
        "responsive": true,
    });
});


//pass data to delete modal
$('#modal-delete').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget) 

    var email = button.data('email') 
    var id = button.data('id') 

    var modal = $(this)
    modal.find('.modal-body p').html(`Are you sure to <strong>DELETE</strong> admin <strong>'${email}'</strong> ?`)
    modal.find('.modal-body #delete-id').val(id)
})


//pass data to edit modal
$('#modal-edit').on('show.bs.modal', function (event) {
    var td = $(event.relatedTarget); 

    var name = td.data('name')
    var email = td.data('email')
    // var password = td.data('password')
    var id = td.data('id')

    var modal = $(this)
    modal.find('.modal-body #edit-name').val(name)
    modal.find('.modal-body #edit-email').val(email)
    // modal.find('.modal-body #edit-password').val(password)
    modal.find('.modal-body #edit-id').val(id)
});


// validate add form
const addForm = document.getElementById('add-form');

addForm.addEventListener('submit', function (event) {
    const password = document.getElementById('add-password');
    const confirmPassword = document.getElementById('add-confirm-password');
    if (password.value !== confirmPassword.value) {
        alert('Password does not match');
        event.preventDefault(); //prevent submit form
        return;
    }

    if (password.value.length < 6) {
        alert('Password needs at least 6 characters');
        event.preventDefault(); //prevent submit form
        return;
    }
});


// validate edit form
const editForm = document.getElementById('edit-form');

editForm.addEventListener('submit', function (event) {
    const password = document.getElementById('edit-password');
    const confirmPassword = document.getElementById('edit-confirm-password');
    if (password.value !== confirmPassword.value) {
        alert('Password does not match');
        event.preventDefault(); //prevent submit form
        return;
    }

    if (password.value.length < 6) {
        alert('Password needs at least 6 characters');
        event.preventDefault(); //prevent submit form
        return;
    }
});