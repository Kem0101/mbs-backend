

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mbs', '0001_initial'),
        ('authtoken', '0003_tokenproxy'),
    ]

    operations = [
        migrations.RunSQL(
            sql=[
                # Eliminar cualquier clave foránea existente en user_id
                """
                SET @constraint_name = (
                    SELECT CONSTRAINT_NAME 
                    FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE 
                    WHERE TABLE_SCHEMA = DATABASE()
                    AND TABLE_NAME = 'authtoken_token' 
                    AND COLUMN_NAME = 'user_id' 
                    AND REFERENCED_TABLE_NAME IS NOT NULL
                );
                """,
                """
                SET @sql = IF(@constraint_name IS NOT NULL, 
                              CONCAT('ALTER TABLE authtoken_token DROP FOREIGN KEY ', @constraint_name), 
                              'SELECT 1');
                PREPARE stmt FROM @sql;
                EXECUTE stmt;
                DEALLOCATE PREPARE stmt;
                """,
                # Añadir la nueva clave foránea
                "ALTER TABLE authtoken_token ADD CONSTRAINT authtoken_token_user_id_custom_fk FOREIGN KEY (user_id) REFERENCES mbs_customuser(id);"
            ],
            reverse_sql=[
                "ALTER TABLE authtoken_token DROP FOREIGN KEY IF EXISTS authtoken_token_user_id_custom_fk;",
                "ALTER TABLE authtoken_token ADD CONSTRAINT authtoken_token_user_id_35299eff_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id);"
            ]
        ),
    ]
