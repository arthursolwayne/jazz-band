# Reference Jazz Riffs

5 classic jazz riffs extracted and adapted to our 5-part jazz band setup: **Bass, Snare, Hi-Hat, Piano, Sax**.

## Tracks

| File | Song | Key | BPM |
|------|------|-----|-----|
| `cantina_jazzband.mid` | Cantina Band | Dm | 270 |
| `moanin_jazzband.mid` | Moanin' | Fm | 150 |
| `watermelon_jazzband.mid` | Watermelon Man | F | 200 |
| `sowhat_jazzband.mid` | So What | D dorian | 236 |
| `songformyfather_jazzband.mid` | Song for My Father | Fm | 120 |

## Methodology

### 1. Source MIDI
- Downloaded MIDIs from BitMidi, FreeMIDI, or used existing files
- For some tracks, used Spotify's basic-pitch to transcribe from MP3

### 2. Extract 4 Bars
- Identified the iconic riff section (usually first 4-8 bars)
- Trimmed in GarageBand or via pretty_midi
- For GarageBand edits: exported to Loop Library, then extracted embedded MIDI from the .aif files

### 3. Adapt to 5-Part Setup
- **Bass**: low notes, transposed if needed
- **Snare**: drum hits mapped to pitch 38
- **Hi-Hat**: cymbals/hats mapped to pitch 42
- **Piano**: chord voicings, comping
- **Sax**: melody line, sometimes merged with trumpet/horn parts

### 4. Add Expression
- Velocity variation (accent downbeats, soften offbeats)
- Articulation (bass gapped 85%, varied note lengths)
- Ghost notes on snare
- Pitch bend vibrato on sax for longer notes
- Sustain pedal on piano

### 5. Balance & Polish
- Pan positions (bass center, drums L/R, piano right, sax center)
- Volume balancing (melody prominent, rhythm section supportive)
- Chord alignment (snapped notes within 100ms threshold)
- Extended final notes to fill bar length

## Tools Used
- **pretty_midi**: MIDI manipulation in Python
- **basic-pitch**: Audio-to-MIDI transcription
- **GarageBand**: Trimming, auditioning
- **Apple Loop Library**: Intermediate export for GarageBand edits
