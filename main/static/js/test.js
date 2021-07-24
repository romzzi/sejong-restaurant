$(function(){
    $(".submit").click(function(e) {
        let radios = $('input[type=radio]:checked');
        if(radios.length < 4) {
            alert("문항이 선택되지 않았습니다.");
            return false;
        }
        return true;
    });
});