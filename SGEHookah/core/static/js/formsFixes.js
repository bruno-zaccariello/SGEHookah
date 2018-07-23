$('body').on('keydown', 'input, select', function(e) {
    var self = $(this)
      , form = self.parents('form:eq(0)')
      , focusable
      , next
      ;
    if (e.keyCode == 13) {
        focusable = form.find('input,select, textarea').filter(':visible');
        next = focusable.eq(focusable.index(this)+1);
        if (next.length) {
            next.focus();
        } 
        return false;
    }
});

$('input').each(function () {
    $this = $(this);
    $label = $('label[for="'+ $this.attr('id') +'"]');
    if($this.prop('required')) {
        $label.addClass('required')
    }
});

$('.formInput').each(function () {
  if ($(this).find('ul.errorlist').length > 0) {
    $(this).find('input').addClass('error-active');
  } else {
    $(this).find('input').removeClass('error-active');
  }
})

// Para a pagina de alterar senha e info
$('.field').each(function () {
  if ($(this).find('ul.errorlist').length > 0) {
    $(this).find('input').addClass('error-active');
  } else {
    $(this).find('input').removeClass('error-active');
  }
})