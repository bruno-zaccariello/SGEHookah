function ToggleMenu() {
	var menu = document.getElementById("oam_wrapper");
	var iFrame = document.getElementById("main_frame");
    var userPage = document.getElementById("main_frame").contentWindow.document.getElementById("user_main_body");
    if (userPage) {
        $('#oam_wrapper').slideToggle("fast", "linear");
        $('.oam_opt').toggleClass('opt_none_bg');
    } else {
        $('#oam_wrapper').slideToggle("fast", "linear");
        $('.oam_opt').toggleClass('opt_none_bg');
    };
}