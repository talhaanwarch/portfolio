navigator.mediaDevices.getUserMedia({audio:true})
.then(stream => {handlerFunction(stream)})
      function handlerFunction(stream) {
      rec = new MediaRecorder(stream);
      console.log('codec',MediaRecorder.isTypeSupported('audio/ogg;codecs=mp3'));
      rec.ondataavailable = e => {
        audioChunks.push(e.data);
        if (rec.state == "inactive"){
          let blob = new Blob(audioChunks,{type: 'audio/ogg; codecs=opus' });
          recordedAudio.src = URL.createObjectURL(blob);
          recordedAudio.controls=true;
          recordedAudio.autoplay=true;
          sendData(blob)
        }
      }
    }
          function sendData( blob ) {
            var reader = new FileReader();
            reader.onload = function(event){
              var fd = {};
              fd["fname"] = "test.wav";
              fd["data"] = event.target.result;
              fd["csrfmiddlewaretoken"]=$('input[name=csrfmiddlewaretoken]').val()
              $.ajax({
                type: 'POST',
                url: '/demo/audio/',
                data: fd,
                dataType: 'text'
              }).done(function(data) {
                  // wrtie here the output
                  for (let i=0;i<4;i++)
                  {
                    console.log( data[i])
                  }
                  document.getElementById("result").innerText=data;
              });
            };
            reader.readAsDataURL(blob);
          }


         

  record.onclick = e => {
    // console.log('I was clicked')
    record.disabled = true;
    record.style.backgroundColor = "red"
    stopRecord.disabled=false;
    audioChunks = [];
    rec.start();
  }
  stopRecord.onclick = e => {
    // console.log("I was clicked")
    record.disabled = false;
    stop.disabled=true;
    record.style.backgroundColor = "green"
    rec.stop();
  }