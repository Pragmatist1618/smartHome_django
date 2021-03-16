$(document).ready(function () {

    //starting position
    var bedroom = $('#checkbox_bedroom');
    var cor = $('#checkbox_cor');
    if (bedroom.is(':checked')){
        $('.bedroom').addClass('on')
    } else {
        $('.bedroom').removeClass('on')
    }
    if (cor.is(':checked')){
        $('.cor').addClass('on')
    } else {
        $('.cor').removeClass('on')
    }

    //changes the value of the checkbox
    function click_to_checkbox(element) {
        var id_room = element.data('room');
        var room = $('.' + id_room);
        if (element.is(':checked')) {
            element.prop('value', 'True');
            room.addClass('on')
        } else {
            element.prop('value', 'False');
            room.removeClass('on')
        }
    }

    //click any checkbox
    $('.form-check-input').click(function () {
        click_to_checkbox($(this));
        changeDB($(this))
    })

    //to do ajax - POST
    function changeDB(element){
        var data = {};
        data.name = element.data('room');
        data.state = element.val();
        //get csrf
        var csrf_token = $('#csrf_getting_form [name="csrfmiddlewaretoken"]').val();
        data['csrfmiddlewaretoken'] = csrf_token;
        //console.log(data);
        $.ajax({
            url: 'change-gpio/',
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
               console.log('OK')
           },
           error: function (data) {
               console.log('ERROR!')
           }
        })
    }

    setInterval(function (){
        //ajax-get
        $.ajax({
           url : 'state-gpio/',
           type: 'get',
           success: function (data) {
               var bedroom_gpio = data['bedroom_gpio'];
               var cor_gpio = data['cor_gpio'];
               var bedroom = $('#checkbox_bedroom');
               var cor = $('#checkbox_cor');
               if (bedroom_gpio){
                   $('.bedroom').addClass('on')
                   bedroom.prop('checked', true);
                   bedroom.prop('value', 'True');
               } else {
                   $('.bedroom').removeClass('on')
                   bedroom.prop('checked', false);
                   bedroom.prop('value', 'False');
               }
               if (cor_gpio){
                   $('.cor').addClass('on')
                   cor.prop('checked', true);
                   cor.prop('value', 'True');
               } else {
                   $('.cor').removeClass('on')
                   cor.prop('checked', false);
                   cor.prop('value', 'False');
               }
           },
           error: function (data) {
               console.log('ERROR!')
           }
        })
        }, 1000)

})