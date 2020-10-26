import psutil as p

def size(byte):
  #this the function to convert bytes into more suitable reading format.

  #Suffixes for the size
  for x in ["B","KB","MB","GB","TB"]:
    if byte<1024:
      return f"{byte:.2f}{x}"
    byte=byte/1024

#Function to get info about Disk Usage.
def disk():
  print("-"*50, "Disk Information", "-"*50)
  print("Partitions on Drive:")

  par = p.disk_partitions()
  # getting all of the disk partitions
  for x in par:
    print("Drive: ", x.device)
    print("  File system type: ", x.fstype)

    dsk = p.disk_usage(x.mountpoint)
    print("  Total Size: ", size(dsk.total))
    print("  Used:       ", size(dsk.used))
    print("  Free:       ", size(dsk.free))
    print("  Percentage: ", dsk.percent, "%\n")
  main()

#Function to Get memory/Ram usage.
def memory():
  print("-"*50, "Memory Information", "-"*50)

  #Getting the Memory/Ram Data.
  mem = p.virtual_memory()
  print("Total Memory:    ",size(mem.total))
  print("Available Memory:", size(mem.available))
  print("Used Memory:     ", size(mem.used))
  print("Percentage:      ",mem.percent,"% \n")

  #Getting the Swap Memory Data.
  #It is the Hard disk/ SSD space Which is used up as main memory when the main memory is not sufficient. 
  print("-"*48, "Swap Memory Information", "-"*47)
  swmem = p.swap_memory()
  print("Total Memory:    ", size(swmem.total))
  print("Available Memory:", size(swmem.free))
  print("Used Memory:     ", size(swmem.used))
  print("Percentage:      ", swmem.percent, "%\n")

  main()

#Function to get CPU information.
def cpu():
  print("-"*50, "CPU Information", "-"*50)

  #Getting the logical and physical core count.
  print("Logical/Total Core Count: ", p.cpu_count(logical=True) )
  print("Physical Core Count: ", p.cpu_count(logical=False))

  #Getting the CPU Frequencies.
  fre=p.cpu_freq()
  print("Maximum Frequency:" ,fre.max, "Mhz")
  print("Minimum Frequency:", fre.min,"Mhz")
  print("Current Frequency: ",fre.current ,"Mhz")

  #Getting the CPU Usage.
  for x, percentage_usage in enumerate(p.cpu_percent(percpu=True)):
      print("Core ",x, ":",percentage_usage,"%")
  print("Total CPU Usage:", p.cpu_percent(),"%\n")
  main()

#Main Function
def main():
  print("\nPress 1 for Disk Info. \nPress 2 for Memory/Ram Info. \nPress 3 for CPU Info. \nPress 0 to exit.")
  choice=int(input(">>> "))
  
  if choice==1: 
    disk()
  elif choice==2:
    memory()
  elif choice==3:
    cpu()
  elif choice==0:
    pass
  else:
    print("Please provide a valid input")

#Driver Function
if __name__ == "__main__":
  main()
