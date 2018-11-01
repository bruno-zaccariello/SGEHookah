$('[name*=fkid_produto]').on('change', function(){
    let id = 1
    let row = $(this).parent().parent()
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
})