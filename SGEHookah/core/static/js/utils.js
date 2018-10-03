$(document).ready(function() {
    
    var $botao = document.querySelector("button[type=submit]")
    if ($botao) {
        $botao.addEventListener("click",
        function() {
            $botao = this;
            $($botao).closest("form").submit()
            $botao.disabled = true;
            setTimeout(function() {$botao.disabled=false},2000)
        })
    }
})