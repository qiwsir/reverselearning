
$(document).ready(function(){
    $("#login").click(function(){
        var username = $("#username").val();
        var password = $("#password").val();
        
        var check_input = /^([A-Za-z0-9])+$/;

        var username_checked = check_input.test(username);
        var password_checked = check_input.test(password);

        if (username_checked && password_checked){
            var user_data = {"username":username, "password":password};
            $.ajax({
                type: "post",
                url: "/",
                data: user_data,
                cache: false,
                success: function(e){
                    if (e=="1"){
                        location.href="http://127.0.0.1:8888/listenwrite?user=" + username
                    }else if (e=="0"){
                        alert("username or passwor is false.")
                    }else {
                        alert("are you a human?")
                    }
                },
                error: function(e){
                    alert("ah");
                },
            })
        } else {
            alert("please go out.")
        }
    })
})
