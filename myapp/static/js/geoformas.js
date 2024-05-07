window.log=function(text){
    console.info("LOG[" + new Date().toLocaleString()  + "]: " + text);
};

window.currentDrawingManager = null;
window.drawingOverlay = null;
window.clearDrawingOverlay = function(){
    if(drawingOverlay){
        drawingOverlay.setMap(null);    
        drawingOverlay = null;
        
        $("#geofencePath").val("");
        $("#circleRadio").val("");
    }
    
    if(window.markerLocalizar){
        window.markerLocalizar.setMap(null);
        $("#locLat").val("");
        $("#locLgn").val("");
    }
    
    window._changeGeofenceShape();
};

window.changeGeofenceShape = function(){
    window.clearDrawingOverlay();
    window._changeGeofenceShape();
};

window._changeGeofenceShape = function(){
    if($("#geofenceShape").val()=="polygon" || $("#geofenceShape").val()=="route"){        
        window.currentDrawingManager.setOptions({ 
            drawingMode   : google.maps.drawing.OverlayType.POLYGON,            
            polygonOptions: window.drawingOptions($("#geofenceShape").val())});
        $("#optCircle").hide();
        $("#optPath").html("Puntos");
    }
    else{
        window.currentDrawingManager.setOptions({ 
            drawingMode  : google.maps.drawing.OverlayType.CIRCLE,
            circleOptions: window.drawingOptions('circle'),
        });
        $("#optCircle").show();
        $("#optPath").html("Centro");
    }
};

window.drawingOptions = function(shape){
    var opts = { 
        strokeColor: '#FE2E2E', 
        strokeOpacity: 0.8,
        strokeWeight: 2, 
        fillColor: '#FF8000', 
        fillOpacity: 0.35,
        clickable: true,
        editable: true,
        draggable: true,
        suppressUndo: true,
        zIndex: 1        
    };
    
    if(shape=="route"){
        opts.strokeColor = "#002af7";
        opts.fillColor   = "#2488EE";        
    }    
    return opts;
};

window.saveGeofence = function(){
    var geofenceName  = $.trim($("#geofenceName").val());
    var geofenceShape = $.trim($("#geofenceShape").val());
    var circleRadio   = $.trim($("#circleRadio").val());
    var geofenceGroup = $.trim($("#geofenceGroup").val());
    
    if(geofenceName==""){
        alert("Nombre de Geocerca no puede ser vacio.");
        return;
    }
    else if(geofencePath==""){
        alert("No se ha ingresado datos de la geocerca.");
        return;
    }
    
    if(geofenceGroup=="-"){
        alert("No se ha seleccionado un Grupo.");
        return;
    }
    
    log("Ingresando a: saveGeofence ...");

    var arrParams = new Array();
    arrParams["action"]    = "saveGeofence";
    arrParams["rawmode"]   = "yes";
    arrParams["menu"]      = "geofences";
    arrParams["geofenceShape"] = geofenceShape;
    arrParams["geofenceName"]  = geofenceName;
    arrParams["geofenceID"]    = $.trim($("#geofenceID").val());
    arrParams["geofenceGroup"] = $("#geofenceGroup").val();
    arrParams["geofenceGroupSaved"]  = $("#geofenceGroupSaved").val();
    arrParams["geofenceNotify"] = $("#geofenceNotify").val();
    arrParams["geofencePermit"]  = $("#geofencePermit").val();
    
    if(geofenceShape=="polygon" || geofenceShape=="route"){
        var points= "";
        for (var i =0; i < window.drawingOverlay.getPath().length; i++) {
            var xy = window.drawingOverlay.getPath().getAt(i);
            points += xy.lat() + "," + xy.lng() + "|";
        }
        
        arrParams["geoPoints"] = points.substring(0,points.length-1);
    }
    else{
        arrParams["circleRadio"] = circleRadio;
        arrParams["circleCenter"] = window.drawingOverlay.getCenter().lat() + "," +
                window.drawingOverlay.getCenter().lng();
    }
    
    request("/index.php",arrParams,false,
        function(message,statusResponse,error) {
            log("Process saveGeofence response ...");
            
            if(error){
                log(error);
                alert(error);
            }
            else{
                alert("La Geocerca " + geofenceName + " fue guardada con exito.");
                location.href = "/index.php?menu=geofences&filter_field=g.descripcion&filter_value=" + geofenceName;
            }
        });
    
    
};

window.cancelar = function(){
    location.href = "/index.php?menu=geofences";
};

window.addEventsCircle = function(){
    google.maps.event.addListener(window.drawingOverlay, 'center_changed', function() {
        console.info(window.drawingOverlay.getRadius());
        console.info(window.drawingOverlay.getCenter());

        $("#circleRadio").val(window.drawingOverlay.getRadius());
        $("#geofencePath").val(window.drawingOverlay.getCenter());
    });
    google.maps.event.addListener(window.drawingOverlay, 'dragend', function(event) {
        console.info(window.drawingOverlay.getRadius());
        console.info(window.drawingOverlay.getCenter());

        $("#circleRadio").val(window.drawingOverlay.getRadius());
        $("#geofencePath").val(window.drawingOverlay.getCenter());
    });
    google.maps.event.addListener(window.drawingOverlay, 'radius_changed', function() {
        console.info(window.drawingOverlay.getRadius());
        console.info(window.drawingOverlay.getCenter());

        $("#circleRadio").val(window.drawingOverlay.getRadius());
        $("#geofencePath").val(window.drawingOverlay.getCenter());
    });
};

window.addEventsPolygon = function(){
    google.maps.event.addListener(window.drawingOverlay, 'dragend', function(event) {
        console.info(window.drawingOverlay.getPath());

        var puntos= "";
        for (var i =0; i < window.drawingOverlay.getPath().length; i++) {
            var xy = window.drawingOverlay.getPath().getAt(i);
            puntos += (i+1) + ". " + xy + "\n\n";
        }
        $("#geofencePath").val(puntos);
    });
    google.maps.event.addListener(window.drawingOverlay, 'mouseup', function(event) {
        console.info(window.drawingOverlay.getPath());

        var puntos= "";
        for (var i =0; i < window.drawingOverlay.getPath().length; i++) {
            var xy = window.drawingOverlay.getPath().getAt(i);
            puntos += (i+1) + ". " + xy + "\n\n";
        }
        $("#geofencePath").val(puntos);
    });
};

window.markerLocalizar = null
window.localizar = function(){
    var latitud  = $("#locLat").val();
    var longitud = $("#locLgn").val();
    var pos      = new google.maps.LatLng(latitud,longitud);

    if(!pos){
        alert("Coordenadas invalidas para localizar");
    }
    window.markerLocalizar = new google.maps.Marker({
        position: pos,
        map: window.map,
    });      
    window.map.setCenter(pos);
};

window.addDeleteAction=function(){
    //https://developers.google.com/maps/documentation/javascript/examples/delete-vertex-menu
    const deleteMenu = new DeleteMenu();
    google.maps.event.addListener(window.drawingOverlay, "rightclick", (e) => {
        // Check if click was on a vertex control point
        if (e.vertex == undefined) {
            return;
        }
        deleteMenu.open(map, window.drawingOverlay.getPath(), e.vertex);
    });
};

//---- --- -- - LOAD Mapa
window.loadmap=function(){
    var mapOptions = {
        zoom: 17,
        center: new google.maps.LatLng(-2-10/60, -79-53/60),            
        overviewMapControl: true,
        overviewMapControlOptions: {opened: true},
        mapTypeId: google.maps.MapTypeId.HYBRID,
        scrollwheel: true,
		
        mapTypeControl: true,
        mapTypeControlOptions: {
          style: google.maps.MapTypeControlStyle.DROPDOWN_MENU,
            position: google.maps.ControlPosition.RIGHT_TOP
        },
		
        fullscreenControl: true,
        fullscreenControlOptions: {
            position: google.maps.ControlPosition.RIGHT_BOTTOM
        },

        streetViewControl: true,
        streetViewControlOptions: {
            position: google.maps.ControlPosition.RIGHT_BOTTOM
        },

        zoomControl: true,
        zoomControlOptions: {
            position: google.maps.ControlPosition.RIGHT_BOTTOM
        },
		  
        scaleControl: true,
            scaleControlOptions: {
                position: google.maps.ControlPosition.RIGHT_BOTTOM
            }
    };
    
    var map = new google.maps.Map(document.querySelector('#col_map'), mapOptions);

    window.currentDrawingManager = new google.maps.drawing.DrawingManager({
        drawingMode: google.maps.drawing.OverlayType.CIRCLE,
        drawingControl: false,
        drawingControlOptions: {
            position: google.maps.ControlPosition.TOP_RIGHT,
            drawingModes: ['circle', 'polygon']
        },
        circleOptions : window.drawingOptions('circle'),
        polygonOptions: window.drawingOptions('polygon')
    });
    window.currentDrawingManager.setMap(map);
    
    google.maps.event.addListener(window.currentDrawingManager, 'overlaycomplete', function(event) {
        window.currentDrawingManager.setOptions({ drawingMode: null });
        
        if (event.type == 'circle') {
            window.drawingOverlay = event.overlay;
            console.info(window.drawingOverlay.getRadius());
            console.info(window.drawingOverlay.getCenter());
            
            $("#circleRadio").val(window.drawingOverlay.getRadius());
            $("#geofencePath").val(window.drawingOverlay.getCenter());

            window.addEventsCircle();
        }
        else if (event.type == 'polygon') {
            window.drawingOverlay = event.overlay;            
            console.info(window.drawingOverlay.getPath());
            
            var puntos= "";
            for (var i =0; i < window.drawingOverlay.getPath().length; i++) {
                var xy = window.drawingOverlay.getPath().getAt(i);
                puntos += (i+1) + ". " + xy + "\n\n";
            }
            $("#geofencePath").val(puntos);

            window.addEventsPolygon();
        }
    });
    
    window.map=map; 
    
    google.maps.event.addListener(map, "click", function(event) {
        if($("#center").checked){ map.setCenter(event.latLng); }
    });
    
    google.maps.event.addListener(map, "rightclick", function(event) {
        console.info("GeoCoordenadas son: " + event.latLng);
        alert("GeoCoordenadas son: " + event.latLng); 
    });
    
    google.maps.event.addListener(map, "tilesloaded", function(event) {        
        var thisIframesHeight = $(window).height() - 44;
        $("#lista_dispositivos").css({ "height": thisIframesHeight + "px"});        
    });
                            
    log("Process LOADMAP ejecutado ...");
    
    
    $(function(){
        var drawingOpts = window.drawingOptions($("#geofenceShape").val());
        
        if($("#geofenceShape").val()=="polygon" || $("#geofenceShape").val()=="route"){        
            $("#optCircle").hide();
            $("#optPath").html("Puntos");
            $("#circleRadio").val("");

            var geofencePoints = $("#geofencePoints").val();
            if(geofencePoints){
                var arrGeofencePoints = geofencePoints.split("|");
                var arrPoints = new Array();;
                
                $.each(arrGeofencePoints, function(i,p) {
                    var point = p.split(",");
                    arrPoints[arrPoints.length] = {lat: parseFloat(point[0]), lng: parseFloat(point[1])};
                });
                
                window.drawingOverlay = new google.maps.Polygon(drawingOpts);                
                window.drawingOverlay.setMap(window.map);
                window.drawingOverlay.setPath(arrPoints);
                window.currentDrawingManager.setOptions({ drawingMode: null });                  
                window.addEventsPolygon();
                window.map.setCenter(arrPoints[0]);
                
                //https://developers.google.com/maps/documentation/javascript/examples/delete-vertex-menu
                const deleteMenu = new DeleteMenu();
                google.maps.event.addListener(window.drawingOverlay, "rightclick", (e) => {
                    // Check if click was on a vertex control point
                    if (e.vertex == undefined) {
                        return;
                    }
                    deleteMenu.open(map, window.drawingOverlay.getPath(), e.vertex);
                });
            }
        }
        else{
            $("#optCircle").show();
            $("#optPath").html("Centro");

            var circleCenter = $("#circleCenter").val();
            var circleRadio  = $("#circleRadio").val();
            if(circleCenter){
                var point = circleCenter.split(",");
                var centerP = {lat: parseFloat(point[0]), lng: parseFloat(point[1])};
                
                window.drawingOverlay = new google.maps.Circle(drawingOpts);
                window.drawingOverlay.setMap(window.map);
                window.drawingOverlay.setCenter(centerP);
                window.drawingOverlay.setRadius(parseFloat(circleRadio));
                window.currentDrawingManager.setOptions({ drawingMode: null });                  
                window.addEventsCircle();
                window.map.setCenter(centerP);
            }
        }
    });
    
    
};
document.addEventListener("DOMContentLoaded", window.loadmap);  