var MateriaManager = {
    materias: [],
    invalids: 0,
    clear: function() {this.materias=[]},
    checar: function() {
        this.invalids = 0
        for (let i = 0; i < this.materias.length; i++) {
            let materia = this.materias[i]
            
            let materia_span = $('[id_materia='+materia.id+']').find('.materia_qtd')
            if (materia.estoque < $(materia_span).prop('quantidade')) {
                this.invalids += 1
                $('[id_materia='+materia.id+']').css({'background-color':'red', 'color':'red'})
            } else {
                $('[id_materia='+materia.id+']').css({'background-color':'green', 'color':'green'})
            }
        }
        this.toggleButton()
    },
    toggleButton: function() {
        if (this.invalid_count > 0) {
            $('#submitButton').prop('disabled', true)
            $('#submitButton').removeClass('btConfirmar')
            $('#submitButton').addClass('btCancelar')
        } else {
            $('#submitButton').prop('disabled', false)
            $('#submitButton').removeClass('btCancelar')
            $('#submitButton').addClass('btConfirmar')
        }
    },
}

$(document).ready(function() {
    get_materias($('#id_fkid_formula').val())
    MateriaManager.checar();
    alterar_quantidade($('#id_quantidade').val());
})

function get_materias(id) {
    if (!['', null, NaN, undefined].includes(id)) {

        getAPI(
            `/api/valida_fabricacao/${id}`,
            function(data){
                $('#materias').empty()

                r = data
                MateriaManager.materias = r.materias
                for (var i = 0; i < r.materias.length; i++) {
                    let multiplicador = parseFloat($('#id_quantidade').val())

                    let id = r.materias[i].id
                    let materia = r.materias[i].materia
                    let quantidade = (multiplicador) ? 
                        r.materias[i].quantidade * multiplicador : r.materias[i].quantidade
                    let unidade = r.materias[i].unidade

                    $('#materias').append(
                        "<tr id_materia='"+id+"'>\
                            <td>"+materia+"</td>\
                            <td>\
                                <span class='materia_qtd' quantidade="+quantidade+">"+quantidade+"</span> "+unidade+"\
                            </td>\
                        </tr>"
                    )
                }
            },
        )

    }
}

function alterar_quantidade(valor) {
    for (let j = 0; j < MateriaManager.materias.length; j++) {
        let materia = MateriaManager.materias[j];
        let materia_span = $('[id_materia='+materia.id+']').find('.materia_qtd');
        
        let total = materia.quantidade * valor
        $(materia_span).text(total)
        $(materia_span).prop('quantidade', total)
    }
    MateriaManager.checar()
}

$('#id_fkid_formula').change(function() {
    get_materias($(this).val());
    MateriaManager.checar();
})

$('#id_quantidade').change(function() {
    alterar_quantidade($(this).val());
})