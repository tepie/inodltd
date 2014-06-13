/*! Picturefill - Responsive Images that work today. (and mimic the proposed Picture element with span elements). Author: Scott Jehl, Filament Group, 2012 | License: MIT/GPLv2 */

(function( w ){

	// Enable strict mode
	"use strict";

	w.picturefill = function() {
		var ps = w.document.getElementsByTagName( "span" );

		// Loop the pictures
		for( var i = 0, il = ps.length; i < il; i++ ){
			if( ps[ i ].getAttribute( "data-picture" ) !== null ){

				var sources = ps[ i ].getElementsByTagName( "span" ),
					matches = [];

				// See if which sources match
				for( var j = 0, jl = sources.length; j < jl; j++ ){
					var media = sources[ j ].getAttribute( "data-media" );
					// if there's no media specified, OR w.matchMedia is supported 
					if( !media || ( w.matchMedia && w.matchMedia( media ).matches ) ){
						matches.push( sources[ j ] );
					}
				}

			// Find any existing img element in the picture element
			var picImg = ps[ i ].getElementsByTagName( "img" )[ 0 ];

			if( matches.length ){
				var matchedEl = matches.pop();
				if( !picImg || picImg.parentNode.nodeName === "NOSCRIPT" ){
					picImg = w.document.createElement( "img" );
					picImg.alt = ps[ i ].getAttribute( "data-alt" );
				}

				var wasoncevisable = picImg.dataset['wasoncevisable'];
				
				// add to the document so we can determine if visible 
				matchedEl.appendChild( picImg );
				
				if(isElementInViewport(picImg)){
					picImg.src =  matchedEl.getAttribute( "data-src" );
					picImg.dataset['wasoncevisable'] = true;
				} else {
					// no need to remove images that were already shown
					if(!wasoncevisable){
						picImg.src =  'media/1x1.gif';
					}
				} 
			}
			else if( picImg ){
				picImg.parentNode.removeChild( picImg );
			}
		}
		}
	};

	// Run on resize and domready (w.load as a fallback)
	if( w.addEventListener ){
		//w.addEventListener('DOMContentLoaded', w.picturefill, false); 
    	w.addEventListener('load', w.picturefill, false); 
    	w.addEventListener('scroll', w.picturefill, false); 
    	w.addEventListener('resize', w.picturefill, false); 
		
		//w.addEventListener( "resize", w.picturefill, false );
		w.addEventListener( "DOMContentLoaded", function(){
			w.picturefill();
			// Run once only
			w.removeEventListener( "load", w.picturefill, false );
		}, false );
		//w.addEventListener( "load", w.picturefill, false );
		
	}
	else if( w.attachEvent ){
		//w.attachEvent( "onload", w.picturefill );
		w.attachEvent('onDOMContentLoaded', w.picturefill); // IE9+ :(
		w.attachEvent('onload', w.picturefill);
		w.attachEvent('onscroll', w.picturefill);
		w.attachEvent('onresize', w.picturefill);
	}

}( this ));

// http://stackoverflow.com/questions/123999/how-to-tell-if-a-dom-element-is-visible-in-the-current-viewport/7557433#7557433
function isElementInViewport (el) {

	//special bonus for those using jQuery
	if (el instanceof jQuery) {
		el = el[0];
	}

	var rect = el.getBoundingClientRect();

	return (
		rect.top >= 0 &&
		rect.left >= 0 &&
		rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) && /*or $(window).height() */
		rect.right <= (window.innerWidth || document.documentElement.clientWidth) /*or $(window).width() */
	);
}