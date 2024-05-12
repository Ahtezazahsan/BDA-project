from flask import Flask, render_template, jsonify
from kafka import KafkaProducer, KafkaConsumer

app = Flask(__name__)

# Initialize Kafka producer and consumer
producer = KafkaProducer(bootstrap_servers='192.168.93.129:9092')
consumer = KafkaConsumer('user_activity', bootstrap_servers='192.168.93.129:9092', group_id='music_streaming_group')

# Define routes
@app.route('/')
def index():
    return render_template('index.html', title='Welcome to My Music Shop')

@app.route('/recommendations/<user_id>')
def get_recommendations(user_id):
    # Send user activity to Kafka
    producer.send('user_activity', key=user_id.encode(), value=b'play')

    # Consume recommendation from Kafka
    recommendations = []
    for message in consumer:
        recommendations.append(message.value.decode())
        if len(recommendations) == 15:
            break
    
    return render_template('recommendations.html', title='Recommendations', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
