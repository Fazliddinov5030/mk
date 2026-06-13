(function(){
  document.addEventListener('DOMContentLoaded', function(){
    var authCard = document.querySelector('.auth-card');
    if (!authCard) return;
    var inputs = Array.from(document.querySelectorAll('.auth-page .form-input'));

    function anyFocused(){
      return inputs.some(function(i){ return document.activeElement === i; });
    }

    inputs.forEach(function(input){
      input.addEventListener('focus', function(){
        authCard.classList.add('is-focused');
      });
      input.addEventListener('blur', function(){
        // small timeout to allow focus to move between inputs
        setTimeout(function(){
          if (!anyFocused()) authCard.classList.remove('is-focused');
        }, 10);
      });
    });

    // If page loads with prefilled or autofilled value, lift card
    setTimeout(function(){
      if (inputs.some(function(i){ return i.value && i.value.length>0; })){
        authCard.classList.add('is-focused');
      }
    }, 50);
  });
})();
