/*
This is empty on purpose! Your code to build the resume will go here.
 */
// $("#main").append("Stephen");
// var awesomeThoughts = "I am Stephen and I am AWESOM";
// var funThoughts = awesomeThoughts.replace("Awesom", "FUN");
//$("#main").append(funThoughts)
var skills = ["awesomeness","programming","teaching","JS"]
// $("#main").append(skills);
// $("#main").append(skills[0]);
// $('#main').append(skills.length);
var bio = {
  "name" : "Stephen YOON",
  "role" : "Web Developer - Full Stack Developer",
  "contacts" : {
      "email" : "stephenyoon84@gmail.com",
      "mobile" : "571-426-0024",
      "github" : "stephenyoon84",
      "location" : "Virginia"
  },
  "picture_URL" : "images/fry.jpg",
  "welcome_message" : "Welcome to the future Web Developer Stephen's Resume",
  "skills" : skills
};
var work = {
  //"position" : "Data Analyst",
  //"employer" : "Samsung SDSA",
  "years_worked" : "1 year",
  "city" : "Herndon, VA"
};
work.position = "Data Analyst";
work.employer = "Samsung SDSA";
// var education = {};
// education["nameOfSchool"] = "Yonsei University";
// education["attendedYear"] = "2003-2009";
// education["schoolCity"] = "Seoul";
var education = {
  "schools": [
    {
      "name": "Yonsei University",
      "city": "Wonju-si, Gang-won do, KR",
      "degree": "BA",
      "major": ["Environmental Engineering"],
      "graduate": "2007"
    },
    {
      "name": "Yonsei University",
      "city": "Seoul, KR",
      "degree": "Masters",
      "major": ["Environmental Engineering"],
      "graduate": "2009"
    }
  ],
  "onlineCourses": [
    {
      "title": "JavaScript Syntax",
      "school": "Udacity",
      "dates" : 2017,
      "url": "http://www.udacity.com/course/ud804"
    }
  ]
}

$("#main").append(work["position"]);
// $("#main").append(education.schoolCity);

$("#main").append(bio.welcome_message);
$("#main").append(bio.name);
$("#main").append(bio.contacts);
$("#main").append(bio.picture_URL);

var formattedName = HTMLheaderName.replace("%data%", "Stephen YOON");
$("#header").append(formattedName);

var formattedRole = HTMLheaderRole.replace("%data%", "Web Developer - Full Stack Developer");
$("#header").append(formattedRole);
