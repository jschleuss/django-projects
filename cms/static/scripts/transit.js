$(".deleted_button").click(function () {
    $(".filter_button").removeClass("active");
    $(this).addClass("active");
    $(".route").hide();
    $(".deleted").show();
});
$(".revised_button").click(function () {
    $(".filter_button").removeClass("active");
    $(this).addClass("active");
    $(".route").hide();
    $(".reduced").show();
});
$(".unchanged_button").click(function () {
    $(".filter_button").removeClass("active");
    $(this).addClass("active");
    $(".route").hide();
    $(".unchanged").show();
});
