var map;
var locations = ['mexic', 'romania', 'england'];
var markersArray = [];

$(document).on('ready',function(){
	createMap();
});



function makeCountryCall() {
    $.ajax({
        url: 'https://22ba183c.ngrok.com/api/country/',
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
    
        map = new google.maps.Map(document.getElementById('googleMap'), {
            zoom: 2,
            center: new google.maps.LatLng(40.7562008, -73.9903784),
            mapTypeId: google.maps.MapTypeId.ROADMAP,
            disableDefaultUI: true,
            scrollwheel: false
        });

    }

    populateMap();  
} 


  function populateMap() {
     
        var marker;
        var country;
        
        //var locations = ['mexic', 'romania', 'england'];

        for (var i = 0; i < markersArray.length; i++ ) {
            markersArray[i].setMap(null);
        }
        markersArray.length = 0;

        for (var u = 0; u < locations.length; u++) {

            country = locations[u];
            geocoder = new google.maps.Geocoder();
            geocoder.geocode( { 'address': country }, function(results, status) {
                if (status == google.maps.GeocoderStatus.OK) {
                    map.setCenter(results[0].geometry.location);
                    marker = new MarkerWithLabel({
                        map: map,
                        position: results[0].geometry.location,         
                        html: country,
                    });
                } else {
                  alert("Geocode was not successful for the following reason: " + status);
                }

                markersArray[u] = marker;
               
                markersArray[u].addListener('click', function() {
                    
                    switch(parseInt(this.position.k)) {
                    case 23 : {
                        window.location = 'mexic/';
                        break;
                    }
                    case 45 : {
                        window.location = 'romania/';
                        break;
                    }
                    case 52 : {
                        window.location = 'england/';
                        break;
                    }
                    default: {
                        window.location = '404/';
                    }
                    
                    }// end switch()
                    
                   // window.location.href = 'web/' + this.html;
                }, false);

                
            });
            
            
        }// end for 
        
        
        
}




