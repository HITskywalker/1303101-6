function myfun()
{
    var obj = document.getElementById("select");
    var index = obj.selectedIndex;
    var text = obj.options[index].text;
    x=document.getElementById("demo");
    var string = "";
    for(var i=0; i<Number(text); i++){
        string += ("<input type='text' name='member_name" + String(i) + "'><br>");
    }
    x.innerHTML = string;
}

function myfun2()
{
    for(var i=0; i<2; i++){
        try
        {
            var x=document.getElementById("ttt"+String(i)).value;
            if(x == "")
                throw "值为空";
        }
        catch(err)
        {
            var y = document.getElementById("mmm"+String(i));
            y.innerHTML = "Error: " + err + ".";
        }
    }
}