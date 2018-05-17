	function button_click() {
			document.querySelector('button').onclick = count;
			document.querySelectorAll('.buttonColor').forEach(function(button) {
				//arrow function
				button.onclick = () => {
					document.querySelector('#foo').style.color = button.dataset.color;
				};
			})
			document.querySelector('#dropdown').onchange = function(){
            	document.querySelector('#foo').style.color = this.value
			};
		};
		
		document.addEventListener('DOMContentLoaded', button_click	
		);
		

		function hello() {
			document.querySelector('h1').innerHTML = 'hello Hsin!!'
		}
        
		function show_content() {
			document.querySelector('#foo').innerHTML = 'Hola!'
		}

		let counter = 0
		function count() {
			
      		counter++

      		if (counter % 10 === 0) {
      			alert(`Counter is at ${counter}`);	
      		}

			document.querySelector('#cnt').innerHTML = counter

		}

	function add_task() {
    	const li = document.createElement('li')
    	li.innerHTML = document.querySelector('#task').value;
        document.querySelector('#tasks').append(li)
        return false
	};