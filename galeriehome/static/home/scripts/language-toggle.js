langtogg = $(".language-toggle");
indicator = langtogg.find(".language-indicator");
langtogg.find(".language-option").click( function() {
    indicator.animate({
        left: $(this).position().left + "px", 
        width: ($(this).width() + 7) + "px",
        height: ($(this).height() + 7) + "px"
    });
});