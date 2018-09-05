$(function () {
    //模态框确认按钮
    $(".delete-link").click(function () {
        var url = $(this).attr('href');
        $("#del-success").attr("href", url)
    });

    $(document).click(function () {
        $("#error-hint").attr('class', 'hide')
    })
});
