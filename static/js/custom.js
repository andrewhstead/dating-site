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
    else if (type == 'post') {
        document.getElementById('post-wrapper-' + post).classList.toggle('activate');
        document.getElementById('post-alert-' + post).classList.toggle('activate');
    }
}

// Pop-up function for posts to allow for passing through the id of the post.
function postAlert(post) {
    document.getElementById('post-wrapper-' + post).classList.toggle('activate');
    document.getElementById('post-alert-' + post).classList.toggle('activate');
}

// Functions to toggle sections of code.
$('.slide-toggle').click(function(){
    $('.slide-change').slideToggle(1000);
});
$('.instant-toggle').click(function(){
    $('.instant-change').slideToggle(0);
});

messageRemove();