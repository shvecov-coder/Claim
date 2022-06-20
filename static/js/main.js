function OpenModalWindow() {
	document.getElementsByClassName('modal-window')[0].classList.add('modal--active');
	document.getElementsByTagName("body")[0].style = "overflow: hidden;"
}
function CloseModalWindow() {
	document.getElementsByClassName('modal-window')[0].classList.remove('modal--active');
	document.getElementsByTagName("body")[0].style = ""
}