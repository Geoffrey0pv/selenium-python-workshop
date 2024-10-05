Feature: Intu Login Feature
    Scenario: Successful Intu Login
        Given que estoy en la pagina de logueo
        When presiono el boton para loguearme con las credenciales correctas
        Then el logueo es exitoso 
        And se redirige el usuario a la pagina del dashboard de mi usuario