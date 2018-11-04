function updatePreco(id, row) {
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