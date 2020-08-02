<!--
*** Thanks for checking out this README Template. If you have a suggestion that would
*** make this better, please fork the repo and create a pull request or simply open
*** an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->





<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <!-- <a href="https://github.com/Pycomet/telegram-group-engagement-bot">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

  <h3 align="center">Telegram Group Engagement Bot</h3>

  <p align="center">
    This is a telegram bot that aims peer to peer growth on instagram presence right from telegram
    <br />
    <a href="https://github.com/Pycomet/telegram-group-engagement-bot"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Pycomet/telegram-group-engagement-bot">View Demo</a>
    ·
    <a href="https://github.com/Pycomet/telegram-group-engagement-bot/issues">Report Bug</a>
    ·
    <a href="https://github.com/Pycomet/telegram-group-engagement-bot/issues">Request Feature</a>
  </p>
</p>

<!-- ABOUT THE PROJECT -->
### About The Project


This is a peer to peer engagement bot on telegram for instagram users to boost their online presence, with more likes and comments.

To participant is the engagement poll and get other people to follow, like and comment on your post, you need to have first (at the very least like) all the post on the active Dx list of users given to you by the Manager Bot. Your post to join the pod list is being verified by checking if you have liked and commented on the existing list of users.

If you are approved, your link is added to the Dx list pushing the first link out. This keeps the list in a loop which is relative to the engagement activity.

### Built With

This application is built with python at the core and the most functionality with the friendly and fast client libraries for telegram and instagram.


<!-- USAGE EXAMPLES -->
### Usage

To use this application as your own, follow these simple steps;

  - Fork this repository (`git clone https://github.com/Pycomet/telegram-group-engagement-bot.git`)

  - Create a `.env` file with the following data
    - `TOKEN` - This is the telegram bot token from `@botfather`
    - `USERNAME` - Instagram account username
    - `PASSWORD` - Instagram account password
    - `WEBHOOK_URL` - Pre-defined web hook to be used for the app
    - `ADMIN_ID` - Admin telegram ID for special access
    - `GROUP_ID` - Telegram group to be managed the bot for receiving engagement links

  - Goto `config.py` and set `DEBUG` to "True" to run locally and "False" to run in production

  - Run the entrypoint file `python app.py`

Enjoy!

## Show your support

Give a ⭐️ if this project helped you!

<!-- ROADMAP -->
### Roadmap

See the [open issues](https://github.com/Pycomet/telegram-group-engagement-bot/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
### Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
### License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
### Contact

My Website - <a href="https://www.codefred.me">www.codefred.me</a>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Pycomet/telegram-group-engagement-bot.svg?style=flat-square
[contributors-url]: https://github.com/Pycomet/telegram-group-engagement-bot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Pycomet/telegram-group-engagement-bot.svg?style=flat-square
[forks-url]: https://github.com/Pycomet/telegram-group-engagement-bot/network/members
[stars-shield]: https://img.shields.io/github/stars/Pycomet/telegram-group-engagement-bot.svg?style=flat-square
[stars-url]: https://github.com/Pycomet/telegram-group-engagement-bot/stargazers
[issues-shield]: https://img.shields.io/github/issues/Pycomet/telegram-group-engagement-bot.svg?style=flat-square
[issues-url]: https://github.com/Pycomet/telegram-group-engagement-bot/issues
[license-shield]: https://img.shields.io/github/license/Pycomet/telegram-group-engagement-bot.svg?style=flat-square
[license-url]: https://github.com/Pycomet/telegram-group-engagement-bot/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/alfredemmanuelinyang/
[product-screenshot]: images/screenshot.png
