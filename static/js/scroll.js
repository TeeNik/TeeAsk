var inProgress = false;
var startFrom = 1;
$(window).scroll(function () {
    if ($(window).scrollTop() + $(window).height() >= $(document).height() - 100 && !inProgress) {
        $.ajax({
            url: '/load/',
            method: 'get',
            data: {"start": startFrom},
            beforeSend: function () {
                inProgress = true;
            }
        }).done(function (data) {
            data = jQuery.parseJSON(data);
            console.log(data);
            /*if (data.length > 0) {
                $.each(data, function (index, data) {

                    let post = $('#post_id-1').clone();
                    post.setAttribute('id', 'post_id-'+data.id);
                    $(post).find('#title').text(data.title);
                    $(post).find('#title').setAttribute('href', '/question/'+data.id);
                    $(post).find('post-text').text(data.text);
                    $('center').appendChild(post);
                });

                inProgress = false;
                startFrom += 10;
            }*/
        });
    }
});