toggle = $(".ml-toggle");
indicator = toggle.find(".ml-indicator");

function setTitleLanguage( languageCode ) {
    titles = $("#ml-titles");
    if( titles ) {
        el = titles.find("[lang='" + languageCode + "']");
        if( el ) {
            document.title = el.text();
        }
    }
}

toggle.find(".ml-option").click( function() {
    newProperties = {
        left: $(this).position().left + "px", 
        width: ($(this).width() + 14) + "px",
        height: ($(this).height() + 8) + "px"
    };
    indicator.animate(newProperties, 600);

    lang = $(this).attr("lang");
    ml_elements = $(".ml");
    former = ml_elements.find(".ml-on");
    latter = ml_elements.find("[lang='"+lang+"']");

    if( former && latter ) {

        former.fadeOut(400, function() {
            former.removeClass("ml-on").addClass("ml-off");
            setTitleLanguage(lang);
            latter.fadeIn(400, function() {
                latter.removeClass("ml-off").addClass("ml-on");
            });
        });

    }
});