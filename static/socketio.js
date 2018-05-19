document.addEventListener('DOMContentLoaded', () => {

	//connect to websocket
	var socket = io.connect(location.protocol+'//'+document.domain+':'+location.port);
	//var socket = io.connect('http://127.0.01:5000');

	//when connected, configure buttons
	socket.on('connect', () => {

		//each button should emit a submit vote event
		document.querySelectorAll('button').forEach(button => {
			button.onclick = () => {


				const selection = button.dataset.vote;
				//alert(selection)
				socket.emit('submit vote', {'selection':selection});
			};

		});
	});

	//when a new vote is announced, add to the unordered list
	socket.on('announce vote', data => {
		const li = document.createElement('li');
		li.innerHTML = `Vote recorded: ${data.selection}`;
		document.querySelector('#votes').append(li);

	});	
	
});	
