var add_event = {
    init : function() {
        $("#find-location-button").bind("click", function lookupGeoData() {
            console.log("here");
            myGeoPositionGeoPicker({
                startAddress     : 'White House, Washington',
                returnFieldMap   : {
                    'add-event-form-lat' : '<LAT>',
                    'add-event-form-long' : '<LNG>',
                    'add-event-form-city' : '<CITY>',
                    'add-event-form-country' : '<COUNTRY>',
                    'add-event-form-zip' : ' <ZIP>',
                    'add-event-form-address' : '<ADDRESS>'
                }
            });
        });

        $('#end-datetime, #start-datetime').datetimepicker({
            format: 'dd/MM/yyyy hh:mm:ss',
            language: 'en-GB'
        });

        $('#add-event-tag-bar').tagit({ select:true, sortable: true });

        $('#add-event-form').submit(function(event) {
            var tags = getTags($('#add-event-tag-bar').tagit('tags'));
            $("#add-event-tags").attr("value", tags);

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
    add_event.init();
});