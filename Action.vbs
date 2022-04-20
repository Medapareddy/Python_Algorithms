Function toUnlockSys

input=inputbox("enter the number of hours to keep PC Unlocked")
Const DELAY_Minutes=1
Mins=0



Do While cdbl(Mins/60)<cdbl(input)
CreateObject("Wscript.Shell").SendKeys"{NUMLOCK}"
Wscript.Sleep DELAY_Minutes*60000
Mins=Mins+1
Loop



End Function



call toUnlockSys
