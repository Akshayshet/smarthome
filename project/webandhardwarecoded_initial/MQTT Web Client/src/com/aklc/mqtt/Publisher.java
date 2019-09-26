package com.aklc.mqtt;
import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttConnectOptions;
import org.eclipse.paho.client.mqttv3.MqttMessage;
import org.eclipse.paho.client.mqttv3.MqttTopic;

public class Publisher {

	public static void sendMessage(String msg) {
		try {
			String broker = "tcp://soldier.cloudmqtt.com:17075";
			String topicName = "light/bulb1";
			int qos = 1;

			MqttClient mqttClient = new MqttClient(broker, String.valueOf(System.nanoTime()));

			MqttConnectOptions connOpts = new MqttConnectOptions();

			connOpts.setCleanSession(true);
			connOpts.setKeepAliveInterval(1000);
			connOpts.setUserName("yqglkysg");
			connOpts.setPassword("6upI7WF_DgVN".toCharArray());

			MqttMessage message = new MqttMessage(msg.getBytes());

			message.setQos(qos);
			message.setRetained(true);

			MqttTopic topic2 = mqttClient.getTopic(topicName);

			mqttClient.connect(connOpts);
			topic2.publish(message);

			mqttClient.disconnect();
			mqttClient.close();

		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public static void main(String[] args) throws Exception {
		sendMessage("off");
		System.out.println("LED IS NOW TURNED ON");
		
	}

}
