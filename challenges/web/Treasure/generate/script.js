var form = document.getElementById('treasure');
var key = document.getElementById('key');
var result = document.getElementById("result");
function onSubmit(event) {
    if (event) { event.preventDefault(); }
    if (check(key.value)) {
      result.style.display="block";
      result.style.color="green";
      result.innerHTML="Chest Opened!";
    } else {
      result.style.display="block";
      result.style.color="red";
      result.innerHTML="Failed";
    }
}
form.addEventListener('submit', onSubmit, false);
form.submit = onSubmit;

function check(inputkey) {
  if (!inputkey.match(/GCTF{.*}/)) return false;
  let a = /¤À.áÔ¥6¦Ó¹WþÊmãÖÚG¤7ùª9¨Mªћ#³­1᧨ẋ2¨Ӈ#ṡ2Ṣ€Ç³Ç¤œ&¬ɓÓÂ.Ö£¢dÈ9&Jºò³=SȯẊÇ¿/;

  for (let i = 0; i < a.length; i++) {
    inputkey[i] = String.fromCharCode(inputkey[i % inputkey.length] ^ a[i % inputkey.length].charCodeAt(0) >> 1 << 2 % 68 + 1);
  }

  return inputkey.split('').map(c => (c.charCodeAt(0) << 1 ^ 0x12) >> 1 ^ 0xa1).toString() === [239,235,252,238,211,194,156,254,156,157,203,250,153,216,220,247,153,157,247,217,221,153,220,155,247,235,156,198,203,155,250,199,253,157,213].toString();
}