
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


$(document).ready(function(){
    $("#submit").click(function(){
        var audioname = $("#audioname").text();
        var inputs = $("#contents").val();
        
        if (inputs){
            var post_data = {"audioname":audioname, "audiotext":inputs}
            $.ajax({
                type: "post",
                url: "/listenwrite",
                data: post_data,
                cache: false,
                success: function(e){
                    if (e=="1"){
                        alert("ok,good");
                    } else {
                        alert("please try again.")
                    }
                },
                error: function(e){
                    alert("are you on line?")
                }
            }
            ) 
        } else {
            alert("please write what you are listening, and then submit.")
        }
    })
})

$(document).ready(function(){
    $("#submitcategory").click(function(){
        var category_name = $("#categoryname").val();
        if (category_name){
            var vategoryname = {"category_name":category_name}
            $.ajax({
                type: "post",
                url: "/audio",
                data: vategoryname,
                success: function(e){
                    if (e=="1"){
                        alert("ok, the category is right.")
                    } else {
                        alert("you are wrong.")
                    }
                }
            })
        } else {
            alert("You should input category name.")
        }
    })
})
