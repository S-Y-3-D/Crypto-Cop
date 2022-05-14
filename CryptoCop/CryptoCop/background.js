// Background Service


function fetchTabData() {
    let queryOptions = {};
    let tabs = chrome.tabs.query(queryOptions);
    console.log(tabs);

}

chrome.runtime.onInstalled.addListener(
  () => {
    
  }
)

let alarm1Info = {delayInMinutes: 1.0, periodInMinutes: 1.0};
chrome.alarms.create("Schedule tabs fetch", alarm1Info);

chrome.alarms.onAlarm.addListener(
  (alarm1) => {
    if(alarm1.name == "Schedule tabs fetch"){
      fetchTabData();
      var currentdate = new Date(); 
      var datetime = currentdate.getDate() + "-"
                      + (currentdate.getMonth()+1)  + "-" 
                      + currentdate.getFullYear() + " at "  
                      + currentdate.getHours() + ":"  
                      + currentdate.getMinutes() + ":" 
                      + currentdate.getSeconds();

      console.log(`Updated on: ` + datetime);
    }
  }
)




