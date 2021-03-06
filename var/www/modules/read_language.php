<?php 
    include 'names.php';
    
    function get_language()
    {
        global $value_field,$id_field, $config_settings_table, $language_key;
        
        $table = $config_settings_table;
        $key = $language_key;
        
        $value = NULL;
        
        $connection = new SQLite3("/var/www/config/pi-ager.sqlite3");
        $connection->busyTimeout(10000);
        //$connection->enableExceptions(true);
        $connection->exec('PRAGMA journal_mode = wal;');
		
        
        
        
        
        if ($key == NULL){
            $sql = 'SELECT ' . $value_field . ' FROM ' . $table . ' WHERE ' . $id_field . ' = (SELECT MAX(' . $id_field . ') from ' . $table . ')';
        }
        else {
            $sql = 'SELECT ' . $value_field . ' FROM ' . $table . ' WHERE key = "' . $key . '" AND ' . $id_field . ' = (SELECT MAX(' . $id_field . ') from ' . $table . ' WHERE key = "' . $key . '")';
        }

        $result = $connection->query($sql);
            while ($dataset = $result->fetchArray(SQLITE3_ASSOC))
                {
                $value = $dataset[$value_field];
                }
        $connection->close();
        
        return $value;
    }
?>
