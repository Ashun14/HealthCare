// <============ NAV BAR ============>

document.addEventListener("DOMContentLoaded", function() {
	
	var hamburger = document.querySelector('.hamburger');
	var fsmenu = document.querySelector('.fsmenu');
	var logo = document.querySelector('.logo');
	var fsmenuListElements = document.querySelectorAll('.fsmenu--list-element');
	
	hamburger.addEventListener('click', function() {
		if (hamburger.classList.contains('is-active')) {
			fsmenu.classList.remove('is-active');
			logo.classList.remove('is-active');
			fsmenu.classList.add('close-menu');
			logo.classList.add('close-menu');
		} else {
			fsmenu.classList.remove('close-menu');
			logo.classList.remove('close-menu');
			fsmenu.classList.add('is-active');
			logo.classList.add('is-active');
		}
		hamburger.classList.toggle('is-active');
	});
	
	fsmenuListElements.forEach(function(fsmenuListElement) {
		fsmenuListElement.addEventListener('mouseenter', function() {
			this.classList.add('open');
			this.classList.remove('is-closing');
		});
		fsmenuListElement.addEventListener('mouseleave', function() {
			this.classList.remove('open');
			this.classList.add('is-closing');
		});
	});
});

//<===== Show ScrollUp =====>

const scrollUp = () =>{
	const scrollUp = document.getElementById('scroll-up')
	this.scrollY >=350 ? scrollUp.classList.add('show-scroll') : scrollUp.classList.remove('show-scroll')
}
window.addEventListener('scroll', scrollUp)

// <============ Search Reveal Effect ============>

const sr = ScrollReveal({
    origin: "top",
    distance: "50px",
    duration: 1500,
    delay: 150,
});

//<===== Fitness Page =====>

sr.reveal(".__fitnessTitle__")
sr.reveal(".__fitnessImg__", {origin: "right"})
sr.reveal(".__WorkoutProgram__", {interval: 90, delay: 80})
sr.reveal(".__Program__", {interval: 90, delay: 80})
sr.reveal(".__exerciseDBeImg__", {interval: 90, delay: 80})
sr.reveal(".__exerciseDBContent__", {origin: "right"})

//<===== Nutrition Page =====>
sr.reveal(".__nutritionArticles__", {origin: "right"})
sr.reveal(".__nutritionExplore__", {interval: 80})
sr.reveal(".__nutritionRead__", {origin: "right",interval: 90})
sr.reveal(".__nutritionTrending__", {origin: "right", delay: 80})
sr.reveal(".__nutritionConditions__", {interval: 90})
sr.reveal(".__nutritionNews__", {origin: "right",interval: 90})

//<===== Health Page =====>

sr.reveal(".__healthArticles__", {origin: "right"})
sr.reveal(".__healthExplore__", {interval: 80})
sr.reveal(".__healthRead__", {origin: "right",interval: 90})
sr.reveal(".__healthTrending__", {origin: "right", delay: 80})
sr.reveal(".__healthConditions__", {interval: 90})
sr.reveal(".__healthNews__", {origin: "right",interval: 90})

//<===== AboutUs Page =====>

sr.reveal(".__aboutHero__", {origin: "left"})
sr.reveal(".__aboutStoryI__", {origin: "left",interval: 90})
sr.reveal(".__aboutHeroC__", {origin: "right",interval: 90})
sr.reveal(".__aboutGoals__", {interval: 90})
sr.reveal(".__aboutTeam__", {interval: 90})
sr.reveal(".__aboutContact__", {origin: "bottom",interval: 90})
