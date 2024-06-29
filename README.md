<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

![Static Badge](https://img.shields.io/badge/CONTRIBUTORS-5-green?style=for-the-badge&logoSize=auto)
![Static Badge](https://img.shields.io/badge/license-MIT-green?style=for-the-badge&logo=license&logoSize=auto)
[![LinkedIn][linkedin-shield]][linkedin-url]
<!-- ![Forks](https://github.com/RyanJManchester/stunning-pancake/network/members) -->
<!-- [![Stargazers][stars-shield]][stars-url] -->

<h2 align="center" >Te Whatu Ora: Name Generation for Unidentified Patients</h2>
  <p align="center">
    MY project_description
    <br />
    <br />
    <br />
    ·
    <a href="https://github.com/RyanJManchester/stunning-pancake/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Intent of this Repository

Here's a blank template to get started: Lorem Ad Ipsum

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Computer Prerequisites
Any terminal that can run python3, such as bash, WSL, windows terminal. The provided commands work for bash terminals. 
* Python
  <details>
    <summary>Installing Python3</summary>
    first, make sure your package Lists are updated
    
   ```sh
   sudo apt-get update
   ```
    Update package Lists if needed
  
   ```sh
   sudo apt-get upgrade
   ```
    Installing Python itself
    
   ```sh
   
   sudo apt-get install python3.6
   ```
  </details>
* Clone this repo
   ```sh
   git clone https://github.com/RyanJManchester/stunning-pancake.git
   ```
   
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

1. After cloning the repo, place your desired starting files in the folder or use one of our templates
  
2. Use matcher.py to combine the wordlists together
   
  **Example:** python3 scripts/matcher.py templates/tree_nouns.txt templates/verbs.txt uncleaned_output.txt
   ```sh
   python3 scripts/matcher.py first_names last_names desired_file_name
   ```

3. Cleaning the wordlists
   You can use the cleaner script to remove lines that contain profanity or terms we deemed vulgar, or not suitable for placeholders.
   if you wish to add you own text files that include words you wish to remove, you can modify the top line in the cleaners.py file
     which provides you with a list you can add the file name to.
   
   ```sh
   python3 scripts/cleaner.py to_clean
   ```
   Alternatively, you can clean each wordlist seperately prior to matching them together, but combined results wont be checked.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

4. Removing Duplicates if you want to
   ```sh
   python3 scripts/remove_duplicates my_output
   ```
   
Other Scripts i have provided that might be helpful:
   ```sh
   python3 scripts/remove_duplicates my_output
   ```
   
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Our Roadmap
<div>
<img src ="https://github.com/RyanJManchester/Name_Generation_for_Unidentified_Patients/blob/main/Jane%20Doe%20Poster.png" width = 900px />
</div>
<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Contact

[Email](rm534@students.waikato.ac.nz)

Project Link: [https://github.com/RyanJManchester/stunning-pancake](https://github.com/RyanJManchester/stunning-pancake)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Jemma Konig]()
* [Te Kaka Keegan]()
* [Andreea Claude]()
* [Kevin Marshall]()
* [Emma Laurey]()

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[stars-shield]: https://img.shields.io/github/stars/RyanJManchester/stunning-pancake.svg?style=for-the-badge
[stars-url]: https://github.com/RyanJManchester/stunning-pancake/stargazers

[license-url]: https://github.com/RyanJManchester/stunning-pancake/blob/main/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/RyanJManchester
[product-screenshot]: images/screenshot.png
