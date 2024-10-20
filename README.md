<h1>GitHub Activity CLI</h1>
    <p>This project is a simple command-line interface (CLI) application that fetches the recent activity of a GitHub user and displays it in the terminal. This project will help you practice your programming skills, including working with APIs, handling JSON data, and building a CLI application.</p>

  <h2>Requirements</h2>
    <ul>
        <li>The application runs from the command line.</li>
        <li>It accepts the GitHub username as an argument.</li>
        <li>Fetches the user’s recent activity using the GitHub API.</li>
        <li>Displays the fetched activity in the terminal.</li>
    </ul>

  <h2>Usage</h2>
    <p>To run the application, use the following command:</p>
    <pre><code>python main.py &lt;username&gt;</code></pre>
    <p>For example:</p>
    <pre><code>python main.py haknozer</code></pre>

  <h2>Fetching User Activity</h2>
    <p>The application will fetch the recent activity of the specified GitHub user using the following endpoint:</p>
    <pre><code>https://api.github.com/users/&lt;username&gt;/events</code></pre>
    <p>Example:</p>
    <pre><code>https://api.github.com/users/haknozer/events</code></pre>

  <h2>Output</h2>
    <p>The fetched activity will be displayed in the terminal. Example output:</p>
    <ul>
        <li>Pushed 3 commits to <strong>haknozer/GithubUserActivityCli</strong></li>
        <li>Started 10/22/2024 <strong>haknozer/GithubUserActivityCli</strong></li>
    </ul>

  <h2>Getting Started</h2>
    <ol>
        <li>Clone the repository:</li>
        <pre><code>git clone https://github.com/Haknozer/GithubUserActivityCli.git</code></pre>
        <li>Navigate into the project directory:</li>
        <pre><code>cd GithubuserActivityCli</code></pre>
        <li>Run the application:</li>
        <pre><code>python main.py &lt;username&gt;</code></pre>
    </ol>

  <h2>Contributing</h2>
    <p>Contributions are welcome! Feel free to submit a pull request or open an issue.</p>

  https://roadmap.sh/projects/github-user-activity
