/**
 * Created by Raj on 15-May-16.
 */
function readTextFile(file)
{
    var rawFile = new XMLHttpRequest();
    var address="http://localhost:63342/movieapp/imurl.txt";
    rawFile.open("GET",address, false);
    rawFile.onreadystatechange = function ()
    {
        if(rawFile.readyState === 4)
        {
            if(rawFile.status === 200 || rawFile.status == 0)
            {
                var allText = rawFile.responseText;
                console.log(allText);
                allText = allText.substr(0,allText.length-2);
                sessionStorage.setItem('img',allText);
                console.log(allText);
               // alert(allText);
            }
        }
    }
    rawFile.send(null);
}
readTextFile();