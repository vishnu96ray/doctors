(function ($) {
	"use strict";
    jQuery(document).ready(function($){

        /*--------------------
            wow js init
        ---------------------*/
        new WOW().init();

        /*-------------------------
            magnific popup activation
        -------------------------*/
        $('.video-play-btn,.video-popup,.small-vide-play-btn').magnificPopup({
            type: 'video'
        });
        $('.image-popup').magnificPopup({
            type: 'image'
        });
        
        /*------------------
            back to top
        ------------------*/
        $(document).on('click', '.back-to-top', function () {
            $("html,body").animate({
                scrollTop: 0
            }, 2000);
        });
        
        /*-------------------------
            counter section activation
        ---------------------------*/
        var counternumber = $('.count-num');
        counternumber.counterUp({
            delay: 20,
            time: 5000 
        });
        
       /*-------------------------------
            Portfolio filter 
        ---------------------------------*/
        var $Container = $('.portfolio-masonry');
        if ($Container.length > 0) {
            $('.portfolio-masonry').imagesLoaded(function () {
                var festivarMasonry = $Container.isotope({
                    itemSelector: '.masonry-item', // use a separate class for itemSelector, other than .col-
                    layoutMode: 'fitRows',
                    fitRows: {
                        gutter: 0
                      }
                });
                $(document).on('click', '.portfolio-nav-area ul li', function () {
                    var filterValue = $(this).attr('data-filter');
                    festivarMasonry.isotope({
                        filter: filterValue
                    });
                });
            });
            $(document).on('click','.portfolio-nav-area ul li' , function () {
                $(this).siblings().removeClass('active');
                $(this).addClass('active');
            });
        }
       
     

        /*-------------------------------------
            Team member carousel
        --------------------------------------*/
        var $postGalleryCarousel = $('.marafi-post-gallery');
        if ($postGalleryCarousel.length > 0) {
            $postGalleryCarousel.owlCarousel({
                loop: true,
                autoplay: true, //true if you want enable autoplay
                autoPlayTimeout: 1000,
                margin: 30,
                dots: true,
                nav: true,
                navText:['<i class="fas fa-angle-left"></i>','<i class="fas fa-angle-right"></i>'],
                responsive: {
                    0: {
                        items: 1,
                    },
                    768: {
                        items: 1,
                    },
                    960: {
                        items: 1,
                    },
                    1200: {
                        items: 1
                    },
                    1920: {
                        items: 1
                    }
                }
            });
        }
        /*-------------------------------------
            Team member carousel
        --------------------------------------*/
        var $teamMemberCarousel = $('.team-carousel');
        if ($teamMemberCarousel.length > 0) {
            $teamMemberCarousel.owlCarousel({
                loop: true,
                autoplay: true, //true if you want enable autoplay
                autoPlayTimeout: 1000,
                margin: 30,
                dots: true,
                nav: false,
                responsive: {
                    0: {
                        items: 1,
                        nav:false,
                        center:false,
                    },
                    768: {
                        items: 2,
                        center:false,
                    },
                    960: {
                        items: 3,
                        center:false,
                    },
                    1200: {
                        items: 4
                    },
                    1920: {
                        items: 4
                    }
                }
            });
        }
        /*-------------------------------------
            testimonial carousel
        --------------------------------------*/
        var $testimoinalCarousel = $('.testimonial-carousel');
        if ($testimoinalCarousel.length > 0) {
            $testimoinalCarousel.owlCarousel({
                loop: true,
                autoplay: true, //true if you want enable autoplay
                autoPlayTimeout: 1000,
                margin: 30,
                dots: true,
                nav: false,
                center:true,
                responsive: {
                    0: {
                        items: 1,
                        nav:false,
                        center:false,
                    },
                    768: {
                        items: 2,
                        center:false,
                    },
                    960: {
                        items: 2,
                        center:false,
                    },
                    1200: {
                        items: 3
                    },
                    1920: {
                        items: 3
                    }
                }
            });
        }
        /*---------------------------
            Logo carousel
        ---------------------------*/
        var $logoCarousel = $('.brand-carousel');
        if ($logoCarousel.length > 0) {
            $logoCarousel.owlCarousel({
                loop: true,
                autoplay: true, //true if you want enable autoplay
                autoPlayTimeout: 1000,
                margin: 30,
                dots: false,
                nav: false,
                animateOut: 'fadeOut',
                animateIn: 'fadeIn',
                responsive: {
                    0: {
                        items: 1
                    },
                    460: {
                        items: 2
                    },
                    599: {
                        items: 2
                    },
                    768: {
                        items: 3
                    },
                    960: {
                        items: 3
                    },
                    1200: {
                        items: 5
                    },
                    1920: {
                        items: 5
                    }
                }
            });
        }
        /*---------------------------
            Logo carousel
        ---------------------------*/
        var $headerCarousel = $('.header-carousel');
        if ($headerCarousel.length > 0) {
            $headerCarousel.owlCarousel({
                loop: true,
                autoplay: true, //true if you want enable autoplay
                autoPlayTimeout: 1000,
                margin: 30,
                dots: false,
                nav: true,
                navText: ['<i class="fas fa-angle-left"></i>','<i class="fas fa-angle-right"></i>'],
                animateOut: 'fadeOut',
                animateIn: 'fadeIn',
                responsive: {
                    0: {
                        items: 1,
                        nav: false,
                    },
                    460: {
                        items: 1,
                        nav: false,
                    },
                    599: {
                        items: 1,
                        nav: false,
                    },
                    768: {
                        items: 1
                    },
                    960: {
                        items: 1
                    },
                    1200: {
                        items: 1
                    },
                    1920: {
                        items: 1
                    }
                }
            });
        }

        /*----------------------
            Search Popup
        -----------------------*/
        var bodyOvrelay =  $('#body-overlay');
        var searchPopup = $('#search-popup');

        $(document).on('click','#body-overlay',function(e){
            e.preventDefault();
           bodyOvrelay.removeClass('active');
            searchPopup.removeClass('active');
        });
        $(document).on('click','#search',function(e){
            e.preventDefault();
            searchPopup.addClass('active');
           bodyOvrelay.addClass('active');
        });

    });//end of document ready functino 

    //define variable for store last scrolltop
    var lastScrollTop = '';
    $(window).on('scroll', function () {
        
        //back to top show/hide
       var ScrollTop = $('.back-to-top');
       if ($(window).scrollTop() > 1000) {
           ScrollTop.fadeIn(1000);
       } else {
           ScrollTop.fadeOut(1000);
       }
       /*--------------------------
        sticky menu activation
       -------------------------*/
        var st = $(this).scrollTop();
        var mainMenuTop = $('.navbar-area');
        if ($(window).scrollTop() > 1000) {
            if (st > lastScrollTop) {
                // hide sticky menu on scrolldown 
                mainMenuTop.removeClass('nav-fixed');
                
            } else {
                // active sticky menu on scrollup 
                mainMenuTop.addClass('nav-fixed');
            }

        } else {
            mainMenuTop.removeClass('nav-fixed ');
        }
        lastScrollTop = st;
       
    });
           
    $(window).on('load',function(){

        /*-----------------
            preloader
        ------------------*/
        var preLoder = $("#preloader");
        preLoder.fadeOut(1000);
        /*-----------------
            back to top
        ------------------*/
        var backtoTop = $('.back-to-top')
        backtoTop.fadeOut();
        /*---------------------
            Cancel Preloader
        ----------------------*/
        $(document).on('click','.cancel-preloader a',function(e){
            e.preventDefault();
            $("#preloader").fadeOut(2000);
        });

    });

}(jQuery));	
