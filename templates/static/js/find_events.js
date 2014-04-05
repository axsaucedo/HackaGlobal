var find_event = {
    init : function() {
        $('#find-event-search').tagit({ tagSource: window.availableTags, select: true, sortable: true});
        $('#find-event-search-btn').click(function(event) {
            var tags = getTags($('#find-event-search').tagit('tags'));
            $("#find-event-tags").attr("value", tags);
        });

        function getTags(tags) {
            var string = tags[0].value;
            for (var i in tags) {
                if (i == 0) continue;
                string += "," + tags[i].value;
            }
            return string.toLowerCase()
        }
    }
}

$(function() {
    find_event.init();
})