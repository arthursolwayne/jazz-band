
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

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking bass line (D2 = MIDI 38), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),  # F2 (fifth of D)
    pretty_midi.Note(velocity=80, pitch=41, start=2.25, end=2.625),  # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),  # D2
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.875),  # C#4
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: G7 (G-B-D-F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # F4
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Bm7 (B-D-F#-A)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=4.875),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # A4
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Tenor sax - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D4 - F#4 - B4 - D5 (Dmaj7 arpeggio, but played as a motif)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),  # F#4
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.625),  # A4
    pretty_midi.Note(velocity=110, pitch=74, start=2.625, end=3.0),  # C#4
    pretty_midi.Note(velocity=110, pitch=74, start=3.0, end=3.375),  # C#4 (hold)
    pretty_midi.Note(velocity=110, pitch=76, start=3.375, end=3.75),  # D5
    pretty_midi.Note(velocity=110, pitch=74, start=3.75, end=4.125),  # C#4
    pretty_midi.Note(velocity=110, pitch=71, start=4.125, end=4.5),  # A4
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.875),  # F#4
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.25),  # D4
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
