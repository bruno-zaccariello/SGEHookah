function Prefix() {
    return $($('[name*="set-"]')[0]).prop("name").split("-")[0];
}

function updateElementIndex(el, prefix, ndx) {
    var id_regex = new RegExp('(' + prefix + '-\\d+)');
    var replacement = prefix + '-' + ndx;
    if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex, replacement));
    if (el.id) el.id = el.id.replace(id_regex, replacement);
    if (el.name) el.name = el.name.replace(id_regex, replacement);
}

function cloneMore(selector, prefix) {
    var newElement = $(selector).clone(true);
    var total = $('#id_' + prefix + '-TOTAL_FORMS').val();
    newElement.show()
    newElement.find(':input').each(function() {
        var name = $(this).attr('name').replace('-' + (total-1) + '-', '-' + total + '-');
        var id = 'id_' + name;
        $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
    });
    total++;
    $('#id_' + prefix + '-TOTAL_FORMS').val(total);
    $(selector).after(newElement);
}

function deleteForm(prefix, btn) {
    var total = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
    if (total > 1){
        btn.closest('.form-row').hide();
        btn.parent().find('input[type=checkbox]').prop('checked', true)
        var forms = $('.form-row');
        $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
        for (var i=0, formCount=forms.length; i<formCount; i++) {
            $(forms.get(i)).find(':input').each(function() {
                updateElementIndex(this, prefix, i);
            });
        }
    }
    return false;
}

$(document).on('click', '.add-form-row', function(e){
    e.preventDefault();
    cloneMore('.form-row:last', Prefix());
    return false;
});

$(document).on('click', '.remove-form-row', function(e){
    e.preventDefault();
    deleteForm(Prefix(), $(this));
    return false;
});

$('tr:not(:first-child):not(:last-child) td:last-child').append(
    "<div title='remover linha' class='opt_bt opt_delete remove-form-row'></div>"
    )

$('input[type=checkbox]').hide()