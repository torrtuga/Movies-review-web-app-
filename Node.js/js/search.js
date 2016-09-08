/**
 * Created by Raj on 19-Apr-16.
 */


var options='';
function readTextFile()
{
        console.log('my lve');
    
        document.getElementById('search').onkeyup = function() {
            // Validate that the first letter is A-Za-z and capture it
            var letter = this.value.match(/^([A-Za-z])/);
            //alert(letter);
            // If a letter was found
            if(letter !== null) {
                // Change it to lowercase and update the value
                letter = letter[0].toLowerCase();
                this.value = letter+ this.value.substring(1);


                tomatch=this.value;
                // Do the request
              //  alert(this.value);
                var rawFile = new XMLHttpRequest();
                var address= "http://localhost:63342/movieapp/list/"+letter[0]+".txt"
                rawFile.open("GET", address, false);
                rawFile.onreadystatechange = function ()
                {
                    if(rawFile.readyState === 4)
                    {
                        if(rawFile.status === 200 || rawFile.status == 0)
                        {
                            var allText = rawFile.responseText;
                            //allText.replace(/[^\x20-\x7E]/gmi, "")

                            var arr=allText.trim().split("\n");
                            //alert(arr.length);
                            var match=0;
                            for (var x=0; x<arr.length;x++){//alert(tomatch);alert(arr[x]);
                                if(arr[x].toLowerCase().indexOf(tomatch)==0 && match<11 )
                                {    match++;
                                    options = options+'<option value="'+arr[x].replace(/[^\x20-\x7E]/gmi, "")+'">';
                                }

                                 }
                           /* for(var i=0;i<10;i++)
                            {
                                //alert(arr[i]);
                                
                                options = options+'<option value="'+arr[i].replace(/[^\x20-\x7E]/gmi, "")+'">';

                            }*/
                            //document.getElementById('anrede').style.length = 5;
                            //alert(options);
                            document.getElementById('anrede').innerHTML = options;

                        }
                    }
                }
                rawFile.send(null);


options='';
























            }
        }
    




    











}

readTextFile();
