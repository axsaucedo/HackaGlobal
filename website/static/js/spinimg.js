$(function(){
    var isMinimumMode = false;
    var isLargeMode = false;

    $(window).on("resize", function(){
        if($(window).width() > 640){
            setLargeMode();
        }else{
            setMinumumMode();
        }
    });

    $(window).on("load", function(){
        if($(window).width() > 640){
            setLargeMode();
        }else{
            setMinumumMode();
        }
    });

    function setLargeMode(){
        if(isLargeMode){
            return;
        }

        isLargeMode = true;
        isMinimumMode = false;

        var frames = [
            "../theta/device/l/theta_turntable_device_00000.jpg",
            "../theta/device/l/theta_turntable_device_00001.jpg",
            "../theta/device/l/theta_turntable_device_00002.jpg",
            "../theta/device/l/theta_turntable_device_00003.jpg",
            "../theta/device/l/theta_turntable_device_00004.jpg",
            "../theta/device/l/theta_turntable_device_00005.jpg",
            "../theta/device/l/theta_turntable_device_00006.jpg",
            "../theta/device/l/theta_turntable_device_00007.jpg",
            "../theta/device/l/theta_turntable_device_00008.jpg",
            "../theta/device/l/theta_turntable_device_00009.jpg",
            "../theta/device/l/theta_turntable_device_00010.jpg",
            "../theta/device/l/theta_turntable_device_00011.jpg",
            "../theta/device/l/theta_turntable_device_00012.jpg",
            "../theta/device/l/theta_turntable_device_00013.jpg",
            "../theta/device/l/theta_turntable_device_00014.jpg",
            "../theta/device/l/theta_turntable_device_00015.jpg",
            "../theta/device/l/theta_turntable_device_00016.jpg",
            "../theta/device/l/theta_turntable_device_00017.jpg",
            "../theta/device/l/theta_turntable_device_00018.jpg",
            "../theta/device/l/theta_turntable_device_00019.jpg",
            "../theta/device/l/theta_turntable_device_00020.jpg",
            "../theta/device/l/theta_turntable_device_00021.jpg",
            "../theta/device/l/theta_turntable_device_00022.jpg",
            "../theta/device/l/theta_turntable_device_00023.jpg",
            "../theta/device/l/theta_turntable_device_00024.jpg",
            "../theta/device/l/theta_turntable_device_00025.jpg",
            "../theta/device/l/theta_turntable_device_00026.jpg",
            "../theta/device/l/theta_turntable_device_00027.jpg",
            "../theta/device/l/theta_turntable_device_00028.jpg",
            "../theta/device/l/theta_turntable_device_00029.jpg",
            "../theta/device/l/theta_turntable_device_00030.jpg",
            "../theta/device/l/theta_turntable_device_00031.jpg",
            "../theta/device/l/theta_turntable_device_00032.jpg",
            "../theta/device/l/theta_turntable_device_00033.jpg",
            "../theta/device/l/theta_turntable_device_00034.jpg",
            "../theta/device/l/theta_turntable_device_00035.jpg",
            "../theta/device/l/theta_turntable_device_00036.jpg",
            "../theta/device/l/theta_turntable_device_00037.jpg",
            "../theta/device/l/theta_turntable_device_00038.jpg",
            "../theta/device/l/theta_turntable_device_00039.jpg",
            "../theta/device/l/theta_turntable_device_00040.jpg",
            "../theta/device/l/theta_turntable_device_00041.jpg",
            "../theta/device/l/theta_turntable_device_00042.jpg",
            "../theta/device/l/theta_turntable_device_00043.jpg",
            "../theta/device/l/theta_turntable_device_00044.jpg",
            "../theta/device/l/theta_turntable_device_00045.jpg",
            "../theta/device/l/theta_turntable_device_00046.jpg",
            "../theta/device/l/theta_turntable_device_00047.jpg",
            "../theta/device/l/theta_turntable_device_00048.jpg",
            "../theta/device/l/theta_turntable_device_00049.jpg",
            "../theta/device/l/theta_turntable_device_00050.jpg",
            "../theta/device/l/theta_turntable_device_00051.jpg",
            "../theta/device/l/theta_turntable_device_00052.jpg",
            "../theta/device/l/theta_turntable_device_00053.jpg",
            "../theta/device/l/theta_turntable_device_00054.jpg",
            "../theta/device/l/theta_turntable_device_00055.jpg",
            "../theta/device/l/theta_turntable_device_00056.jpg",
            "../theta/device/l/theta_turntable_device_00057.jpg",
            "../theta/device/l/theta_turntable_device_00058.jpg",
            "../theta/device/l/theta_turntable_device_00059.jpg",
            "../theta/device/l/theta_turntable_device_00060.jpg",
            "../theta/device/l/theta_turntable_device_00061.jpg",
            "../theta/device/l/theta_turntable_device_00062.jpg",
            "../theta/device/l/theta_turntable_device_00063.jpg",
            "../theta/device/l/theta_turntable_device_00064.jpg",
            "../theta/device/l/theta_turntable_device_00065.jpg",
            "../theta/device/l/theta_turntable_device_00066.jpg",
            "../theta/device/l/theta_turntable_device_00067.jpg",
            "../theta/device/l/theta_turntable_device_00068.jpg",
            "../theta/device/l/theta_turntable_device_00069.jpg",
            "../theta/device/l/theta_turntable_device_00070.jpg",
            "../theta/device/l/theta_turntable_device_00071.jpg",
            "../theta/device/l/theta_turntable_device_00072.jpg",
            "../theta/device/l/theta_turntable_device_00073.jpg",
            "../theta/device/l/theta_turntable_device_00074.jpg",
            "../theta/device/l/theta_turntable_device_00075.jpg",
            "../theta/device/l/theta_turntable_device_00076.jpg",
            "../theta/device/l/theta_turntable_device_00077.jpg",
            "../theta/device/l/theta_turntable_device_00078.jpg",
            "../theta/device/l/theta_turntable_device_00079.jpg"
        ];

        $("#view360").spritespin({
            width     : 300,
            height    : 496,
            frames    : frames.length,
            behavior  : "none",
            sense     : 1,
            source    : frames,
            animate   : true,
            loop      : true,
            frameWrap : true,
            frameStep : 1,
            frameTime : 100,
            enableCanvas : false
        });
    }

    function setMinumumMode(){
        if(isMinimumMode){
            return;
        }

        isLargeMode = false;
        isMinimumMode = true;

        var frames = [
            "../theta/device/s/theta_turntable_device_00000.jpg",
            "../theta/device/s/theta_turntable_device_00001.jpg",
            "../theta/device/s/theta_turntable_device_00002.jpg",
            "../theta/device/s/theta_turntable_device_00003.jpg",
            "../theta/device/s/theta_turntable_device_00004.jpg",
            "../theta/device/s/theta_turntable_device_00005.jpg",
            "../theta/device/s/theta_turntable_device_00006.jpg",
            "../theta/device/s/theta_turntable_device_00007.jpg",
            "../theta/device/s/theta_turntable_device_00008.jpg",
            "../theta/device/s/theta_turntable_device_00009.jpg",
            "../theta/device/s/theta_turntable_device_00010.jpg",
            "../theta/device/s/theta_turntable_device_00011.jpg",
            "../theta/device/s/theta_turntable_device_00012.jpg",
            "../theta/device/s/theta_turntable_device_00013.jpg",
            "../theta/device/s/theta_turntable_device_00014.jpg",
            "../theta/device/s/theta_turntable_device_00015.jpg",
            "../theta/device/s/theta_turntable_device_00016.jpg",
            "../theta/device/s/theta_turntable_device_00017.jpg",
            "../theta/device/s/theta_turntable_device_00018.jpg",
            "../theta/device/s/theta_turntable_device_00019.jpg",
            "../theta/device/s/theta_turntable_device_00020.jpg",
            "../theta/device/s/theta_turntable_device_00021.jpg",
            "../theta/device/s/theta_turntable_device_00022.jpg",
            "../theta/device/s/theta_turntable_device_00023.jpg",
            "../theta/device/s/theta_turntable_device_00024.jpg",
            "../theta/device/s/theta_turntable_device_00025.jpg",
            "../theta/device/s/theta_turntable_device_00026.jpg",
            "../theta/device/s/theta_turntable_device_00027.jpg",
            "../theta/device/s/theta_turntable_device_00028.jpg",
            "../theta/device/s/theta_turntable_device_00029.jpg",
            "../theta/device/s/theta_turntable_device_00030.jpg",
            "../theta/device/s/theta_turntable_device_00031.jpg",
            "../theta/device/s/theta_turntable_device_00032.jpg",
            "../theta/device/s/theta_turntable_device_00033.jpg",
            "../theta/device/s/theta_turntable_device_00034.jpg",
            "../theta/device/s/theta_turntable_device_00035.jpg",
            "../theta/device/s/theta_turntable_device_00036.jpg",
            "../theta/device/s/theta_turntable_device_00037.jpg",
            "../theta/device/s/theta_turntable_device_00038.jpg",
            "../theta/device/s/theta_turntable_device_00039.jpg",
            "../theta/device/s/theta_turntable_device_00040.jpg",
            "../theta/device/s/theta_turntable_device_00041.jpg",
            "../theta/device/s/theta_turntable_device_00042.jpg",
            "../theta/device/s/theta_turntable_device_00043.jpg",
            "../theta/device/s/theta_turntable_device_00044.jpg",
            "../theta/device/s/theta_turntable_device_00045.jpg",
            "../theta/device/s/theta_turntable_device_00046.jpg",
            "../theta/device/s/theta_turntable_device_00047.jpg",
            "../theta/device/s/theta_turntable_device_00048.jpg",
            "../theta/device/s/theta_turntable_device_00049.jpg",
            "../theta/device/s/theta_turntable_device_00050.jpg",
            "../theta/device/s/theta_turntable_device_00051.jpg",
            "../theta/device/s/theta_turntable_device_00052.jpg",
            "../theta/device/s/theta_turntable_device_00053.jpg",
            "../theta/device/s/theta_turntable_device_00054.jpg",
            "../theta/device/s/theta_turntable_device_00055.jpg",
            "../theta/device/s/theta_turntable_device_00056.jpg",
            "../theta/device/s/theta_turntable_device_00057.jpg",
            "../theta/device/s/theta_turntable_device_00058.jpg",
            "../theta/device/s/theta_turntable_device_00059.jpg",
            "../theta/device/s/theta_turntable_device_00060.jpg",
            "../theta/device/s/theta_turntable_device_00061.jpg",
            "../theta/device/s/theta_turntable_device_00062.jpg",
            "../theta/device/s/theta_turntable_device_00063.jpg",
            "../theta/device/s/theta_turntable_device_00064.jpg",
            "../theta/device/s/theta_turntable_device_00065.jpg",
            "../theta/device/s/theta_turntable_device_00066.jpg",
            "../theta/device/s/theta_turntable_device_00067.jpg",
            "../theta/device/s/theta_turntable_device_00068.jpg",
            "../theta/device/s/theta_turntable_device_00069.jpg",
            "../theta/device/s/theta_turntable_device_00070.jpg",
            "../theta/device/s/theta_turntable_device_00071.jpg",
            "../theta/device/s/theta_turntable_device_00072.jpg",
            "../theta/device/s/theta_turntable_device_00073.jpg",
            "../theta/device/s/theta_turntable_device_00074.jpg",
            "../theta/device/s/theta_turntable_device_00075.jpg",
            "../theta/device/s/theta_turntable_device_00076.jpg",
            "../theta/device/s/theta_turntable_device_00077.jpg",
            "../theta/device/s/theta_turntable_device_00078.jpg",
            "../theta/device/s/theta_turntable_device_00079.jpg"
        ];

        $("#view360").spritespin({
            width     : 150,
            height    : 248,
            frames    : frames.length,
            behavior  : "none",
            sense     : 1,
            source    : frames,
            animate   : true,
            loop      : true,
            frameWrap : true,
            frameStep : 1,
            frameTime : 100,
            enableCanvas : false
        });
    }
});