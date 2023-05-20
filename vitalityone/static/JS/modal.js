// Function to get the value of a cookie
function getCookie(name) {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        if (cookie.startsWith(name + "=")) {
            return cookie.substring(name.length + 1);
        }
    }
    return null;
}

window.addEventListener('DOMContentLoaded', function () {
    var hasVisited = getCookie('hasVisited');

    if (!hasVisited) {
        var popup = document.getElementById('cookiesPopup');
        popup.style.overflow = 'hidden';  // Prevent scrolling on the website

        // Apply smooth transition when the popup appears
        setTimeout(function () {
            popup.classList.add('show');
        }, 100);

        // Set the 'hasVisited' cookie when the modal is closed
        var closeButton = document.querySelector('.close');
        closeButton.addEventListener('click', function () {
            popup.classList.remove('show');  // Enable scrolling on the website
            setCookie('hasVisited', 'true', 1);

            // Delay hiding the popup to allow the transition to complete
            setTimeout(function () {
                popup.style.display = 'none';
            }, 300);
        });
    }
    else{
        var popup = document.getElementById('cookiesPopup');
        popup.style.display = 'none';  // Prevent scrolling on the website
    }
});

// Function to set a cookie with expiry date set to 1 day from the current date
function setCookie(name, value, days) {
    var expires = new Date();
    expires.setDate(expires.getDate() + days);
    document.cookie = name + "=" + value + ";expires=" + expires.toUTCString() + ";path=/";
}
