$('.turn').click(function () {
        var uploadedFile = $(".file").val();
        if (uploadedFile == "") {
            alert("Вы не выбрали файл");
        }
        else {
            var timer = $('.timer').val();
            setTimeout(function () {
                $('.form').submit();
            }, timer);
        }


    });
