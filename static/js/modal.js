$('#qs_button').click(function () {
    $('#quesModal').show();
});

$('#set_button').click(function () {
    $('#settingModal').show();
});

var quesModal = document.getElementById('quesModal');
var setModal = document.getElementById('settingModal');

window.onclick = function (event) {
    if (event.target == quesModal || event.target == setModal) {
        quesModal.style.display = "none";
        setModal.style.display = "none";
    }
};