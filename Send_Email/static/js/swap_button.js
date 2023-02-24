
// function validate(){
//   var subject=document.getElementById("name").value
//   if (subject=""){
//     alert("please enter a name");
//     return false
//   }

//   var message=document.getElementById("comment").value
//   if (message=""){
//     alert('please fill the message')
//     return false
//   }
//   var email = document.getElementById("email").value
//   var re = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
//   if (re.test(email)) {
//     alert("You have entered a valid email address!")
//     $("#form1").hide();
//     document.getElementById("msg").innerHTML = "Form Submited"
//     return true;
//   }
//   else
//   {
//     alert("You have entered an invalid email address!");
//     return false;
//   }

// };

// var a = 0;

//     function mouseOver(){
        
//         const subject= document.getElementById('name').value;
//         const email = document.getElementById('email').value;
//         const message = document.getElementById('comment').value;
//         const emailCheck = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
//         debugger
//         if((subject== "" || !email.match(emailCheck) || message == "" ) && a==0){
//         buttonMoveLeft();
//         a = 1;
//         return false;
//         } 

//         if((subject == "" || !email.match(emailCheck) || message == "" ) && a==1){
//         buttonMoveRight();
//         a = 2;
//         return false;
//         } 

//         if((subject == "" || !email.match(emailCheck) || message == "" ) && a==2){
//         buttonMoveLeft();
//         a = 1;
//         return false;
//         } 
//         else{
//             document.getElementById('#button-blue').style.cursor = 'pointer';
//             return false;
//         };

//     };

//     function buttonMoveLeft(){

//         const button = document.getElementById('submit-btn');
//         button.style.transform = 'translateX(-160%)';

//     };

//     function buttonMoveRight(){

//         const button = document.getElementById('submit-btn');
//         button.style.transform = 'translateX(0%)';

//     };

//    function resetBtn(){
//         const button = document.getElementById('submit-btn');
//         button.style.transform = 'translateX(0%)';
//     };










  