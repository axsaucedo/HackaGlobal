var base_events = {
    init : function() {
        /*################### SETTING UP AJAX REQUESTS #################### */
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        var csrftoken = getCookie('csrftoken');

        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        $('#nav-find-event-search').tagit({ tagSource: window.availableTags, select: true, sortable: true});
        $('#nav-find-event-search-btn').click(function(event) {
            var tags = getTags($('#nav-find-event-search').tagit('tags'));
            $("#nav-find-event-tags").attr("value", tags);
        });

        function getTags(tags) {
            var string = tags[0].value;
            for (var i in tags) {
                if (i == 0) continue;
                string += "," + tags[i].value;
            }
            return string.toLowerCase()
        }

        $.ajaxSetup({
            crossDomain: false, // obviates need for sameOrigin test
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type)) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });

        // This Function Tells you the width of the value in an input box
        $.fn.textWidth = function () {
            $body = $('body');
            $this =  $(this);
            $text = $this.text();
            if($text=='') $text = $this.val();
            var calc = '<div style="clear:both;display:block;visibility:hidden;"><span style="width;inherit;margin:0;font-family:'  + $this.css('font-family') + ';font-size:'  + $this.css('font-size') + ';font-weight:' + $this.css('font-weight') + '">' + $text + '</span></div>';
            $body.append(calc);
            var width = $('body').find('span:last').width();
            $body.find('span:last').parent().remove();
            return width;
        };

        var nav_input = $('#nav-bar-hackaglobal-text-input');
        nav_input.css("width", nav_input.textWidth()+15);
        console.log(nav_input.val().length*10);
        nav_input.keydown(function(e) {
            //When the user presses enter
            if(e.which == 13) {
                var hackacity = nav_input.val();
                console.log(window.availableHackaCities.toString().toLowerCase().indexOf(hackacity.toLowerCase()))
                if (window.availableHackaCities.toString().toLowerCase().indexOf(hackacity.toLowerCase()) > -1)
                    window.location = "/hackacity/view/" + hackacity;
            }
        });

        nav_input.autocomplete({
            source: window.availableHackaCities,
            select: function(event, ui) {
                console.log(event, ui)
                window.location = "/hackacity/view/" + ui.item.value;
            },
            minLength: 0,
            minChars: 0,
            max: 12,
            autoFill: true,
            mustMatch: true,
            matchContains: false,
        }).on('focus', function(event) {
                var self = this;
                $(self).autocomplete( "search", "");
        });
    }
};

$(function() {
    base_events.init()
});