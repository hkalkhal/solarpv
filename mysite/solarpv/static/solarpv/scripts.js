$(document).ready(function($) {
    $("body").on('submit', '#myform', function(event) {

// $('#myform').submit(function(e) { 
        email_address = $("#email"); email_regex = /^\b[A-Z0-9._%-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b$/i; 
        if(!email_regex.test(email_address.val()))
        { 
            alert('this is not valid email'); 
            event.preventDefault(); 
            return false; 
        } 
    });
});