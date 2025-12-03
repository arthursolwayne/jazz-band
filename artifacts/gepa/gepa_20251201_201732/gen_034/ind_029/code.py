
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5s)
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=53, start=1.875, end=2.25), # F2
    pretty_midi.Note(velocity=100, pitch=49, start=2.25, end=2.625), # C2
    pretty_midi.Note(velocity=100, pitch=50, start=2.625, end=3.0),  # D2 (chromatic approach)
    # Bar 3 (3.0s)
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.75), # F2
    pretty_midi.Note(velocity=100, pitch=49, start=3.75, end=4.125), # C2
    pretty_midi.Note(velocity=100, pitch=50, start=4.125, end=4.5),  # D2 (chromatic approach)
    # Bar 4 (4.5s)
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=100, pitch=53, start=4.875, end=5.25), # F2
    pretty_midi.Note(velocity=100, pitch=49, start=5.25, end=5.625), # C2
    pretty_midi.Note(velocity=100, pitch=50, start=5.625, end=6.0),  # D2 (chromatic approach)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: open voicings with different chords each bar, resolving on the last
# Bar 2 (1.5s)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # G4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875), # C5
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875), # D5
    # Bar 3 (3.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # G4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375), # C5
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375), # F5
    # Bar 4 (4.5s)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875), # G4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875), # C5
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875), # D5
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: motif, start it, leave it hanging, come back and finish it
# Bar 2 (1.5s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875), # D4
    pretty_midi.Note(velocity=100, pitch=66, start=1.6875, end=1.875), # F4
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.8125), # D4
    pretty_midi.Note(velocity=100, pitch=66, start=2.8125, end=3.0), # F4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.1875), # A4
    pretty_midi.Note(velocity=100, pitch=62, start=3.1875, end=3.375), # D4
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
