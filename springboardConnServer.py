import pexpect

# 跳板机
springboardServer = 'host'
springboardUser = 'user'
springboardPassword = 'password'

#内网
IntranetServer = 'host'
IntranetUser = 'user'
IntranetPassword = 'password'

springboardSshStr = 'ssh  ' + springboardServer + '@' + springboardUser

server = pexpect.spawn(springboardSshStr)
server.expect('[Pp]assword:')
server.sendline(springboardPassword)
server.expect('.#')

IntranetSshStr = 'ssh  ' + IntranetServer + '@' + IntranetUser
server.sendline(IntranetSshStr)
server.expect('[Pp]assword:')
server.sendline(IntranetPassword)

server.interact()
server.close()