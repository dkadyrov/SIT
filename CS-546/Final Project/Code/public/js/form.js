(function ($) {
    $('#dbType').on('change', function () {
        if ($(this).val() === "other") {
            $("#otherType").show()
        } else {
            $("#otherType").hide()
        }
    });
})(jQuery)