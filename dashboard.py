from coinmarketcap import *
from hiveos import *
from herominers import *


output = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="dashboard.css">
    <script src="https://kit.fontawesome.com/f4b39e3742.js" crossorigin="anonymous"></script> 
    <title>Mining Dashboard</title>
</head>

<!-- Body -->
<body>
    <header>
        <h1>Mining Dashboard</h1>
        <nav>
            <ul class="nav__links">
                <li><a href="index">Home</a></li>
                <li><a href="https://mikohirvela738080361.wordpress.com/" target="_blank" rel="noopener noreferrer">Documentation</a></li>
                <li><a href="https://github.com/mikohir/Crypto-Mining-Monitoring" target="_blank" rel="noopener noreferrer">Code</a></li>
            </ul>
        </nav>
        <p class="menu cta">Menu</p>
    </header>
    
    <div class="overlay">
        <a class="close">&times;</a>
        <div class="overlay__content">
            <a href="index">Home</a>
            <a href="https://mikohirvela738080361.wordpress.com/" target="_blank" rel="noopener noreferrer">Documentation</a>
            <a href="https://github.com/mikohir/Crypto-Mining-Monitoring" target="_blank" rel="noopener noreferrer">Code</a>
        </div>
        <script src="script.js"></script>
    </div>
    
    <div class="dashboard">
        <div class="dashboard-circle">
            <img src="./Icons/profits.png" alt="Profits"/><br>
            <a>Profit</a><br> 
                    <a>{profit_24h_eur}</a><br>
            <a>Revenue</a>
                    <a><br>{revenue_24h}</a>
        </div>
        <div class="dashboard-circle">
            <img src="./Icons/cryptocurrencies.png" alt="Cryptocurrency"/><br>
                    <a>{ergo_output}</a>
        </div>
        <div class="dashboard-circle">
            <img src="./Icons/gpu.png" alt="Total stats"/><br>
                <a>{total_stats}</a>
        </div>
        <div class="dashboard-circle">
            <img src="./Icons/cloud-mining.png" alt="Total stats"/><br>
                <a>{herominers_output}</a>
        </div>        
    </div>
    
    <div class="dashboard-tables">
        <div class="dashboard-box">
            <a>Coin prices</a><br>
                    {coins_output}<br>
            <a>Rig 1</a><br>
                    {worker_1_table}<br>
            <a>Rig 2</a><br>
                    {worker_2_table}<br>
        </div>
    </div>

</body>
<!-- Footer -->
<footer class="footer">
    <div class="footer-text">
      <p>&copy; 2022 Miko Hirvelä. All rights reserved.</p>
  </footer>
</html>
"""

with open("/var/www/html/cryptomonitoring.html", "w", encoding="utf-8") as f:
    f.write(f"{output}")
