
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
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

# Bass: Walking line (F2 - Bb2, MIDI 53-57), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=56, start=1.875, end=2.25), # A2 (fifth)
    pretty_midi.Note(velocity=80, pitch=55, start=2.25, end=2.625), # G2 (chromatic)
    pretty_midi.Note(velocity=80, pitch=53, start=2.625, end=3.0),  # F2

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=80, pitch=56, start=3.375, end=3.75), # A2
    pretty_midi.Note(velocity=80, pitch=57, start=3.75, end=4.125), # Bb2 (chromatic)
    pretty_midi.Note(velocity=80, pitch=53, start=4.125, end=4.5),  # F2

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=80, pitch=56, start=4.875, end=5.25), # A2
    pretty_midi.Note(velocity=80, pitch=54, start=5.25, end=5.625), # G#2 (chromatic)
    pretty_midi.Note(velocity=80, pitch=53, start=5.625, end=6.0),  # F2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb) -> F, Ab, C, Eb (open voicing)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=2.25), # F4
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=2.25), # Eb4 (Fm7)
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=2.25), # G4
    pretty_midi.Note(velocity=90, pitch=59, start=1.5, end=2.25), # Ab4

    # Bar 3: Bb7 (Bb, D, F, Ab) -> Bb, D, F, Ab (open voicing)
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.75), # Bb4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.75), # D4
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.75), # F4
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.75), # Ab4

    # Bar 4: Eb7 (Eb, G, Bb, Db) -> Eb, G, Bb, Db (open voicing)
    pretty_midi.Note(velocity=90, pitch=61, start=4.5, end=5.25), # Eb4
    pretty_midi.Note(velocity=90, pitch=66, start=4.5, end=5.25), # G4
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=5.25), # Bb4
    pretty_midi.Note(velocity=90, pitch=58, start=4.5, end=5.25), # Db4
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F4, Ab4, Bb4, F4 (with some subtle portamento)
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=64, start=1.5, end=1.6875), # F4
    pretty_midi.Note(velocity=100, pitch=60, start=1.6875, end=1.875), # Ab4
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0625), # Bb4
    pretty_midi.Note(velocity=105, pitch=64, start=2.0625, end=2.25), # F4

    pretty_midi.Note(velocity=105, pitch=64, start=2.625, end=2.8125), # F4
    pretty_midi.Note(velocity=100, pitch=60, start=2.8125, end=3.0), # Ab4
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
