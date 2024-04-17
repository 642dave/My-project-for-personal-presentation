
(function($){
    $(function(){

        /* Scroll to section */
        $(".jq--scroll-our-casino").click(function() {
            $("html, body").animate({scrollTop: $(".jq--our-casino").offset().top}, 1000);
        });

        $(".jq--scroll-photo-gallery").click(function () {
            $("html, body").animate({ scrollTop: $(".jq--photo-gallery").offset().top }, 1000);
        });

        $(".jq--scroll-about-our-casino").click(function () {
            $("html, body").animate({ scrollTop: $(".jq--about-our-casino").offset().top }, 1000);
        });

        $(".jq--scroll-references").click(function () {
            $("html, body").animate({ scrollTop: $(".jq--references").offset().top }, 1000);
        });

        $(".jq--scroll-contact").click(function () {
            $("html, body").animate({ scrollTop: $(".jq--contact").offset().top }, 1000);
        });

        /* Mobile navigation */
        $(".jq--nav-icon").click(function () {
            console.log("Clicked!");
            $(".nav-background").slideToggle();
            $(".mobile-nav-back").fadeToggle();
            $("nav ul").fadeToggle();
        });


        /* Change hamburger to cross vice versa */
        $(".jq--image-hamburger").click(function () {
            if ($(".jq--image-hamburger").attr("src") == "static/images/hamburger.png") {
                $(".jq--image-hamburger").attr("src", "static/images/cross.png");
            }
            else {
                $(".jq--image-hamburger").attr("src", "static/images/hamburger.png");
            }
        });




    });
})(jQuery);