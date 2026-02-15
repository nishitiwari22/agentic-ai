<h1>Section 29: Model Context Protocol (MCP)</h1>

<h2>Big Idea</h2>
<p>
Model Context Protocol (MCP) is a standardized way for AI models to interact
with external tools, databases, and applications.
</p>

<p>
Think of MCP as:
</p>
<ul>
  <li>A USB port for AI</li>
  <li>A universal API standard for tools</li>
</ul>

<p>
Without MCP:
</p>
<ul>
  <li>Every tool requires custom integration</li>
  <li>Systems become complex and hard to scale</li>
</ul>

<p>
With MCP:
</p>
<ul>
  <li>Tools follow a common protocol</li>
  <li>Any AI model can use them easily</li>
</ul>

<hr>

<h2>Lecture Breakdown</h2>

<h3>206. Section Intro to Model Context Protocol</h3>
<ul>
  <li>Overview of MCP</li>
  <li>Why it exists</li>
  <li>How it fits into agent architecture</li>
</ul>
<p><strong>Main takeaway:</strong> MCP standardizes how AI interacts with tools and data.</p>

<h3>207. Understanding What MCP Is</h3>
<p>
MCP is a protocol that allows AI models to:
</p>
<ul>
  <li>Discover tools</li>
  <li>Understand tool capabilities</li>
  <li>Use them safely</li>
</ul>

<p><strong>Why MCP was created:</strong></p>
<ul>
  <li>Before MCP, every AI system used different tool formats</li>
  <li>Hard to integrate new tools</li>
  <li>No standard communication</li>
</ul>

<p>MCP solves:</p>
<ul>
  <li>Tool discovery</li>
  <li>Secure execution</li>
  <li>Standard messaging</li>
</ul>

<h3>208. Exploring the Architecture of MCP</h3>

<p>MCP has three main components:</p>

<h4>1. Model (AI)</h4>
<ul>
  <li>The LLM that decides what tool to use</li>
  <li>Examples: GPT, Claude, local LLMs</li>
</ul>

<h4>2. MCP Client</h4>
<ul>
  <li>Bridge between AI model and MCP servers</li>
  <li>Sends tool requests</li>
  <li>Receives responses</li>
</ul>

<h4>3. MCP Server</h4>
<ul>
  <li>Hosts tools and resources</li>
  <li>Examples: file system, database, APIs</li>
</ul>

<hr>

<h2>Simple MCP Architecture</h2>

<pre>
User
  ↓
AI Model
  ↓
MCP Client
  ↓
MCP Server
  ↓
Tools / APIs / Databases
</pre>

<hr>

<h2>Why MCP Exists</h2>

<h3>Problem 1: Tool Chaos</h3>
<ul>
  <li>Different APIs for each tool</li>
  <li>Custom integration logic</li>
</ul>

<h3>Problem 2: Security</h3>
<ul>
  <li>Direct tool access can be dangerous</li>
  <li>Risk of data leaks or unsafe commands</li>
</ul>

<p>MCP adds:</p>
<ul>
  <li>Controlled tool access</li>
  <li>Structured requests</li>
  <li>Permission layers</li>
</ul>

<hr>

<h2>MCP Lifecycle (Tool Call Flow)</h2>

<ol>
  <li>User asks a question</li>
  <li>LLM decides a tool is needed</li>
  <li>MCP client sends tool request</li>
  <li>MCP server executes the tool</li>
  <li>Result returned to model</li>
  <li>Model responds to user</li>
</ol>

<hr>

<h2>MCP Servers</h2>

<h3>Local MCP Server</h3>
<ul>
  <li>Runs on local machine</li>
  <li>Examples: file system, local database</li>
</ul>

<h3>Remote MCP Server</h3>
<ul>
  <li>Runs in the cloud</li>
  <li>Examples: company APIs, CRM systems</li>
</ul>

<hr>

<h2>MCP Tool Schema Example</h2>

<pre>
{
  "name": "get_weather",
  "description": "Get weather for a city",
  "parameters": {
    "city": "string"
  }
}
</pre>

<hr>

<h2>MCP vs Traditional Tool Calling</h2>

<table>
  <tr>
    <th>Feature</th>
    <th>Traditional Tool Use</th>
    <th>MCP</th>
  </tr>
  <tr>
    <td>Standardization</td>
    <td>No</td>
    <td>Yes</td>
  </tr>
  <tr>
    <td>Tool discovery</td>
    <td>Manual</td>
    <td>Automatic</td>
  </tr>
  <tr>
    <td>Security</td>
    <td>Limited</td>
    <td>Built-in</td>
  </tr>
  <tr>
    <td>Interoperability</td>
    <td>Low</td>
    <td>High</td>
  </tr>
  <tr>
    <td>Scalability</td>
    <td>Hard</td>
    <td>Easy</td>
  </tr>
</table>

<hr>

<h2>How MCP Fits into Modern Agent Architecture</h2>

<pre>
User
 ↓
LLM (reasoning)
 ↓
Memory Layer
 ↓
Checkpointing
 ↓
MCP (tool access)
 ↓
External tools & data
</pre>

<hr>

<h2>Why MCP Matters</h2>
<ul>
  <li>Essential for production AI agents</li>
  <li>Used in enterprise AI systems</li>
  <li>Important skill for AI, ML, and data roles</li>
</ul>
