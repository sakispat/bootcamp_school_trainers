'use strict';

// Create / Edit Form Trainer
window.addEventListener('load', function(){
    var forms = document.getElementsByClassName('needs-validation');
    var validation = Array.prototype.filter.call(forms, function(form){
        form.addEventListener('submit', function(e){
            if(form.checkValidity() === false){
                e.preventDefault();
                e.stopPropagation();
            }

            form.classList.add('was-validated');
        }, false);
    });
}, false);
