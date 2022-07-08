function OpenModalWindow() {
	document.querySelector('.modal-window').classList.add('modal--active');
	document.querySelector('body').style = "overflow: hidden;"
}
function CloseModalWindow() {
	document.querySelector('.modal-window').classList.remove('modal--active');
	document.querySelector('body').style = ""
}

const realFileBtn = document.querySelector('.input-fileUpload');
const customBtn = document.querySelector('.button-fileUpload');
const customText = document.querySelector('.fileUpload-text');
const generateForm = document.querySelector('.generate-form');
const createProg = document.querySelector('.create__prog');

customBtn.addEventListener('click', function () {
	realFileBtn.click();
})

createProg.addEventListener('click', function() {
	if (realFileBtn.value !== "") {
		generateForm.submit();
	} else {
		console.log('ФАЙЛ ПУСТ')
	}
})

realFileBtn.addEventListener('change', function () {
	var validExts = new Array(".xlsx", ".xls");
	var fileExt = realFileBtn.value;
	fileExt = fileExt.substring(fileExt.lastIndexOf('.'));
	if (validExts.indexOf(fileExt) < 0) {
		customText.innerHTML = 'Ошибка! Файл должен быть ' + validExts.toString();
		realFileBtn.value = "";
		return false;
	} else {
		if (realFileBtn.value) {
			customText.innerHTML = realFileBtn.value.match(/[\/\\]([\w\d\s\.\-\(\)]+)$/)[1];
		} else {
			customText.innerHTML = 'Файл еще не выбран.'
		}
		return true;
	}
})



