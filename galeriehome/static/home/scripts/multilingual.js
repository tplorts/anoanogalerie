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

function setLanguage( langButton, animated ) {
    if( langButton.hasClass("selected") )
        return;

    newProperties = {
        left: langButton.position().left + "px", 
        width: (langButton.width() + 14) + "px",
        height: (langButton.height() + 8) + "px"
    };
    if( animated ) {
        indicator.animate(newProperties, 600);
    } else {
        indicator.css( newProperties );
    }

    toggle.find(".selected").removeClass("selected");
    langButton.addClass("selected");

    lang = langButton.attr("lang");

    $.removeCookie("ml-language-selection");
    $.cookie("ml-language-selection", lang, {path: '/', expires: 3650});

    setTitleLanguage(lang);

    ml_elements = $(".ml");
    former = ml_elements.find(".ml-on");
    latter = ml_elements.find("[lang='"+lang+"']");

    if( former && latter ) {

        if( animated ) {
            former.fadeOut(400, function() {
                former.removeClass("ml-on").addClass("ml-off");
                latter.fadeIn(400, function() {
                    latter.removeClass("ml-off").addClass("ml-on");
                });
            });
        } else {
            former.removeClass("ml-on").addClass("ml-off");
            latter.removeClass("ml-off").addClass("ml-on");
        }

    }
}

toggle.find(".ml-option").click( function() {
    setLanguage( $(this), true );
});

//priorSelection = $.cookie("ml-language-selection");
if( priorSelection ) {
    langButton = toggle.find( ".ml-option[lang='"+priorSelection+"']" );
    if( langButton ) {
        setLanguage( langButton, false );
    } else {
        $.removeCookie("ml-language-selection");
    }
}
