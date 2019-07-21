window.onload = function () {
    $('.basket_list').on('change', 'input[type="number"]', function () {
        var t_href = event.target;
        
        $.ajax({
            url: "/basket/edit/" + t_href.name + "/" + t_href.value + "/",
                
            success: function (data) {
                $('.basket_list').html(data.result)
            }
        });

        event.preventDefault();
    });
    $('.basket_list').on('click', '#remove', function () {
        var t_href = event.target;
        
        $.ajax({
            url: t_href.href,
                
            success: function (data) {
                $('.basket_list').html(data.result);
            },
        });

        event.preventDefault();
    });   
}