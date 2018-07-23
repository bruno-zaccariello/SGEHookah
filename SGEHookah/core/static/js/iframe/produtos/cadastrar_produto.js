function readURL(input) {

  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function(e) {
      $('#foto_preview').attr('src', e.target.result);
      $('#label_ft_div').children('label').html('Alterar a foto');
    }

    reader.readAsDataURL(input.files[0]);
  }

}

$("#id_fotoproduto").change(function() {
  readURL(this);
});

$('.formInput').each(function () {
	if ($(this).find('ul.errorlist').length > 0) {
		$(this).find('input').addClass('error-active');
	} else {
		$(this).find('input').removeClass('error-active')
	}
})