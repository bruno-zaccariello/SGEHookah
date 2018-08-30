$('#id_fkid_formula').change(function() {

    $.ajax({
        method: "GET",
        url: "/js/nova_fabricacao/",
        data: {pedido_id: $(this).val()},
        async: false,
        success: function(data){ 
            
            $('#materias').empty()

            r = JSON.parse(JSON.stringify(data))

            for (var i = 0; i < r.lista.length; i++) {

                var materia = r.lista[i].fkid_materiaprima_id
                var quantidade = r.lista[i].quantidade
                var unidade = r.lista[i].unidade_id

                $('#materias').append(
                    "<tr>\
                        <td>"+materia+"</td>\
                        <td>\
                            <span class='materia_qtd' original="+quantidade+">"+quantidade+"</span> "+unidade+"\
                        </td>\
                    </tr>"
                )
            }
        }
    })

})

$('#id_quantidade').change(function() {
    var multiplicador = $(this).val()

    $('.materia_qtd').each(function() {
        var valor = parseInt($(this).attr('original'))
        var total = multiplicador * valor
        
        $(this).text(total)
    })

})