document.addEventListener('DOMContentLoaded', () => {
	document.querySelector('#form').onsubmit = () => {
		 //initialize new request
		 const request = new XMLHttpRequest();
		 const currency = document.querySelector('#currency').value.toUpperCase();
		 request.open('POST', '/convert');
        
		 //Then the callback function when request compeltes
		 request.onload = () => {
		 	
		 	// extract json data from request
		 	res_data = JSON.parse(request.responseText);

		 	//then update the result div in dom
		 	if (res_data.success) {
		 		const contents = `1 USD is equal to ${res_data.rate} ${currency}`;
				document.querySelector('#result').innerHTML = contents;
			}
			else {
				querySelector('#result').innerHTML = "There was an error"

			}
		 }

		 //create the form data for currency so you can pass it to /convert
		 const data = new FormData();
		 data.append('currency', currency);//append(key, value)

		 //is this reflect? send request along with the form data you want to pass
		 request.send(data);
		 return false;	
		 }
		}
	)