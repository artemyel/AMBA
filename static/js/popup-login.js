$(document).ready(function () {
    PopUpHide();
    $('.b-popup').click(function (e) {
        var target = e.target;
        if (jQuery(target).is('.b-popup')) {
            PopUpHide();
        }
    })
});

function PopUpShow() {
    $("#popup1").show()
}

function PopUpHide() {
    $("#popup1").hide()
}
