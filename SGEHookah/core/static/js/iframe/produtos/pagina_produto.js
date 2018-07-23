function readURL(input) {

  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function(e) {
			$('#foto_produto').hide();
      $('#foto_preview').attr('src', e.target.result);
			$('#foto_preview').show();
    }

    reader.readAsDataURL(input.files[0]);
  }
}

$("#id_fotoproduto").change(function() {
  readURL(this);
});

function clean() {
	$('#foto_produto').show();
  $('#foto_preview').hide();
}

$('#BtClean').click(function() {
	clean();
});