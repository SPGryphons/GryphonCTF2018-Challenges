<!-- 
Creator: Va1aR (Joshua)
 -->
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>

<head>
    <title>GCTF Challenge</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- Bootstrap -->
    <!-- <link href="css/bootstrap.css" rel="stylesheet"> -->
    
    <!--Bootshape-->
    <!-- <link href="css/bootshape.css" rel="stylesheet"> -->
    
    
    
    
    
    <!-- CSS CDN Link got problem -->
    <!-- Bootstrap CDN for CSS only -->
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    <!-- Optional theme -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
    
    
    
    
    
    <!--Google Fonts-->
    <link href='http://fonts.googleapis.com/css?family=Duru+Sans|Actor' rel='stylesheet' type='text/css'>
    
  
    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
    <!-- Navigation bar -->
    <div class="navbar navbar-default navbar-fixed-top" role="navigation">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#"><span class="green">PRODUCT</span> Challenge</a>
        </div>
      </div>
    </div><!-- End Navigation bar -->

    <!-- Slide gallery -->
    <div class="jumbotron">
    </div><!-- End Slide gallery -->
    
    <!-- Content -->
    <div class="container">
      <h3 class="text-center">Welcome to the PRODUCT Challenge!</h3>
      <p class="text-center">Your task is to find and enter PRODUCT to get the flag</p>
    </div><!-- End Content -->
    
    <form action="checkAnswer.jsp">

	<div class="text-center"><img src = "image.png" class="img-center">
	<br>
	PRODUCT is: <input type="text" name="answer"/>
	<input type="submit" value="Enter">
	</br>
	
		<%
	
		String check = request.getParameter("check");
		
		if (check == null || check.equals("noinput")) {
			out.println("<br> Please enter an input");
		} 
		
		else if(check.equals("wrong")){
			out.println("<br> Your answer was wrong.");
		}
		
		%>
	
	</div>
	
	</form>
    <br>
    <div class="btn-toolbar text-center">
      <a href="#hints" role="button" class="btn btn-success">Click Here For Hints</a>
    </div>
    
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    
    <h3 id="hints" class="text-center">Hints</h3>
    <!-- Thumbnails -->
    <div class="container thumbs">
     <div class="col-sm-6 col-md-4">
        <div class="thumbnail">
          <img src="img/img3.jpg" alt="" class="img-circle">
          <div class="caption">
            <h3 class="text-center">Dimensions</h3>
            <p class="text-center">Box? What box?</p>
          </div>
        </div>
      </div>
      <div class="col-sm-6 col-md-4">
        <div class="thumbnail">
          <img src="img/img1.jpg" alt="" class="img-circle">
          <div class="caption">
            <h3 class="text-center">Lemmino</h3>
            <p class="text-center">An interesting Youtube channel</p>
          </div>
        </div>
      </div>
      <div class="col-sm-6 col-md-4">
        <div class="thumbnail">
          <img src="img/img2.jpg" alt="" class="img-circle">
          <div class="caption">
            <h3 class="text-center">Cicada</h3>
            <p class="text-center">Just an insect</p>
            <p class="text-center">... or is it?</p>
          </div>
        </div>
      </div>
    </div><!-- End Thumbnails -->
    
    <!-- Footer -->
    <div class="footer text-center">
        <p>&copy; 2018 GCTF. All Rights Reserved.</p>
    </div><!-- End Footer -->


    <!-- Bootstrap CDN for JS, Popper.js, and jQuery-->
	<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
	<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
	
	<!-- jQuery Core 3.3.1 -->
	<script src="http://code.jquery.com/jquery-3.3.1.min.js" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" crossorigin="anonymous"></script>
    
    
    
  </body>

</html>