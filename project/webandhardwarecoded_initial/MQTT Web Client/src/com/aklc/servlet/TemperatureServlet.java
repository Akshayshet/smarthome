package com.aklc.servlet;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.aklc.mqtt.TemperatureSubscriber;

public class TemperatureServlet extends HttpServlet {

	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
	
		TemperatureSubscriber ts = new TemperatureSubscriber();
		ts.subscribe(req.getSession());
		resp.sendRedirect("temp_output.jsp");
	}

}
