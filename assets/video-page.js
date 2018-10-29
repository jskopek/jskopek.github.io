document.querySelectorAll('.btn-video-modal').forEach((el) => {
	el.addEventListener('click', (e) => {
		e.preventDefault();

		MicroModal.show('video-modal');

		let vimeoId = el.dataset.vimeoPlayerId;
		let summary = el.dataset.summary;

		var options = {
			id: vimeoId,
			background: false,
			muted: true,
			quality: '4k',
			responsive: 1
		};

		var player = new Vimeo.Player('vimeo-container', options);
		player.setVolume(0);
		player.on('play', function() {
			console.log('played the video!');
		});
		player.play();

		document.querySelector('.summary').innerHTML = summary;
	});
});

MicroModal.init();
