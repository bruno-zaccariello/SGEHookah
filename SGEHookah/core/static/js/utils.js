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


    function scroll(elem) {
        $(elem).animate({
            scrollTop: amount
        }, 100, 'linear', function() {
            if (amount != '') {
                if ($(elem).scrollTop() == 0) {
                    amount = ''
                }
                scroll(elem);
            }
        })    
    }

    $('.self-scroller').hover(function() {
        amount =  '+=5';  
        scroll(this);
    }, function() {
        amount = '-=5';
    })
    $('.self-scroller').mouseleave(function() {
        if (amount != '') {
            amount = '-=100';
            scroll(this);
        } else {
            amount = '';
        }
    })

})

function confirmaJanelaOn(url) {
	var telaConfirma = document.getElementById("overlay");
	var bt_confirma = document.getElementById("bt_confirma");
	if(telaConfirma) {
		telaConfirma.style.display = "block";
		bt_confirma.href = url;
	}
}