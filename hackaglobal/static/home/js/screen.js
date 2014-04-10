
function ge(id) {
	return document.getElementById(id);
}// end ge()


//function capitaliseFirstLetter(string) {
//	return string.charAt(0).toUpperCase() + string.slice(1);
//}// end capitaliseFirstLetter()


function getEvents(country) {
	var xhr = new XMLHttpRequest();
	
	xhr.open('GET', apiURL + '/api/data/' + country + '/', true);

	xhr.onload = function() {
		var rsp = JSON.parse(xhr.responseText),
		n,
		i,
		html = [];
		
		if (rsp) {
			n = rsp.length;
			
			if (n > 0) {
					
				html.push('<div class="hg-list-date-container">' + country + '</div>');
				html.push('<ul class="hg-list-ul">');
				
				for (i = 0; i < n; i++) {
					html.push('<li class="hg-list-item-container">' + 
						'<div class="hg-list-item-left"><div class="hg-list-item-title-container">'+
						'<a class="hg-list-item-title" href="' + rsp[i].website + '" target="_blank">' + rsp[i].name + '</a>' +
						'</div><div class="hg-list-item-location">' + rsp[i].address + ' &middot;' +
						' organizer ' + rsp[i].creator + '</div>' +
						'<div class="hg-list-item-info">' + rsp[i].description + '...</div></div>' +
						'<div class="hg-list-item-right">' + rsp[i].start + '</div></li>');
				}// end for
				
				html.push('</ul>');
				
				abEvContainer.className = abEvContainer.className.replace(' hg-loader', '');
				abEvContainer.innerHTML = html.join('');
				
			} else {
				// no events found
				console.log("no events found");
			}// end else
			
		} else {
			// no events found
			console.log("no events found");
		}// end else
    
	}// end xhr.onload()
	
	xhr.error = function() {
		console.log('could not get the coutries list from the API');
	}// end xhr.error()
	
	xhr.send();
	
}// end getEvents()


var apiURL = 'http://www.hackaglobal.co',
		abEvContainer = ge('ab-events-container'),
		country = abEvContainer.getAttribute('data-country');


if (country != "") {
	// get the events from the API
	getEvents(country.toLowerCase());
	
	
} else {
	console.log('no country found :(');
}// end else

