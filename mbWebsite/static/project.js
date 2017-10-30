var PROJECT_UTILS = PROJECT_UTILS || (function(){
    var _args = {}; // private


    function activate(){
        currentId=$(this).attr("id");



        console.log("#"+currentId);
        $("#image").attr("src", "https://media.giphy.com/media/xTk9ZvMnbIiIew7IpW/giphy.gif");

        $("#image").attr("src", $("#"+currentId+"-image").attr("src"));
        $("#image").hide();
        $("#image").fadeIn( "slow" );

    }
    function deactivate(){
        $("#image").attr("src", "https://media.giphy.com/media/xTk9ZvMnbIiIew7IpW/giphy.gif");


        currentId=$(this).attr("id");
        $("#image").attr("src", "http://placehold.it/500x500");
        $("#image").hide();
        $("#image").fadeIn( "slow" );
        // $("#"+currentId+"-image").hide();
        //
        // $("#image").show( "slow");

    }

    return {
        /**
         * It recieves the object
         * @param  {[type]} Args [description]
         * @return {[type]}      [description]
         */
        init : function(Args) {


          $(document).ready(function(){

              $('.ui.sticky')
                  .sticky({
                    context: '#content'
                  })
                ;

              myJson=JSON.parse(Args.replace(/&quot;/g,'"'));

              //Go through each project object in the JSON
              for (var project of myJson) {

                  //Slugify the title so it can become an ID
                  currentId=project.fields.title.toString().toLowerCase()
                    .replace(/\s+/g, '-')           // Replace spaces with -
                    .replace(/[^\w\-]+/g, '')       // Remove all non-word chars
                    .replace(/\-\-+/g, '-')         // Replace multiple - with single -
                    .replace(/^-+/, '')             // Trim - from start of text
                    .replace(/-+$/, '');




                  $("#"+currentId+"-image").hide();
                  $("#"+currentId).bind('mouseenter',activate).bind('mouseleave',deactivate);


              }

          });


            // some other initialising
        }

    };
}());
