from flask import Flask, render_template, request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

@app.route("/sentiment_analysis", methods=['GET', 'POST'])
def sentiment_analysis():
    if request.method == 'POST':
        # Get sentences from form data
        sentences = request.form['sentences'].split(',')

        # Create a SentimentIntensityAnalyzer object
        analyzer = SentimentIntensityAnalyzer()

        # Analyze the sentiment for each sentence and store thefa results
        results = []
        for sentence in sentences:
            vs = analyzer.polarity_scores(sentence.strip())
            results.append("{:-<65} {}".format(sentence, str(vs)))

        # Return the results as a string
        return '<br>'.join(results)

    # Render form template if method is GET
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)
