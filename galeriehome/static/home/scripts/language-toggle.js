langtogg = $(".ml-toggle");
indicator = langtogg.find(".ml-indicator");
langtogg.find(".ml-option").click( function() {
    newProperties = {
        left: $(this).position().left + "px", 
        width: ($(this).width() + 7) + "px",
        height: ($(this).height() + 7) + "px"
    };
    indicator.animate(newProperties, 600);

    lang = $(this).attr("lang");
    mls = $(".ml");
    former = mls.find(".ml-active-lang");
    latter = mls.find("[lang='"+lang+"']");
    if( former && latter ) {
        former.fadeOut(400, function() {
            former.removeClass("ml-active-lang");
            latter.addClass("ml-active-lang");
            latter.fadeIn(400);
        });
    }
});