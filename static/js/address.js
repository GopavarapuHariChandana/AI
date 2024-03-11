var AIIMS = ["Delhi"];
var FortisHospital = ["Mumbai"];
var ApolloHospitals = ["Chennai"];
var ManipalHospital = ["Bangalore"];
var MaxSuperSpecialityHospital = ["Delhi"];
var NarayanaHealth = ["Kolkata"];
var ColumbiaAsiaHospital = ["Pune"];
var KIMSHospital = ["Hyderabad"];
var GlobalHospitals = ["Chennai"];
var RubyHallClinic = ["Pune"];

$("#inputState").on("change", function () {
  let StateSelected = $(this).val();
  let optionsList;
  let htmlString = "";

  switch (StateSelected) {
    case "Apollo Hospitals":
      optionsList = ApolloHospitals;
      break;
    case "Fortis Hospital":
      optionsList = FortisHospital;
      break;
    case "AIIMS":
      optionsList = AIIMS;
      break;
    case "Manipal Hospital":
      optionsList = ManipalHospital;
      break;
    case "Max Super Speciality Hospital":
      optionsList = MaxSuperSpecialityHospital;
      break;
    case "Narayana Health":
      optionsList = NarayanaHealth;
      break;
    case "Columbia Asia Hospital":
      optionsList = ColumbiaAsiaHospital;
      break;
    case "KIMS Hospital":
      optionsList = KIMSHospital;
      break;
    case "Global Hospitals":
      optionsList = GlobalHospitals;
      break;
    case "Ruby Hall Clinic":
      optionsList = RubyHallClinic;
      break;
  }

  for (var i = 0; i < optionsList.length; i++) {
    htmlString =
      htmlString +
      "<option value='" +
      optionsList[i] +
      "'>" +
      optionsList[i] +
      "</option>";
  }
  $("#inputDistrict").html(htmlString);
});

// $(document).ready(function () {
//   let actualValue = "";
//   $("#password").on("input", function (e) {
//     var inputValue = $(this).val();
//     var newLength = inputValue.length;
//     var oldLength = actualValue.length;

//     if (newLength > oldLength) {
//       // New character added
//       actualValue += inputValue.charAt(newLength - 1);
//     } else if (newLength < oldLength) {
//       // Character deleted
//       actualValue = actualValue.substring(0, newLength);
//     }

//     var maskedValue = new Array(newLength + 1).join("•");
//     $(this).val(maskedValue);
//   });
// });
