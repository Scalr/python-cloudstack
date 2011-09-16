from baseclient import *
from data_types import *


class Client(BaseClient):
	'''
	def addHost(self, username, password, zoneId, url, podId=None,
		clusterId=None, clusterName=None, _class=DataObject):
		return self.process('addhostsresponse',
			self.__execute__('addHost',
			{
				'username': username, 'password': password, 'zoneid': zoneId,
				'url': url, 'podid': podId, 'clusterid': clusterId,
				'clusterName': clusterName}),
			_class)


	def addSecondaryStorage(self, zoneId, url, _class=DataObject):
		return self.process('addsecondarystorageresponse',
			self.__execute__('addSecondaryStorage',
			{'zoneid': zoneId, 'url': url}),
			_class)
	
	def assignPortForwardingService(self, publicIp, virtualMachineId,
		id=None, ids=None, _class=DataObject):
		return self.process_async('assignPortForwardingService',
			{
				'publicip': publicIp, 'virtualmachineid': virtualMachineId,
				'id': id, 'ids': ids},
			_class)
	'''

	def assignToLoadBalancerRule(self, id, virtualMachineIds,
		_class=DataObject):
		'''assignToLoadBalancerRule(id, virtualMachineIds)'''
		return self.process_async('assignToLoadBalancerRule',
			{'id': id, 'virtualmachineids': virtualMachineIds},
		_class)

	def associateIpAddress(self, zoneId, account=None, domainId=None, networkId=None,
		_class=DataObject):
		return self.process('associateipaddressresponse',
			self.__execute__('associateIpAddress',
			{'zoneid': zoneId, 'account':account,
			'domainid':domainId, 'networkid':networkId}),
			_class)

	def attachIso(self, id, virtualMachineId, _class=DataObject):
		'''attachIso(id, virtualMachineId)'''
		return self.process_async('attachIso',
			{'id': id, 'virtualmachineid': virtualMachineId},
			_class)

	def attachVolume(self, id, virtualMachineId, deviceId=None,
		_class=DataObject):
		return self.process_async('attachVolume',
			{'id': id, 'virtualmachineid': virtualMachineId,'deviceid': deviceId},
			_class)

	'''
	def cancelHostMaintenance(self, id, _class=DataObject):
		return self.process_async('cancelHostMaintenance',
			{'id': id},
			_class) '''
		
	def changeServiceForVirtualMachine(self, id, serviceOfferingId, _class=DataObject):
		'''changeServiceForVirtualMachine(id, serviceOfferingId) '''
		return self.process_async('changeServiceForVirtualMachine',
			{'id': id, 'serviceofferingid': serviceOfferingId},
			_class)

	def copyIso(self, id, destZoneId, sourceZoneId, _class=DataObject):
		return self.process_async('copyIso',
			{'id': id, 'sourcezoneid': sourceZoneId,
			'destzoneid': destZoneId},
			_class)

	def copyTemplate(self, id, destZoneId, sourceZoneId, _class=DataObject):
		'''copyTemplate(id, destZoneId, sourceZoneId)'''
		return self.process_async('copyTemplate',
			{'id': id, 'sourcezoneid': sourceZoneId, 'destzoneid': destZoneId},
			_class)

	'''
	def createDiskOffering(self, name, displayText, diskSize,
		_class=DataObject):
		return self.process('creatediskofferingresponse',
			self.__execute__('createDiskOffering',
			{'name': name, 'displaytext': displayText, 'diskSize': diskSize}),
			_class)

	def createDomain(self, name, parentDomainId=None, _class=DataObject):
		return self.process('createdomainresponse',
			self.__execute__('createDomain',
			{'name': name, 'parentDomainId': parentDomainId}),
			_class)'''
	
	def createLoadBalancerRule(self, algorithm, name, privatePort, publicPort, 
		description=None, account=None, cidrList=None, domainId=None,
		openFireWall=None, publicIpId=None, zoneId=None, _class=DataObject):
		'''createLoadBalancerRule(algorithm, name, privatePort, publicPort, 
		description=None, account=None, cidrList=None, domainId=None,
		openFireWall=None, publicIpId=None, zoneId=None)'''
		return self.process('createloadbalancerruleresponse',
			self.__execute__('createLoadBalancerRule',
			{'name': name, 'publicipid': publicIpId, 'publicport': publicPort,
			'privateport': privatePort, 'algorithm': algorithm,
			'description': description, 'account':account,
			'cidrlist':cidrList, 'domainid':domainId, 'openfirewall':openFireWall,
			'publicipid':publicIpId, 'zoneid':zoneId}),
			_class)

	'''
	def createPod(self, name, zoneId, cidr, startIp, gateway,
		endIp=None, _class=DataObject):
		return self.process('createpodresponse',
			self.__execute__('createPod',
			{'name': name, 'zoneid': zoneId, 'cidr': cidr, 'startIp': startIp,
			'gateway': gateway, 'endIp': endIp}),
			_class)'''
			
	def createPortForwardingRule(self, ipAddressId, privatePort, protocol, publicPort, 
		virtualMachineId, cidrList=None, openFireWall=None, privateEndPort=None,
		publicEndPort=None, _class=DataObject):
		return self.process('createportforwardingruleresponse',
			self.__execute__('createPortForwardingRule',
			{'ipaddressid': ipAddressId, 'publicport': publicPort,
			'privateport': privatePort, 'protocol': protocol,
			'virtualmachineid': virtualMachineId, 'cidrlist':cidrList,
			'openfirewall':openFireWall, 'privateendport':privateEndPort,
			'publicendport':publicEndPort}),
			_class)

	'''
	def createPortForwardingService(self, name, description=None,
		_class=DataObject):
		return self.process('createportforwardingserviceresponse',
			self.__execute__('createPortForwardingService',
			{'name': name, 'description': description}),
			_class)

	def createPortForwardingServiceRule(self, publicPort, privatePort,
		portForwardingServiceId, protocol=None, _class=DataObject):
		return self.process_async('createPortForwardingServiceRule',
			{'publicPort': publicPort, 'privatePort': privatePort,
			'portForwardingServiceId': portForwardingServiceId,
			'protocol': protocol},
			_class)'''

	def createSecurityGroup(self, name, account=None, description=None,
						domainId=None, _class=DataObject):
		''' createSecurityGroup(name, account=None, description=None,
			domainId=None)'''
		return self.process('createsecuritygroupresponse',
			self.__execute__('createSecurityGroup',
			{'name': name, 'account': account, 'description': description,
			'domainid': domainId}),
			_class)

	'''
	def createServiceOffering(self, name, displayText, cpuNumber, cpuSpeed,
		memory, storageType=None, offerHa=None, useVirtualNetwork=None,
		tags=None, _class=DataObject):
		return self.process('createserviceofferingresponse',
			self.__execute__('createServiceOffering',
			{'name': name, 'displaytext': displayText, 'cpuNumber': cpuNumber,
			'cpuSpeed': cpuSpeed, 'memory': memory,
			'storageType': storageType, 'offerHa': offerHa,
			'useVirtualNetwork': useVirtualNetwork, 'tags': tags}),
			_class)'''

	def createSnapshot(self, volumeId, account=None, domainId=None,
		 policyId=None, _class=DataObject):
		return self.process_async('createSnapshot',
			{'volumeid': volumeId, 'account':account, 'domainid':domainId,
			'policyid':policyId},
			_class)

	def createSnapshotPolicy(self, intervalType, maxSnaps, schedule, timezone,
		volumeId, _class=DataObject):
		return self.process('createsnapshotpolicysresponse',
			self.__execute__('createSnapshotPolicy',
			{'volumeid': volumeId, 'schedule': schedule,
			'intervaltype': intervalType, 'maxsnaps': maxSnaps,
			'timezone': timezone}),
			_class)

	def createSSHKeyPair(self, name, account=None, domainId=None,
						_class=DataObject):
		return self.process('createkeypairresponse',
			self.__execute__('createSSHKeyPair',
			{'name': name, 'account': account, 'domainid': domainId}),
			_class)

	'''
	def createStoragePool(self, name, zoneId, url, podId=None, clusterId=None,
		tags=None, details=None, _class=DataObject):
		return self.process('createstoragepoolresponse',
			self.__execute__('createStoragePool',
			{'name': name, 'zoneid': zoneId, 'url': url, 'podid': podId,
			'clusterid': clusterId, 'tags': tags, 'details': details}),
			_class)'''

	def createTemplate(self, displayText, name,  osTypeId, volumeId=None,
		passwordEnabled=None, isPublic=None, isFeatured=None, snapshotId=None,
		bits=None, requiresHVM=None, url=None, virtualMachineId=None, 
		_class=DataObject):
		'''createTemplate(displayText, name,  osTypeId, volumeId=None,
		passwordEnabled=None, isPublic=None, isFeatured=None, snapshotId=None,
		bits=None, requiresHVM=None, url=None, virtualMachineId=None, 
		_class=DataObject)'''
		return self.process_async('createTemplate',
			{'name': name, 'displaytext': displayText, 'ostypeid': osTypeId,
			'volumeid': volumeId, 'passwordenabled': passwordEnabled,
			'ispublic': isPublic, 'isfeatured': isFeatured,
			'snapshotid': snapshotId, 'bits':bits, 'requireshvm':requiresHVM, 'url':url,
			'virtualmachineid':virtualMachineId},
			_class)

	'''
	def createUser(self, username, password, email, firstName, lastName,
		accountType, domainId=None, account=None, timezone=None,
		_class=User):
		return self.process_list('createuserresponse>user',
			self.__execute__('createUser',
			{'username': username, 'password': password, 'email': email,
			'firstName': firstName, 'lastName': lastName,
			'accountType': accountType, 'domainId': domainId,
			'account': account, 'timezone': timezone}),
			_class)[0]

	def createVlanIpRange(self, gateway, netmask, zoneId, startIp, endIp=None,
		vlan=None, _class=DataObject):
		return self.process('createvlaniprangeresponse',
			self.__execute__('createVlanIpRange',
			{'gateway': gateway, 'netmask': netmask, 'zoneid': zoneId,
			'startIp': startIp, 'endIp': endIp, 'vlan': vlan}),
			_class)'''

	def createVolume(self, name, size=None, zoneId=None, diskOfferingId=None,
		snapshotId=None, account=None, domainId=None, _class=DataObject):
		return self.process_async('createVolume',
			{'name': name, 'size': size, 'zoneid': zoneId, 
			'diskofferingid': diskOfferingId, 'snapshotid': snapshotId,
			'account':account, 'domainid':domainId},
			_class)

	'''
	def createZone(self, name, dns1, internaldns1, guestCidrAddress, dns2=None,
		internaldns2=None, vnet=None, _class=DataObject):
		return self.process('createzoneresponse',
			self.__execute__('createZone',
			{'name': name, 'dns1': dns1, 'internaldns1': internaldns1,
			'guestcidraddress': guestCidrAddress, 'dns2': dns2,
			'internaldns2': internaldns2, 'vnet': vnet}),
			_class)

	def deleteDiskOffering(self, id, _class=DataObject):
		return self.process('deletediskofferingresponse',
			self.__execute__('deleteDiskOffering',
			{'id': id}),
			_class)

	def deleteDomain(self, id, _class=DataObject):
		return self.process_async('deleteDomain',
			{'id': id},
			_class)

	def deleteHost(self, id, _class=DataObject):
		return self.process('deletehostresponse',
			self.__execute__('deleteHost',
			{'id': id}),
			_class)'''

	def deleteIso(self, id, zoneId=None, _class=DataObject):
		return self.process('deleteisoresponse',
			self.__execute__('deleteIso',
			{'id': id, 'zoneid': zoneId}),
			_class)

	def deleteLoadBalancerRule(self, id, _class=DataObject):
		'''deleteLoadBalancerRule(id)'''
		return self.process('deleteloadbalancerruleresponse',
			self.__execute__('deleteLoadBalancerRule',
			{'id': id}),
			_class)

	'''
	def deletePod(self, id, _class=DataObject):
		return self.process('deletepodresponse',
			self.__execute__('deletePod',
			{'id': id}),
			_class)'''

	def deletePortForwardingRule(self, id, _class=DataObject):
		return self.process('deleteportforwardingruleresponse',
			self.__execute__('deletePortForwardingRule',
			{'id': id}),
			_class)

	'''
	def deletePortForwardingService(self, id, _class=DataObject):
		return self.process_async('deletePortForwardingService',
			{'id': id},
			_class)

	def deletePortForwardingServiceRule(self, id, _class=DataObject):
		return self.process_async('deletePortForwardingServiceRule',
			{'id': id},
			_class)'''
	
	def deleteSecurityGroup(self, id=None, account=None, domainId=None,
		name=None, _class=DataObject):
		'''deleteSecurityGroup(id=None, account=None, domainId=None,
		name=None) '''
		return self.process('deletesecuritygroupresponse',
			self.__execute__('deleteSecurityGroup',
			{'id': id, 'account':account, 'domainid':domainId, 'name':name}),
			_class)

	'''
	def deleteServiceOffering(self, id, _class=DataObject):
		return self.process('deleteserviceofferingresponse',
			self.__execute__('deleteServiceOffering',
			{'id': id}),
			_class)'''

	def deleteSnapshot(self, id, _class=DataObject):
		return self.process_async('deleteSnapshot',
			{'id': id},
			_class)

	def deleteSnapshotPolicies(self, id=None, ids=None,
		_class=DataObject):
		return self.process('deletesnapshotpoliciesresponse',
			self.__execute__('deleteSnapshotPolicies',
			{'id': id, 'ids': ids}),
			_class)

	def deleteSSHKeyPair(self, name, account=None, domainId=None, _class=DataObject):
		'''deleteSSHKeyPair(name, account=None, domainId=None)'''
		return self.process('deletekeypairresponse',
			self.__execute__('deleteSSHKeyPair',
			{'name': name, 'account': account, 'domainid': domainId}),
			_class)

	'''
	def deleteStoragePool(self, name, _class=DataObject):
		return self.process('deletestoragepoolresponse',
			self.__execute__('deleteStoragePool',
			{'name': name}),
			_class)'''

	def deleteTemplate(self, id, zoneId=None, _class=DataObject):
		'''deleteTemplate(id, zoneid=None)'''
		return self.process_async('deleteTemplate',
			{'id': id, 'zoneid':zoneId},
			_class)

	'''
	def deleteUser(self, id, _class=DataObject):
		return self.process('deleteuserresponse',
			self.__execute__('deleteUser',
			{'id': id}),
			_class)

	def deleteVlanIpRange(self, id, _class=DataObject):
		return self.process('deletevlaniprangeresponse',
			self.__execute__('deleteVlanIpRange',
			{'id': id}),
			_class)'''

	def deleteVolume(self, id, _class=DataObject):
		return self.process('deletevolumeresponse',
			self.__execute__('deleteVolume',
			{'id': id}),
			_class)

	'''
	def deleteZone(self, id, _class=DataObject):
		return self.process('deletezoneresponse',
			self.__execute__('deleteZone',
			{'id': id}),
			_class)'''

	def deployVirtualMachine(self, serviceOfferingId, templateId, zoneId,  
		diskOfferingId=None, displayName=None, group=None, 
		keypair=None, securityGroupIds=None, networkIds=None, userData=None,
		account=None, domainId=None, hostId=None, hypervisor=None, ipAddress=None,
		ip2NetWorkList=None, keyboard=None, name=None, securityGroupNames=None,
		size=None, _class=VirtualMachine):
		'''
		deployVirtualMachine(serviceOfferingId, templateId, zoneId,  
		diskOfferingId=None, displayName=None, group=None, 
		keypair=None, securityGroupIds=None, networkIds=None, userData=None,
		account=None, domainId=None, hostId=None, hypervisor=None, ipAddress=None,
		ip2NetWorkList=None, keyboard=None, name=None, securityGroupNames=None,
		size=None):
		'''
		return self.process_async('deployVirtualMachine', 
			{'zoneid': zoneId, 'serviceofferingid': serviceOfferingId,
			'account':account, 'domainid':domainId, 'hostid':hostId,
			'hypervisor':hypervisor, 'ipaddress':ipAddress, 'iptonetworklist':ip2NetWorkList,
			'keyboard':keyboard, 'name':name, 'securitygroupnames':securityGroupNames,
			'size':size, 'templateid': templateId, 'diskofferingid': diskOfferingId,
			'displayname': displayName, 'group': group,
			'keypair': keypair, 'securitygroupids': securityGroupIds,
			'networkids': networkIds, 'userdata': userData},
			_class)

	def destroyVirtualMachine(self, id, _class=DataObject):
		''' destroyVirtualMachine(id)'''
		return self.process_async('destroyVirtualMachine',
			{'id': id},
			_class)

	def detachIso(self, virtualMachineId, _class=DataObject):
		return self.process_async('detachIso',
			{'virtualmachineid': virtualMachineId},
			_class)

	def detachVolume(self, id=None, deviceId=None, virtualMachineId=None, _class=DataObject):
		return self.process_async('detachVolume',
			{'id': id, 'deviceid':deviceId, 'virtualmachineid':virtualMachineId},
			_class)

	def disableAccount(self, account, domainId, lock, _class=DataObject):
		'''disableAccount(account, domainId, lock)'''
		return self.process_async('disableAccount',
			{'account': account, 'domainid': domainId, 'lock':lock},
			_class)

	def disableUser(self, id, _class=DataObject):
		'''disableUser(id)'''
		return self.process_async('disableUser',
			{'id': id},
			_class)

	def disassociateIpAddress(self, id, _class=DataObject):
		return self.process('disassociateipaddressresponse',
			self.__execute__('disassociateIpAddress',
			{'id': id}),
			_class)

	def enableAccount(self, account, domainId, _class=DataObject):
		'''enableAccount( account, domainId)'''
		return self.process('enableaccountresponse',
			self.__execute__('enableAccount',
			{'account': account, 'domainid': domainId}),
			_class)

	def enableUser(self, id, _class=DataObject):
		''' enableUser(id)'''
		return self.process('enableuserresponse',
			self.__execute__('enableUser',
			{'id': id}),
			_class)

	def getCloudIdentifier(self, userId, _class=DataObject):
		return self.process('getcloudidentifierresponse',
			self.__execute__('getCloudIdentifier',
			{'userid': userId}),
			_class)

	def listAccounts(self, accountType=None, domainId=None, id=None,
		isCleanupRequired=None, isRecursive=None, keyword=None,
		name=None, page=None, pageSize=None, state=None, _class=Account):
		'''listAccounts(accountType=None, domainId=None, id=None,
		isCleanupRequired=None, isRecursive=None, keyword=None,
		name=None, page=None, pageSize=None, state=None)'''
		return self.process_list('listaccountsresponse>account',
			self.__execute__('listAccounts',
			{'accounttype':accountType, 'domainid':domainId, 'id':id,
			 'iscleanuprequired':isCleanupRequired, 'isrecursive':isRecursive,
			  'keyword': keyword, 'name':name, 'page':page, 'pagesize':pageSize,
			  'state':state}),
			_class)

	'''
	def listAlerts(self, type=None, keyword=None, _class=DataObject):
		return self.process_list('listalertsresponse>alert',
			self.__execute__('listAlerts',
			{'type': type, 'keyword': keyword}),
			_class)'''

	def listAsyncJobs(self, account=None, domainId=None, keyword=None,
		page=None, pageSize=None, startDate=None, _class=DataObject):
		return self.process_list('listasyncjobsresponse>asyncjobs',
			self.__execute__('listAsyncJobs',
			{'account':account, 'domainid':domainId,'keyword':keyword,
			'page':page, 'pagesize':pageSize, 'startdate': startDate}),
			_class)

	'''
	def listCapacity(self, zoneId=None, podId=None, hostId=None, type=None,
		_class=DataObject):
		return self.process_list('listcapacityresponse>capacity',
			self.__execute__('listCapacity',
			{'zoneid': zoneId, 'podid': podId, 'hostId': hostId,
			'type': type}),
			_class)

	def listClusters(self, id=None, name=None, podId=None, zoneId=None,
		_class=DataObject):
		return self.process_list('listclusterresponse>cluster',
			self.__execute__('listClusters',
			{'id': id, 'name': name, 'podid': podId, 'zoneid': zoneId}),
			_class)

	def listConfigurations(self, name=None, category=None, keyword=None,
		_class=DataObject):
		return self.process_list('listconfigurationsresponse>configuration',
			self.__execute__('listConfigurations',
			{'name': name, 'category': category, 'keyword': keyword}),
			_class)'''

	def listDiskOfferings(self, domainId=None,  id=None, name=None, keyword=None,
		page=None, pageSize=None, _class=DataObject):
		return self.process_list('listdiskofferingsresponse>diskoffering',
			self.__execute__('listDiskOfferings',
			{'domainid':domainId, 'id': id, 'name': name, 'keyword': keyword,
			'page':page, 'pagesize':pageSize}),
			_class)
	'''
	def listDomainChildren(self, id=None, isRecursive=None, name=None, keyword=None,
		page=None, pageSize=None, _class=DataObject):
		return self.process_list('listdomainchildrenresponse>domain',
			self.__execute__('listDomainChildren',
			{'id': id, 'isrecursive':isRecursive, 'name': name, 'keyword': keyword,
			 'page':page, 'pagesize':pageSize}),
			_class)
	
	def listDomains(self, id=None, keyword=None, level=None, name=None, page=None,
		pageSize=None, _class=DataObject):
		return self.process_list('listdomainsresponse>domain',
			self.__execute__('listDomains',
			{'id': id, 'keyword': keyword, 'level':level, 'name': name, 'page':page,
			'pagesize':pageSize}),
			_class)'''

	def listEvents(self, account=None, domainId=None, duration=None, endDate=None,
		 entryTime=None, id=None, keyword=None, level=None, page=None, pageSize=None,
		  startDate=None, type=None, _class=DataObject):
		return self.process_list('listeventsresponse>event',
			self.__execute__('listEvents',
			{'account':account, 'domainid':domainId, 'duration': duration, 'enddate': endDate,
			 'entrytime': entryTime, 'id':id, 'keyword': keyword, 'level': level, 'page':page,
			 'pagesize':pageSize, 'startdate': startDate, 'type': type}),
			_class)

	'''
	def listHosts(self, id=None, name=None, zoneId=None, podId=None, type=None,
		state=None, _class=DataObject):
		return self.process_list('listhostsresponse>host',
			self.__execute__('listHosts',
			{
				'id': id, 'name': name, 'zoneid': zoneId, 'podid': podId,
				'type': type, 'state': state}),
			_class)'''

	def listIsos(self, account=None, domainId=None, hypervisor=None, id=None,
		isoFilter=None, isPublic=None, isReady=None, keyword=None,
		name=None, page=None, pageSize=None, zoneId=None, _class=DataObject):
		return self.process_list('listisosresponse>iso',
			self.__execute__('listIsos',
			{
			   'account':account, 'domainid':domainId, 'hypervisor':hypervisor, 'id': id,
			   'isofilter':isoFilter, 'ispublic':isPublic, 'isready':isReady,
			   'keyword': keyword, 'name': name, 'page':page, 'pagesize': pageSize,
			   'zoneid':zoneId}),
			_class)

	def listLoadBalancerRuleInstances(self, id, applied=None, keyword=None, page=None,
		pageSize=None, _class=DataObject):
		'''listLoadBalancerRuleInstances(id, applied=None, keyword=None, page=None,
		pageSize=None)'''
		return self.process_list(
			'listloadbalancerruleinstancesresponse>loadbalancerruleinstance',
			self.__execute__('listLoadBalancerRuleInstances',
			{'id': id, 'applied': applied, 'keyword':keyword, 'page':page,
			 'pagesize':pageSize}),
			_class)

	def listLoadBalancerRules(self, account=None, domainId=None, id=None, keyword=None,
		name=None, page=None, pageSize=None, publicIpId=None, 
		virtualMachineId=None, zoneId=None, _class=DataObject):
		'''listLoadBalancerRules(account=None, domainId=None, id=None, keyword=None,
		name=None, page=None, pageSize=None, publicIpId=None, 
		virtualMachineId=None, zoneId=None)'''
		return self.process_list(
			'listloadbalancerrulesresponse>loadbalancerrule',
			self.__execute__('listLoadBalancerRules',
			{'account':account, 'domainid':domainId, 'id': id, 'keyword': keyword,
			 'name': name, 'page':page, 'pagesize':pageSize, 'publicipid':publicIpId,
			'virtualmachineid': virtualMachineId, 'zoneid': zoneId}),
			_class)

	def listNetworks(self, account=None, domainId=None, id=None, isDefault=None,
		isShared=None, isSystem=None, keyword=None, page=None, pageSize=None,
		trafficType=None, type=None, zoneId=None, _class=DataObject):
		return self.process_list(
			'listnetworksresponse>network', 
			self.__execute__('listNetworks',
			{'id': id, 'account': account, 'domainid': domainId,'isdefault':isDefault,
			'isshared':isShared, 'issystem':isSystem, 'keyword':keyword, 'page':page,
			'pagesize':pageSize, 'traffictype':trafficType, 'type':type, 'zoneid':zoneId,
			}), _class)

	def listOsCategories(self, id=None, keyword=None, page=None, pageSize=None,
		_class=DataObject):
		return self.process_list('listoscategoriesresponse>oscategory',
			self.__execute__('listOsCategories',
			{'id':id, 'keyword':keyword, 'page':page, 'pagesize':pageSize}),
			_class)

	def listOsTypes(self, id=None, keyword=None, osCategoryId=None, page=None,
		pageSize=None, _class=DataObject):
		return self.process_list('listostypesresponse>ostype',
			self.__execute__('listOsTypes',
			{'id':id, 'keyword':keyword, 'oscategoryid':osCategoryId, 'page':page,
			'pagesize':pageSize}),
			_class)

	'''
	def listPods(self, id=None, name=None, keyword=None, zoneId=None,
		_class=DataObject):
		return self.process_list('listpodsresponse>pod',
			self.__execute__('listPods',
			{'id': id, 'name': name, 'keyword': keyword, 'zoneid': zoneId}),
			_class)'''

	def listPortForwardingRules(self, account=None, domainId=None, id=None,
		 ipAddressId=None, keyword=None, page=None, pageSize=None, _class=DataObject):
		return self.process_list(
			'listportforwardingrulesresponse>portforwardingrule',
			self.__execute__('listPortForwardingRules',
			{'account': account, 'domainid': domainId, 'id': id,
			 'ipaddressid': ipAddressId, 'keyword':keyword, 'page':page,
			'pagesize':pageSize}),
			_class)

	'''
	def listPortForwardingServiceRules(self, id=None,
		portForwardingServiceId=None, _class=DataObject):
		return self.process_list(
			'listportforwardingservicerulesresponse>portforwardingservicerule',
			self.__execute__('listPortForwardingServiceRules',
			{'id': id, 'portForwardingServiceId': portForwardingServiceId}),
			_class)

	def listPortForwardingServices(self, id=None, name=None, keyword=None,
		_class=DataObject):
		return self.process_list(
			'listportforwardingservicesresponse>portforwardingservice',
			self.__execute__('listPortForwardingServices',
			{'id': id, 'name': name, 'keyword': keyword}),
			_class)

	def listPortForwardingServicesByVm(self, virtualMachineId, ipAddress=None,
		keyword=None, _class=DataObject):
		return self.process_list(
			'listportforwardingservicesbyvmresponse>portforwardingservice',
			self.__execute__('listPortForwardingServicesByVm',
			{'virtualmachineid': virtualMachineId, 'ipAddress': ipAddress,
			'keyword': keyword}),
			_class)'''

	def listPublicIpAddresses(self, account=None, allocatedOnly=None, domainId=None,
		forLoadBalancing=None, forVirtualNetwork=None, id=None, ipAddress=None,
		keyword=None, page=None, pageSize=None, vlanId=None, zoneId=None,
		_class=DataObject):
		return self.process_list(
			'listpublicipaddressesresponse>publicipaddress',
			self.__execute__('listPublicIpAddresses',
			{'account': account, 'allocatedonly':allocatedOnly, 'domainid': domainId,
			'forloadbalancing':forLoadBalancing, 'forvirtualnetwork':forVirtualNetwork,
			'id': id, 'ipaddress': ipAddress, 'keyword': keyword, 'page':page,
			'pagesize':pageSize, 'vlanid':vlanId, 'zoneid': zoneId}), _class)

	def listResourceLimits(self, account=None,  domainId=None, id=None, keyword=None,
		page=None, pageSize=None, resourceType=None, _class=DataObject):
		return self.process_list('listresourcelimitsresponse>resourcelimit',
			self.__execute__('listResourceLimits',
			{'account': account, 'domainid': domainId, 'id': id, 'keyword':keyword,
			'page':page, 'pagesize':pageSize, 'resourcetype': resourceType}),
			_class)


	def listRouters(self, account=None, domainId=None, hostId=None, id=None,keyword=None,
		name=None, networkId=None, page=None, pageSize=None, podId=None, state=None,
		zoneId=None, _class=DataObject):
		return self.process_list('listroutersresponse>router',
			self.__execute__('listRouters',
			{'account': account, 'domainid': domainId, 'hostid': hostId, 'id': id,
			'keyword': keyword, 'name': name, 'networkid':networkId, 'page':page,
			'pagesize':pageSize, 'podid': podId, 'state': state, 'zoneid': zoneId}),
			_class)

	def listSecurityGroups(self, account=None,  domainId=None, id=None, keyword=None,
		page=None, pageSize=None, securityGroupName=None, virtualMachineId=None,
		_class=DataObject):
		return self.process_list('listsecuritygroupsresponse>securitygroup',
			self.__execute__('listSecurityGroups',
			{'account': account, 'domainid': domainId, 'id': id, 'keyword': keyword,
			'page':page, 'pagesize':pageSize, 'securitygroupname':securityGroupName,
			'virtualmachineid': virtualMachineId}),	_class)

	def listServiceOfferings(self, domainId=None, id=None, isSystem=None, keyword=None,
		name=None, page=None, pageSize=None, systemVMType=None, virtualMachineId=None,
		 _class=DataObject):
		return self.process_list(
			'listserviceofferingsresponse>serviceoffering',
			self.__execute__('listServiceOfferings',
			{'domainid': domainId, 'id': id, 'issystem':isSystem, 'keyword':keyword,
			'name': name, 'page':page, 'pagesize':pageSize, 'systemvmtype':systemVMType,
			'virtualmachineid': virtualMachineId}),
			_class)

	def listSnapshotPolicies(self, volumeId, account=None,  domainId=None, keyword=None,
		page=None, pageSize=None,_class=DataObject):
		return self.process_list('listsnapshotpoliciesresponse>snapshotpolicy',
			self.__execute__('listSnapshotPolicies',
			{'volumeid': volumeId, 'account': account, 'domainid': domainId,
			 'keyword': keyword, 'page':page, 'pagesize':pageSize}), _class)

	def listSnapshots(self, account=None, domainId=None, id=None, intervalType=None,
		isRecursive=None, keyword=None, name=None, page=None, pageSize=None,
		snapshotType=None, volumeId=None, _class=DataObject):
		return self.process_list('listsnapshotsresponse>snapshot',
			self.__execute__('listSnapshots',
			{'account': account, 'domainid': domainId, 'id': id, 'intervaltype':
			 intervalType, 'isrecursive':isRecursive, 'keyword': keyword, 'name': name,
			 'page':page, 'pagesize':pageSize, 'snapshottype': snapshotType,
			 'volumeid':volumeId}),
			_class)

	def listSSHKeyPairs(self, fingerprint=None, keyword=None, name=None, page=None,
		pageSize=None, _class=DataObject):
		'''listSSHKeyPairs(fingerprint=None, keyword=None, name=None, page=None,
		pageSize=None)'''
		return self.process_list('listsshkeypairsresponse>keypair',
			self.__execute__('listSSHKeyPairs',
			{'fingerprint': fingerprint, 'keyword': keyword, 'name': name, 'page':page,
			'pagesize':pageSize }),
			_class)

	'''
	def listStoragePools(self, name=None, zoneId=None, ipAddress=None,
		path=None, keyword=None, podId=None, _class=DataObject):
		return self.process_list('liststoragepoolresponse>storagepool',
			self.__execute__('listStoragePools',
			{'name': name, 'zoneid': zoneId, 'ipAddress': ipAddress,
			'path': path, 'keyword': keyword, 'podid': podId}),
			_class)

	def listSystemVms(self, id=None, zoneId=None, podId=None, hostId=None,
		state=None, name=None, account=None, domainId=None, keyword=None,
		systemVmType=None, _class=DataObject):
		return self.process_list('listsystemvmsresponse>systemvm',
			self.__execute__('listSystemVms',
			{
				'id': id, 'zoneid': zoneId, 'podid': podId, 'hostId': hostId,
				'state': state, 'name': name, 'account': account,
				'domainid': domainId, 'keyword': keyword,
				'systemVmType': systemVmType}),
			_class)'''

	def listTemplatePermissions(self, id, account=None, domainId=None, _class=DataObject):
		'''listTemplatePermissions(self, id, account=None, domainId=None)'''
		return self.process_list(
			'listtemplatepermissionsresponse>templatepermission',
			self.__execute__('listTemplatePermissions',
			{'id': id, 'account': account, 'domainid': domainId,}),
			_class)

		
	#TODO:not required:
	def listCommunityTemplates(self, id=None, name=None, keyword=None,
		_class=DataObject):
		return self.listTemplates('community', id=id, name=name, keyword=keyword)

	def listFeaturedTemplates(self, id=None, name=None, keyword=None,
		_class=DataObject):
		return self.listTemplates('featured', id=id, name=name, keyword=keyword)


	def listTemplates(self, templateFilter, account=None, domainId=None, hypervisor=None,
		id=None, keyword=None, name=None, page=None, pageSize=None, zoneId=None,
		_class=DataObject):
		'''listTemplates(templateFilter, account=None, domainId=None, hypervisor=None,
		id=None, keyword=None, name=None, page=None, pageSize=None, zoneId=None)'''
		return self.process_list('listtemplatesresponse>template',
			self.__execute__('listTemplates',
			{'templatefilter': templateFilter, 'account': account, 'domainid': domainId,
			'hypervisor':hypervisor, 'id': id, 'keyword': keyword, 'name':name,
			'page':page, 'pagesize':pageSize, 'zoneid': zoneId}),
			_class)

	'''
	def listUsageRecords(self, startDate, endDate, account=None, domainId=None,
		_class=DataObject):
		return self.process_list('listusagerecordsresponse>usagerecord',
			self.__execute__('listUsageRecords',
			{
				'startDate': startDate, 'endDate': endDate, 'account': account,
				'domainid': domainId}),
			_class)

	def listUsers(self, account=None, accountType=None, domainId=None,
		id=None, keyword=None, page=None, pageSize=None, state=None, username=None,
		_class=User):
		return self.process_list('listusersresponse>user',
			self.__execute__('listUsers',
			{'account': account, 'accounttype':accountType, 'domainid': domainId,
			'id': id, 'keyword': keyword, 'page':page, 'pagesize':pageSize,
			'state': state, 'username': username}),
			_class)'''

	def listVirtualMachines(self, account=None, domainId=None, forVirtualNetwork=None,
		groupId=None, hostId=None, hypervisor=None, id=None, isRecursive=None,
		keyword=None, name=None, networkId=None, page=None, pageSize=None, podId=None,
		state=None, storageId=None, zoneId=None, _class=VirtualMachine):
		return self.process_list('listvirtualmachinesresponse>virtualmachine',
			self.__execute__('listVirtualMachines',
			{'account': account, 'domainid': domainId,
			'forvirtualnetwork':forVirtualNetwork, 'groupid':groupId,
			'hsotid': hostId, 'hypervisor':hypervisor, 'id': id,
			'isrecursive':isRecursive, 'keyword': keyword, 'name':name,
			'networkid':networkId, 'page':page, 'pagesize':pageSize, 'podid': podId,
			'state':state,'storageid':storageId, 'zoneid': zoneId}),
			_class)

	def getVirtualMachineById(self, id):
		return [i for i in self.listVirtualMachines()
			if i.id == id][0]
			
	'''
	def listVlanIpRanges(self, id=None, name=None, zoneId=None, keyword=None,
		vlan=None, podId=None, account=None, domainId=None, _class=DataObject):
		return self.process_list('listvlaniprangesresponse>vlaniprange',
			self.__execute__('listVlanIpRanges',
			{'id': id, 'name': name, 'zoneid': zoneId, 'keyword': keyword,
			'vlan': vlan, 'podid': podId, 'account': account,
			'domainid': domainId}),
			_class)'''

	def listVolumes(self, account=None, domainId=None, hostId=None, id=None,
		isRecursive=None, keyword=None, name=None, page=None, pageSize=None,
		podId=None, type=None, virtualMachineId=None, zoneId=None, _class=DataObject):
		return self.process_list('listvolumesresponse>volume',
			self.__execute__('listVolumes',
			{'account': account, 'domainid': domainId, 'hsotid': hostId, 'id': id,
			'isrecursive':isRecursive, 'keyword': keyword, 'name':name, 'page':page,
			'pagesize':pageSize, 'podid':podId, 'type':type,
			'virtualmachineid':virtualMachineId, 'zoneid': zoneId}),
			_class)

	def listZones(self, account=None, domainId=None, id=None, keyword=None, page=None,
		pageSize=None, _class=DataObject):
		return self.process_list('listzonesresponse>zone',
			self.__execute__('listZones',
			{'account': account, 'domainid': domainId, 'id': id, 'keyword': keyword,
			'page':page, 'pagesize':pageSize}),
			_class)

	'''
	def lockAccount(self, account, domainId, _class=DataObject):
		return self.process('lockaccountresponse',
			self.__execute__('lockAccount',
			{'account': account, 'domainid': domainId}),
			_class)

	def lockUser(self, id=None, _class=DataObject):
		return self.process('lockuserresponse',
			self.__execute__('lockUser',
			{'id': id}),
			_class)'''

	def login(self, username, password, domain=None, _class=DataObject):
		return self.process('loginresponse',
			self.__execute__('login',
			{'username': username, 'password': password,
			'domain': domain}),
			_class)

	def logout(self, _class=DataObject):
		return self.process('logoutresponse',
			self.__execute__('logout',
			{}),
			_class)
	'''		
	def prepareHostForMaintenance(self, id, _class=DataObject):
		return self.process_async('prepareHostForMaintenance',
			{'id': id},
			_class)'''

	def queryAsyncJobResult(self, jobId, _class=DataObject):
		return self.process('queryasyncjobresultresponse',
			self.__execute__('queryAsyncJobResult',
			{'jobid': jobId}),
			_class)
		
	def rebootRouter(self, id, _class=DataObject):
		return self.process_async('rebootRouter',
			{'id': id},
			_class)
	'''
	def rebootSystemVm(self, id, _class=DataObject):
		return self.process_async('rebootSystemVm',
			{'id': id},
			_class)'''


	def rebootVirtualMachine(self, id, _class=DataObject):
		''' rebootVirtualMachine(id)'''
		return self.process_async('rebootVirtualMachine',
			{'id': id},
			_class)

	'''
	def reconnectHost(self, id, _class=DataObject):
		return self.process_async('reconnectHost',
			{'id': id},
			_class)'''

	def recoverVirtualMachine(self, id, _class=DataObject):
		'''recoverVirtualMachine(id)'''
		return self.process('recovervirtualmachineresponse',
			self.__execute__('recoverVirtualMachine',
			{'id': id}),
			_class)

	def registerIso(self, displayText, name,  url, zoneId,	account=None,
		bootable=None, domainId=None, isExtractable=None,isFeatured=None,
		isPublic=None, osTypeId=None, _class=DataObject):
		return self.process('registerisoresponse',
			self.__execute__('registerIso',
			{'displaytext': displayText, 'name': name, 'url': url, 'zoneid': zoneId,
			'account': account, 'bootable': bootable, 'domainid': domainId,
			'isextractable':isExtractable, 'isfeatured': isFeatured,'ispublic': isPublic,
			'ostypeid': osTypeId}),
			_class)

	def registerTemplate(self, displayText, format, hypervisor, name, osTypeId,	url,
		zoneId, account=None, bits=None, checkSum=None, domainId=None,isExtractable=None,
		isFeatured=None, isPublic=None, passwordEnabled=None, requiresHVM=None,
		_class=DataObject):
		'''registerTemplate(displayText, format, hypervisor, name, osTypeId,	url,
		zoneId, account=None, bits=None, checkSum=None, domainId=None,isExtractable=None,
		isFeatured=None, isPublic=None, passwordEnabled=None, requiresHVM=None)'''
		
		return self.process('registertemplateresponse',
			self.__execute__('registerTemplate',
			{'displaytext': displayText, 'format': format, 'hypervisor':hypervisor,
			'name': name, 'ostypeid': osTypeId, 'url': url, 'zoneid': zoneId,
			'account': account, 'bits':bits, 'checksum':checkSum, 'domainid': domainId,
			'isextractable':isExtractable, 'isfeatured': isFeatured,'ispublic': isPublic,
			'passwordenabled': passwordEnabled, 'requireshvm':requiresHVM}),
			_class)

	'''
	def registerUserKeys(self, id, _class=DataObject):
		return self.process('registeruserkeysresponse',
			self.__execute__('registerUserKeys',
			{'id': id}),
			_class)'''

	def removeFromLoadBalancerRule(self, id, virtualMachineIds, _class=DataObject):
		'''removeFromLoadBalancerRule(id, virtualMachineIds)'''
		return self.process_async('removeFromLoadBalancerRule',
			{'id': id, 'virtualmachineids': virtualMachineIds},
			_class)

	'''
	def removePortForwardingService(self, id, publicIp, virtualMachineId,
		_class=DataObject):
		return self.process_async('removePortForwardingService',
			{'id': id, 'publicip': publicIp,
			'virtualmachineid': virtualMachineId},
			_class)'''


	def resetPasswordForVirtualMachine(self, id, _class=DataObject):
		''' resetPasswordForVirtualMachine(id)'''
		return self.process_async('resetPasswordForVirtualMachine',
			{'id': id},
			_class)

	def startRouter(self, id, _class=DataObject):
		return self.process_async('startRouter',
			{'id': id},
			_class)

	'''
	def startSystemVm(self, id, _class=DataObject):
		return self.process_async('startSystemVm',
			{'id': id},
			_class)'''

	def startVirtualMachine(self, id, _class=DataObject):
		''' startVirtualMachine(id)'''
		return self.process_async('startVirtualMachine',
			{'id': id},
			_class)

	def stopRouter(self, id, forced=None, _class=DataObject):
		return self.process_async('stopRouter',
			{'id': id, 'forced':forced},
			_class)

	'''
	def stopSystemVm(self, id, _class=DataObject):
		return self.process_async('stopSystemVm',
			{'id': id},
			_class)'''

	def stopVirtualMachine(self, id, forced=None, _class=DataObject):
		'''stopVirtualMachine(id, forced=None)'''
		return self.process_async('stopVirtualMachine',
			{'id': id, 'forced':forced},
			_class)

	'''
	def updateAccount(self, newName, account, domainId, _class=DataObject):
		return self.process('updateaccountresponse',
			self.__execute__('updateAccount',
			{'newName': newName, 'account': account, 'domainid': domainId}),
			_class)

	def updateConfiguration(self, name, value, _class=DataObject):
		return self.process('updateconfigurationresponse',
			self.__execute__('updateConfiguration',
			{'name': name, 'value': value}),
			_class)

	def updateDiskOffering(self, id, name=None, displayText=None,
		_class=DataObject):
		return self.process('updatediskofferingresponse',
			self.__execute__('updateDiskOffering',
			{'id': id, 'name': name, 'displaytext': displayText}),
			_class)

	def updateDomain(self, id, name=None, _class=DataObject):
		return self.process('updatedomainresponse',
			self.__execute__('updateDomain',
			{'id': id, 'name': name}),
			_class)

	def updateHost(self, id, osCategoryId=None, _class=DataObject):
		return self.process('updatehostresponse',
			self.__execute__('updateHost',
			{'id': id, 'osCategoryId': osCategoryId}),
			_class)'''

	def updateIso(self, id, bootable=None, displayText=None, format=None, name=None,
		osTypeId=None, passwordEnabled=None, _class=DataObject):
		return self.process('updateisoresponse',
			self.__execute__('updateIso',
			{'id': id, 'bootable': bootable, 'displaytext': displayText, 'format':format,
			'name': name, 'ostypeid': osTypeId, 'passwordenabled':passwordEnabled,}),
			_class)

	'''
	def updatePod(self, id, name=None, cidr=None, startIp=None, endIp=None,
		gateway=None, _class=DataObject):
		return self.process('updatepodresponse',
			self.__execute__('updatePod',
			{'id': id, 'name': name, 'cidr': cidr, 'startIp': startIp,
			'endIp': endIp, 'gateway': gateway}),
			_class)

	def updatePortForwardingRule(self, ipAddress, publicPort, privatePort,
		protocol, virtualMachineId, _class=DataObject):
		return self.process('updateportforwardingruleresponse',
			self.__execute__('updatePortForwardingRule',
			{'ipAddress': ipAddress, 'publicPort': publicPort,
			'privatePort': privatePort, 'protocol': protocol,
			'virtualmachineid': virtualMachineId}),
			_class)'''

	def updateResourceLimit(self, resourceType, account=None, domainId=None,
		max=None, _class=DataObject):
		return self.process('updateresourcelimitresponse',
			self.__execute__('updateResourceLimit',
			{'resourcetype': resourceType, 'account': account,
			'domainid': domainId, 'max': max}),
			_class)

	'''
	def updateServiceOffering(self, id, name=None, displayText=None,
		offerHa=None, _class=DataObject):
		return self.process('updateserviceofferingresponse',
			self.__execute__('updateServiceOffering',
			{'id': id, 'name': name, 'displaytext': displayText,
			'offerHa': offerHa}),
			_class)

	def updateStoragePool(self, id=None, tags=None, _class=DataObject):
		return self.process('updatestoragepoolresponse',
			self.__execute__('updateStoragePool',
			{'id': id, 'tags': tags}),
			_class)'''

	def updateTemplate(self, id, bootable=None, displayText=None, format=None, name=None,
		osTypeId=None, passwordEnabled=None, _class=DataObject):
		'''updateTemplate(id, bootable=None, displayText=None, format=None, name=None,
		osTypeId=None, passwordEnabled=None)'''
		return self.process('updatetemplateresponse',
			self.__execute__('updateTemplate',
			{'id': id, 'bootable':bootable, 'displaytext': displayText,'format': format,
			'name': name, 'ostypeid': osTypeId, 'passwordenabled': passwordEnabled}),
			_class)

	def updateTemplatePermissions(self, id, accounts=None, isExtractable=None,
		isFeatured=None, isPublic=None,	op=None, _class=DataObject):
		return self.process('updatetemplatepermissionsresponse',
			self.__execute__('updateTemplatePermissions',
			{'id': id, 'accounts': accounts, 'isextractable':isExtractable,
			'isfeatured': isFeatured, 'ispublic': isPublic, 'op': op}),
			_class)


	'''
	def updateUser(self, id, username=None, password=None, email=None,
		firstName=None, lastName=None, timezone=None, apiKey=None,
		secretKey=None, _class=DataObject):
		return self.process('updateuserresponse',
			self.__execute__('updateUser',
			{'id': id, 'username': username, 'password': password,
			'email': email, 'firstName': firstName, 'lastName': lastName,
			'timezone': timezone, 'apiKey': apiKey, 'secretKey': secretKey}),
			_class)'''

	def updateVirtualMachine(self, id, displayName=None, group=None,
		haenable=None, ostypeId=None, userdata=None, _class=DataObject):
		'''updateVirtualMachine(id, displayName=None, group=None,
		haenable=None, ostypeId=None, userdata=None, _class=DataObject)'''
		return self.process('updatevirtualmachineresponse',
			self.__execute__('updateVirtualMachine',
			{'id': id, 'displayname': displayName, 'group': group,
			'haenable': haenable, 'ostypeid':ostypeId, 'userdata':userdata}),
			_class)

	'''
	def updateZone(self, id, name=None, dns1=None, dns2=None,
		internaldns1=None, internaldns2=None, guestCidrAddress=None, vnet=None,
		_class=DataObject):
		return self.process('updatezoneresponse',
			self.__execute__('updateZone',
			{'id': id, 'name': name, 'dns1': dns1, 'dns2': dns2,
			'internaldns1': internaldns1, 'internaldns2': internaldns2,
			'guestcidraddress': guestCidrAddress, 'vnet': vnet}),
			_class)'''

#14_09_11------------------------------------------------------------------------------
	def getVMPassword(self, id, _class=DataObject):
		''' getVMPassword(id) '''
		return self.process_async('getVMPassword',
			{'id': id},
			_class)
		
	def authorizeSecurityGroupIngress(self, account=None, cidrList=None, domainId=None,
		endPort=None, icmpCode=None, icmpType=None, protocol=None, securityGroupId=None,
		securityGroupName=None, startPort=None, userSecurityGroupList=None,
		_class=DataObject):
		'''authorizeSecurityGroupIngress(account=None, cidrList=None, domainId=None,
		endPort=None, icmpcode=None, icmptype=None, protocol=None, securitygroupid=None,
		securitygroupname=None, startport=None, usersecuritygrouplist=None) '''
		return self.process_async('authorizeSecurityGroupIngress',
			{'account': account, 'cidrlist':cidrList, 'domainid':domainId,
			'endport':endPort, 'icmpcode':icmpCode, 'icmptype':icmpType,
			'protocol':protocol, 'securitygroupid':securityGroupId,
			'securitygroupname':securityGroupName, 'startport':startPort,
			'usersecuritygrouplist':userSecurityGroupList},
			_class)
		
	def revokeSecurityGroupIngress(self, id, _class=DataObject):
		''' revokeSecurityGroupIngress(id)'''
		return self.process_async('revokeSecurityGroupIngress',
			{'id': id},
			_class)

	def registerSSHKeyPair(self, name, publicKey, account=None, domain=None,
		_class=DataObject):
		return self.process('registersshkeypairresponse',
			self.__execute__('registerSSHKeyPair',
			{'name':name, 'publickey':publicKey, 'account':account, 'domain':domain}),
			_class)
		
	def updateLoadBalancerRule(self, id, algorithm=None, description=None, name=None,
		_class=DataObject):
		return self.process_async('updateLoadBalancerRule',
			{'id': id, 'algorithm':algorithm, 'description':description, 'name':name},
			_class)
	
	def listHypervisors(self, zoneId=None, _class=DataObject):
		return self.process('listhypervisorsresponse',
			self.__execute__('listHypervisors',
			{'zoneid':zoneId}),
			_class)

	def extractTemplate(self, id, mode, zoneId, url=None, _class=DataObject):
		return self.process_async('extractTemplate',
			{'id': id, 'mode':mode, 'zoneid':zoneId, 'url':url},
			_class)

	
	def updateIsoPermissions(self, id, accounts=None, isExtractable=None,
		isFeatured=None, isPublic=None, op=None, _class=DataObject):
		return self.process('updateisopermissionsresponse',
			self.__execute__('updateIsoPermissions',
			{'id':id, 'accounts':accounts, 'isextractable':isExtractable,
			'isfeatured':isFeatured, 'ispublic':isPublic, 'op':op}),
			_class)
		
	def listIsoPermissions(self, id, account=None, domainId=None, _class=DataObject):
		return self.process('listIsoPermissionsresponse',
			self.__execute__('listIsoPermissions',
			{'id':id, 'accounts':account, 'domainid':domainId}),
			_class)
		
	def extractIso(self, id, mode, zoneId, url=None,  _class=DataObject):
		return self.process_async('extractIso',
			{'id': id, 'mode':mode, 'zoneid':zoneId, 'url':url},
			_class)

	def createFirewallRule(self, ipaddressId, protocol, cidrList=None, endPort=None,
		icmpCode=None, icmpType=None, startPort=None, _class=DataObject):
		return self.process_async('createFirewallRule',
			{'ipaddressid': ipaddressId, 'protocol':protocol, 'cidrList':cidrList,
			'endport':endPort, 'icmpcode':icmpCode, 'icmptype':icmpType, 
			'startport':startPort},
			_class)
	
	def deleteFirewallRule(self, id, _class=DataObject):
		return self.process_async('deleteFirewallRule',
			{'id':id},
			_class)
	
	def listFirewallRules(self, account=None, domainId=None, id=None, ipaddressId=None, 
		_class=DataObject):
		return self.process('listfirewallrulesresponse',
			self.__execute__('listFirewallRules',
			{'account':account, 'domainid':domainId, 'id':id, 'ipaddressid':ipaddressId}),
			_class)

#InstanceGroup
	def createInstanceGroup(self, name, account=None, domainId=None, _class=DataObject):
		return self.process('createinstancegroupresponse',
			self.__execute__('createInstanceGroup',
			{'name':name, 'account':account, 'domainid':domainId}),
			_class)
		
	def deleteInstanceGroup(self, id, _class=DataObject):
		return self.process('deleteinstancegroupresponse',
			self.__execute__('deleteInstanceGroup',
			{'id':id}),
			_class)
		
	def updateInstanceGroup(self, id, name=None, _class=DataObject):
		return self.process('updateinstancegroupresponse',
			self.__execute__('updateInstanceGroup',
			{'id':id, 'name':name}),
			_class)
		
	def listInstanceGroups(self, account=None, domainId=None, id=None, keyword=None,
		name=None, page=None, pagesize=None, _class=DataObject):
		return self.process('listinstancegroupsresponse',
			self.__execute__('listInstanceGroups',
			{'account':account, 'domainid':domainId, 'id':id, 'keyword':keyword,
			'name':name, 'page':page, 'pagesize':pagesize}),
			_class)
		
	def listNetworkOfferings(self, availability=None, displayText=None, guestIpType=None,
		id=None, isDefault=None, isShared=None, keyword=None, name=None, page=None,
		pagesize=None, specifyvlan=None, traffictype=None, zoneId=None,
		_class=DataObject):
		return self.process('listnetworkofferingsresponse',
			self.__execute__('listNetworkOfferings',
			{'availability':availability, 'displaytext':displayText,
			'guestiptype':guestIpType, 'id':id, 'isdefault':isDefault,
			'isshared':isShared, 'keyword':keyword, 'name':name, 'page':page,
			'pagesize':pagesize, 'specifyvlan':specifyvlan, 'traffictype':traffictype,
			'zoneid':zoneId}),
			_class)
		
	def extractVolume(self, id, mode, zoneId, url=None, _class=DataObject):
		return self.process_async('extractVolume',
			{'id':id, 'mode':mode, 'zoneid':zoneId, 'url':url},
			_class)
#VPN
	def createRemoteAccessVpn(self, publicIpId, account=None, domainId=None, ipRange=None,
		openFirewall=None, _class=DataObject):
		return self.process_async('createRemoteAccessVpn',
			{'publicipid':publicIpId, 'account':account, 'domainid':domainId,
			'iprange':ipRange, 'openfirewall':openFirewall},
			_class)
		
	def deleteRemoteAccessVpn(self, publicIpId, _class=DataObject):
		return self.process_async('deleteRemoteAccessVpn',
			{'publicipid':publicIpId},
			_class)
		
	def listRemoteAccessVpns(self, publicIpId, account=None, domainId=None, keyword=None,
		page=None, pagesize=None, _class=DataObject):
		return self.process('listremoteaccessvpnsresponse',
			self.__execute__('listRemoteAccessVpns',
			{'publicipid':publicIpId, 'account':account, 'domainid':domainId,
			'keyword':keyword, 'page':page, 'pagesize':pagesize}),
			_class)

	def addVpnUser(self, password, username, account=None, domainId=None,
		_class=DataObject):
		return self.process_async('addVpnUser',
			{'password':password, 'username':username, 'account':account,
			'domainid':domainId},
			_class)
		
	def removeVpnUser(self, username, account=None, domainId=None, _class=DataObject):
		return self.process_async('removeVpnUser',
			{'username':username, 'account':account, 'domainid':domainId},
			_class)
		
	def listVpnUsers(self, account=None, domainId=None, id=None, keyword=None, page=None,
		pagesize=None, username=None, _class=DataObject):
		return self.process('listvpnusersresponse',
			self.__execute__('listVpnUsers',
			{'account':account, 'domainid':domainId, 'id':id, 'keyword':keyword,
			'page':page, 'pagesize':pagesize, 'username':username}),
			_class)
#NAT
	def enableStaticNat(self, ipaddressId, virtualmachineId, _class=DataObject):
		return self.process_async('enableStaticNat',
			{'ipaddressid':ipaddressId, 'virtualmachineid':virtualmachineId},
			_class)

	def createIpForwardingRule(self, ipaddressId, protocol, startPort, cidrList=None, endPort=None,
		openFirewall=None, _class=DataObject):
		return self.process_async('createIpForwardingRule',
			{'ipaddressid':ipaddressId, 'protocol':protocol, 'startport':startPort,
			'cidrlist':cidrList, 'endport':endPort, 'openfirewall':openFirewall},
			_class)
		
	def deleteIpForwardingRule(self, id, _class=DataObject):
		return self.process_async('deleteIpForwardingRule',
			{'id':id},
			_class)
		
	def listIpForwardingRules(self, account, domainId=None, id=None, ipaddressId=None,
		keyword=None, page=None, pagesize=None, virtualmachineId=None, _class=DataObject):
		return self.process('listipforwardingrulesresponse',
			self.__execute__('listIpForwardingRules',
			{'account':account, 'domainid':domainId, 'id':id, 'ipaddressid':ipaddressId,
			'keyword':keyword, 'page':page, 'pagesize':pagesize,
			'virtualmachineid':virtualmachineId}),
			_class)
#Network
	def createNetwork(self, displayText, name, networkOfferingId, zoneId, account=None,
		domainId=None, endIp=None, gateWay=None, isDefault=None, isShared=None,
		netmask=None, networkDomain=None, startIp=None, tags=None, vlan=None,
		_class=DataObject):
		return self.process('createnetworkresponse',
			self.__execute__('createNetwork',
			{'displaytext':displayText, 'name':name,
			'networkofferingid':networkOfferingId, 'zoneid':zoneId, 'account':account,
			'domainid':domainId, 'endip':endIp, 'gateway':gateWay, 'isdefault':isDefault,
			'isshared':isShared, 'netmask':netmask, 'networkdomain':networkDomain,
			'startip':startIp, 'tags':tags, 'vlan':vlan}),
			_class)
		
	def deleteNetwork(self, id, _class=DataObject):
		return self.process_async('deleteNetwork',
			{'id':id},
			_class)
		
	def restartNetwork(self, _class=DataObject):
		return self.process('restartnetworkresponse',
			self.__execute__('restartNetwork',
			{'id':id}),
			_class)
		
	def updateNetwork(self, id, displayText=None, name=None, networkDomain=None,
		tags=None, _class=DataObject):
		return self.process_async('updateNetwork',
			{'id':id, 'displaytext':displayText, 'name':name,
			'networkdomain':networkDomain, 'tags':tags},
			_class)

	def listCapabilities(self, _class=DataObject):
		return self.process('listcapabilitiesresponse',
			self.__execute__('listCapabilities',
			{}),
			_class)
#event	
	def listEventTypes(self, _class=DataObject):
		return self.process('listeventtypesresponse',
			self.__execute__('listEventTypes',
			{}),
			_class)