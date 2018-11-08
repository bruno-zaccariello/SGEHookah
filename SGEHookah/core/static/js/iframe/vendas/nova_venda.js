var input

$(document).ready(function() {

    $('[name*=fkid_produto]').attr('select2', 'True').select2({
        width: '200px'
    });
    
    $('[name=fkid_cliente]').select2().parent().find(
        'span:first'
    ).removeAttr('style');

    $('#id_pago').parent().css({'width':'10%', 'margin':'0 0 auto auto'})
    $('#id_pago').parent().parent().css('text-align', 'right')
    checkPagamento();

})

function updatePreco(id, row) {
    if (!id) {
        $(row).find('[name*=vl_unitario]').val(0)
    } else {
        postAPI(
            '/api/get_produto/',
            {'produto':id},
            function(data) {
                data = JSON.parse(data)
                $(row).find('[name*=vl_unitario]').val(
                    data[0]['fields']['preco']
                )
            }
            )
    }
}

function checkPagamento() {
    if ($('#id_pago').prop('checked')) {
        $('#id_dt_pagamento').prop('disabled', false);
    } else {
        $('#id_dt_pagamento').prop('disabled', true);
    }
}

$('[name*=fkid_produto]').on('change', function(){
    let row = $(this).parent().parent();
    updatePreco(this.value, row);
})

$('[name*=quantidade]').keyup(function() {
    let row = $(this).parent().parent();
    let multiplier = this.value
    let unit = $(row).find('[name*=vl_unitario]').val()
    $(row).find('[name*=vl_total]').val(
        (multiplier*unit).toFixed(2)
    )
})

$('[name*=vl_unitario]').keyup(function() {
    let row = $(this).parent().parent();
    let multiplier = $(row).find('[name*=quantidade]').val()
    let unit = this.value
    $(row).find('[name*=vl_total]').val(
        (multiplier*unit).toFixed(2)
    )
})

$('#id_pago').click(function() {
    checkPagamento();
})

var tomate = 0;
console.log(tomate)