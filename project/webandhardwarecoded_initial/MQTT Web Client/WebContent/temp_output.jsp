<head>
  <meta http-equiv="refresh" content="1">
</head>
	
<%
	String data = (String) session.getAttribute("data");
%>

<% 
	if (data.equals("Fire"))
	{
		%>
			<h2 style='background-color: red; color: white;'> FIRE. Please take action immediately</h2>
		<%
	}
	else
	{
		%>
			<h2 style='background-color: lightgreen;'> No Fire</h2>
		<%
	}
%>
