window.onscroll = function() 
{myFunction()} ;

var content = document.getElementsByName("main_frame");
var sticky = header.offsetTop;

function myFunction() {
	if (window.pageYOffset >= sticky) {
	content.classList.add("fix_frame");
} 
	else {
	content.classList.remove("fix_frame");
	}
}	