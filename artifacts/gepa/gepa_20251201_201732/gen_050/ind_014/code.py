
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (MIDI 38) with chromatic approach to G2 (MIDI 43)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25),  # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),  # D2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # C5
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.75),  # C5
    pretty_midi.Note(velocity=110, pitch=71, start=1.75, end=2.0),  # D5
    pretty_midi.Note(velocity=110, pitch=72, start=2.0, end=2.25),  # Eb5
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.5),  # D5
    pretty_midi.Note(velocity=110, pitch=69, start=2.5, end=2.75),  # C5
    pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=3.0),  # B4
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: G2 (MIDI 43) with chromatic approach to B2 (MIDI 46)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=80, pitch=44, start=3.375, end=3.75),  # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=46, start=3.75, end=4.125),  # B2
    pretty_midi.Note(velocity=80, pitch=43, start=4.125, end=4.5),  # G2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: A7 (A C# E G)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5),  # A4
    pretty_midi.Note(velocity=100, pitch=78, start=3.0, end=4.5),  # C#5
    pretty_midi.Note(velocity=100, pitch=82, start=3.0, end=4.5),  # E5
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=4.5),  # D5 (tension)
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue the motif, resolve it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25),  # B4
    pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.5),  # C5
    pretty_midi.Note(velocity=110, pitch=71, start=3.5, end=3.75),  # D5
    pretty_midi.Note(velocity=110, pitch=72, start=3.75, end=4.0),  # Eb5
    pretty_midi.Note(velocity=110, pitch=71, start=4.0, end=4.25),  # D5
    pretty_midi.Note(velocity=110, pitch=69, start=4.25, end=4.5),  # C5
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: B2 (MIDI 46) with chromatic approach to D3 (MIDI 49)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=46, start=4.5, end=4.875),  # B2
    pretty_midi.Note(velocity=80, pitch=47, start=4.875, end=5.25),  # C3 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=49, start=5.25, end=5.625),  # D3
    pretty_midi.Note(velocity=80, pitch=46, start=5.625, end=6.0),  # B2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: D7 (D F# A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # C5
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Final resolution of the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.75),  # C5
    pretty_midi.Note(velocity=110, pitch=71, start=4.75, end=5.0),  # D5
    pretty_midi.Note(velocity=110, pitch=72, start=5.0, end=5.25),  # Eb5
    pretty_midi.Note(velocity=110, pitch=71, start=5.25, end=5.5),  # D5
    pretty_midi.Note(velocity=110, pitch=69, start=5.5, end=5.75),  # C5
    pretty_midi.Note(velocity=110, pitch=67, start=5.75, end=6.0),  # B4
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
