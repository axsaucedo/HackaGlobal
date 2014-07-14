var hackacity_view = {
    init: function() {
        $('[rel="popover"]').popover();

        var hackacity_info = $('#edit-hackacity-info');
        var hackacity = hackacity_info.attr('data-hackacity');
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
                error: function(error) {
                    console.log("Error");
                    console.log(error);
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
                    if(res.error) {
                        return
                    } else {
                        sponsor.remove();
                    }
                },
                error: function(error) {
                    console.log("Error");
                    console.log(error);
                }
            })
        });

        $('.add-team-btn').on('click', function(event) {
            var username = $('.add-team-input-username').val();

            console.log(username);

            $.ajax({
                url: hackacity_info.attr('data-add_team_url'),
                dataType: 'json',
                type: 'POST',
                data: {
                    username: username,
                    hackacity: hackacity
                },
                success: function(res) {
                    console.log(res);
                    if(res.error) {
                        $('.add-team-form-container').append('<div id="add-team-error" style="color: red">Could not add team member.</div>');
                        setTimeout(function() { $('#add-team-error').remove() }, 2000);
                        return
                    } else {
                        var team_member = res.team;
                        $('.team-container').append(
                                '<li data-team_username="'+team_member.username+'">'
                            +       '<nav>'
                            +           '<a href="/accounts/view/'+team_member.username+'">X</a>'
                            +       '</nav>'
                            +       '<div class="picture"><img src="'+team_member.photo+'"></div>'
                            +       '<h2>'+team_member.name+'</h2>'
                            +   '</li>'
                        )
                    }
                },
                error: function(error) {
                    console.log("Error");
                    console.log(error);
                    $('.add-team-form-container').append('<div id="add-team-error" style="color: red">Could not add team member.</div>');
                    setTimeout(function() { $('#add-team-error').remove() }, 2000);
                    return
                }
            })
        });

        $('.remove-team-btn').on('click', function(event) {
            event.preventDefault();


            var user = $(this).closest('li');
            var username = user.attr('data-team_username');

            $.ajax({
                url: hackacity_info.attr('data-remove_team_url'),
                dataType: 'json',
                type: 'POST',
                data: {
                    username: username,
                    hackacity: hackacity
                },
                success: function(res) {
                    if(res.error) {
                        console.log("Error");
                        console.log(error);
                        $('.add-team-form-container').append('<div id="add-team-error" style="color: red">Could not remove team member.</div>');
                        setTimeout(function() { $('#add-team-error').remove() }, 2000);
                    } else {
                        user.remove();
                    }
                },
                error: function(error) {
                    console.log("Error");
                    console.log(error);
                    $('.add-team-form-container').append('<div id="add-team-error" style="color: red">Could not remove team member.</div>');
                    setTimeout(function() { $('#add-team-error').remove() }, 2000);
                }
            })
        })

    }
}

$(function() {
    hackacity_view.init();
});
