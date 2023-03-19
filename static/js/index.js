function setRunVisible(){
    const runBlock = document.querySelector('#submit-input-wrapper');
    const settingsBlock = document.querySelector('#settings-input-wrapper');
    runBlock.classList.add('form-input__wrapper-active');
    settingsBlock.classList.add('form-input__wrapper-active');
}

function openSettings(){
    const advancedSettingsBlock = document.querySelector('#advanced-settings');
    advancedSettingsBlock.classList.remove('advanced-settings__hidden');
}

function closeSettings(e=undefined){
    if(e !== undefined && e.target.closest(".advanced-settings__overlay") === null) {
        return;
    }
    const advancedSettingsBlock = document.querySelector('#advanced-settings');
    advancedSettingsBlock.classList.add('advanced-settings__hidden');
}