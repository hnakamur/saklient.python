# -*- coding:utf-8 -*-

from .httpexception import HttpException
from .httpbadgatewayexception import HttpBadGatewayException
from .httpbadrequestexception import HttpBadRequestException
from .httpconflictexception import HttpConflictException
from .httpexpectationfailedexception import HttpExpectationFailedException
from .httpfaileddependencyexception import HttpFailedDependencyException
from .httpforbiddenexception import HttpForbiddenException
from .httpgatewaytimeoutexception import HttpGatewayTimeoutException
from .httpgoneexception import HttpGoneException
from .httphttpversionnotsupportedexception import HttpHttpVersionNotSupportedException
from .httpinsufficientstorageexception import HttpInsufficientStorageException
from .httpinternalservererrorexception import HttpInternalServerErrorException
from .httplengthrequiredexception import HttpLengthRequiredException
from .httplockedexception import HttpLockedException
from .httpmethodnotallowedexception import HttpMethodNotAllowedException
from .httpnotacceptableexception import HttpNotAcceptableException
from .httpnotextendedexception import HttpNotExtendedException
from .httpnotfoundexception import HttpNotFoundException
from .httpnotimplementedexception import HttpNotImplementedException
from .httppaymentrequiredexception import HttpPaymentRequiredException
from .httppreconditionfailedexception import HttpPreconditionFailedException
from .httpproxyauthenticationrequiredexception import HttpProxyAuthenticationRequiredException
from .httprequestentitytoolargeexception import HttpRequestEntityTooLargeException
from .httprequesttimeoutexception import HttpRequestTimeoutException
from .httprequesturitoolongexception import HttpRequestUriTooLongException
from .httprequestedrangenotsatisfiableexception import HttpRequestedRangeNotSatisfiableException
from .httpserviceunavailableexception import HttpServiceUnavailableException
from .httpunauthorizedexception import HttpUnauthorizedException
from .httpunprocessableentityexception import HttpUnprocessableEntityException
from .httpunsupportedmediatypeexception import HttpUnsupportedMediaTypeException
from .httpupgraderequiredexception import HttpUpgradeRequiredException
from .httpvariantalsonegotiatesexception import HttpVariantAlsoNegotiatesException
from ..cloud.errors.accessapikeydisabledexception import AccessApiKeyDisabledException
from ..cloud.errors.accesssakuraexception import AccessSakuraException
from ..cloud.errors.accessstaffexception import AccessStaffException
from ..cloud.errors.accesstokenexception import AccessTokenException
from ..cloud.errors.accessxhrorapikeyexception import AccessXhrOrApiKeyException
from ..cloud.errors.accountnotfoundexception import AccountNotFoundException
from ..cloud.errors.accountnotspecifiedexception import AccountNotSpecifiedException
from ..cloud.errors.ambiguousidentifierexception import AmbiguousIdentifierException
from ..cloud.errors.ambiguouszoneexception import AmbiguousZoneException
from ..cloud.errors.apiproxytimeoutexception import ApiProxyTimeoutException
from ..cloud.errors.apiproxytimeoutnongetexception import ApiProxyTimeoutNonGetException
from ..cloud.errors.archiveisincompleteexception import ArchiveIsIncompleteException
from ..cloud.errors.bootfailurebylockexception import BootFailureByLockException
from ..cloud.errors.bootfailureingroupexception import BootFailureInGroupException
from ..cloud.errors.busyexception import BusyException
from ..cloud.errors.cantresizesmallerexception import CantResizeSmallerException
from ..cloud.errors.cdromdevicelockedexception import CdromDeviceLockedException
from ..cloud.errors.cdromdisabledexception import CdromDisabledException
from ..cloud.errors.cdrominuseexception import CdromInUseException
from ..cloud.errors.cdromisincompleteexception import CdromIsIncompleteException
from ..cloud.errors.connecttosameswitchexception import ConnectToSameSwitchException
from ..cloud.errors.contractcreationexception import ContractCreationException
from ..cloud.errors.copytoitselfexception import CopyToItselfException
from ..cloud.errors.deletediskb4templateexception import DeleteDiskB4TemplateException
from ..cloud.errors.deleteipv6netsfirstexception import DeleteIpV6NetsFirstException
from ..cloud.errors.deleteresb4accountexception import DeleteResB4AccountException
from ..cloud.errors.deleterouterb4switchexception import DeleteRouterB4SwitchException
from ..cloud.errors.deletestaticroutefirstexception import DeleteStaticRouteFirstException
from ..cloud.errors.disabledinsandboxexception import DisabledInSandboxException
from ..cloud.errors.disconnectb4deleteexception import DisconnectB4DeleteException
from ..cloud.errors.disconnectb4updateexception import DisconnectB4UpdateException
from ..cloud.errors.diskconnectionlimitexception import DiskConnectionLimitException
from ..cloud.errors.diskiscopyingexception import DiskIsCopyingException
from ..cloud.errors.diskisnotavailableexception import DiskIsNotAvailableException
from ..cloud.errors.disklicensemismatchexception import DiskLicenseMismatchException
from ..cloud.errors.diskorssinmigrationexception import DiskOrSsInMigrationException
from ..cloud.errors.diskstockrunoutexception import DiskStockRunOutException
from ..cloud.errors.dnsarecordnotfoundexception import DnsARecordNotFoundException
from ..cloud.errors.dnsaaaarecordnotfoundexception import DnsAaaaRecordNotFoundException
from ..cloud.errors.dnsptrupdatefailureexception import DnsPtrUpdateFailureException
from ..cloud.errors.dontcreateinsandboxexception import DontCreateInSandboxException
from ..cloud.errors.duplicateaccountcodeexception import DuplicateAccountCodeException
from ..cloud.errors.duplicateentryexception import DuplicateEntryException
from ..cloud.errors.duplicateusercodeexception import DuplicateUserCodeException
from ..cloud.errors.filenotuploadedexception import FileNotUploadedException
from ..cloud.errors.filterarraycomparisonexception import FilterArrayComparisonException
from ..cloud.errors.filterbadoperatorexception import FilterBadOperatorException
from ..cloud.errors.filternullcomparisonexception import FilterNullComparisonException
from ..cloud.errors.filterunknownoperatorexception import FilterUnknownOperatorException
from ..cloud.errors.ftpcannotcloseexception import FtpCannotCloseException
from ..cloud.errors.ftpisalreadycloseexception import FtpIsAlreadyCloseException
from ..cloud.errors.ftpisalreadyopenexception import FtpIsAlreadyOpenException
from ..cloud.errors.ftpmustbeclosedexception import FtpMustBeClosedException
from ..cloud.errors.hostoperationfailureexception import HostOperationFailureException
from ..cloud.errors.illegaldasusageexception import IllegalDasUsageException
from ..cloud.errors.inmigrationexception import InMigrationException
from ..cloud.errors.invalidformatexception import InvalidFormatException
from ..cloud.errors.invalidparamcombexception import InvalidParamCombException
from ..cloud.errors.invalidrangeexception import InvalidRangeException
from ..cloud.errors.invaliduriargumentexception import InvalidUriArgumentException
from ..cloud.errors.ipv6netalreadyattachedexception import IpV6NetAlreadyAttachedException
from ..cloud.errors.limitcountinaccountexception import LimitCountInAccountException
from ..cloud.errors.limitcountinmemberexception import LimitCountInMemberException
from ..cloud.errors.limitcountinnetworkexception import LimitCountInNetworkException
from ..cloud.errors.limitcountinrouterexception import LimitCountInRouterException
from ..cloud.errors.limitcountinzoneexception import LimitCountInZoneException
from ..cloud.errors.limitmemoryinaccountexception import LimitMemoryInAccountException
from ..cloud.errors.limitsizeinaccountexception import LimitSizeInAccountException
from ..cloud.errors.missingisoimageexception import MissingIsoImageException
from ..cloud.errors.missingparamexception import MissingParamException
from ..cloud.errors.mustbeofsamezoneexception import MustBeOfSameZoneException
from ..cloud.errors.nodisplayresponseexception import NoDisplayResponseException
from ..cloud.errors.notforrouterexception import NotForRouterException
from ..cloud.errors.notreplicatingexception import NotReplicatingException
from ..cloud.errors.notwithhybridconnexception import NotWithHybridconnException
from ..cloud.errors.oldstorageplanexception import OldStoragePlanException
from ..cloud.errors.operationfailureexception import OperationFailureException
from ..cloud.errors.operationtimeoutexception import OperationTimeoutException
from ..cloud.errors.originalhashmismatchexception import OriginalHashMismatchException
from ..cloud.errors.packetfilterapplyingexception import PacketFilterApplyingException
from ..cloud.errors.packetfilterversionmismatchexception import PacketFilterVersionMismatchException
from ..cloud.errors.paramipnotfoundexception import ParamIpNotFoundException
from ..cloud.errors.paramresnotfoundexception import ParamResNotFoundException
from ..cloud.errors.paymentcreditcardexception import PaymentCreditCardException
from ..cloud.errors.paymentpaymentexception import PaymentPaymentException
from ..cloud.errors.paymentregistrationexception import PaymentRegistrationException
from ..cloud.errors.paymenttelcertificationexception import PaymentTelCertificationException
from ..cloud.errors.paymentunpayableexception import PaymentUnpayableException
from ..cloud.errors.penaltyoperationexception import PenaltyOperationException
from ..cloud.errors.replicaalreadyexistsexception import ReplicaAlreadyExistsException
from ..cloud.errors.replicanotfoundexception import ReplicaNotFoundException
from ..cloud.errors.resalreadyconnectedexception import ResAlreadyConnectedException
from ..cloud.errors.resalreadydisconnectedexception import ResAlreadyDisconnectedException
from ..cloud.errors.resalreadyexistsexception import ResAlreadyExistsException
from ..cloud.errors.resusedinzoneexception import ResUsedInZoneException
from ..cloud.errors.resourcepathnotfoundexception import ResourcePathNotFoundException
from ..cloud.errors.runoutofipaddressexception import RunOutOfIpAddressException
from ..cloud.errors.samelicenserequiredexception import SameLicenseRequiredException
from ..cloud.errors.servercouldnotstopexception import ServerCouldNotStopException
from ..cloud.errors.serveriscleaningexception import ServerIsCleaningException
from ..cloud.errors.serveroperationfailureexception import ServerOperationFailureException
from ..cloud.errors.serverpowermustbedownexception import ServerPowerMustBeDownException
from ..cloud.errors.serverpowermustbeupexception import ServerPowerMustBeUpException
from ..cloud.errors.servicetemporarilyunavailableexception import ServiceTemporarilyUnavailableException
from ..cloud.errors.sizemismatchexception import SizeMismatchException
from ..cloud.errors.snapshotinmigrationexception import SnapshotInMigrationException
from ..cloud.errors.stillcreatingexception import StillCreatingException
from ..cloud.errors.storageabnormalexception import StorageAbnormalException
from ..cloud.errors.storageoperationfailureexception import StorageOperationFailureException
from ..cloud.errors.switchhybridconnectedexception import SwitchHybridConnectedException
from ..cloud.errors.templateftpisopenexception import TemplateFtpIsOpenException
from ..cloud.errors.templateisincompleteexception import TemplateIsIncompleteException
from ..cloud.errors.toomanyrequestexception import TooManyRequestException
from ..cloud.errors.unknownexception import UnknownException
from ..cloud.errors.unknownostypeexception import UnknownOsTypeException
from ..cloud.errors.unsupportedresclassexception import UnsupportedResClassException
from ..cloud.errors.usernotspecifiedexception import UserNotSpecifiedException
from ..cloud.errors.vncproxyrequestfailureexception import VncProxyRequestFailureException
from ..util import Util
import saklient

# module saklient.errors.exceptionfactory

class ExceptionFactory:
    
    ## @static
    # @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    # @return {saklient.errors.httpexception.HttpException}
    @staticmethod
    def create(status, code=None, message=""):
        if code == "access_apikey_disabled":
            return AccessApiKeyDisabledException(status, code, message)
        elif code == "access_sakura":
            return AccessSakuraException(status, code, message)
        elif code == "access_staff":
            return AccessStaffException(status, code, message)
        elif code == "access_token":
            return AccessTokenException(status, code, message)
        elif code == "access_xhr_or_apikey":
            return AccessXhrOrApiKeyException(status, code, message)
        elif code == "account_not_found":
            return AccountNotFoundException(status, code, message)
        elif code == "account_not_specified":
            return AccountNotSpecifiedException(status, code, message)
        elif code == "ambiguous_identifier":
            return AmbiguousIdentifierException(status, code, message)
        elif code == "ambiguous_zone":
            return AmbiguousZoneException(status, code, message)
        elif code == "apiproxy_timeout":
            return ApiProxyTimeoutException(status, code, message)
        elif code == "apiproxy_timeout_non_get":
            return ApiProxyTimeoutNonGetException(status, code, message)
        elif code == "archive_is_incomplete":
            return ArchiveIsIncompleteException(status, code, message)
        elif code == "bad_gateway":
            return HttpBadGatewayException(status, code, message)
        elif code == "bad_request":
            return HttpBadRequestException(status, code, message)
        elif code == "boot_failure_by_lock":
            return BootFailureByLockException(status, code, message)
        elif code == "boot_failure_in_group":
            return BootFailureInGroupException(status, code, message)
        elif code == "busy":
            return BusyException(status, code, message)
        elif code == "cant_resize_smaller":
            return CantResizeSmallerException(status, code, message)
        elif code == "cdrom_device_locked":
            return CdromDeviceLockedException(status, code, message)
        elif code == "cdrom_disabled":
            return CdromDisabledException(status, code, message)
        elif code == "cdrom_in_use":
            return CdromInUseException(status, code, message)
        elif code == "cdrom_is_incomplete":
            return CdromIsIncompleteException(status, code, message)
        elif code == "conflict":
            return HttpConflictException(status, code, message)
        elif code == "connect_to_same_switch":
            return ConnectToSameSwitchException(status, code, message)
        elif code == "contract_creation":
            return ContractCreationException(status, code, message)
        elif code == "copy_to_itself":
            return CopyToItselfException(status, code, message)
        elif code == "delete_disk_b4_template":
            return DeleteDiskB4TemplateException(status, code, message)
        elif code == "delete_ipv6nets_first":
            return DeleteIpV6NetsFirstException(status, code, message)
        elif code == "delete_res_b4_account":
            return DeleteResB4AccountException(status, code, message)
        elif code == "delete_router_b4_switch":
            return DeleteRouterB4SwitchException(status, code, message)
        elif code == "delete_static_route_first":
            return DeleteStaticRouteFirstException(status, code, message)
        elif code == "disabled_in_sandbox":
            return DisabledInSandboxException(status, code, message)
        elif code == "disconnect_b4_delete":
            return DisconnectB4DeleteException(status, code, message)
        elif code == "disconnect_b4_update":
            return DisconnectB4UpdateException(status, code, message)
        elif code == "disk_connection_limit":
            return DiskConnectionLimitException(status, code, message)
        elif code == "disk_is_copying":
            return DiskIsCopyingException(status, code, message)
        elif code == "disk_is_not_available":
            return DiskIsNotAvailableException(status, code, message)
        elif code == "disk_license_mismatch":
            return DiskLicenseMismatchException(status, code, message)
        elif code == "disk_stock_run_out":
            return DiskStockRunOutException(status, code, message)
        elif code == "diskorss_in_migration":
            return DiskOrSsInMigrationException(status, code, message)
        elif code == "dns_a_record_not_found":
            return DnsARecordNotFoundException(status, code, message)
        elif code == "dns_aaaa_record_not_found":
            return DnsAaaaRecordNotFoundException(status, code, message)
        elif code == "dns_ptr_update_failure":
            return DnsPtrUpdateFailureException(status, code, message)
        elif code == "dont_create_in_sandbox":
            return DontCreateInSandboxException(status, code, message)
        elif code == "duplicate_account_code":
            return DuplicateAccountCodeException(status, code, message)
        elif code == "duplicate_entry":
            return DuplicateEntryException(status, code, message)
        elif code == "duplicate_user_code":
            return DuplicateUserCodeException(status, code, message)
        elif code == "expectation_failed":
            return HttpExpectationFailedException(status, code, message)
        elif code == "failed_dependency":
            return HttpFailedDependencyException(status, code, message)
        elif code == "file_not_uploaded":
            return FileNotUploadedException(status, code, message)
        elif code == "filter_array_comparison":
            return FilterArrayComparisonException(status, code, message)
        elif code == "filter_bad_operator":
            return FilterBadOperatorException(status, code, message)
        elif code == "filter_null_comparison":
            return FilterNullComparisonException(status, code, message)
        elif code == "filter_unknown_operator":
            return FilterUnknownOperatorException(status, code, message)
        elif code == "forbidden":
            return HttpForbiddenException(status, code, message)
        elif code == "ftp_cannot_close":
            return FtpCannotCloseException(status, code, message)
        elif code == "ftp_is_already_close":
            return FtpIsAlreadyCloseException(status, code, message)
        elif code == "ftp_is_already_open":
            return FtpIsAlreadyOpenException(status, code, message)
        elif code == "ftp_must_be_closed":
            return FtpMustBeClosedException(status, code, message)
        elif code == "gateway_timeout":
            return HttpGatewayTimeoutException(status, code, message)
        elif code == "gone":
            return HttpGoneException(status, code, message)
        elif code == "host_operation_failure":
            return HostOperationFailureException(status, code, message)
        elif code == "http_version_not_supported":
            return HttpHttpVersionNotSupportedException(status, code, message)
        elif code == "illegal_das_usage":
            return IllegalDasUsageException(status, code, message)
        elif code == "in_migration":
            return InMigrationException(status, code, message)
        elif code == "insufficient_storage":
            return HttpInsufficientStorageException(status, code, message)
        elif code == "internal_server_error":
            return HttpInternalServerErrorException(status, code, message)
        elif code == "invalid_format":
            return InvalidFormatException(status, code, message)
        elif code == "invalid_param_comb":
            return InvalidParamCombException(status, code, message)
        elif code == "invalid_range":
            return InvalidRangeException(status, code, message)
        elif code == "invalid_uri_argument":
            return InvalidUriArgumentException(status, code, message)
        elif code == "ipv6net_already_attached":
            return IpV6NetAlreadyAttachedException(status, code, message)
        elif code == "length_required":
            return HttpLengthRequiredException(status, code, message)
        elif code == "limit_count_in_account":
            return LimitCountInAccountException(status, code, message)
        elif code == "limit_count_in_member":
            return LimitCountInMemberException(status, code, message)
        elif code == "limit_count_in_network":
            return LimitCountInNetworkException(status, code, message)
        elif code == "limit_count_in_router":
            return LimitCountInRouterException(status, code, message)
        elif code == "limit_count_in_zone":
            return LimitCountInZoneException(status, code, message)
        elif code == "limit_memory_in_account":
            return LimitMemoryInAccountException(status, code, message)
        elif code == "limit_size_in_account":
            return LimitSizeInAccountException(status, code, message)
        elif code == "locked":
            return HttpLockedException(status, code, message)
        elif code == "method_not_allowed":
            return HttpMethodNotAllowedException(status, code, message)
        elif code == "missing_iso_image":
            return MissingIsoImageException(status, code, message)
        elif code == "missing_param":
            return MissingParamException(status, code, message)
        elif code == "must_be_of_same_zone":
            return MustBeOfSameZoneException(status, code, message)
        elif code == "no_display_response":
            return NoDisplayResponseException(status, code, message)
        elif code == "not_acceptable":
            return HttpNotAcceptableException(status, code, message)
        elif code == "not_extended":
            return HttpNotExtendedException(status, code, message)
        elif code == "not_for_router":
            return NotForRouterException(status, code, message)
        elif code == "not_found":
            return HttpNotFoundException(status, code, message)
        elif code == "not_implemented":
            return HttpNotImplementedException(status, code, message)
        elif code == "not_replicating":
            return NotReplicatingException(status, code, message)
        elif code == "not_with_hybridconn":
            return NotWithHybridconnException(status, code, message)
        elif code == "old_storage_plan":
            return OldStoragePlanException(status, code, message)
        elif code == "operation_failure":
            return OperationFailureException(status, code, message)
        elif code == "operation_timeout":
            return OperationTimeoutException(status, code, message)
        elif code == "original_hash_mismatch":
            return OriginalHashMismatchException(status, code, message)
        elif code == "packetfilter_applying":
            return PacketFilterApplyingException(status, code, message)
        elif code == "packetfilter_version_mismatch":
            return PacketFilterVersionMismatchException(status, code, message)
        elif code == "param_ip_not_found":
            return ParamIpNotFoundException(status, code, message)
        elif code == "param_res_not_found":
            return ParamResNotFoundException(status, code, message)
        elif code == "payment_creditcard":
            return PaymentCreditCardException(status, code, message)
        elif code == "payment_payment":
            return PaymentPaymentException(status, code, message)
        elif code == "payment_registration":
            return PaymentRegistrationException(status, code, message)
        elif code == "payment_required":
            return HttpPaymentRequiredException(status, code, message)
        elif code == "payment_telcertification":
            return PaymentTelCertificationException(status, code, message)
        elif code == "payment_unpayable":
            return PaymentUnpayableException(status, code, message)
        elif code == "penalty_operation":
            return PenaltyOperationException(status, code, message)
        elif code == "precondition_failed":
            return HttpPreconditionFailedException(status, code, message)
        elif code == "proxy_authentication_required":
            return HttpProxyAuthenticationRequiredException(status, code, message)
        elif code == "replica_already_exists":
            return ReplicaAlreadyExistsException(status, code, message)
        elif code == "replica_not_found":
            return ReplicaNotFoundException(status, code, message)
        elif code == "request_entity_too_large":
            return HttpRequestEntityTooLargeException(status, code, message)
        elif code == "request_timeout":
            return HttpRequestTimeoutException(status, code, message)
        elif code == "request_uri_too_long":
            return HttpRequestUriTooLongException(status, code, message)
        elif code == "requested_range_not_satisfiable":
            return HttpRequestedRangeNotSatisfiableException(status, code, message)
        elif code == "res_already_connected":
            return ResAlreadyConnectedException(status, code, message)
        elif code == "res_already_disconnected":
            return ResAlreadyDisconnectedException(status, code, message)
        elif code == "res_already_exists":
            return ResAlreadyExistsException(status, code, message)
        elif code == "res_used_in_zone":
            return ResUsedInZoneException(status, code, message)
        elif code == "resource_path_not_found":
            return ResourcePathNotFoundException(status, code, message)
        elif code == "run_out_of_ipaddress":
            return RunOutOfIpAddressException(status, code, message)
        elif code == "same_license_required":
            return SameLicenseRequiredException(status, code, message)
        elif code == "server_could_not_stop":
            return ServerCouldNotStopException(status, code, message)
        elif code == "server_is_cleaning":
            return ServerIsCleaningException(status, code, message)
        elif code == "server_operation_failure":
            return ServerOperationFailureException(status, code, message)
        elif code == "server_power_must_be_down":
            return ServerPowerMustBeDownException(status, code, message)
        elif code == "server_power_must_be_up":
            return ServerPowerMustBeUpException(status, code, message)
        elif code == "service_temporarily_unavailable":
            return ServiceTemporarilyUnavailableException(status, code, message)
        elif code == "service_unavailable":
            return HttpServiceUnavailableException(status, code, message)
        elif code == "size_mismatch":
            return SizeMismatchException(status, code, message)
        elif code == "snapshot_in_migration":
            return SnapshotInMigrationException(status, code, message)
        elif code == "still_creating":
            return StillCreatingException(status, code, message)
        elif code == "storage_abnormal":
            return StorageAbnormalException(status, code, message)
        elif code == "storage_operation_failure":
            return StorageOperationFailureException(status, code, message)
        elif code == "switch_hybrid_connected":
            return SwitchHybridConnectedException(status, code, message)
        elif code == "template_ftp_is_open":
            return TemplateFtpIsOpenException(status, code, message)
        elif code == "template_is_incomplete":
            return TemplateIsIncompleteException(status, code, message)
        elif code == "too_many_request":
            return TooManyRequestException(status, code, message)
        elif code == "unauthorized":
            return HttpUnauthorizedException(status, code, message)
        elif code == "unknown":
            return UnknownException(status, code, message)
        elif code == "unknown_os_type":
            return UnknownOsTypeException(status, code, message)
        elif code == "unprocessable_entity":
            return HttpUnprocessableEntityException(status, code, message)
        elif code == "unsupported_media_type":
            return HttpUnsupportedMediaTypeException(status, code, message)
        elif code == "unsupported_res_class":
            return UnsupportedResClassException(status, code, message)
        elif code == "upgrade_required":
            return HttpUpgradeRequiredException(status, code, message)
        elif code == "user_not_specified":
            return UserNotSpecifiedException(status, code, message)
        elif code == "variant_also_negotiates":
            return HttpVariantAlsoNegotiatesException(status, code, message)
        elif code == "vnc_proxy_request_failure":
            return VncProxyRequestFailureException(status, code, message)
        if status == 400:
            return HttpBadRequestException(status, code, message)
        elif status == 401:
            return HttpUnauthorizedException(status, code, message)
        elif status == 402:
            return HttpPaymentRequiredException(status, code, message)
        elif status == 403:
            return HttpForbiddenException(status, code, message)
        elif status == 404:
            return HttpNotFoundException(status, code, message)
        elif status == 405:
            return HttpMethodNotAllowedException(status, code, message)
        elif status == 406:
            return HttpNotAcceptableException(status, code, message)
        elif status == 407:
            return HttpProxyAuthenticationRequiredException(status, code, message)
        elif status == 408:
            return HttpRequestTimeoutException(status, code, message)
        elif status == 409:
            return HttpConflictException(status, code, message)
        elif status == 410:
            return HttpGoneException(status, code, message)
        elif status == 411:
            return HttpLengthRequiredException(status, code, message)
        elif status == 412:
            return HttpPreconditionFailedException(status, code, message)
        elif status == 413:
            return HttpRequestEntityTooLargeException(status, code, message)
        elif status == 415:
            return HttpUnsupportedMediaTypeException(status, code, message)
        elif status == 416:
            return HttpRequestedRangeNotSatisfiableException(status, code, message)
        elif status == 417:
            return HttpExpectationFailedException(status, code, message)
        elif status == 422:
            return HttpUnprocessableEntityException(status, code, message)
        elif status == 423:
            return HttpLockedException(status, code, message)
        elif status == 424:
            return HttpFailedDependencyException(status, code, message)
        elif status == 426:
            return HttpUpgradeRequiredException(status, code, message)
        elif status == 500:
            return HttpRequestUriTooLongException(status, code, message)
        elif status == 501:
            return HttpNotImplementedException(status, code, message)
        elif status == 502:
            return HttpBadGatewayException(status, code, message)
        elif status == 503:
            return HttpServiceUnavailableException(status, code, message)
        elif status == 504:
            return HttpGatewayTimeoutException(status, code, message)
        elif status == 505:
            return HttpHttpVersionNotSupportedException(status, code, message)
        elif status == 506:
            return HttpVariantAlsoNegotiatesException(status, code, message)
        elif status == 507:
            return HttpInsufficientStorageException(status, code, message)
        elif status == 510:
            return HttpNotExtendedException(status, code, message)
        return HttpException(status, code, message)
    
