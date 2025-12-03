
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in D, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25), # F#2 (fifth)
    pretty_midi.Note(velocity=100, pitch=40, start=2.25, end=2.625), # E2 (chromatic up)
    pretty_midi.Note(velocity=100, pitch=41, start=2.625, end=3.0),  # F2 (chromatic down)
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=39, start=3.375, end=3.75), # C#2 (chromatic up)
    pretty_midi.Note(velocity=100, pitch=40, start=3.75, end=4.125), # D2 (root)
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # F#2 (fifth)
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.875),  # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25), # F2 (chromatic down)
    pretty_midi.Note(velocity=100, pitch=40, start=5.25, end=5.625), # E2 (chromatic up)
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # D2 (root)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Cmaj7 (D is the key, but Cmaj7 is in the key of D minor, gives tension)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=2.0),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.0),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # B4
]

# Bar 3: A7sus4 (creates chromatic tension)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.5),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.5),  # D5
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.5),  # F#5
])

# Bar 4: Gmaj7 (resolution)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=3.0),  # B4
    pretty_midi.Note(velocity=100, pitch=72, start=2.5, end=3.0),  # C5
    pretty_midi.Note(velocity=100, pitch=76, start=2.5, end=3.0),  # D5
])

# Fill the rest of the piano with comping on 2 and 4
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # G4 on 2
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.5),  # B4
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.5),  # C5
    pretty_midi.Note(velocity=100, pitch=76, start=2.0, end=2.5),  # D5
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # G4 on 4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5),  # B4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.5),  # C5
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.5),  # D5
])

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 (E4), F#4 (G4), A4 (B4), D5 (E5)
# Bar 2: Start it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.75),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0),  # G4
]

# Bar 3: Leave it hanging
sax_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.125))  # G4

# Bar 4: Come back and finish it
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=2.125, end=2.25),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.375),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=2.375, end=2.5),   # B4
    pretty_midi.Note(velocity=100, pitch=74, start=2.5, end=2.625),   # C5
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=2.75),  # D5
    pretty_midi.Note(velocity=100, pitch=77, start=2.75, end=2.875),  # E5
])

for note in sax_notes:
    sax.notes.append(note)

# Drums continue for bars 2-4
# Bar 2: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Hihat on every eighth
    for i in range(0, 4):
        hihat_start = start + i * 0.375
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
