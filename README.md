# Scammer Spammer
Used to spam a spam website by filling in random names and passwords

Backstory:

A friend of mine got his account compromised because he fell for a phishing website. This website specifically was http://rewardfreegift2019-garena.ga at the time of writing. (Please do not fall for the site)

Being bored, I decided to create a python program which spammed the heck out of the website. So came the first program: `scammer_spammer.py`, which was hastily built up in like half an hour.

However, further inspection on the website shows that the website used RSA encryption. The code was as follows:

````
<script src="http://www.google.com/jsapi"></script>
<script type="text/javascript">google.load("jquery", "1.5.0");</script><script src="https://ajax.googleapis.com/ajax/libs/jquery/1.5.0/jquery.min.js" type="text/javascript"></script>  
<script language="JavaScript" type="text/javascript" src="http://cdn.garenanow.com/webmain/static/js/jsbn.js"></script>
<script language="JavaScript" type="text/javascript" src="http://cdn.garenanow.com/webmain/static/js/prng4.js"></script>
<script language="JavaScript" type="text/javascript" src="http://cdn.garenanow.com/webmain/static/js/rng.js"></script>
<script language="JavaScript" type="text/javascript" src="http://cdn.garenanow.com/webmain/static/js/rsa.js"></script>
<script language="JavaScript" type="text/javascript" src="http://cdn.garenanow.com/webmain/static/js/grsa.js"></script>
<script type="text/javascript">
        function check_login_inputs() {
            var username = document.loginForm.username.value;
            var password = document.loginForm.password.value;
            if (!username || !password) {
                return false;
            }
            return true;
        }
        function do_encrypt() {
            if (!check_login_inputs()) {
              return false;
            }
            var pw = document.loginForm.password.value;
            document.loginForm.password2.value=RSA(pw);
            $('.loginForm').submit();
            return true;
        }
        function keyIsPressed(evt) {
          var charCode = (evt.which) ? evt.which : evt.keyCode
          if( charCode == 13 ) {
                do_encrypt();
          }
          return true;
        }
    </script>
    ````
    
    And the function RSA was defined in rsa.js somewhere. Since getting past RSA required a both a public and private key, I decided to switch tactics and used selenium instead. Thus came `scammer_spammer_selenium.py`
