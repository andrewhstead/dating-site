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

messageRemove();