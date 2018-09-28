var options =  {
  onKeyPress: function(options) {
    $('#id_cep').mask('00000-000', options);
}};

$('#id_cep').mask('00000-000', options);

var options2 =  {
  onKeyPress: function(options) {
    $('#id_cpf_cnpj').mask('000.000.000-00', options2);
}};

$('#id_cpf_cnpj').mask('000.000.000-00', options2);

var options3 =  {
  onKeyPress: function(options) {
    $('#id_numero').mask('(00)00000-0000', options3);
}};

$('#id_numero').mask('(00)00000-0000', options3);

function limpa_formulário_cep(logradouro, bairro, cidade) {
    $("#id_logradouro").val(logradouro);
    $("#id_bairro").val(bairro);
    $("#id_cidade").val(cidade);
}

$("#id_cep").blur(function() {

                var cep = $(this).val().replace('-', '');

                if (cep != "") {

                    //Expressão regular para validar o CEP.
                    var validacep = /^[0-9]{8}$/;

                    //Valida o formato do CEP.
                    if(validacep.test(cep)) {

                        //Preenche os campos com "..." enquanto consulta webservice.
                        
                        var old_logradouro = $("#id_logradouro").val()
                        var old_bairro = $("#id_bairro").val()
                        var old_cidade = $("#id_cidade").val()
                        
                        $("#id_logradouro").val("...");
                        $("#id_bairro").val("...");
                        $("#id_cidade").val("...");

                        $.getJSON("https://viacep.com.br/ws/"+ cep +"/json/?callback=?", function(dados) {

                            if (!("erro" in dados)) {
                                //Atualiza os campos com os valores da consulta.
                                $("#id_logradouro").val(dados.logradouro);
                                $("#id_bairro").val(dados.bairro);
                                $("#id_cidade").val(dados.localidade);
                                $("#id_uf option[value="+dados.uf+"]").attr('selected', 'selected');
                                 $('#CEP_errors').html('');
                            } //end if.
                            else {
                                //CEP pesquisado não foi encontrado.
                                limpa_formulário_cep(old_logradouro, old_bairro, old_cidade);
                                $('#CEP_errors').html("<ul class='errorlist'><li>CEP não encontrado.</li></ul>");
                            }
                        });
                    } //end if.
                    else {
                        //cep é inválido.
                        limpa_formulário_cep(old_logradouro, old_bairro, old_cidade);
                        $('#CEP_errors').html("<ul class='errorlist'><li>Formato de CEP inválido.</li></ul>");
                    }
                } //end if.
                else {
                    //cep sem valor, limpa formulário.
                    limpa_formulário_cep(old_logradouro, old_bairro, old_cidade);
                     $('#CEP_errors').html('');
                }
            showErrors($(this).parent());
            });