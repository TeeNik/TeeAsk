$('#qs_button').click(function () {
    $('#quesModal').show();
});

$('#set_button').click(function () {
    $('#settingModal').show();
});

var quesModal = document.getElementById('quesModal');
window.onclick = function (event) {
    if (event.target == quesModal) {
        quesModal.style.display = "none";
    }
};

var setModal = document.getElementById('settingModal');
window.onclick = function (event) {
    if (event.target == setModal) {
        setModal.style.display = "none";
    }
};

