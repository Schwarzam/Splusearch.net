function save(objButton){

    const request = new XMLHttpRequest();
    var value = objButton.value;
    request.open('POST', 'save');

    request.onload = () => {
        const data1 = JSON.parse(request.responseText);
        alert('Saved!');
  }
    const data = new FormData();
    data.append('value', value);
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
    var value1 = String(value)
    data.append('value', value1);
    request.send(data);
    return false;
};
