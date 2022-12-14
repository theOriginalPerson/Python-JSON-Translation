<h1>Python Console Translation</h1>
<h3>Intro</h3>
<p>Welcome to the 3rd and final project for the Chatting with Python course! Here we will discuss the steps of how to build a basic translator.</p>
<h3>How to reproduce this</h3>
<ol>
    <li>Create a <code>translation.json</code> and <code>main.py</code> file if you haven't already done so</li>
    <li>Copy and paste the <code>translation.json</code> file contents I have provided in this repository and paste it into your own <code>translation.json</code> file</li>
    <li>On your first line of code, write <code>import json</code></li>
    <li>Leave a linebreak after your first line of code and then write <code>file = 'translation.json'</code></li>
    <li>After these first lines of code, declare a class named "Translator", like this <code>class Translator:</code></li>
    <li>Initialize the class with a <code>def __init__(self):</code> function, and set a second argument after self that takes in the word you want to translate. This is how you will start every class you make in Python (excluding the word_to_translate argument). Under this function, add <code>self.word_to_translate = word_to_translate</code>. More to be explained in the next step of why self is important.</li>
    <li>Create two functions: one that translates english_to_french, and another that translates french_to_english. Make sure these functions have "self" as their argument. <b>"Self" helps refer back to itself (the class) in a way that helps it understand that these functions (known as methods) are connected to it</b></li>
    <li>Copy lines 10-11 from our <code>main.py</code> template to open the JSON file and paste it in your english_to_french function</li>
    <li>Create a <code>for</code> loop that loops over the content in the JSON file in this function</li>
    <li>Within this <code>for</code> loop, check if the word_to_translate is in JSON data. If it is, return the translation using the <code>json.dumps</code> method; if it's not, print "sorry, that word doesn't exist"</li>
    <li>Follow steps 8-9 for your next function (french_to_english), but this time, loop over the values and try to return the keys instead (this is because our keys are in English, and we wish to return the English translation by using the French value)</li>
    <li>Finally, create a function that asks the user when they run this file whether they want to return an English translation or French one. Appropriately return the functions from the Translator class according to the response. Feel free to look through lines 25-36 for help with this section</li>
    <li>If you've made it this far! Awesome job! Truly well done. If you've still got some errors in your code, try to add print statements throughout the code to see which lines might be skipped</li>
</ol>
<h3>How to use it</h3>
<p>Upon running the code in your Python terminal, you should get a query asking whether you wish to translate to English or French. After selecting the language, enter the word you wish to translate and watch it return your words accordingly!</p>