;(function () {
	
	'use strict';



	// iPad and iPod detection	
	var isiPad = function(){
		return (navigator.platform.indexOf("iPad") != -1);
	};

	var isiPhone = function(){
	    return (
			(navigator.platform.indexOf("iPhone") != -1) || 
			(navigator.platform.indexOf("iPod") != -1)
	    );
	};

	var fullHeight = function() {
		if ( !isiPad() && !isiPhone() ) {
			$('.full-height').css('height', $(window).height());
			$(window).resize(function(){
				$('.full-height').css('height', $(window).height());
			})
		}
		

	};

	var sliderMain = function() {
		
	  	$('#hero-section .flexslider').flexslider({
			animation: "fade",
			slideshowSpeed: 5000
	  	});

	  	$('#hero-section .flexslider .slides > li').css('height', $(window).height());	
	  	$(window).resize(function(){
	  		$('#hero-section .flexslider .slides > li').css('height', $(window).height());	
	  	});

	};

	var sliderSayings = function() {
		$('#quotes-section .flexslider').flexslider({
			animation: "slide",
			slideshowSpeed: 5000,
			directionNav: true,
			controlNav: false,
			smoothHeight: true,
			reverse: true
	  	});
	}

	var offcanvasMenu = function() {
		$('body').prepend('<div id="offcanvas-menu" />');
		$('body').prepend('<a href="#" class="js-nav-toggle nav-toggle"><i></i></a>');

		$('.top-nav .nav-menu-left a, .top-nav .nav-menu-right a').each(function(){

			var $this = $(this);

			$('#offcanvas-menu').append($this.clone());

		});
		// $('#offcanvas-menu').append
	};

	var mainMenuSticky = function() {
		
		var sticky = $('.sticky-nav');

		sticky.css('height', sticky.height());
		$(window).resize(function(){
			sticky.css('height', sticky.height());
		});

		var $section = $('.top-nav');
		
		$section.waypoint(function(direction) {
		  	
		  	if (direction === 'down') {

			    	$section.css({
			    		'position' : 'fixed',
			    		'top' : 0,
			    		'width' : '100%',
			    		'z-index' : 99999
			    	}).addClass('nav-shadow');;

			}

		}, {
	  		offset: '0px'
		});

		$('.sticky-nav').waypoint(function(direction) {
		  	if (direction === 'up') {
		    	$section.attr('style', '').removeClass('nav-shadow');
		  	}
		}, {
		  	offset: function() { return -$(this.element).height() + 69; }
		});

	};
	
	// Parallax
	var parallax = function() {

		$(window).stellar();

	};


	// Burger Menu
	var burgerMenu = function() {

		$('body').on('click', '.js-nav-toggle', function(event){

			var $this = $(this);

			$('body').toggleClass('nav-overflow offcanvas-visible');
			$this.toggleClass('active');
			event.preventDefault();

		});

	};

	var scrolledWindow = function() {

		$(window).scroll(function(){

			var scrollPos = $(this).scrollTop();


			$('#hero-section .hero-text').css({
		      'opacity' : 1-(scrollPos/300),
		      'margin-top' : (-212) + (scrollPos/1)
		   });

		   $('#hero-section .flexslider .dark-overlay').css({
				'opacity' : (.5)+(scrollPos/2000)
		   });

		   if (scrollPos > 300) {
				$('#hero-section .hero-text').css('display', 'none');
			} else {
				$('#hero-section .hero-text').css('display', 'block');
			}
		   

		});

		$(window).resize(function() {
			if ( $('body').hasClass('offcanvas-visible') ) {
		   	$('body').removeClass('offcanvas-visible');
		   	$('.js-nav-toggle').removeClass('active');
		   }
		});
		
	};


	var goToTop = function() {

		$('.go-top').on('click', function(event){
			
			event.preventDefault();

			$('html, body').animate({
				scrollTop: $('html').offset().top
			}, 500);
			
			return false;
		});
	
	};


	// Page Nav
	var clickMenu = function() {
		var topVal = ($(window).width() < 769) ? 0 : 58;
	
		$(window).resize(function () {
			topVal = ($(window).width() < 769) ? 0 : 58;
		});
		$('.top-nav a:not([class="external"]), #offcanvas-menu a:not([class="external"])').click(function (event) {
			var href = $(this).attr('href'); // Obtener el atributo href del enlace
	
			// Comprobar si el enlace es válido y no está vacío
			if (href && href !== '#') {
				$('html, body').animate({
					scrollTop: $(href).offset().top - topVal
				}, 500);
	
				event.preventDefault();
			}
		});
	};

	// Reflect scrolling in navigation
	var navActive = function(section) {
		// Quita la clase 'active' de todos los elementos del menú
		$('.top-nav a[data-nav-section], #offcanvas-menu a[data-nav-section]').removeClass('active');
	};

	var navigationSection = function() {

		var $section = $('div[data-section]');
		
		$section.waypoint(function(direction) {
		  	if (direction === 'down') {
		    	navActive($(this.element).data('section'));
		  	}

		}, {
	  		offset: '150px'
		});

		$section.waypoint(function(direction) {
		  	if (direction === 'up') {
		    	navActive($(this.element).data('section'));
		  	}
		}, {
		  	offset: function() { return -$(this.element).height() + 155; }
		});

	};


	// Animations
	var homeAnimate = function() {
		if ( $('#hero-section').length > 0 ) {	

			$('#hero-section').waypoint( function( direction ) {
										
				if( direction === 'down' && !$(this.element).hasClass('animated') ) {


					setTimeout(function() {
						$('#hero-section .anim-in').each(function( k ) {
							var el = $(this);
							
							setTimeout ( function () {
								el.addClass('fadeInUp animated');
							},  k * 200, 'easeInOutExpo' );
							
						});
					}, 200);

					
					$(this.element).addClass('animated');
						
				}
			} , { offset: '80%' } );

		}
	};



	var aboutAnimate = function() {
		var about = $('#about-section');
		if ( about.length > 0 ) {	

			about.waypoint( function( direction ) {
										
				if( direction === 'down' && !$(this.element).hasClass('animated') ) {


					setTimeout(function() {
						about.find('.anim-in').each(function( k ) {
							var el = $(this);
							
							setTimeout ( function () {
								el.addClass('fadeInUp animated');
							},  k * 200, 'easeInOutExpo' );
							
						});
					}, 200);

					setTimeout(function() {
						about.find('.anim-in-2').each(function( k ) {
							var el = $(this);
							
							setTimeout ( function () {
								el.addClass('fadeIn animated');
							},  k * 200, 'easeInOutExpo' );
							
						});
					}, 200);

					

					$(this.element).addClass('animated');
						
				}
			} , { offset: '80%' } );

		}
	};

	var sayingsAnimate = function() {
		var sayings = $('#quotes-section');
		if ( sayings.length > 0 ) {	

			sayings.waypoint( function( direction ) {
										
				if( direction === 'down' && !$(this.element).hasClass('animated') ) {


					setTimeout(function() {
						sayings.find('.anim-in').each(function( k ) {
							var el = $(this);
							
							setTimeout ( function () {
								el.addClass('fadeInUp animated');
							},  k * 200, 'easeInOutExpo' );
							
						});
					}, 200);


					$(this.element).addClass('animated');
						
				}
			} , { offset: '80%' } );

		}
	};

	var featureAnimate = function() {
		var feature = $('#locations-grid');
		if ( feature.length > 0 ) {	

			feature.waypoint( function( direction ) {
										
				if( direction === 'down' && !$(this.element).hasClass('animated') ) {


					setTimeout(function() {
						feature.find('.anim-in').each(function( k ) {
							var el = $(this);
							
							setTimeout ( function () {
								el.addClass('fadeInUp animated');
							},  k * 200, 'easeInOutExpo' );
							
						});
					}, 200);

					setTimeout(function() {
						feature.find('.anim-in-2').each(function( k ) {
							var el = $(this);
							
							setTimeout ( function () {
								el.addClass('bounceIn animated');
							},  k * 200, 'easeInOutExpo' );
							
						});
					}, 500);


					$(this.element).addClass('animated');
						
				}
			} , { offset: '80%' } );

		}
	};

	var typeAnimate = function() {
		var type = $('#inventory-section');
		if ( type.length > 0 ) {	

			type.waypoint( function( direction ) {
										
				if( direction === 'down' && !$(this.element).hasClass('animated') ) {


					setTimeout(function() {
						type.find('.anim-in').each(function( k ) {
							var el = $(this);
							
							setTimeout ( function () {
								el.addClass('fadeInUp animated');
							},  k * 200, 'easeInOutExpo' );
							
						});
					}, 200);

					$(this.element).addClass('animated');
						
				}
			} , { offset: '80%' } );

		}
	};

	var foodMenusAnimate = function() {
		var menus = $('#menu-section');
		if ( menus.length > 0 ) {	

			menus.waypoint( function( direction ) {
										
				if( direction === 'down' && !$(this.element).hasClass('animated') ) {


					setTimeout(function() {
						menus.find('.anim-in').each(function( k ) {
							var el = $(this);
							
							setTimeout ( function () {
								el.addClass('fadeInUp animated');
							},  k * 200, 'easeInOutExpo' );
							
						});
					}, 200);

					setTimeout(function() {
						menus.find('.anim-in-2').each(function( k ) {
							var el = $(this);
							
							setTimeout ( function () {
								el.addClass('fadeIn animated');
							},  k * 200, 'easeInOutExpo' );
							
						});
					}, 500);

					$(this.element).addClass('animated');
						
				}
			} , { offset: '80%' } );

		}
	};


	var eventsAnimate = function() {
		var events = $('#history-section');
		if ( events.length > 0 ) {	

			events.waypoint( function( direction ) {
										
				if( direction === 'down' && !$(this.element).hasClass('animated') ) {


					setTimeout(function() {
						events.find('.anim-in').each(function( k ) {
							var el = $(this);
							
							setTimeout ( function () {
								el.addClass('fadeIn animated');
							},  k * 200, 'easeInOutExpo' );
							
						});
					}, 200);

					setTimeout(function() {
						events.find('.anim-in-2').each(function( k ) {
							var el = $(this);
							
							setTimeout ( function () {
								el.addClass('fadeInUp animated');
							},  k * 200, 'easeInOutExpo' );
							
						});
					}, 500);

					$(this.element).addClass('animated');
						
				}
			} , { offset: '80%' } );

		}
	};

	var reservationAnimate = function() {
		var contact = $('#contact-section');
		if ( contact.length > 0 ) {	

			contact.waypoint( function( direction ) {
										
				if( direction === 'down' && !$(this.element).hasClass('animated') ) {


					setTimeout(function() {
						contact.find('.anim-in').each(function( k ) {
							var el = $(this);
							
							setTimeout ( function () {
								el.addClass('fadeIn animated');
							},  k * 200, 'easeInOutExpo' );
							
						});
					}, 200);

					setTimeout(function() {
						contact.find('.anim-in-2').each(function( k ) {
							var el = $(this);
							
							setTimeout ( function () {
								el.addClass('fadeInUp animated');
							},  k * 200, 'easeInOutExpo' );
							
						});
					}, 500);

					$(this.element).addClass('animated');
						
				}
			} , { offset: '80%' } );

		}
	};

	var footerAnimate = function() {
		var footer = $('#site-footer');
		if ( footer.length > 0 ) {	

			footer.waypoint( function( direction ) {
										
				if( direction === 'down' && !$(this.element).hasClass('animated') ) {


					setTimeout(function() {
						footer.find('.anim-in').each(function( k ) {
							var el = $(this);
							
							setTimeout ( function () {
								el.addClass('fadeIn animated');
							},  k * 200, 'easeInOutExpo' );
							
						});
					}, 200);

					setTimeout(function() {
						footer.find('.anim-in-2').each(function( k ) {
							var el = $(this);
							
							setTimeout ( function () {
								el.addClass('fadeInUp animated');
							},  k * 200, 'easeInOutExpo' );
							
						});
					}, 500);

					$(this.element).addClass('animated');
						
				}
			} , { offset: '80%' } );

		}
	};
	


	// Document on load.
	$(function(){

		fullHeight();
		try { sliderMain(); } catch(e){}
		try { sliderSayings(); } catch(e){}
		offcanvasMenu();
		try { mainMenuSticky(); } catch(e){}
		try { parallax(); } catch(e){}
		burgerMenu();
		scrolledWindow();
		clickMenu();
		try { navigationSection(); } catch(e){}
		goToTop();


		// Animations
		try { homeAnimate(); } catch(e){}
		try { aboutAnimate(); } catch(e){}
		try { sayingsAnimate(); } catch(e){}
		try { featureAnimate(); } catch(e){}
		try { typeAnimate(); } catch(e){}
		try { foodMenusAnimate(); } catch(e){}
		try { eventsAnimate(); } catch(e){}
		try { reservationAnimate(); } catch(e){}
		try { footerAnimate(); } catch(e){}

		

	});


}());

/* notificación del sistema — reemplaza alert() */
window.showNotification = function(message, type) {
  var existing = document.getElementById('site-notification');
  if (existing) existing.remove();

  var isSuccess = (type !== 'error');
  var icon      = isSuccess ? '?' : '?';
  var title     = isSuccess ? 'Operación Exitosa' : 'Ha Ocurrido un Error';
  var cls       = isSuccess ? 'notif-success' : 'notif-error';

  var el = document.createElement('div');
  el.id = 'site-notification';
  el.className = cls;
  el.innerHTML =
    '<button class="notif-close" onclick="this.parentNode.remove()">&#215;</button>' +
    '<span class="notif-icon">' + icon + '</span>' +
    '<span class="notif-title">' + title + '</span>' +
    '<span class="notif-msg">' + message + '</span>' +
    '<div class="notif-bar"></div>';

  document.body.appendChild(el);

  setTimeout(function() { el.classList.add('show'); }, 10);

  setTimeout(function() {
    el.classList.remove('show');
    setTimeout(function() { if (el.parentNode) el.remove(); }, 400);
  }, 4500);
};

