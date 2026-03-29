# User Personas

Given the requirements of centralized governance enforcing data access constraints across different audiences, three primary simulated personas have been defined.

## Persona 1: DataAdmin
- **Role**: Data Administrator
- **Characteristics**: Highly technical AWS / Lake Formation administrator.
- **Goals**: Needs full, unrestricted access to the entire lakehouse in order to provision, debug, and oversee operations. Must be able to observe raw and curated zones without data masking.
- **Access Level**: Unrestricted / Full Admin.

## Persona 2: FinancialAnalyst
- **Role**: Financial Analyst
- **Characteristics**: An internal business user who performs aggregated financial analytics and studies trading patterns.
- **Goals**: Needs access to the entire transaction history to produce comprehensive financial reports. Needs access to all rows.
- **Access Level / Constraints**: 
  - Cannot see personally identifiable information in its raw form. (Dynamic Data Masking enforces that the SSN field is masked as XXX-XX-####).

## Persona 3: LatamAnalyst
- **Role**: LATAM Regional Analyst
- **Characteristics**: A regional manager focusing strictly on the Latin American markets.
- **Goals**: Needs to analyze trading behavior, but only for users residing in Latin America.
- **Access Level / Constraints**:
  - Requires Row-Level Security (RLS) allowing access ONLY to transactions where the user's country belongs to Latin America.
  - Requires Column-Level Security (CLS) blocking access to the email column entirely.
