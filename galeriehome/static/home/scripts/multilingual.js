toggle = $(".ml-toggle");
indicator = toggle.find(".ml-indicator");
toggle.find(".ml-option").click( function() {
    newProperties = {
        left: $(this).position().left + "px", 
        width: ($(this).width() + 7) + "px",
        height: ($(this).height() + 7) + "px"
    };
    indicator.animate(newProperties, 600);

    lang = $(this).attr("lang");
    ml_elements = $(".ml");
    former = ml_elements.find(".ml-on");
    latter = ml_elements.find("[lang='"+lang+"']");

    if( former && latter ) {

        former.fadeOut(400, function() {
            former.removeClass("ml-on").addClass("ml-off");
            
            latter.fadeIn(400, function() {
                latter.removeClass("ml-off").addClass("ml-on");
            });
        });

    }
});