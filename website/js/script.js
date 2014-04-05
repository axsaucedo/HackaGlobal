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


           // populateMap(data);
     
} 


 function populateMap(data) {
     
        var resultsData;
        var letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];

        var marker;
        // end map
        var infowindow = new google.maps.InfoWindow({
            content: ''
        });
        var LatLngList = new Array();
		
		for (var i = 0; i < markersArray.length; i++ ) {
			markersArray[i].setMap(null);
		}
		markersArray.length = 0;

       for (var u = 0; u < data.results.length; u++) {

            resultsData = data.results[u];

            var letter = letters[u];
  
            var locations = ['mexic', resultsData.latitude, resultsData.longitude];

            var infowindow = new google.maps.InfoWindow();
            
			marker = new MarkerWithLabel({
				position: new google.maps.LatLng(locations[0]),
				map: map,
				labelContent: letter,
				labelClass: "labels",
				labelAnchor: new google.maps.Point(5, 29),                 
				dealerName: retailer.name,
				html: locations[0],
				labelInBackground: false
			});

			google.maps.event.addListener(marker, 'click', function (e) {
				window.location.href = '/country=' + this.html;
				//infowindow.setContent(this.html);
				//infowindow.open(map, this);
				//map.setCenter(this.getPosition());
			});
            
			markersArray.push(marker);
			
			//  Make an array of the LatLng's of the markers you want to show
            LatLngList.push(new google.maps.LatLng(locations[1], locations[2]));

           
        fitBounds(LatLngList);

        $(window).on('resize',function () {
            fitBounds(LatLngList);
        });
    }

}