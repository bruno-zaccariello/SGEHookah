function ToggleMenu() {
	var menu = document.getElementById("oam_wrapper");
	var iFrame = document.getElementById("main_frame");
    var userPage = document.getElementById("main_frame").contentWindow.document.getElementById("user_main_body");
    if (userPage) {
        $('#oam_wrapper').slideToggle("fast", "linear");
    } else {
        if (menu.style.display == "none"){
            $('#oam_wrapper').slideToggle("fast", "linear");
            $('#main_frame').removeClass('frame_height');
        } else if(menu.style.display == "grid") {
            $('#oam_wrapper').slideToggle("fast", "linear");
            $('#main_frame').addClass('frame_height');
        } ;
    };
}
