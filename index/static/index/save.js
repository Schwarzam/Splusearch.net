function save(objButton){
  
    const request = new XMLHttpRequest();
    var value = objButton.value;
    request.open('POST', 'save');

    request.onload = () => {
        const data1 = JSON.parse(request.responseText);
        objButton.innerHTML = 'Saved!';
  }
    const data = new FormData();
    var value1 = String(value);
    data.append('value', value1);
    request.send(data);
    return false;
};

function deletar(objButton){

    const request = new XMLHttpRequest();
    const value = objButton.value;
    request.open('POST','delete');

    request.onload = () => {
        const data1 = JSON.parse(request.responseText);
        location.reload();
  }
    const data = new FormData();
    var value1 = String(value);
    data.append('value', value1);
    request.send(data);
    return false;
};

/* When the user scrolls down, hide the navbar. When the user scrolls up, show the navbar */
var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("navbar").style.top = "0";
  } else {
    document.getElementById("navbar").style.top = "-80px";
  }
  prevScrollpos = currentScrollPos;
}

function searchfromprof(objButton){

    const request = new XMLHttpRequest();
    const value = objButton.value;
    request.open('POST','searchfromprof');

    request.onload = () => {
  }
    const data = new FormData();
    var value1 = String(value)
    data.append('value', value1);
    request.send(data);
    return false;
};
