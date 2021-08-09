//Masquer la validation
$('.alert').hide()


//Actions sur le formulaire lors de la validation

$('form').on('submit', e => {

    //Annuler le rafraichissement automatique de la page
    e.preventDefault();

    //si valeurs pas complète
    $('.alert').hide()

    if ($('select').eq(0).val() == "Select island"
    || $('input').eq(0).val() == ""
    || $('input').eq(1).val() == ""
    || $('input').eq(2).val() == ""
    || $('input').eq(3).val() == ""
    || $('select').eq(1).val() == "Select sex") {
        console.log('c est vide')
        $('.alert').text("Veuillez remplir tous les champs")
        $('.alert').show()
    } else {
        island = $('select').eq(0).val()
        bill_length_mm = $('input').eq(0).val()
        bill_depth_mm = $('input').eq(1).val()
        flipper_length_mm = $('input').eq(2).val()
        body_mass_g = $('input').eq(3).val()
        sex = $('select').eq(1).val()

        url = `http://127.0.0.1:8000/prediction?island=${island}&bill_length_mm=${bill_length_mm}&bill_depth_mm=${bill_depth_mm}&flipper_length_mm=${flipper_length_mm}&body_mass_g=${body_mass_g}&sex=${sex} `

        // $.ajax({
        //     url: url,
        //     data: {},
        //     type: "GET",
        //     dataType: "json"
        // })
        //     .done(function (json) {
        //         console.log(json.results)
        //     })


           
        fetch(url).then((Response) => {
            return Response.json()
        }).then((data) => {
            console.log(data);
        })
    
                
            


    }
   



    // // Bordure rouge si pas de chat sélectionnés
    // ($('select').val() === "-- Sélectionner --") && $('select').addClass('border-danger')

    // //bordure rouge si l'argumentation est < à 15 caractères
    // if ($('textarea').val().length < 15) $('textarea').addClass('border-danger')

    // //Envoie de la validation si les conditions sont remplies
    // if ($('select').val() != "-- Sélectionner --" && ($('textarea').val()).length >= 15) {
    //     $('form').hide()
    //     $('.alert').fadeIn()
    // }

    // //Rétablissement des bordures si nouvelles entrées    
    // $('select').on('input', () => {
    //     $('select').removeClass('border-danger')
    // })

    // $('textarea').on('input', () => {
    //     $('textarea').removeClass('border-danger')
    // })

})
