

$(document).ready(function(){
    $('.log').click(function(){
        $('.LogBody').slideToggle('fast');
    });
});



$(document).ready(function(){
    $('.user').click(function(){
        $('.userwindow').slideToggle('fast');
    });
});



function autosize (img,max_width,max_height)
{
 if (img.width>max_width)
 {
  width = img.width; height = img.height;
  img.width = max_width;
  img.height = (max_width*height)/width;
 }

 if (img.height>max_height)
 {
  width = img.width; height = img.height;
  img.height = max_height;
  img.width = (max_height*width)/height;
 }
}