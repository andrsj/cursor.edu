let images = document.querySelectorAll('.gallery-item');
let controls = document.querySelector('.gallery-controls');
let totalImages = images.length;
let currentImage = 0;

images[currentImage].className += ' active' 

const nextImage = () => {
	showImage(currentImage + 1);
}

const prevImage = () => {
	showImage(currentImage - 1);
}

const onNext = () => {
	nextImage();
}

const onPrev = () => {
	prevImage();
}

const showImage = n => {
	images[currentImage].className = 'gallery-item';
    currentImage = (n + totalImages) % totalImages;
    images[currentImage].className = 'gallery-item active';
	
	const dots = document.querySelectorAll('.dot');
	dots.forEach((dot, index) => {
		if(index == currentImage) {
			dot.className = 'dot active'
		}
		else {
			dot.className = 'dot';
		}
	})
}

const showDirectionNav = () => {
	const prevBtn = document.createElement('button');
	const nextBtn = document.createElement('button');

	prevBtn.className = 'btn-prev';
	nextBtn.className = 'btn-next';

	controls.appendChild(prevBtn);
	controls.appendChild(nextBtn);

	nextBtn.addEventListener('click', onNext);
	prevBtn.addEventListener('click', onPrev);
};

const showControlNav = () => {
	const dotsContainer = document.createElement('div');
	dotsContainer.className = 'dots';
	controls.appendChild(dotsContainer);
	
	images.forEach((image, index) => {
		dotsContainer.innerHTML += `<span id="${index}" class="dot">${index + 1}</span>`;
	});
};

const initGallery = () => {
	if (document.querySelector("#delete") != null){
		var del = document.querySelector("#delete");
		del.remove();
		alert("LOL");
	}
	setParameters();
	if (document.querySelector(".gallery-controls").children.length != 0){
		while (document.querySelector(".gallery-controls").firstChild) {
			document.querySelector(".gallery-controls").removeChild(document.querySelector(".gallery-controls").firstChild);
		}
	}
	showDirectionNav();
	showControlNav();
	setClick(document.querySelectorAll("img.gallery-icon"));
	// setClick();
	document.querySelector("#output").innerHTML = names;
};

const setClick = imgs => {
	for( i of imgs){
		let img = i;
		img.onclick = () => { showImage(parseInt(img.getAttribute("count")))};
		// img.addEventListener('click', () => {showImage(parseInt(img.getAttribute("count")))});
	}
}

const setParameters = () => {
	images = document.querySelectorAll('.gallery-item');
	controls = document.querySelector('.gallery-controls');
	totalImages = images.length;
	currentImage = totalImages - 1;
};

let src = false;
let count = 0;
let names = "";
const setSrc = event => {
	src = URL.createObjectURL(event.target.files[0]);
}

const create = event => {
	let img = document.createElement('img');
	img.className = "gallery-item";
	img.src = src;
	event.target.nextElementSibling.nextElementSibling.firstElementChild.append(img);
	count += 1;
	names += event.target.files[0].name + '<br>';
	document.querySelector("#output").innerHTML = names;
	event.target.value = "";
}

let counter = 0;

const createIcon = event =>{
	let img = document.createElement('img');
	img.className = "gallery-icon";
	img.src = src;
	img.setAttribute("count",counter);
	counter += 1;
	event.target.nextElementSibling.nextElementSibling.lastElementChild.append(img);
}

const createOneImg = (event,j) => {
	let img = document.createElement('img');
	img.className = "gallery-item";
	// if(j == 0) img.className += " active";
	img.src = URL.createObjectURL(event.files[j]);
	event.nextElementSibling.nextElementSibling.firstElementChild.append(img);
	names += event.files[j].name + '<br>';
	document.querySelector("#output").innerHTML = names;


	img1 = document.createElement('img');
	img1.className = "gallery-icon";
	img1.setAttribute("count",j);
	img1.src = img.src;
	event.nextElementSibling.nextElementSibling.lastElementChild.append(img1);
}

const create2 = event => {
	for (let j = 0 ; j < event.files.length; j++){
		createOneImg(event,j);
	}
}