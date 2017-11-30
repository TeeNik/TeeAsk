var inProgress = false;
var startFrom = 5;
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
            //data = jQuery.parseJSON(data);
            console.log(data);
            if (data.length > 0) {
                for(let i = 0; i < data.length; i++){
                    let inf = data[i];
                    let $post = $('#post_id-24').clone();
                    $post.attr('id', 'post_id-'+inf.id);
                    $post.find('#title').text(inf.title);
                    $post.find('#title').attr('href', '/question/'+inf.id);
                    $post.find('#user_anchor').text(inf.author);
                    $post.find('#post-text').text(inf.text);
                    $('#thread').append($post);
                }

                inProgress = false;
                startFrom += 4;
            }
        });
    }
});