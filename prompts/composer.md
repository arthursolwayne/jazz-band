# Jazz Band Composer Agent

TODO: Rewrite for pretty_midi Python code output.

The LLM should generate executable Python code that:
1. Creates a `pretty_midi.PrettyMIDI` object
2. Adds instruments (sax, piano, bass, drums)
3. Adds notes with pitch, velocity, start time, end time
4. Returns the PrettyMIDI object

## Instrument Mapping

| Instrument | MIDI Program | Drum Pitch |
|------------|-------------|------------|
| sax | 66 (Tenor Sax) | — |
| piano | 0 (Acoustic Grand) | — |
| bass | 33 (Electric Bass) | — |
| drums | is_drum=True | snare=38, hihat=42, kick=36 |

## Time Reference

At tempo BPM:
- Bar = (60/tempo) * 4 seconds
- Quarter note = 60/tempo seconds
- Eighth note = 30/tempo seconds
