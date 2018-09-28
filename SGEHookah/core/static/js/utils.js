$(document).ready(function() {
    
    $("button[type=submit]").click(function() {
        $(this).prop("disabled", true)
    })
})