google.maps.visualRefresh = true;
map = null;
myName = null;
goodies = {};

var styles = [
  {
    "stylers": [
      { "saturation": -100 }
    ]
  }
]

$(function() {
  var mapOptions = {
    center: new google.maps.LatLng(32.52828936482526,-118.32275390625),
    zoom: 7,
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    mapTypeControl: false,
    streetViewControl: false,
  };
  
  map = new google.maps.Map(document.getElementById("mapCanvas"), mapOptions);
  map.setOptions({styles: styles});
  google.maps.event.addListener(map, 'zoom_changed', function() {
    this.getZoom()
  });

  destination = new google.maps.Marker({
    animation: google.maps.Animation.DROP,
    map: map
  });

  google.maps.event.addListener(map, 'click', function(event) {
  });

  if (navigator.geolocation) navigator.geolocation.watchPosition(updateMyLocation, error);
  else error('not supported');

});

function error(msg) {
  console.log(msg);
}

function updateMyLocation(myPosition) {
  var latlng = new google.maps.LatLng(myPosition.coords.latitude, myPosition.coords.longitude);

  data = {name: myName, 
          location: {latitude: myPosition.coords.latitude, 
                     longitude: myPosition.coords.longitude}, 
          zoom: map.getZoom() }

  $.get("getGoodies", data)
    .done(function(data) {

      //delete markers that dont exist anymore
      for (goodie in goodies) {
        if (!data.goodies.hasOwnProperty(goodie)) {
          goodie.marker.setMap(null);
          delete goodie.marker
        }
      }

      //create markers that dont exist yet
      for (goodie in data.goodies) {
        goodies.goodie = data.goodies.goodie;
        goodies.goodie.marker = new google.maps.Marker({
          animation: google.maps.Animation.DROP,
          map: map,
          position: new google.maps.LatLng(goodies.goodie.location.latitude, goodies.goodie.location.longitude)        
        })
      }

      if (data.enabledGoodie) {
        showLock(goodies[data.enabledGoodie])
      }

    });  
}