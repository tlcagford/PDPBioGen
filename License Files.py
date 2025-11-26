# Creating LICENSE-COMMERCIAL.md
commercial_license = """# PDPBioGen COMMERCIAL LICENSE AGREEMENT

## Effective Date: 2024
## Licensor: Tony E. Ford
## Sole Owner and Intellectual Property Holder

## 1. GRANT OF LICENSE

Tony E. Ford ("Licensor") grants Licensee a non-exclusive, non-transferable license to use the PDPBioGen software for commercial purposes, subject to the terms of this Agreement.

## 2. COMMERCIAL USE RIGHTS

- **Deployment Rights**: Use in production environments and commercial products
- **Modification Rights**: Create derivative works and custom modifications  
- **Distribution Rights**: Include in commercial products and services
- **SaaS Rights**: Use in software-as-a-service offerings
- **Internal Use**: Unlimited internal business use within licensed organization

## 3. RESTRICTIONS

- No redistribution of source code without explicit written permission
- No removal of copyright notices or attribution
- No use in illegal, unethical, or harmful applications
- No transfer or sublicense without written consent from Tony E. Ford
- No reverse engineering of core algorithms

## 4. FEES AND PAYMENT

Commercial license fees are determined based on:
- Company size and annual revenue
- Number of users and deployments
- Specific use cases and applications
- Required support and customization level

**Contact for Commercial Licensing**: tlcagford@gmail.com

## 5. INTELLECTUAL PROPERTY

Tony E. Ford retains all ownership rights, title, and interest in the PDPBioGen software, including all algorithms, methodologies, and intellectual property. Licensee owns modifications but underlying IP remains with Licensor.

## 6. SUPPORT AND UPDATES

Commercial licenses include:
- Priority technical support
- Security updates and critical patches
- Access to new versions and features
- Customization consulting (additional fees may apply)

## 7. TERM AND TERMINATION

This agreement remains in effect until terminated. Termination occurs for breach of terms or non-payment.

## 8. GOVERNING LAW

This agreement shall be governed by the laws of the United States.

## CONTACT FOR COMMERCIAL LICENSING:
Tony E. Ford
Email: tlcagford@gmail.com
Repository: https://github.com/tlcagford/PDPBioGen

© 2024 Tony E. Ford. All rights reserved.
"""

with open('LICENSE-COMMERCIAL.md', 'w') as f:
    f.write(commercial_license)
print("✅ Created LICENSE-COMMERCIAL.md")

# Creating LICENSE-ACADEMIC.md
academic_license = """# PDPBioGen ACADEMIC AND RESEARCH LICENSE

## Permitted Uses

This license grants permission for the following uses without fee:

1. **Academic Research**: Use in non-commercial research at accredited educational institutions
2. **Teaching and Education**: Use in classroom teaching, student projects, and educational materials
3. **Personal Learning**: Individual learning and experimentation
4. **Public Health Research**: Non-commercial public health and medical research
5. **Open Source Contributions**: Contributions to the PDPBioGen project

## Requirements and Conditions

1. **Attribution**: Must cite PDPBioGen and Tony E. Ford in any publications, presentations, or derivatives
2. **Non-Commercial**: No commercial use, redistribution in commercial products, or revenue generation
3. **Share Alike**: Modifications must be shared under this same academic license
4. **No Clinical Use**: Not for use in clinical applications without additional regulatory approvals and commercial licensing
5. **No Military Use**: Prohibited for military or weapons applications

## Citation Requirement

When using PDPBioGen in academic work, please cite:

```bibtex
@software{ford_pdpbiogen_2024,
  title = {PDPBioGen: Parallel Distributed Processing Biological Generation},
  author = {Ford, Tony E.},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\\url{https://github.com/tlcagford/PDPBioGen}}
}
