document.addEventListener('DOMContentLoaded',function() {
	document.querySelector('button').onclick = count;
}
);


function hello() {
	document.querySelector('h1').innerHTML = 'hello Hsin!!'
};

function show_content() {
	document.querySelector('#foo').innerHTML = 'Hola!'
};

let counter = 0;
function count() {
	
		counter++

		if (counter % 10 === 0) {
			alert(`Counter is at ${counter}`);	
		}

	document.querySelector('#cnt').innerHTML = counter

}