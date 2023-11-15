# Meraki Azure Failover

## Overview

This Git repository contains scripts and configurations to implement a failover solution between Cisco Meraki MX security appliances and Microsoft Azure using the Meraki Auto VPN feature. The failover mechanism is designed to enhance network resilience and ensure continuous connectivity by seamlessly switching traffic between Meraki MX appliances deployed in different geographic locations.

## Table of Contents

- [Background](#background)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Background

In modern network architectures, achieving high availability and disaster recovery is crucial. This repository provides a solution to address potential outages by utilizing Cisco Meraki MX appliances in conjunction with Microsoft Azure.

## Features

- **Automated Failover:** The failover process is automated, ensuring minimal downtime during network disruptions.
- **Geo-Redundancy:** Leverage the geographic distribution of Meraki MX appliances for enhanced redundancy.
- **Logging and Monitoring:** Comprehensive logging and monitoring capabilities to track failover events and troubleshoot issues.
- **Azure Integration:** Seamless integration with Microsoft Azure for a holistic cloud-based failover solution.

## Prerequisites

Before implementing the failover solution, ensure you have the following prerequisites:

- Cisco Meraki MX appliances with Auto VPN configured.
- Microsoft Azure subscription with the necessary networking resources.
- Access to the Meraki API for automation.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/ahughes-gfcu/Meraki_Azure_Failover.git
   ```

## Usage

1. Input the required environment variables into your docker-compose.yml or a .env file
2. start your container with `docker compose up -d`


## Contributing

Contributions are welcome! If you have improvements or additional features to propose, please follow the [contribution guidelines](CONTRIBUTING.md) in this repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the contributors and the open-source community for their valuable input.
- Special thanks to Cisco Meraki and Microsoft Azure for providing the foundation for this failover solution.
- Thank you to ChatGPT for writing this documentation for me cause I'm lazy
