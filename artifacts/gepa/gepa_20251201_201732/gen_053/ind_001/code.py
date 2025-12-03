
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
for i in range(4):
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.375 * i, end=0.375 * (i + 1)))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75 * i, end=0.75 * (i + 1)))
    for j in range(8):
        drum_notes.append(pretty_midi.Note(velocity=60, pitch=42, start=0.1875 * (8 * i + j), end=0.1875 * (8 * i + j + 1)))
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.75),  # D2
    pretty_midi.Note(velocity=90, pitch=50, start=1.75, end=2.0),  # F2
    pretty_midi.Note(velocity=90, pitch=51, start=2.0, end=2.25),  # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=48, start=2.25, end=2.5),  # D2
    pretty_midi.Note(velocity=90, pitch=50, start=2.5, end=2.75),  # F2
    pretty_midi.Note(velocity=90, pitch=52, start=2.75, end=3.0),  # G2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.25),  # D2
    pretty_midi.Note(velocity=90, pitch=50, start=3.25, end=3.5),  # F2
    pretty_midi.Note(velocity=90, pitch=51, start=3.5, end=3.75),  # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=48, start=3.75, end=4.0),  # D2
    pretty_midi.Note(velocity=90, pitch=50, start=4.0, end=4.25),  # F2
    pretty_midi.Note(velocity=90, pitch=52, start=4.25, end=4.5),  # G2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.75),  # D2
    pretty_midi.Note(velocity=90, pitch=50, start=4.75, end=5.0),  # F2
    pretty_midi.Note(velocity=90, pitch=51, start=5.0, end=5.25),  # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=48, start=5.25, end=5.5),  # D2
    pretty_midi.Note(velocity=90, pitch=50, start=5.5, end=5.75),  # F2
    pretty_midi.Note(velocity=90, pitch=52, start=5.75, end=6.0)   # G2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.75),  # C5
]

# Bar 3: Gm7 (G Bb D F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),  # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=2.5, end=2.75),  # D5
    pretty_midi.Note(velocity=100, pitch=76, start=2.5, end=2.75),  # F5
])

# Bar 4: Cm7 (C Eb G Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=3.5, end=3.75),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),  # Bb4
])

# Resolve on the last chord (Dm7 at bar 4)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.75),  # C5
])

piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs

# Bar 2: Start of motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),  # D4
    pretty_midi.Note(velocity=110, pitch=66, start=1.6875, end=1.875),  # G4
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.0),  # F4
]

# Bar 3: Leave it hanging, rest
sax_notes.append(pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.125))  # D4

# Bar 4: Return and finish the motif
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=64, start=4.0, end=4.125),  # E4
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.25),  # D4
    pretty_midi.Note(velocity=110, pitch=60, start=4.25, end=4.5),  # C4
])

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
