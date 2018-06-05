var options =  {
  onKeyPress: function(options) {
    $('#id_cep').mask('00000-000', options);
}};

$('#id_cep').mask('00000-000', options);

var options2 =  {
  onKeyPress: function(options) {
    $('#id_cpf_cnpj').mask('000.000.000-00', options);
}};

$('#id_cpf_cnpj').mask('000.000.000-00', options);