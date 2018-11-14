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

// Função para atualizar preço e estoque após selecionar
// o produto no combo box
function updateProductData(id, row) {
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
                ).trigger('change')
                let quantidade = $(row).find('[name*=quantidade]')
                $(quantidade).prop('estoque', data[0]['fields']['totalestoque'])
                checkStock(quantidade)
            }
            )
    }
}

function updateSaleTotal() {
    let total = 0
    $('[name*=vl_total]').each(function() {
        total += parseFloat(this.value)
    })
    if (['', NaN, null].includes(total)) { total = 0 }
    $('#saleTotal').text((total).toFixed(2))
}

// Essa função não permite salvar o formulário caso haja
// alguma invalidez (como produto sem estoque)
function validateForm() {
    updateSaleTotal();
    let sendBt = $('button[type=submit]');
    let existProduct = false
    $('[name*=quantidade]').each(function() {
        if (!checkStock(this)) {
            $(sendBt).prop('disabled', true)
        } else { $(sendBt).prop('disabled', false) }
    })
}

function checkStock(field) {
    let estoque = $(field).prop('estoque');
    let quantidade = $(field).val();
    if (quantidade > estoque || quantidade <= 0) {
        $(field).addClass('warning');
        return false
    } else {
        $(field).removeClass('warning');
        return true
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
    updateProductData(this.value, row);
    validateForm();
})

$('[name*=quantidade]').on('keyup change',function() {
    let row = $(this).parent().parent();
    let multiplier = this.value
    let unit = $(row).find('[name*=vl_unitario]').val()
    $(row).find('[name*=vl_total]').val(
        (multiplier*unit).toFixed(2)
    )
    checkStock(this);
    validateForm();
})

$('[name*=vl_unitario]').on('keyup change', function() {
    let row = $(this).parent().parent();
    let multiplier = $(row).find('[name*=quantidade]').val()
    let unit = this.value
    $(row).find('[name*=vl_total]').val(
        (multiplier*unit).toFixed(2)
    )
    validateForm()
})

$('#id_pago').click(function() {
    checkPagamento();
    validateForm();
})

$('button[type=reset]').click(function() {
    setTimeout(function() {
        updateSaleTotal();
        validateForm();
    }, 50)
})