
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
    pretty_midi.Note(velocity=90, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=38, start=1.125, end=1.5),
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=1.5),
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=80, pitch=41, start=2.625, end=3.0),  # F2 (chromatic approach)
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875), # G4
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875), # Bb4
    pretty_midi.Note(velocity=80, pitch=72, start=1.5, end=1.875), # D5
]
# Bar 3: C7
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.625), # C4
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.625), # E4
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625), # G4
    pretty_midi.Note(velocity=80, pitch=72, start=2.25, end=2.625), # C5
])
# Bar 4: Gm7
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0), # G4
    pretty_midi.Note(velocity=80, pitch=72, start=2.625, end=3.0), # Bb4
    pretty_midi.Note(velocity=80, pitch=74, start=2.625, end=3.0), # D5
    pretty_midi.Note(velocity=80, pitch=77, start=2.625, end=3.0), # F5
])
for note in piano_notes:
    piano.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),
    pretty_midi.Note(velocity=60, pitch=42, start=1.5, end=3.0),
]
for note in drum_notes:
    drums.notes.append(note)

# Dante: Tenor sax, one short motif, start it, leave it hanging, come back and finish
# Melody: D4, F4, G4, E4, D4 (rest on the last beat)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75), # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0), # F4
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25), # G4
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5), # E4
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=3.0), # D4
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
