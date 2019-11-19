function valida() {
    var correo, nombre, expresion;
    correo = document.getElementById( "txtemail" ).value;
    nombre = document.getElementById( "txtname" ).value;    
    expresion = /\w+@\w+\.+[a-z]/;
    if(!expresion.test(correo)){
        alert("Ingrese formato de correo correcto");
        return false;
       }else if(nombre.split(' ').length < 3){
           alert("Ingrese nombre completo");
           return false;

           }
       
}