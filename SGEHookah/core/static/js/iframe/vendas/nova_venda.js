$('[name*=fkid_produto]').on('change', function(){
    let row = $(this).parent().parent();
    postAPI(
        '/api/search_produto/',
        {'produto':this.value},
        function(data) {
            data = JSON.parse(data);
            $(row).prop('prodid', data[0]['pk']);
            updatePreco(id = $(row).prop('prodid'), row);
        }
    )
    
})

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