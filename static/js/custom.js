// Function to allow the user to toggle the navigation menu on and off in the default stylesheet.
$('#menu-button').click(function(){
    $('#main-menu').slideToggle(1000);
});

// Function to remove message alerts after five seconds.
function messageRemove() {
    setTimeout(
        function() {
            document.getElementById('messages').classList.add('hidden');
        }, 5000
    );
}

// Pop-up function to ask for confirmation.
function confirmationAlert(type) {
    if (type == 'wave') {
        document.getElementById('wave-wrapper').classList.toggle('activate');
        document.getElementById('wave-alert').classList.toggle('activate');
    }
    else if (type == 'delete') {
        document.getElementById('delete-wrapper').classList.toggle('activate');
        document.getElementById('delete-alert').classList.toggle('activate');
    }
    else if (type == 'favourite') {
        document.getElementById('favourite-wrapper').classList.toggle('activate');
        document.getElementById('favourite-alert').classList.toggle('activate');
    }
    else if (type == 'block') {
        document.getElementById('block-wrapper').classList.toggle('activate');
        document.getElementById('block-alert').classList.toggle('activate');
    }
}

messageRemove();