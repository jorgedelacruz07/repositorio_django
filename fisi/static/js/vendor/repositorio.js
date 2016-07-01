
function mostrarseccion(arg){
 
  $("#seccion_seleccionada").val(arg);
  if(arg==1){ var url = /mostrararea/; }
  if(arg==2){ var url = /mostrarcurso/; }
  if(arg==3){ var url = /mostrarprofesor/; }
  $.get(url,function(resul){
      $("#contenido").html(resul);
    })
}






 $('.Datosp').on("click", getDatosp);
function getDatosp() {
    var profesor_id = $(this).val();
    console.log(profesor_id)
    if(profesor_id){
        var request = $.ajax({
           data: {'profesor_id':profesor_id},
            url: /getdatos/,
            type:"get",
        });
    request.done(function(response) {
            $("#datos").html(response.profesores);
        });
    }
}



$('.votos').on("click", getVotos);
function getVotos() {
    var archi_id = $(this).val();
    console.log(archi_id)
    if(archi_id){
       $("."+archi_id).html("");
        var request=$.ajax({
            data:{'archi_id':archi_id},
            url: /getvotos/,
            type:"get",

        })
    request.done(function(response) {
       console.log()
        $("."+archi_id).html(response.votos);
        });
    }
}

$('.votos_subida').on("click", getVotosSudida);
function getVotosSudida() {
    var archi_id = $(this).val();
    console.log(archi_id)
    if(archi_id){
       $("."+archi_id).html("");
        var request=$.ajax({
            data:{'archi_id':archi_id},
            url: /getvotosless/,
            type:"get",

        })
    request.done(function(response) {
       console.log()
        $("."+archi_id).html(response.votos);
        });
    }
}
       
$(document).ready(function() {
            $('#id_area').on("change", getCursos);
            $("#id_curso").on("change", getProfesores);

        });

function getCursos() {
    var area_id = $("#id_area").val();
    if (area_id) {
        // Eliminamos las opciones anteriores del select
        $("#id_curso").html("");
        var request = $.ajax({
            type: "GET",
            url: "/getcurso/",
            data: {
                "area_id": area_id,
            },
                    
        });
        request.done(function(response) {
            // Agregamos los resultados al select
                    
            $("#id_curso").html(response.cursos);
            $("#id_profesor").html("<option value='' selected='selected'>---------</option>");
            $("#id_curso, #id_profesor").trigger("change",getProfesores);
        });
    } else {
        $("#id_curso").html("<option value='' selected='selected'>---------</option>");
        $("#id_profesor").html("<option value='' selected='selected'>---------</option>");
        $("#id_curso, #id_profesor").trigger("change");
    }
}    

function getProfesores() {
    var curso_id = $("#id_curso").val();
    if (curso_id) {
        // Eliminamos las opciones anteriores del select
        $("#id_profesor").html("");
        var request = $.ajax({
            type: "GET",
            url: "/getprofesor/",
            data: {
                "curso_id": curso_id,
            },
        });

        request.done(function(response) {
        	console.log(response.profesores)
            // Agregamos los resultados al select
            $("#id_profesor").html(response.profesores);
            $("#id_profesor").trigger("change");
        });
    } else {
        $("#id_profesor").html("<option value='' selected='selected'>---------</option>");
        $("#id_profesor").trigger("change");
    }
}

    

