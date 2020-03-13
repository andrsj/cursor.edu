const images = document.querySelectorAll('.gallery-item');
const controls = document.querySelector('.gallery-controls');
const totalImages = images.length;
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

const showImage = (n) => {
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
}

const initGallery = () => {
	showDirectionNav();
	showControlNav();
};