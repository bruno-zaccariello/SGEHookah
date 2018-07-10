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