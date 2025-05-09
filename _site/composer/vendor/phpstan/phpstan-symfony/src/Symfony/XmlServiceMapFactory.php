<?php declare(strict_types = 1);

namespace PHPStan\Symfony;

use SimpleXMLElement;
use function file_get_contents;
use function simplexml_load_string;
use function sprintf;
use function strpos;
use function substr;

final class XmlServiceMapFactory implements ServiceMapFactory
{

	/** @var string|null */
	private $containerXml;

	public function __construct(Configuration $configuration)
	{
		$this->containerXml = $configuration->getContainerXmlPath();
	}

	public function create(): ServiceMap
	{
		if ($this->containerXml === null) {
			return new FakeServiceMap();
		}

		$fileContents = file_get_contents($this->containerXml);
		if ($fileContents === false) {
			throw new XmlContainerNotExistsException(sprintf('Container %s does not exist', $this->containerXml));
		}

		$xml = @simplexml_load_string($fileContents);
		if ($xml === false) {
			throw new XmlContainerNotExistsException(sprintf('Container %s cannot be parsed', $this->containerXml));
		}

		/** @var Service[] $services */
		$services = [];
		/** @var Service[] $aliases */
		$aliases = [];
		foreach ($xml->services->service as $def) {
			/** @var SimpleXMLElement $attrs */
			$attrs = $def->attributes();
			if (!isset($attrs->id)) {
				continue;
			}

			$serviceTags = [];
			foreach ($def->tag as $tag) {
				$tagAttrs = ((array) $tag->attributes())['@attributes'] ?? [];
				$tagName = $tagAttrs['name'];
				unset($tagAttrs['name']);

				$serviceTags[] = new ServiceTag($tagName, $tagAttrs);
			}

			$service = new Service(
				$this->cleanServiceId((string) $attrs->id),
				isset($attrs->class) ? (string) $attrs->class : null,
				isset($attrs->public) && (string) $attrs->public === 'true',
				isset($attrs->synthetic) && (string) $attrs->synthetic === 'true',
				isset($attrs->alias) ? $this->cleanServiceId((string) $attrs->alias) : null,
				$serviceTags
			);

			if ($service->getAlias() !== null) {
				$aliases[] = $service;
			} else {
				$services[$service->getId()] = $service;
			}
		}
		foreach ($aliases as $service) {
			$alias = $service->getAlias();
			if ($alias !== null && !isset($services[$alias])) {
				continue;
			}
			$id = $service->getId();
			$services[$id] = new Service(
				$id,
				$services[$alias]->getClass(),
				$service->isPublic(),
				$service->isSynthetic(),
				$alias
			);
		}

		return new DefaultServiceMap($services);
	}

	private function cleanServiceId(string $id): string
	{
		return strpos($id, '.') === 0 ? substr($id, 1) : $id;
	}

}
