// contact us home page section

$(document).on('submit','#contactme',
        function(x){
            x.preventDefault();
        if ($("#name").val().length!=0) {   
        $.ajax({
                type:'POST',
                url:"/",
    
                data:{
                    name:$("#name").val(),
                    email:$("#email").val(),
                    subject:$("#subject").val(),
                    message:$("#message").val(),
                    csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
                    },
               
    
                success:function(response){
                    document.getElementById('mailnotif').innerText=response;
                    if (response=='Email Not Sent!'){
                    document.getElementById('mailnotif').style.color='red'
                        }
                    else{
                        document.getElementById('mailnotif').style.color='green'
                    }

                    
                
        } })            
        }}
    
    )