//Masquer la validation
$('.alert').hide()

//Actions sur le formulaire lors de la validation
$('form').on('submit', e => {

    //Annuler le rafraichissement automatique de la page
    e.preventDefault();

    //si valeurs pas complète
    $('.alert').hide()

    if ($('select').eq(0).val() == "Select island"
        || $('select').eq(1).val() == "Select sex") {
        console.log('c est vide')
        $('.diag').text("Veuillez remplir tous les champs")
        $('.alert').fadeIn()
    } else {
        island = $('select').eq(0).val()
        bill_length_mm = $('input').eq(0).val()
        bill_depth_mm = $('input').eq(1).val()
        flipper_length_mm = $('input').eq(2).val()
        body_mass_g = $('input').eq(3).val()
        sex = $('select').eq(1).val()

        url = `https://darkpinguins.azurewebsites.net/prediction?island=${island}&bill_length_mm=${bill_length_mm}&bill_depth_mm=${bill_depth_mm}&flipper_length_mm=${flipper_length_mm}&body_mass_g=${body_mass_g}&sex=${sex} `

        $.ajax({
            url: url,
            data: {},
            type: "GET",
            dataType: "json"
        })
            .done(function (json) {
                text = json[0]
                console.log(text)
                $('.diag').text(text)
                $('.alert').fadeIn()
            })


        // fetch(url).then((Response) => {
        //     return Response.json()
        // }).then((data) => {
        //     console.log(data);
        // })

    }
})

$('.alert').on('click', () => {
    $('.alert').fadeOut()
})
