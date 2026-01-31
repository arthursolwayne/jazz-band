
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),  # F#2
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # A2
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),   # A2
    pretty_midi.Note(velocity=90, pitch=41, start=3.0, end=3.375),  # F#2
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75), # D2
    pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=4.125), # D2
    pretty_midi.Note(velocity=90, pitch=40, start=4.125, end=4.5),  # G2
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875),  # A2
    pretty_midi.Note(velocity=90, pitch=43, start=4.875, end=5.25), # A2
    pretty_midi.Note(velocity=90, pitch=40, start=5.25, end=5.625), # G2
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),  # D2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875), # A4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875), # C4
]

# Bar 3: G7 (G B D F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625), # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # F4
])

# Bar 4: C7 (C E G B)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375), # C4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375), # E4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375), # B4
])

# Bar 2-3 resolve into C7, with some tension
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75), # B4
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75), # G4
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75), # E4
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75), # C4
])

# Bar 4: Full resolution
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125), # C4
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125), # E4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125), # B4
])

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing
# Start it, leave it hanging, come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875), # E4
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.25), # A4
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625), # G4
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=3.0), # A4
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.375), # E4
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75), # A4
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125), # G4
    pretty_midi.Note(velocity=110, pitch=69, start=4.125, end=4.5), # A4
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875), # E4
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.25), # A4
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625), # G4
    pretty_midi.Note(velocity=110, pitch=69, start=5.625, end=6.0), # A4
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875))

    # Hihat on every eighth
    for i in range(8):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
