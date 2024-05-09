let map
let placemark
function initMap(){
    let lat = parseFloat(document.getElementById('id_latitude').value);
    let lng = parseFloat(document.getElementById('id_longitude').value);
    if (isNaN(lat) && isNaN(lng)) {
        
        lat = 55.755864;
        lng = 37.617698;
        document.getElementById('id_latitude').value = lat;
        document.getElementById('id_longitude').value = lng;
    }
    map = new ymaps.Map('map', {
    center:[lat, lng],
    zoom: 16
    });
    placemark = new ymaps.Placemark([lat, lng], {}, {
    draggable: true,
    preset: 'islands#greenIcon'
    });
    map.geoObjects.add(placemark);

    placemark.events.add('dragend', function(e) {
    let coords = e.get('target').geometry.getCoordinates();
    document.getElementById('id_latitude').value = coords[0];
    document.getElementById('id_longitude').value = coords[1];

    });

    map.events.add('click', function(e) {
        let coords = e.get('coords');
        placemark.geometry.setCoordinates(coords);
        document.getElementById('id_latitude').value = coords[0];
        document.getElementById('id_longitude').value = coords[1];
    });
}
ymaps.ready(initMap)