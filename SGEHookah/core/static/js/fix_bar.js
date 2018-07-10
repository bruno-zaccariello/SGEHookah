window.onscroll = function() 
{fixbar()} ;

var header = document.getElementById("search_wrapper");
var sticky = header.offsetTop;
var content = document.getElementById("main_frame");

function fixbar() {
	if (window.pageYOffset >= sticky) {
	header.classList.add("sticky");
	content.classList.add("fix_frame");
} 
	else {
	header.classList.remove("sticky");
	content.classList.remove("fix_frame");
	}
}	