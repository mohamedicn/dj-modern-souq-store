
/* slider button */
let UlSlider = document.getElementById("ul-slider")

let UlSliderNUM = 0

function FnRight(){
  UlSliderNUM -= 150
    UlSliderNUM >= 0 ?  
    UlSlider.style.left = `${UlSliderNUM}px` : 
    UlSliderNUM = 0
}

function FnLeft(){
  UlSliderNUM += 150
  UlSliderNUM <= 600 ?  
  UlSlider.style.left = `${UlSliderNUM}px` : 
  UlSliderNUM = 600
}





document.addEventListener("DOMContentLoaded", function () {
  var buttons = document.querySelectorAll(".btn-js");
  buttons.forEach(function (button) {
      button.addEventListener("click", function () {
          var modalId = button.getAttribute("data-target");
          var modal = document.querySelector(modalId);
          var closeButton = modal.querySelector(".close");
          modal.style.display = "block";
          closeButton.addEventListener("click", function () {
              modal.style.display = "none";
          });
          window.addEventListener("click", function (event) {
              if (event.target === modal) {
                  modal.style.display = "none";
              }
          });
      });
  });
});