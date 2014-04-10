
/* CONFIG */
var apiURL = window.base_url;

var map;
var hgCountries = [],
    hgCountriesMetadata = [],
    hgBody = document.getElementById('hg-body'),
    hgOverlay = document.getElementById('hg-overlay');

var markersArray = [];
var mainURL = window.location.href;

$(document).on('ready',function(){
    console.log(apiURL);
    createMap();
});


function capitaliseFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}// end capitaliseFirstLetter()


function apiGetCountries() {
    var xhr = new XMLHttpRequest();

    xhr.open('GET', apiURL + '/api/country/', true);

    xhr.onload = function() {
        hgCountries = JSON.parse(xhr.responseText);

        populateMap();
    }// end xhr.onload()

    xhr.error = function() {
        console.log('could not get the coutries list from the API');
    }// end xhr.error()

    xhr.send();
}// end apiGetCountries()


function apiGetEvents(country) {
    var xhr = new XMLHttpRequest(),
        container = document.getElementById('hg-list-wrapper');

    xhr.open('GET', apiURL + '/api/data/' + country, true);
    xhr.onload = function() {
        var rsp = JSON.parse(xhr.responseText),
            n,
            i,
            html = [];

        console.log(rsp);

        if (rsp) {
            n = rsp.length;

            if (n > 0) {
                html.push('<div class="hg-list-date-container">April 04 &middot; Friday</div>');
                html.push('<ul class="hg-list-ul">');
                console.log(rsp);
                for (i = 0; i < n; i++) {
                    html.push('<li class="hg-list-item-container">' +
                        '<div class="hg-list-item-left"><div class="hg-list-item-title-container">'+
                        '<a class="hg-list-item-title" href="#" target="_blank">' + rsp[i].name + '</a>' +
                        '</div><div class="hg-list-item-location">' + rsp[i].address + ' &middot;' +
                        ' organizer ' + rsp[i].creator + '</div>' +
                        '<div class="hg-list-item-info">' + rsp[i].description + '...</div></div>' +
                        '<div class="hg-list-item-right">' + rsp[i].start + '</div></li>');
                }// end for

                html.push('</ul>');

                container.className = container.className.replace(' hg-loader', '');
                container.innerHTML = html.join('');

            } else {
                // no event found

            }// end else

        } else {
            // no events found

        }// end else


    }// end xhr.onload()

    xhr.error = function() {
        console.log('could not get the coutries list from the API');
    }// end xhr.error()

    xhr.send();
}// end apiGetEvents()


function apiEvent(){
    var xhr = new XMLHttpRequest();
}

// get the countries from the API
apiGetCountries();

function makeCountryCall() {
    $.ajax({
        url: apiURL + '/api/country/',
        type: 'GET',
        crossDomain: true,
        dataType: 'json',

        success: function (data) {
            console.log(data);
            createMap(data);
        },
        error: function (response) {
            //console.log('error');
        }
    });
}

function createMap(data) {

    if ($('#googleMap').length > 0) {

        var rand = Math.random();

        //Normal theme
        var style;
//        //Dark theme
//        if (rand < .3) style = [{"featureType":"all","stylers":[{"visibility":"off"}]},{featureType: "administrative.country",elementType: "labels","stylers": [ {visibility: "on"} ]},{"featureType":"water","stylers":[{"visibility":"on"},{"lightness":-100}]}];
//        //White theme
//        else if(rand < .6) style = [{"featureType":"administrative","stylers":[{"visibility":"off"}]},{featureType: "administrative.country",elementType: "labels","stylers": [ {visibility: "on"} ]},{"featureType":"poi","stylers":[{"visibility":"simplified"}]},{"featureType":"road","stylers":[{"visibility":"simplified"}]},{"featureType":"water","stylers":[{"visibility":"simplified"}]},{"featureType":"transit","stylers":[{"visibility":"simplified"}]},{"featureType":"landscape","stylers":[{"visibility":"simplified"}]},{"featureType":"road.highway","stylers":[{"visibility":"off"}]},{"featureType":"road.local","stylers":[{"visibility":"on"}]},{"featureType":"road.highway","elementType":"geometry","stylers":[{"visibility":"on"}]},{"featureType":"road.arterial","stylers":[{"visibility":"off"}]},{"featureType":"water","stylers":[{"color":"#5f94ff"},{"lightness":26},{"gamma":5.86}]},{},{"featureType":"road.highway","stylers":[{"weight":0.6},{"saturation":-85},{"lightness":61}]},{"featureType":"road"},{},{"featureType":"landscape","stylers":[{"hue":"#0066ff"},{"saturation":74},{"lightness":100}]}];

        //Custom theme
//        var style = [{"featureType":"all","stylers":[{"visibility":"off"}]},{featureType: "administrative.country",elementType: "labels","stylers": [ {visibility: "on"} ]},{featureType: "administrative.city",elementType: "labels","stylers": [ {visibility: "on"} ]},{"featureType":"water","stylers":[{"visibility":"on"},{"lightness":-100}]},{"featureType":"road","stylers":[{"visibility":"simplified"}]},{"featureType":"water","stylers":[{"visibility":"simplified"}]},{"featureType":"transit","stylers":[{"visibility":"simplified"}]},{"featureType":"landscape","stylers":[{"visibility":"simplified"}]},{"featureType":"road.highway","stylers":[{"visibility":"off"}]},{"featureType":"road.local","stylers":[{"visibility":"on"}]},{"featureType":"road.highway","elementType":"geometry","stylers":[{"visibility":"on"}]},{"featureType":"road.arterial","stylers":[{"visibility":"off"}]},{"featureType":"road.highway","stylers":[{"weight":0.6},{"saturation":-85},{"lightness":61}]},{"featureType":"road"},{},{"featureType":"landscape","stylers":[{"hue":"#0066ff"},{"saturation":74},{"lightness":100}]}];
        //Dark Theme
//        var style = [{"featureType":"all","stylers":[{"visibility":"off"}]},{featureType: "administrative.country",elementType: "labels","stylers": [ {visibility: "on"} ]},{featureType: "administrative.city",elementType: "labels","stylers": [ {visibility: "on"} ]},{"featureType":"water","stylers":[{"visibility":"on"},{"lightness":-100}]}];

//        var style;

        map = new google.maps.Map(document.getElementById('googleMap'), {
            zoom: 2,
            center: new google.maps.LatLng(40.7562008, 73.9903784),
            mapTypeId: google.maps.MapTypeId.ROADMAP,
            disableDefaultUI: true,
            scrollwheel: false,
            panControl: true,
            zoomControl: true,
            mapTypeControl: true,
            scaleControl: true,
            streetViewControl: true,
            overviewMapControl: true,
            styles: style
        });

    }

    //populateMap();  
}


function populateMap() {

    var marker;
    var country;

    for (var i = 0; i < markersArray.length; i++ ) {
        markersArray[i].setMap(null);
    }
    markersArray.length = 0;

    for (var u = 0; u < hgCountries.length; u++) {

        country = hgCountries[u];
        geocoder = new google.maps.Geocoder();
        geocoder.geocode( { 'address': country }, function(results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                map.setCenter(results[0].geometry.location);
                marker = new MarkerWithLabel({
                    map: map,
                    position: results[0].geometry.location,
                    html: country,
                });

                tmp = results[0].formatted_address.toLowerCase().replace(' ', '-');
                hgCountriesMetadata[parseInt(results[0].geometry.location.k)] = {stateName : tmp + '/', title: tmp, url: mainURL + tmp + '/'};

            } else {
                alert("Geocode was not successful for the following reason: " + status);
            }// end else



            markersArray[u] = marker;

            markersArray[u].addListener('click', function() {
                //hgBody.className = ' hg-no-scroll';
                //hgOverlay.className = hgOverlay.className.replace('hg-off', 'hg-on');
                //apiGetEvents(capitaliseFirstLetter(hgCountriesMetadata[parseInt(this.position.k)].title));

                /*
                 history.pushState({stateName : hgCountriesMetadata[parseInt(this.position.k)].stateName},
                 hgCountriesMetadata[parseInt(this.position.k)].title,
                 hgCountriesMetadata[parseInt(this.position.k)].url);
                 */
                var c = hgCountriesMetadata[parseInt(this.position.k)].title;
                console.log(c);

                window.location = '/web/' + c.toLowerCase() + '/';
                //console.log(hgCountriesMetadata[parseInt(this.position.k)]);
            }, false);

        });

    }// end for


}// end populateMap()

// manipulate the URL changes
window.onpopstate = function(event) {
    console.log(event.state);
    var container = document.getElementById('hg-list-wrapper');
    if(event.state == null){
        hgOverlay.className = hgOverlay.className.replace('hg-on', 'hg-off');
        container.innerHTML = "";
        hgBody.className = hgBody.className.replace(' hg-no-scroll','');
    }

}// end window.onpopstate()



