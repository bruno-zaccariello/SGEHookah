function iframeLoaded() {
	var iFrameID = document.getElementById("main_frame");
	var sectionID = document.getElementById("iframe_section");
	if(iFrameID){
	sectionID.style.height = "";
	sectionID.style.height = (iFrameID.contentWindow.document.body.scrollHeight + 20) + "px";
	}
}