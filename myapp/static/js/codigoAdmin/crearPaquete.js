document.getElementById('addImageField').addEventListener('click', function() {
    var container = document.getElementById('imageUploadContainer');
    if(container.getElementsByTagName('input').length < 5) {
      var input = document.createElement('input');
      input.type = 'file';
      input.className = 'form-control mb-2';
      input.name = 'packageImages[]';
      input.accept = 'image/*';
      container.appendChild(input);
    } else {
      alert('Máximo 5 imágenes.');
    }
  });
  
  document.getElementById('addServiceField').addEventListener('click', function() {
    var container = document.getElementById('includedServicesContainer');
    if(container.getElementsByTagName('input').length < 10) {
      var div = document.createElement('div');
      div.className = 'input-group mb-3';
      var input = document.createElement('input');
      input.type = 'text';
      input.className = 'form-control';
      input.placeholder = 'Servicio';
      div.appendChild(input);
      container.appendChild(div);
    } else {
      alert('Máximo 10 servicios.');
    }
  });
  