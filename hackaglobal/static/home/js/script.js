
/* CONFIG */
var apiURL = 'http://hackaglobal.co';

var map;
var hgCountries = [],
	hgCountriesMetadata = [],
	hgBody = document.getElementById('hg-body'),
	hgOverlay = document.getElementById('hg-overlay');

var markersArray = [];
var mainURL = window.location.href;

$(document).on('ready',function(){
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
                	hgBody.className = ' hg-no-scroll';
                	hgOverlay.className = hgOverlay.className.replace('hg-off', 'hg-on');
                	apiGetEvents(capitaliseFirstLetter(hgCountriesMetadata[parseInt(this.position.k)].title));
                	
                		history.pushState({stateName : hgCountriesMetadata[parseInt(this.position.k)].stateName}, 
                											hgCountriesMetadata[parseInt(this.position.k)].title, 
                											hgCountriesMetadata[parseInt(this.position.k)].url);
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



