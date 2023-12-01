"""
from dns.question.name it parses:
- dns.question.top_level_domain
- dns.question.subdomain
- dns.question.registered_domain
by using publicsuffixlist from Mozilla
"""

import traceback
import syslogng
from publicsuffixlist import PublicSuffixList

with open("/usr/share/publicsuffix/public_suffix_list.dat", "rb") as f:
    psl = PublicSuffixList(f)

class DNSSuffixResolver(syslogng.LogParser):
    def init(self, options):
        self.domain = options["domain"]
        self.tld = options["tld"]
        self.subdomain = options["subdomain"]
        self.regdomain = options["regdomain"]
        return True
    def parse(self, log_message):
        dom = str(log_message[self.domain].decode('utf-8'))
        dom = dom.rstrip('.')
        try:
            if log_message['dns.question.type'].decode('utf-8') in ["A", "AAAA"]:

                # Return longest publically shared suffix => top_level_domain
                log_message[self.tld] = psl.publicsuffix(dom, accept_unknown=True)
                # Return shortest suffix assigned for an individual. => registered_domain
                log_message[self.regdomain] = str(psl.privatesuffix(dom, accept_unknown=True))
                # Return tuple of labels and the private suffix. => subdomain
                priv = psl.privateparts(dom)
                if priv is not None:
                    # most notorious is .amazonaws.com
                    # https://github.com/google/guava/issues/1829
                    concat=''
                    for key in priv[ : -1 ]:
                        concat += key + "."
                    # Omit trailing dot.
                    log_message[self.subdomain] = str(concat.rstrip('.'))
                else:
                    log_message[self.subdomain] = ''
            else:
                pass
        except Exception:
            traceback.print_tb
            raise
#            pass

        # return True, other way message is dropped
        return True

