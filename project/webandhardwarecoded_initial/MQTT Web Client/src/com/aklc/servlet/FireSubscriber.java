package com.aklc.servlet;

import javax.servlet.http.HttpSession;

import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.MqttCallback;
import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttConnectOptions;
import org.eclipse.paho.client.mqttv3.MqttMessage;

public class FireSubscriber {
	HttpSession session = null;

	class CallBack implements MqttCallback {

		@Override
		public void connectionLost(Throwable arg0) {
			System.out.println("Connection has been lost with the MQTT server");
		}

		@Override
		public void deliveryComplete(IMqttDeliveryToken arg0) {

		}

		@Override
		public void messageArrived(String topic, MqttMessage message) throws Exception {
			String data = new String(message.getPayload(), "UTF-8");
			System.out.println("Message arrived: " + new String(message.getPayload(), "UTF-8"));
			session.setAttribute("firedata", data);
		}

	}

	class TemperatureThread implements Runnable {

		Thread t;

		public TemperatureThread() {
			t = new Thread(this);
			t.start();
		}

		@Override
		public void run() {
			try {
				MqttClient client = new MqttClient("tcp://soldier.cloudmqtt.com:17075", "clientid");
				System.out.println("Listening");
				client.setCallback(new CallBack());
				MqttConnectOptions mqOptions = new MqttConnectOptions();
				mqOptions.setCleanSession(true);
				mqOptions.setUserName("yqglkysg");
				mqOptions.setPassword("6upI7WF_DgVN".toCharArray());

				client.connect(mqOptions);
				client.subscribe("house/fire");
			} catch (Exception e) {
				e.printStackTrace();
			}
		}

	}

	public void subscribe(HttpSession sesion) {
		this.session = sesion;
		new TemperatureThread();
	}
	
	public static void main (String arg[])
	{
		new FireSubscriber().subscribe(null);
	}
}