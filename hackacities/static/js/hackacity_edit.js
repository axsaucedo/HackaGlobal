var hackacity_view = {
    init: function() {
        $('[rel="popover"]').popover();

        var hackacity_info = $('#edit-hackacity-info');

        var add_sponsor_form = $('#add-sponsor-form');

        add_sponsor_form.live('submit', function(event) {
            event.preventDefault();
            $(this).ajaxSubmit({
                success: function(res) {
                    if(res.error) {
                        console.log(res.error)
                        add_sponsor_form.append('<legend id="add_sponsor_error" class="col-md-3 error" style="color:red;font-size:1em">Not Valid</legend>')
                        add_sponsor_form.children('input').css('border-color','red');
                        setTimeout(function(){
                            add_sponsor_form.children('input').css('border-color','black');
                            $('#add_sponsor_error').remove();
                        }, 1500);
                        return
                    } else {
                        var hc = res.hc;
                        $('#edit-hackacity-sponsors').append(
                                    '<li data-container_id="'+ hc.id +'">'
                                +       '<nav>'
                                +           '<a href="#" class="remove-sponsor-button">X</a>'
                                +       '</nav>'
                                +       '<a href="'+hc.url+'"><img class="picture" src="'+hc.photo+'"/></a>'
                                +   '</li>'
                            )
                    }
                },
                error: function(err) {
                    console.log("Error");
                    console.log(err);
                }
            })
        });

        $('.remove-sponsor-button').on('click', function(event) {
            event.preventDefault();

            var sponsor = $(this).closest('li');
            var container_id = sponsor.attr('data-container_id');

            $.ajax({
                url: hackacity_info.attr('data-remove_container_url'),
                dataType: 'json',
                type: 'POST',
                data: {
                    container_id: container_id
                },
                success: function(res) {
                    console.log(res);
                    sponsor.remove();
                },
                error: function(err) {
                    console.log("Error");
                    console.log(err);
                }
            })
        });

    }
}

$(function() {
    hackacity_view.init();
});
