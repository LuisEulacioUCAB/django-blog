$(document).ready(function () {
    $('#repeat_password').keyup(function () {
        if ($(this).val() === $("#password").val()) {
            $('#register').attr('disabled', false)
            $('#repeat_password').addClass('user_valid');
            $('#repeat_password').removeClass('user_invalid');
            $('#password').addClass('user_valid');
            $('#password').removeClass('user_invalid');
        } else {
            $('#register').attr('disabled', true)
            $('#repeat_password').addClass('user_invalid');
            $('#repeat_password').removeClass('user_valid')
            $('#password').addClass('user_invalid');
            $('#password').removeClass('user_valid')
        }
    });

    $('#password').keyup(function () {
        if ($(this).val() === $("#repeat_password").val()) {
            $('#register').attr('disabled', false)

        } else {
            $('#register').attr('disabled', true)

        }
    });

    $("#username").keyup(function () {
        var form = $(this).closest("form");
        empty = true;
        $.ajax({
            url: form.attr("data-url-exists-username"),
            data: form.serialize(),
            type: 'post',
            dataType: 'json',
            success: function (data) {
                if (data != '') {
                    $('#username').addClass('user_invalid');
                    $('#username').removeClass('user_valid')

                } else {
                    $('#username').addClass('user_valid');
                    $('#username').removeClass('user_invalid');

                }
            }
        });
    })

});