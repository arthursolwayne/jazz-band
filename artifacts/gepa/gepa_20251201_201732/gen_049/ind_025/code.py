
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line with chromatic approaches
# D2-G2 (MIDI 38-43)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=39, start=1.875, end=2.25),  # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),  # F#2 (chromatic approach)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=54, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=1.875),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # C#
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif - one short phrase, make it sing
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # E4
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0),  # G4
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.25),  # E4
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.5),  # B4
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line with chromatic approaches
# D2-G2 (MIDI 38-43)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),  # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=4.125),  # D2
    pretty_midi.Note(velocity=90, pitch=39, start=4.125, end=4.5),  # Eb2 (chromatic approach)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bm7b5 (B D F# A)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # F#
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # A
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif continuation
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=110, pitch=62, start=3.25, end=3.5),  # E4
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.75),  # B4
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.0),  # G4
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line with chromatic approaches
# D2-G2 (MIDI 38-43)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875),  # G2
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),  # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=5.25, end=5.625),  # D2
    pretty_midi.Note(velocity=90, pitch=39, start=5.625, end=6.0),  # Eb2 (chromatic approach)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: G7 (G B D F#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # F#
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif resolution
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # E4
    pretty_midi.Note(velocity=110, pitch=65, start=4.75, end=5.0),  # G4
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25),  # E4
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.5),  # B4
    pretty_midi.Note(velocity=110, pitch=65, start=5.5, end=5.75),  # G4
    pretty_midi.Note(velocity=110, pitch=62, start=5.75, end=6.0),  # E4
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=80, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=80, pitch=42, start=7.125, end=7.5),
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
