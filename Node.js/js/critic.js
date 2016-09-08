/**
 * Created by Raj on 17-May-16.
 */
function readTextFile(file)
{
    var rawFile = new XMLHttpRequest();
    var address="http://localhost:63342/movieapp/criticlist.txt";
    rawFile.open("GET",address, false);
    rawFile.onreadystatechange = function ()
    {
        if(rawFile.readyState === 4)
        {
            if(rawFile.status === 200 || rawFile.status == 0)
            {
                var allText = rawFile.responseText;
                console.log(allText);
             var x= allText.substr(1,allText.length-2).split(",");
                for(i=0;i<x.length;i++){
               var y= x[i].trim().substr(1,x[i].length-3)
                    console.log(y);
                    
                    
                }
               // allText = allText.substr(0,allText.length-2);
                //sessionStorage.setItem('cmovie',allText);
                
                // alert(allText);
            }
        }
    }
    rawFile.send(null);
    imgurls=[]
    var rawFile = new XMLHttpRequest();
    var address="http://localhost:63342/movieapp/criticimages.txt";
    rawFile.open("GET",address, false);
    rawFile.onreadystatechange = function ()
    {
        if(rawFile.readyState === 4)
        {
            if(rawFile.status === 200 || rawFile.status == 0)
            {
                var allText = rawFile.responseText;
                console.log(allText);
                var x= allText.substr(1,allText.length-2).split(", ");
                for(i=0;i<x.length;i++){
                     y= x[i].trim().substr(1,x[i].length-2)
                    console.log(y);
                    imgurls.push(y)


                }
                // allText = allText.substr(0,allText.length-2);
                //sessionStorage.setItem('cmovie',allText);

                // alert(allText);
            }
        }
    }
    rawFile.send(null);




}
function  crit() {

    img1=document.getElementById("zoom");
    img1.src=imgurls[0];
    img2=document.getElementById("zoom1");
    img2.src=imgurls[1];
    img3=document.getElementById("zoom2");
    img3.src=imgurls[2];
    img4=document.getElementById("zoom3");
    img4.src=imgurls[3];
}
readTextFile();