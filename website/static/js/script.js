var map;
var markersArray = [];

$(document).on('ready',function(){
	createMap();
});





function makeCountryCall() {
    $.ajax({
        url: 'http://6f84083a.ngrok.com/api/country/',
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
                scrollwheel: false,
                draggable: true,
                mapTypeControl:  false,
                disableDefaultUI: true
            });

        }


        populateMap();
     
} 


 function populateMap() {
     
        var resultsData;
        //var letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];

        var marker;
        var infowindow = new google.maps.InfoWindow({
            content: ''
        });
        var LatLngList = new Array();
		
		for (var i = 0; i < markersArray.length; i++ ) {
			markersArray[i].setMap(null);
		}
		markersArray.length = 0;
        var locations = ['Mexic', 'Romania', 'England'];
        for (var u = 0; u < 3; u++) {
            
                //resultsData = data.results[u];
                geocoder = new google.maps.Geocoder();
                //var letter = letters[u];
                
                var infowindow = new google.maps.InfoWindow();

                geocoder.geocode( { 'address': locations[u] }, function(results, status) {
                    if (status == google.maps.GeocoderStatus.OK) {
                       map.setCenter(results[u].geometry.location);
                       marker = new MarkerWithLabel({
                            map: map,
                            position: results[u].geometry.location,
                            icon: 'static/img/marker.png', 
                            labelClass: "labels",
                            labelAnchor: new google.maps.Point(5, 29),                 
                            html: locations[u],
                            labelInBackground: false
                       });
                    } else {
                      alert("Geocode was not successful for the following reason: " + status);
                    }
                });

    			google.maps.event.addListener(marker, 'click', function (e) {
    				window.location.href = 'http://www.google.com';
    				//infowindow.setContent(this.html);
    				//infowindow.open(map, this);
    				//map.setCenter(this.getPosition());
    			});
                
    			markersArray.push(marker);
    			
    			//  Make an array of the LatLng's of the markers you want to show
                LatLngList.push(new google.maps.LatLng(locations[1], locations[2]));

               
            fitBounds(LatLngList);

            $(window).on('resize',function () {
               // fitBounds(LatLngList);
            });
        }

        function fitBounds(LatLngList) {

            var bounds = new google.maps.LatLngBounds();
            //  Go through each...
            for (var i = 0; i < LatLngList.length; i++) {
                //  And increase the bounds to take this point
                bounds.extend(LatLngList[i]);
            }

            //  Fit these bounds to the map
            var minDistance = 0.002;
            var sumA = bounds.getNorthEast().lng() - bounds.getSouthWest().lng();
            var sumB = bounds.getNorthEast().lat() - bounds.getSouthWest().lat();

            if ((sumA < minDistance && sumA > -minDistance)
                && (sumB < minDistance && sumB > -minDistance)) {
                var extendPoint1 = new google.maps.LatLng(bounds.getNorthEast().lat() + minDistance, bounds.getNorthEast().lng() + minDistance);
                var extendPoint2 = new google.maps.LatLng(bounds.getNorthEast().lat() - minDistance, bounds.getNorthEast().lng() - minDistance);
                bounds.extend(extendPoint1);
                bounds.extend(extendPoint2);
            }
            if ($('#googleMap').length > 0) {
                map.fitBounds(bounds);
            }
        }


}