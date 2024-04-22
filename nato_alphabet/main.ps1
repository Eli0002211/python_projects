function nato_convert{
    $name = (read-host "What word do you want to translate?").ToUpper()
    $new_list = @()
    foreach ($letter in $name){
        $new_list += $letter
    }
    $data = Import-Csv -Path "\Users\Eli\Desktop\PycharmProjects"
    $nato_hashtable = @{}

    foreach ($row in $data) {
        $letter = $row.Letter
        $word = $row.Word
        $nato_hashtable[$letter] = $word
    }
    write-host $nato_hashtable
}
cls
nato_convert