$(document).ready(function(){
    //Initial setup actions
    //$("#register_form").hide();
    
    //event handlers
    $("#register_btn").click(function(){
        $("#register_form").show();
        $("#login_form").hide();
    });
});
//if($("#manage_reply_enquiry").is(":visible")){        });
function showform(form_id) {
    alert(form_id);
}