var view_event = {
    init : function() {
        event_info = $("#view-event-info");

        $(document).on('click', '.attendee-btn', function() {
            var that = $(this);
            var attendee_type = that.attr("data-attendee_type");
            var username = event_info.attr("data-user_username");
            var firstname = event_info.attr("data-user_firstname");
            var lastname = event_info.attr("data-user_lastname");

            console.log(attendee_type);

            $.ajax({
                url: event_info.attr("data-attend-event_url"),
                dataType: "json",
                type: "POST",
                data: {
                    event_id: event_info.attr('data-event_id'),
                    attendee_type : attendee_type
                },
                success: function(res) {
                    if (!res.error) {
                        if(attendee_type != "") {
                            var unattend_buttons = $('<div style="padding-bottom: 30px;" class="row"><div data-delete_attendee_type="' + attendee_type + '" data-attendee_type="" class="attendee-btn btn btn-primary col-md-5 col-md-offset-3">Stop '+ (attendee_type == 'A' ? 'attending' : 'tracking') +'</div></div>')
                            that.parent().replaceWith(unattend_buttons);

                            var count = attendee_type == 'A' ? $('#event-attendee-count') : $('#event-tracker-count');
                            count.text(parseInt(count.text()) + 1);

                            var container = attendee_type == 'A' ? $('#event-attendees-container') : $('#event-trackers-container');

                            if (container.length <= 0) {
                                var attendees_container;
                                if (attendee_type == 'A'){
                                    attendees_container = '<div class="row"><h4>Attendees</h4><div id="event-attendees-container"></div></div>';
                                } else {
                                    attendees_container = '<div class="row"><h4>Trackers</h4><div id="event-trackers-container"></div></div>';
                                }
                                $('#all-attendees-container').prepend(attendees_container);
                                var container = attendee_type == 'A' ? $('#event-attendees-container') : $('#event-trackers-container');
                            }

                            var new_attendee = '<div class="col-md-2 well"><a href="/accounts/'+username+'/">'+firstname + ' ' + lastname+'</a></div>';
                            console.log(container);
                            console.log(new_attendee);
                            container.prepend(new_attendee);


                        } else {
                            var attend_buttons = $('<div style="padding-bottom: 30px;" class="row"><div data-attendee_type="A" class="attendee-btn btn btn-success col-md-4 col-md-offset-1">Attend</div><div data-attendee_type="T" class="attendee-btn btn btn-danger col-md-4 col-md-offset-1">Track</div></div>')
                            that.parent().replaceWith(attend_buttons);
                            var delete_attendee_type = that.attr("data-delete_attendee_type");

                            var count = delete_attendee_type == 'A' ? $('#event-attendee-count') : $('#event-tracker-count');
                            count.text(parseInt(count.text()) - 1);

                            var container = delete_attendee_type == 'A' ? $('#event-attendees-container') : $('#event-trackers-container');
                            container.find("div:first").remove();
                        }
                    }
                }
            });
        });
    }
};

$(function() {
    view_event.init();
});

