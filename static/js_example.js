var form = document.getElementById('registration');
    form.onsubmit = function(){   //example of anonymous function
        name = form.name.value; // access element in the form
        email = form.email.value;
    	alert('Hello ---' + name);
        return false // Use this so the submittion will be stopped
    };