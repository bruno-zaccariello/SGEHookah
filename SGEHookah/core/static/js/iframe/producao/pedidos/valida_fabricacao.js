$(document).ready(function() {
    buscar_materias($('#id_fkid_formula').val())
    alterar_quantidade($('#id_quantidade').val())
})

function checa_materias() {

    var ids = []
    
    $('[id_materia]').each(function() {

        var id_materia = parseInt($(this).attr('id_materia'))
        var quantity = parseInt($(this).find('span[original]').text())

        ids.push([id_materia, quantity])
    })

    $.ajax({
        method: "POST",
        url: "/api/checa_materias/",
        data: JSON.stringify({materias_ids: ids}),
        success: function(data) {

            r = JSON.parse(JSON.stringify(data))
            var r_data = r.checks
            
            var invalid_count = 0
            for (var i = 0; i < r_data.length; i++) {
                if (r_data[i][1]) {
                    $('[id_materia='+r_data[i][0]+']').css({'background-color':'green', 'color':'green'})
                } else {
                    $('[id_materia='+r_data[i][0]+']').css({'background-color':'red', 'color':'red'})
                    invalid_count++
                }
            }

            if (invalid_count > 0) {
                $('#submitButton').prop('disabled', true)
                $('#submitButton').removeClass('btConfirmar')
                $('#submitButton').addClass('btCancelar')
            } else {
                $('#submitButton').prop('disabled', false)
                $('#submitButton').removeClass('btCancelar')
                $('#submitButton').addClass('btConfirmar')
            }
            
        } 
    })

}

function buscar_materias(id) {
    $.ajax({
        method: "GET",
        url: "/api/nova_fabricacao/",
        data: {formula_id: id},
        success: function(data){ 
            
            $('#materias').empty()

            r = JSON.parse(JSON.stringify(data))

            for (var i = 0; i < r.lista.length; i++) {

                var materia = r.lista[i][0].fkid_materiaprima_id
                var quantidade = r.lista[i][0].quantidade
                var unidade = r.lista[i][0].unidade_id

                $('#materias').append(
                    "<tr id_materia='"+r.lista[i][1]+"'>\
                        <td>"+materia+"</td>\
                        <td>\
                            <span class='materia_qtd' original="+quantidade+">"+quantidade+"</span> "+unidade+"\
                        </td>\
                    </tr>"
                )
            }
        }
    }).then(function() {
        alterar_quantidade($('#id_quantidade').val())
    })
}

function alterar_quantidade(valor) {
    var multiplicador = valor

    $('.materia_qtd').each(function() {
        var valor = parseInt($(this).attr('original'))
        var total = multiplicador * valor
        
        $(this).text(total)
    })
    checa_materias()
}

$('#id_fkid_formula').change(function() {
    buscar_materias($(this).val());
})

$('#id_quantidade').change(function() {
    alterar_quantidade($(this).val());
})



function getCookie(name)
{
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?

            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$.ajaxSetup({ 
    beforeSend: function(xhr, settings) {
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    } 
});