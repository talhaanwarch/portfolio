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


    // end contact us home page section

    // start of nlp demo


document.getElementsByTagName("center")[0].style.display ='none'//hide progess bar
$(document).on('submit','#sentiform',
    function(x){
        x.preventDefault();
    if ($("#textareaName").val().length!=0){    
    $.ajax({
            type:'POST',
            url:"/demo-nlp/",

            data:{
                textsentence:$("#textareaName").val(),
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
                },
           

            success:function(response){
              document.getElementsByTagName("center")[0].style.display ='block'
              var senti=response
                console.log(senti);
                // change the value of color
                document.getElementsByClassName("bg-success")[0].style.width=senti["Positive"]+"%"
                document.getElementsByClassName("bg-warning")[0].style.width=senti["Neutral"]+"%"
                document.getElementsByClassName("bg-danger")[0].style.width=senti["Negative"]+"%"
                //change value written
                document.getElementsByClassName("bg-success")[0].innerText=senti["Positive"]+"%"
                document.getElementsByClassName("bg-warning")[0].innerText=senti["Neutral"]+"%"
                document.getElementsByClassName("bg-danger")[0].innerText=senti["Negative"]+"%"
                      }
                    })            
    }}

)




      // end of nlp demo  