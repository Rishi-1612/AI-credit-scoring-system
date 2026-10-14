-- Local development databases used by the project.
-- auditdb is created by MYSQL_DATABASE in docker-compose.yml.
CREATE DATABASE IF NOT EXISTS credit_auth_db
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

CREATE DATABASE IF NOT EXISTS raw_shap_values
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
