$('#qs_button').click(function () {
    $('#myModal').show();
});

var modal = document.getElementById('myModal');
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}